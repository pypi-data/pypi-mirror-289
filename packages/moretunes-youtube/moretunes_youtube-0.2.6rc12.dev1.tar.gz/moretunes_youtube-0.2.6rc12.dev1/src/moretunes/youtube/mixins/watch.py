from typing import Dict, List, Optional, Union

from ..continuations import get_continuations
from ..mixins._protocol import MixinProtocol
from ..parsers.watch import *
from ..speed_nav import *


class WatchMixin(MixinProtocol):
    def _request_watch_playlist(self, video_id, playlist_id, radio, shuffle):
        pack = {
            'body': {
                "enablePersistentPlaylistPanel": True,
                "isAudioOnly": True,
                "tunerSettingValue": "AUTOMIX_SETTING_NORMAL",
            },
            'endpoint': 'next',
            'is_playlist': False
        }

        if video_id:
            pack['body']["videoId"] = video_id
            if not playlist_id:
                playlist_id = "RDAMVM" + video_id
            if not (radio or shuffle):
                pack['body']["watchEndpointMusicSupportedConfigs"] = {
                    "watchEndpointMusicConfig": {
                        "hasPersistentPlaylistPanel": True,
                        "musicVideoType": "MUSIC_VIDEO_TYPE_ATV",
                    }
                }

        if playlist_id:
            playlist_id = playlist_id.lstrip("VL")
            pack['is_playlist'] = playlist_id.startswith("PL") or playlist_id.startswith("OLA")
            pack['body']["playlistId"] = playlist_id

        if shuffle and playlist_id is not None:
            pack['body']["params"] = "wAEB8gECKAE%3D"
        if radio:
            pack['body']["params"] = "wAEB"

        return pack | {'response': self._send_request(pack['endpoint'], pack['body'])}

    @staticmethod
    def _parse_core_result(res_pack, extra_bs):
        next_render = nav2.watch_next(res_pack['response'])

        res_pack['results'] = nav2.panel_render(next_render)

        res_pack['output'] = {
            "lyrics": get_tab_browse_id(next_render, 1),
            "related": get_tab_browse_id(next_render, 2),
            "tracks": parse_watch_playlist(res_pack['results']["contents"], extra_bs=extra_bs),
            "playlist": next((x for x in res_pack['results']["contents"]
                              if nav2.panel_pid(x, default=None)), None)
        }
        return res_pack

    def _extend_watch_playlist_results(self, res_pack: dict, need: int, extra_bs: bool):
        def req_func(additional_params):
            return self._send_request(res_pack['endpoint'], res_pack['body'], additional_params)

        def parse_func(contents):
            parse_watch_playlist(contents, extra_bs=extra_bs)

        if "continuations" in res_pack['results']:
            res_pack['output']["tracks"].extend(
                get_continuations(
                    res_pack['results'],
                    "playlistPanelContinuation",
                    need,
                    req_func,
                    parse_func,
                    "" if res_pack['is_playlist'] else "Radio",
                )
            )
        return res_pack

    def get_watch_playlist(
        self,
        video_id: Optional[str] = None,
        playlist_id: Optional[str] = None,
        limit=25,
        radio: bool = False,
        shuffle: bool = False,
        extra_bs: bool = True,
    ) -> Dict[str, Union[List[Dict], str, None]]:
        """
        Get a watch list of tracks. This watch playlist appears when you press
        play on a track in YouTube Music.

        Please note that the `INDIFFERENT` likeStatus of tracks returned by this
        endpoint may be either `INDIFFERENT` or `DISLIKE`, due to ambiguous data
        returned by YouTube Music.

        :param video_id: videoId of the played video
        :param playlist_id: playlistId of the played playlist or album
        :param limit: minimum number of watch playlist items to return
        :param radio: get a radio playlist (changes each time)
        :param shuffle: shuffle the input playlist. only works when the playlistId parameter
            is set at the same time. does not work if radio=True
        :return: List of watch playlist items. The counterpart key is optional and only
            appears if a song has a corresponding video counterpart (UI song/video
            switcher).

        Example::

            {
                "tracks": [
                    {
                      "videoId": "9mWr4c_ig54",
                      "title": "Foolish Of Me (feat. Jonathan Mendelsohn)",
                      "length": "3:07",
                      "thumbnail": [
                        {
                          "url": "https://lh3.googleusercontent.com/ulK2YaLtOW0PzcN7ufltG6e4ae3WZ9Bvg8CCwhe6LOccu1lCKxJy2r5AsYrsHeMBSLrGJCNpJqXgwczk=w60-h60-l90-rj",
                          "width": 60,
                          "height": 60
                        }...
                      ],
                      "feedbackTokens": {
                        "add": "AB9zfpIGg9XN4u2iJ...",
                        "remove": "AB9zfpJdzWLcdZtC..."
                      },
                      "likeStatus": "INDIFFERENT",
                      "videoType": "MUSIC_VIDEO_TYPE_ATV",
                      "artists": [
                        {
                          "name": "Seven Lions",
                          "id": "UCYd2yzYRx7b9FYnBSlbnknA"
                        },
                        {
                          "name": "Jason Ross",
                          "id": "UCVCD9Iwnqn2ipN9JIF6B-nA"
                        },
                        {
                          "name": "Crystal Skies",
                          "id": "UCTJZESxeZ0J_M7JXyFUVmvA"
                        }
                      ],
                      "album": {
                        "name": "Foolish Of Me",
                        "id": "MPREb_C8aRK1qmsDJ"
                      },
                      "year": "2020",
                      "counterpart": {
                        "videoId": "E0S4W34zFMA",
                        "title": "Foolish Of Me [ABGT404] (feat. Jonathan Mendelsohn)",
                        "length": "3:07",
                        "thumbnail": [...],
                        "feedbackTokens": null,
                        "likeStatus": "LIKE",
                        "artists": [
                          {
                            "name": "Jason Ross",
                            "id": null
                          },
                          {
                            "name": "Seven Lions",
                            "id": null
                          },
                          {
                            "name": "Crystal Skies",
                            "id": null
                          }
                        ],
                        "views": "6.6K"
                      }
                    },...
                ],
                "playlistId": "RDAMVM4y33h81phKU",
                "lyrics": "MPLYt_HNNclO0Ddoc-17"
            }

        """
        if not video_id and not playlist_id:
            raise Exception("You must provide either a video id, a playlist id, or both")

        # edge: podcast playlist/view takes the place of artist ie omgoQzKyLJw

        res_pack = self._request_watch_playlist(video_id, playlist_id, radio, shuffle)
        res_pack = self._parse_core_result(res_pack, extra_bs=extra_bs)

        if (need := limit - len(res_pack['output']['tracks'])) > 0:
            res_pack = self._extend_watch_playlist_results(res_pack, need, extra_bs)

        return res_pack['output']

# beat 0005629062652587891s
