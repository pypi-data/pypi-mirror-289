from typing import Dict, List

from ..parsers.browsing import (
    parse_album,
    parse_content_list,
    parse_playlist,
    parse_related_artist,
    parse_video,
)
from ..parsers.utils import get_ext, i18n, content_playlist


class Parser:
    def __init__(self, language):
        self.lang = language

    @i18n
    def get_search_result_types(self):
        return [
            _("artist"),
            _("playlist"),
            _("song"),
            _("video"),
            _("station"),
            _("profile"),
            _("podcast"),
            _("episode"),
        ]

    @i18n
    def append_channel_contents(self, channel: Dict, results: List) -> Dict:
        cat_map = {
            _("albums"): ("albums", parse_album),  # type: ignore[name-defined]
            _("singles"): ("singles", parse_album),  # type: ignore[name-defined]
            _("videos"): ("videos", parse_video),  # type: ignore[name-defined]
            _("playlists"): ("playlists", parse_playlist),  # type: ignore[name-defined]
            _("related"): ("related", parse_related_artist),  # type: ignore[name-defined]
            "featured on": ("features", parse_playlist),
        }

        for shelf in results:
            if not (render := shelf.get("musicCarouselShelfRenderer")):
                continue

            targ = render["header"]["musicCarouselShelfBasicHeaderRenderer"]["title"]["runs"][0]["text"].lower()

            # todo: add parser for "from your library" songs
            if targ not in cat_map:
                continue

            key, func = cat_map[targ]
            channel[key] = {
                'items': parse_content_list(render["contents"], func)
            }

            if key == 'videos':
                channel[key]['playlist_id'] = render['contents'][0]['musicTwoRowItemRenderer']['navigationEndpoint'][
                        'watchEndpoint']['playlistId']

        return channel
