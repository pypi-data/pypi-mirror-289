import re
from typing import Any, Dict, List, Optional

from ..continuations import (
    get_continuations,
    get_reloadable_continuation_params,
)
from ..helpers import YTM_DOMAIN
from ..parsers.albums import parse_album_header
from ..parsers.browsing import parse_album, parse_content_list, parse_mixed_content, parse_playlist, parse_list_meta
from ..parsers.library import parse_albums
from ..parsers.playlists import parse_playlist_items

from ..models import CoreTrack
from ..navigation import *
from ..parsers.utils import get_ext, parse_real_count, pull_thumbnail, content_playlist  # protected ?
from ._protocol import MixinProtocol
from ._utils import get_datestamp
from ..exceptions import ArtistIsUserException, APIException


class BrowsingMixin(MixinProtocol):
    def get_home(self, limit=3) -> List[Dict]:
        """
        Get the home page.
        The home page is structured as titled rows, returning 3 rows of music suggestions at a time.
        Content varies and may contain artist, album, song or playlist suggestions, sometimes mixed within the same row

        :param limit: Number of rows to return
        :return: List of dictionaries keyed with 'title' text and 'contents' list

        Example list::

            [
                {
                    "title": "Your morning music",
                    "contents": [
                        { //album result
                            "title": "Sentiment",
                            "year": "Said The Sky",
                            "browseId": "MPREb_QtqXtd2xZMR",
                            "thumbnails": [...]
                        },
                        { //playlist result
                            "title": "r/EDM top submissions 01/28/2022",
                            "playlistId": "PLz7-xrYmULdSLRZGk-6GKUtaBZcgQNwel",
                            "thumbnails": [...],
                            "description": "redditEDM • 161 songs",
                            "count": "161",
                            "author": [
                                {
                                    "name": "redditEDM",
                                    "id": "UCaTrZ9tPiIGHrkCe5bxOGwA"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Your favorites",
                    "contents": [
                        { //artist result
                            "title": "Chill Satellite",
                            "browseId": "UCrPLFBWdOroD57bkqPbZJog",
                            "subscribers": "374",
                            "thumbnails": [...]
                        }
                        { //album result
                            "title": "Dragon",
                            "year": "Two Steps From Hell",
                            "browseId": "MPREb_M9aDqLRbSeg",
                            "thumbnails": [...]
                        }
                    ]
                },
                {
                    "title": "Quick picks",
                    "contents": [
                        { //song quick pick
                            "title": "Gravity",
                            "videoId": "EludZd6lfts",
                            "artists": [{
                                    "name": "yetep",
                                    "id": "UCSW0r7dClqCoCvQeqXiZBlg"
                                }],
                            "thumbnails": [...],
                            "album": {
                                "name": "Gravity",
                                "id": "MPREb_D6bICFcuuRY"
                            }
                        },
                        { //video quick pick
                            "title": "Gryffin & Illenium (feat. Daya) - Feel Good (L3V3LS Remix)",
                            "videoId": "bR5l0hJDnX8",
                            "artists": [
                                {
                                    "name": "L3V3LS",
                                    "id": "UCCVNihbOdkOWw_-ajIYhAbQ"
                                }
                            ],
                            "thumbnails": [...],
                            "views": "10M"
                        }
                    ]
                }
            ]

        """
        endpoint = "browse"
        body = {"browseId": "FEmusic_home"}
        response = self._send_request(endpoint, body)
        results = nav(response, SINGLE_COLUMN_TAB + SECTION_LIST)
        home = []
        home.extend(parse_mixed_content(results))

        section_list = nav(response, SINGLE_COLUMN_TAB + ["sectionListRenderer"])
        if "continuations" in section_list:
            request_func = lambda additional_params: self._send_request(endpoint, body, additional_params)

            parse_func = lambda contents: parse_mixed_content(contents)

            home.extend(
                get_continuations(
                    section_list, "sectionListContinuation", limit - len(home), request_func, parse_func
                )
            )

        return home

    def get_artist(self, channel_id: str) -> Dict:
        """
        Get information about an artist and their top releases (songs,
        albums, singles, videos, and related artists). The top lists
        contain pointers for getting the full list of releases.

        For songs/videos, pass the browseId to :py:func:`get_playlist`.
        For albums/singles, pass browseId and params to :py:func:`get_artist_albums`.

        :param channel_id: channel id of the artist
        :return: Dictionary with requested information.

        .. warning::

            The returned channelId is not the same as the one passed to the function.
            It should be used only with :py:func:`subscribe_artists`.

        Example::

            {
                "description": "Oasis were ...",
                "views": "1838795605",
                "name": "Oasis",
                "channelId": "UCUDVBtnOQi4c7E8jebpjc9Q",
                "subscribers": "2.3M",
                "subscribed": false,
                "thumbnails": [...],
                "songs": {
                    "browseId": "VLPLMpM3Z0118S42R1npOhcjoakLIv1aqnS1",
                    "results": [
                        {
                            "videoId": "ZrOKjDZOtkA",
                            "title": "Wonderwall (Remastered)",
                            "thumbnails": [...],
                            "artist": "Oasis",
                            "album": "(What's The Story) Morning Glory? (Remastered)"
                        }
                    ]
                },
                "albums": {
                    "results": [
                        {
                            "title": "Familiar To Millions",
                            "thumbnails": [...],
                            "year": "2018",
                            "browseId": "MPREb_AYetWMZunqA"
                        }
                    ],
                    "browseId": "UCmMUZbaYdNH0bEd1PAlAqsA",
                    "params": "6gPTAUNwc0JDbndLYlFBQV..."
                },
                "singles": {
                    "results": [
                        {
                            "title": "Stand By Me (Mustique Demo)",
                            "thumbnails": [...],
                            "year": "2016",
                            "browseId": "MPREb_7MPKLhibN5G"
                        }
                    ],
                    "browseId": "UCmMUZbaYdNH0bEd1PAlAqsA",
                    "params": "6gPTAUNwc0JDbndLYlFBQV..."
                },
                "videos": {
                    "results": [
                        {
                            "title": "Wonderwall",
                            "thumbnails": [...],
                            "views": "358M",
                            "videoId": "bx1Bh8ZvH84",
                            "playlistId": "PLMpM3Z0118S5xuNckw1HUcj1D021AnMEB"
                        }
                    ],
                    "browseId": "VLPLMpM3Z0118S5xuNckw1HUcj1D021AnMEB"
                },
                "related": {
                    "results": [
                        {
                            "browseId": "UCt2KxZpY5D__kapeQ8cauQw",
                            "subscribers": "450K",
                            "title": "The Verve"
                        },
                        {
                            "browseId": "UCwK2Grm574W1u-sBzLikldQ",
                            "subscribers": "341K",
                            "title": "Liam Gallagher"
                        },
                        ...
                    ]
                }
            }
        """
        response = self._send_request("browse", {"browseId": channel_id.lstrip("MPLA")})
        results = nav(response, SINGLE_COLUMN_TAB + SECTION_LIST)

        artist: Dict[str, Any] = {"description": None, 'songs': None, 'videos': None}

        header = response["header"].get("musicImmersiveHeaderRenderer")
        if header is None:
            raise ArtistIsUserException(channel_id)

        artist["name"] = nav(header, TITLE_TEXT).replace('\u200b', '')
        if description_shelf := find_object_by_key(results, DESCRIPTION_SHELF[0], is_key=True):
            artist["description"] = nav(description_shelf, DESCRIPTION)
            artist["view_count"] = parse_real_count(nav(description_shelf, ["subheader", "runs", 0], True))
        subscription_button = header["subscriptionButton"]["subscribeButtonRenderer"]
        artist["channel_id"] = subscription_button["channelId"]

        if "playButton" in header:
            nav_fork = header["playButton"]["buttonRenderer"]["navigationEndpoint"]
        else:
            nav_fork = None

        # artist channels accessed via their artist_id has a different layout
        if nav_fork and "watchPlaylistEndpoint" in nav_fork:
            artist["shuffle_id"] = nav_fork["watchPlaylistEndpoint"]["playlistId"]
            artist["page_type"] = "channel"
        else:
            artist["artist_id"] = channel_id
            artist["shuffle_id"] = None if not nav_fork else nav_fork["watchEndpoint"]["playlistId"]
            artist["page_type"] = "artist"
            if song_shelf := results[0].get("musicShelfRenderer"):
                artist["songs"] = {
                    "playlist_id": content_playlist(song_shelf),
                    "items": parse_playlist_items(song_shelf["contents"]),
                }

        artist["radio_id"] = artist["shuffle_id"].replace("RDAO", "RDEM") if artist["shuffle_id"] else None
        artist["sub_count"] = parse_real_count(
            nav(subscription_button, ["subscriberCountText", "runs", 0], True)
        )

        artist["subscribed"] = subscription_button["subscribed"]
        artist["thumbnail"] = pull_thumbnail(header)

        artist = self.parser.append_channel_contents(artist, results)
        return artist

    def get_artist_albums(
            self,
            artist_id: str,
            only: Literal['single', 'album', 'all'] = 'all',
            limit: Optional[int] = None
            ) -> List[Dict]:
        """
        Get the full list of an artist's albums or singles

        :param artist_id: target artist to pull albums for
        :param only: filter return types to only include certain album types.
            WARNING: limit may not work correctly when filtering for just EP types.
        :param limit: Number of albums to return. `None` retrieves them all. Default=None
        :return: List of albums in the format of :py:func:`get_library_albums`,
          except artists key is missing.
        """

        extension = {
            "browseId": f'MPAD{artist_id}',
            "params": {'single': 'ggMIegYIAhoCAQI%3D', 'album': 'ggMIegYIARoCAQI'}.get(only, '')}
        endpoint = "browse"
        response = self._send_request(endpoint, extension)

        def local_req(etc_params):
            return self._send_request(endpoint, extension, etc_params)

        # todo: change to a mapping
        # if order:
        #     # pick the correct continuation from response depending on the order chosen
        #     sort_options = nav(
        #         response,
        #         SINGLE_COLUMN_TAB
        #         + SECTION
        #         + HEADER_SIDE
        #         + [
        #             "endItems",
        #             0,
        #             "musicSortFilterButtonRenderer",
        #             "menu",
        #             "musicMultiSelectMenuRenderer",
        #             "options",
        #         ],
        #     )
        #     continuation = next(
        #         (
        #             nav(
        #                 option,
        #                 MULTI_SELECT
        #                 + [
        #                     "selectedCommand",
        #                     "commandExecutorCommand",
        #                     "commands",
        #                     -1,
        #                     "browseSectionListReloadEndpoint",
        #                 ],
        #             )
        #             for option in sort_options
        #             if nav(option, MULTI_SELECT + TITLE_TEXT).lower() == order.lower()
        #         ),
        #         None,
        #     )
        #     # if a valid order was provided, request continuation and replace original response
        #     if continuation:
        #         additional_params = get_reloadable_continuation_params(
        #             {"continuations": [continuation["continuation"]]}
        #         )
        #         response = local_req(additional_params)
        #         results = nav(response, SECTION_LIST_CONTINUATION + CONTENT)
        #     else:
        #         raise ValueError(f"Invalid order parameter {order}")
        #
        # else:
        # just use the results from the first request
        results = nav(response, SINGLE_COLUMN_TAB + SECTION_LIST_ITEM)

        contents = nav(results, GRID_ITEMS, True) or nav(results, CAROUSEL_CONTENTS)
        albums = parse_albums(contents)

        results = nav(results, GRID, True)
        if "continuations" in results:
            remaining_limit = None if limit is None else (limit - len(albums))
            albums.extend(
                get_continuations(results, "gridContinuation", remaining_limit, local_req, parse_albums)
            )

        return albums

    def get_user(self, channel_id: str) -> Dict:
        """
        Retrieve a user's page. A user may own videos or playlists.

        :param channel_id: channelId of the user
        :return: Dictionary with information about a user.

        Example::

            {
              "name": "4Tune – No Copyright Music",
              "videos": {
                "browseId": "UC44hbeRoCZVVMVg5z0FfIww",
                "results": [
                  {
                    "title": "Epic Music Soundtracks 2019",
                    "videoId": "bJonJjgS2mM",
                    "playlistId": "RDAMVMbJonJjgS2mM",
                    "thumbnails": [
                      {
                        "url": "https://i.ytimg.com/vi/bJon...",
                        "width": 800,
                        "height": 450
                      }
                    ],
                    "views": "19K"
                  }
                ]
              },
              "playlists": {
                "browseId": "UC44hbeRoCZVVMVg5z0FfIww",
                "results": [
                  {
                    "title": "♚ Machinimasound | Playlist",
                    "playlistId": "PLRm766YvPiO9ZqkBuEzSTt6Bk4eWIr3gB",
                    "thumbnails": [
                      {
                        "url": "https://i.ytimg.com/vi/...",
                        "width": 400,
                        "height": 225
                      }
                    ]
                  }
                ],
                "params": "6gO3AUNvWU..."
              }
            }
        """

        response = self._send_request("browse", {"browseId": channel_id})
        user = {
            "name": nav(response, ["header", "musicVisualHeaderRenderer"] + TITLE_TEXT),
            "page_type": "user",
        }
        results = nav(response, SINGLE_COLUMN_TAB + SECTION_LIST)
        user = self.parser.append_channel_contents(user, results)
        return user

    def get_user_playlists(self, ext: Dict) -> List[Dict]:
        """
        Retrieve a list of playlists for a given user.
        Call this function again with the returned ``params`` to get the full list.

        :param ext: extension dict from get_user -> playlists
        :return: List of user playlists in the format of :py:func:`get_library_playlists`

        """
        response = self._send_request("browse", {"browseId": ext["browse_id"], "params": ext["params"]})
        results = nav(response, SINGLE_COLUMN_TAB + SECTION_LIST_ITEM + GRID_ITEMS, True)
        if not results:
            return []

        user_playlists = parse_content_list(results, parse_playlist)

        return user_playlists

    def get_album_browse_id(self, playlist_id: str) -> Optional[str]:
        """
        Get an album's browseId based on its audioPlaylistId

        :param playlist_id: id of the audio playlist  (starting with `OLAK5uy_`)
        :return: browseId (starting with `MPREb_`)
        """
        params = {"list": playlist_id}
        response = self._send_get_request(YTM_DOMAIN + "/playlist", params)

        matches = re.search(r"\"MPRE.+?\"", response.text.encode("utf8").decode("unicode_escape"))
        browse_id = None
        if matches:
            browse_id = matches.group().strip('"')
        return browse_id

    def get_album(self, browse_id: str, extra_bs=False, coerce_id=True) -> Dict:
        """
        Get information and tracks of an album

        :param browse_id: browseId of the album, for example
            returned by :py:func:`search`
        :return: Dictionary with album and track metadata.

        Each track is in the following format::

            {
              "title": "Revival",
              "type": "Album",
              "thumbnails": [],
              "description": "Revival is the...",
              "artists": [
                {
                  "name": "Eminem",
                  "id": "UCedvOgsKFzcK3hA5taf3KoQ"
                }
              ],
              "year": "2017",
              "trackCount": 19,
              "duration": "1 hour, 17 minutes",
              "audioPlaylistId": "OLAK5uy_nMr9h2VlS-2PULNz3M3XVXQj_P3C2bqaY",
              "tracks": [
                {
                  "videoId": "iKLU7z_xdYQ",
                  "title": "Walk On Water (feat. Beyoncé)",
                  "artists": [
                    {
                      "name": "Eminem",
                      "id": "UCedvOgsKFzcK3hA5taf3KoQ"
                    }
                  ],
                  "album": "Revival",
                  "likeStatus": "INDIFFERENT",
                  "thumbnails": null,
                  "isAvailable": true,
                  "isExplicit": true,
                  "duration": "5:03",
                  "duration_seconds": 303,
                  "feedbackTokens": {
                    "add": "AB9zfpK...",
                    "remove": "AB9zfpK..."
                  }
                }
              ],
              "other_versions": [
                {
                  "title": "Revival",
                  "year": "Eminem",
                  "browseId": "MPREb_fefKFOTEZSp",
                  "thumbnails": [...],
                  "isExplicit": false
                },
              ],
              "duration_seconds": 4657
            }
        """

        if not browse_id.startswith('MPREb_'):
            if browse_id.startswith('OLAK5uy') and coerce_id:
                print('Fetching browse_id for album, pass directly to avoid extra API call.')
                browse_id = self.get_album_browse_id(browse_id)
            else:
                raise ValueError(f'Invalid album browse_id "{browse_id}". Album id should start with "MPREb_".')

        response = self._send_request("browse", {"browseId": browse_id})

        album, render = parse_list_meta(response)
        album['playlist_id'] = album.pop('id')
        album['artists'] = album.pop('authors')
        album["browse_id"] = browse_id

        album["tracks"] = parse_playlist_items(
            render['contents'][0]['musicShelfRenderer']['contents'],
            context=album, extra_bs=extra_bs)

        # albums that don't have any featured artists exclude track artists in metadata
        if not any(x['artists'] for x in album['tracks']) and album['artists']:
            for tr in album['tracks']:
                tr['artists'] = album['artists']

        if len(render['contents']) > 1:
            album['other_versions'] = parse_content_list(
                render['contents'][1]['musicCarouselShelfRenderer']['contents'], parse_album)

        # results = nav(response, SINGLE_COLUMN_TAB + SECTION_LIST + [1] + CAROUSEL, True)
        # if results is not None:
        #     album["other_versions"] = parse_content_list(results["contents"], parse_album)
        # album["duration_s"] = sum_total_duration(album)

        return album

    def _player_response(self, video_id: str, signature_timestamp: Optional[int] = None):
        if not signature_timestamp:
            signature_timestamp = get_datestamp() - 1

        params = {
            "playbackContext": {"contentPlaybackContext": {"signatureTimestamp": signature_timestamp}},
            "video_id": video_id,
        }
        return self._send_request("player", params)

    def get_song(self, video_id: str, signature_timestamp: Optional[int] = None) -> Dict:
        """
        Returns metadata and streaming information about a song or video.

        :param video_id: Video id
        :param signature_timestamp: Provide the current YouTube signatureTimestamp.
            If not provided a default value will be used, which might result in invalid streaming URLs
        :return: Dictionary with song metadata.

        Example::

            {
                "playabilityStatus": {
                    "status": "OK",
                    "playableInEmbed": true,
                    "audioOnlyPlayability": {
                        "audioOnlyPlayabilityRenderer": {
                            "trackingParams": "CAEQx2kiEwiuv9X5i5H1AhWBvlUKHRoZAHk=",
                            "audioOnlyAvailability": "FEATURE_AVAILABILITY_ALLOWED"
                        }
                    },
                    "miniplayer": {
                        "miniplayerRenderer": {
                            "playbackMode": "PLAYBACK_MODE_ALLOW"
                        }
                    },
                    "contextParams": "Q0FBU0FnZ0M="
                },
                "streamingData": {
                    "expiresInSeconds": "21540",
                    "adaptiveFormats": [
                        {
                            "itag": 140,
                            "url": "https://rr1---sn-h0jelnez.c.youtube.com/videoplayback?expire=1641080272...",
                            "mimeType": "audio/mp4; codecs=\"mp4a.40.2\"",
                            "bitrate": 131007,
                            "initRange": {
                                "start": "0",
                                "end": "667"
                            },
                            "indexRange": {
                                "start": "668",
                                "end": "999"
                            },
                            "lastModified": "1620321966927796",
                            "contentLength": "3967382",
                            "quality": "tiny",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 129547,
                            "highReplication": true,
                            "audioQuality": "AUDIO_QUALITY_MEDIUM",
                            "approxDurationMs": "245000",
                            "audioSampleRate": "44100",
                            "audioChannels": 2,
                            "loudnessDb": -1.3000002
                        }
                    ]
                },
                "playbackTracking": {
                    "videostatsPlaybackUrl": {
                      "baseUrl": "https://s.youtube.com/api/stats/playback?cl=491307275&docid=AjXQiKP5kMs&ei=Nl2HY-6MH5WE8gPjnYnoDg&fexp=1714242%2C9405963%2C23804281%2C23858057%2C23880830%2C23880833%2C23882685%2C23918597%2C23934970%2C23946420%2C23966208%2C23983296%2C23998056%2C24001373%2C24002022%2C24002025%2C24004644%2C24007246%2C24034168%2C24036947%2C24077241%2C24080738%2C24120820%2C24135310%2C24135692%2C24140247%2C24161116%2C24162919%2C24164186%2C24169501%2C24175560%2C24181174%2C24187043%2C24187377%2C24187854%2C24191629%2C24197450%2C24199724%2C24200839%2C24209349%2C24211178%2C24217535%2C24219713%2C24224266%2C24241378%2C24248091%2C24248956%2C24255543%2C24255545%2C24262346%2C24263796%2C24265426%2C24267564%2C24268142%2C24279196%2C24280220%2C24283426%2C24283493%2C24287327%2C24288045%2C24290971%2C24292955%2C24293803%2C24299747%2C24390674%2C24391018%2C24391537%2C24391709%2C24392268%2C24392363%2C24392401%2C24401557%2C24402891%2C24403794%2C24406605%2C24407200%2C24407665%2C24407914%2C24408220%2C24411766%2C24413105%2C24413820%2C24414162%2C24415866%2C24416354%2C24420756%2C24421162%2C24425861%2C24428962%2C24590921%2C39322504%2C39322574%2C39322694%2C39322707&ns=yt&plid=AAXusD4TIOMjS5N4&el=detailpage&len=246&of=Jx1iRksbq-rB9N1KSijZLQ&osid=MWU2NzBjYTI%3AAOeUNAagU8UyWDUJIki5raGHy29-60-yTA&uga=29&vm=CAEQABgEOjJBUEV3RWxUNmYzMXNMMC1MYVpCVnRZTmZWMWw1OWVZX2ZOcUtCSkphQ245VFZwOXdTQWJbQVBta0tETEpWNXI1SlNIWEJERXdHeFhXZVllNXBUemt5UHR4WWZEVzFDblFUSmdla3BKX2R0dXk3bzFORWNBZmU5YmpYZnlzb3doUE5UU0FoVGRWa0xIaXJqSWgB",
                      "headers": [
                        {
                          "headerType": "USER_AUTH"
                        },
                        {
                          "headerType": "VISITOR_ID"
                        },
                        {
                          "headerType": "PLUS_PAGE_ID"
                        }
                      ]
                    },
                    "videostatsDelayplayUrl": {(as above)},
                    "videostatsWatchtimeUrl": {(as above)},
                    "ptrackingUrl": {(as above)},
                    "qoeUrl": {(as above)},
                    "atrUrl": {(as above)},
                    "videostatsScheduledFlushWalltimeSeconds": [
                      10,
                      20,
                      30
                    ],
                    "videostatsDefaultFlushIntervalSeconds": 40
                },
                "videoDetails": {
                    "videoId": "AjXQiKP5kMs",
                    "title": "Sparks",
                    "lengthSeconds": "245",
                    "channelId": "UCvCk2zFqkCYzpnSgWfx0qOg",
                    "isOwnerViewing": false,
                    "isCrawlable": false,
                    "thumbnail": {
                        "thumbnails": []
                    },
                    "allowRatings": true,
                    "viewCount": "12",
                    "author": "Thomas Bergersen",
                    "isPrivate": true,
                    "isUnpluggedCorpus": false,
                    "musicVideoType": "MUSIC_VIDEO_TYPE_PRIVATELY_OWNED_TRACK",
                    "isLiveContent": false
                },
                "microformat": {
                    "microformatDataRenderer": {
                        "urlCanonical": "https://music.youtube.com/watch?v=AjXQiKP5kMs",
                        "title": "Sparks - YouTube Music",
                        "description": "Uploaded to YouTube via YouTube Music Sparks",
                        "thumbnail": {
                            "thumbnails": [
                                {
                                    "url": "https://i.ytimg.com/vi/AjXQiKP5kMs/hqdefault.jpg",
                                    "width": 480,
                                    "height": 360
                                }
                            ]
                        },
                        "siteName": "YouTube Music",
                        "appName": "YouTube Music",
                        "androidPackage": "com.google.android.apps.youtube.music",
                        "iosAppStoreId": "1017492454",
                        "iosAppArguments": "https://music.youtube.com/watch?v=AjXQiKP5kMs",
                        "ogType": "video.other",
                        "urlApplinksIos": "vnd.youtube.music://music.youtube.com/watch?v=AjXQiKP5kMs&feature=applinks",
                        "urlApplinksAndroid": "vnd.youtube.music://music.youtube.com/watch?v=AjXQiKP5kMs&feature=applinks",
                        "urlTwitterIos": "vnd.youtube.music://music.youtube.com/watch?v=AjXQiKP5kMs&feature=twitter-deep-link",
                        "urlTwitterAndroid": "vnd.youtube.music://music.youtube.com/watch?v=AjXQiKP5kMs&feature=twitter-deep-link",
                        "twitterCardType": "player",
                        "twitterSiteHandle": "@YouTubeMusic",
                        "schemaDotOrgType": "http://schema.org/VideoObject",
                        "noindex": true,
                        "unlisted": true,
                        "paid": false,
                        "familySafe": true,
                        "pageOwnerDetails": {
                            "name": "Music Library Uploads",
                            "externalChannelId": "UCvCk2zFqkCYzpnSgWfx0qOg",
                            "youtubeProfileUrl": "http://www.youtube.com/channel/UCvCk2zFqkCYzpnSgWfx0qOg"
                        },
                        "videoDetails": {
                            "externalVideoId": "AjXQiKP5kMs",
                            "durationSeconds": "246",
                            "durationIso8601": "PT4M6S"
                        },
                        "linkAlternates": [
                            {
                                "hrefUrl": "android-app://com.google.android.youtube/http/youtube.com/watch?v=AjXQiKP5kMs"
                            },
                            {
                                "hrefUrl": "ios-app://544007664/http/youtube.com/watch?v=AjXQiKP5kMs"
                            },
                            {
                                "hrefUrl": "https://www.youtube.com/oembed?format=json&url=https%3A%2F%2Fmusic.youtube.com%2Fwatch%3Fv%3DAjXQiKP5kMs",
                                "title": "Sparks",
                                "alternateType": "application/json+oembed"
                            },
                            {
                                "hrefUrl": "https://www.youtube.com/oembed?format=xml&url=https%3A%2F%2Fmusic.youtube.com%2Fwatch%3Fv%3DAjXQiKP5kMs",
                                "title": "Sparks",
                                "alternateType": "text/xml+oembed"
                            }
                        ],
                        "viewCount": "12",
                        "publishDate": "1969-12-31",
                        "category": "Music",
                        "uploadDate": "1969-12-31"
                    }
                }
            }

        """

        response = self._player_response(video_id, signature_timestamp)
        keys = ["videoDetails", "playabilityStatus", "streamingData", "microformat", "playbackTracking"]
        for k in list(response.keys()):
            if k not in keys:
                del response[k]
        return response

    def get_track(self, video_id: str):
        return CoreTrack(**self._player_response(video_id)["videoDetails"])

    def get_song_related(self, browse_id: str):
        """
        Gets related content for a song. Equivalent to the content
        shown in the "Related" tab of the watch panel.

        :param browse_id: The `related` key  in the `get_watch_playlist` response.

        Example::

            [
              {
                "title": "You might also like",
                "contents": [
                  {
                    "title": "High And Dry",
                    "videoId": "7fv84nPfTH0",
                    "artists": [{
                        "name": "Radiohead",
                        "id": "UCr_iyUANcn9OX_yy9piYoLw"
                      }],
                    "thumbnails": [
                      {
                        "url": "https://lh3.googleusercontent.com/TWWT47cHLv3yAugk4h9eOzQ46FHmXc_g-KmBVy2d4sbg_F-Gv6xrPglztRVzp8D_l-yzOnvh-QToM8s=w60-h60-l90-rj",
                        "width": 60,
                        "height": 60
                      }
                    ],
                    "isExplicit": false,
                    "album": {
                      "name": "The Bends",
                      "id": "MPREb_xsmDKhqhQrG"
                    }
                  }
                ]
              },
              {
                "title": "Recommended playlists",
                "contents": [
                  {
                    "title": "'90s Alternative Rock Hits",
                    "playlistId": "RDCLAK5uy_m_h-nx7OCFaq9AlyXv78lG0AuloqW_NUA",
                    "thumbnails": [...],
                    "description": "Playlist • YouTube Music"
                  }
                ]
              },
              {
                "title": "Similar artists",
                "contents": [
                  {
                    "title": "Noel Gallagher",
                    "browseId": "UCu7yYcX_wIZgG9azR3PqrxA",
                    "subscribers": "302K",
                    "thumbnails": [...]
                  }
                ]
              },
              {
                "title": "Oasis",
                "contents": [
                  {
                    "title": "Shakermaker",
                    "year": "2014",
                    "browseId": "MPREb_WNGQWp5czjD",
                    "thumbnails": [...]
                  }
                ]
              },
              {
                "title": "About the artist",
                "contents": "Oasis were a rock band consisting of Liam Gallagher, Paul ... (full description shortened for documentation)"
              }
            ]
        """
        if not browse_id:
            raise Exception("Invalid browseId provided.")

        response = self._send_request("browse", {"browseId": browse_id})
        sections = nav(response, ["contents"] + SECTION_LIST)
        return parse_mixed_content(sections)

    def get_lyrics(self, browse_id: str) -> Dict:
        """
        Returns lyrics of a song or video.

        :param browse_id: Lyrics browse id obtained from `get_watch_playlist`
        :return: Dictionary with song lyrics.

        Example::

            {
                "lyrics": "Today is gonna be the day\\nThat they're gonna throw it back to you\\n",
                "source": "Source: LyricFind"
            }

        """
        lyrics = {}
        if not browse_id:
            raise Exception("Invalid browseId provided. This song might not have lyrics.")

        response = self._send_request("browse", {"browseId": browse_id})
        lyrics["lyrics"] = nav(
            response, ["contents"] + SECTION_LIST_ITEM + DESCRIPTION_SHELF + DESCRIPTION, True
        )
        lyrics["source"] = nav(
            response, ["contents"] + SECTION_LIST_ITEM + DESCRIPTION_SHELF + ["footer"] + RUN_TEXT, True
        )

        return lyrics

    def get_basejs_url(self):
        """
        Extract the URL for the `base.js` script from YouTube Music.

        :return: URL to `base.js`
        """
        response = self._send_get_request(url=YTM_DOMAIN)
        match = re.search(r'jsUrl"\s*:\s*"([^"]+)"', response.text)
        if match is None:
            raise Exception("Could not identify the URL for base.js player.")

        return YTM_DOMAIN + match.group(1)

    def get_signature_timestamp(self, url: Optional[str] = None) -> int:
        """
        Fetch the `base.js` script from YouTube Music and parse out the
        `signatureTimestamp` for use with :py:func:`get_song`.

        :param url: Optional. Provide the URL of the `base.js` script. If this
            isn't specified a call will be made to :py:func:`get_basejs_url`.
        :return: `signatureTimestamp` string
        """
        if url is None:
            url = self.get_basejs_url()
        response = self._send_get_request(url=url)
        match = re.search(r"signatureTimestamp[:=](\d+)", response.text)
        if match is None:
            raise Exception("Unable to identify the signatureTimestamp.")

        return int(match.group(1))

    def get_taste_profile(self) -> Dict:
        """
        Fetches suggested artists from taste profile (music.youtube.com/tasteprofile).
        Tasteprofile allows users to pick artists to update their recommendations.
        Only returns a list of suggested artists, not the actual list of selected entries

        :return: Dictionary with artist and their selection & impression value

        Example::

            {
                "Drake": {
                    "selectionValue": "tastebuilder_selection=/m/05mt_q"
                    "impressionValue": "tastebuilder_impression=/m/05mt_q"
                }
            }

        """

        response = self._send_request("browse", {"browseId": "FEmusic_tastebuilder"})
        profiles = nav(response, TASTE_PROFILE_ITEMS)

        taste_profiles = {}
        for itemList in profiles:
            for item in itemList["tastebuilderItemListRenderer"]["contents"]:
                artist = nav(item["tastebuilderItemRenderer"], TASTE_PROFILE_ARTIST)[0]["text"]
                taste_profiles[artist] = {
                    "selectionValue": item["tastebuilderItemRenderer"]["selectionFormValue"],
                    "impressionValue": item["tastebuilderItemRenderer"]["impressionFormValue"],
                }
        return taste_profiles

    def set_taste_profile(self, artists: List[str], taste_profile: Optional[Dict] = None) -> None:
        """
        Favorites artists to see more recommendations from the artist.
        Use :py:func:`get_tasteprofile` to see which artists are available to be recommended

        :param artists: A List with names of artists, must be contained in the tasteprofile
        :param taste_profile: tasteprofile result from :py:func:`get_tasteprofile`.
            Pass this if you call :py:func:`get_tasteprofile` anyway to save an extra request.
        :return: None if successful
        """

        if taste_profile is None:
            taste_profile = self.get_taste_profile()
        form_data = {
            "impressionValues": [taste_profile[profile]["impressionValue"] for profile in taste_profile],
            "selectedValues": [],
        }

        for artist in artists:
            if artist not in taste_profile:
                raise Exception("The artist, {}, was not present in taste!".format(artist))
            form_data["selectedValues"].append(taste_profile[artist]["selectionValue"])

        self._send_request("browse", {"browseId": "FEmusic_home", "formData": form_data})
