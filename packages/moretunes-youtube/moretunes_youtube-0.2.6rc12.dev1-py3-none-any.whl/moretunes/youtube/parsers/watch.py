from typing import Any, Dict, List

from .songs import *
from ..speed_nav import *
from ..parsers.utils import to_sec

PPVWR = "playlistPanelVideoWrapperRenderer"
PPVR = "playlistPanelVideoRenderer"


def parse_watch_playlist(results: List[Dict[str, Any]], extra_bs=True) -> List[Dict[str, Any]]:
    tracks = []

    for result in results:
        counterpart = None
        if PPVWR in result:
            counterpart = result[PPVWR]["counterpart"][0]["counterpartRenderer"][PPVR]
            result = result[PPVWR]["primaryRenderer"]

        if PPVR not in result or "unplayableText" in result[PPVR]:
            continue

        if 'videoId' not in result[PPVR]:
            continue

        track = parse_watch_track(result[PPVR], extra_bs)
        if counterpart:
            track["counterpart"] = parse_watch_track(counterpart, extra_bs)

        tracks.append(track)

    return tracks


def parse_watch_track(data, extra_bs=True):
    # contained in a try for very edge case of blank track
    #  ie zCts8Rw1WYw has one in its watch playlist for US

    track = {
        "video_id": data["videoId"],
        "name": nav2.title_text(data),
        "duration_s": to_sec(nav2.length_text(data, default=None)),
        # "thumbnail": data['thumbnail']['thumbnails'],
        "thumbnail": data['thumbnail']['thumbnails'][0]['url'].rsplit('=')[0],  # 200ms speedup
        # "feedback_tokens": feedback_tokens,
        # "like_status": like_status,
        # "in_library": library_status,
        "video_type": nav2.nav_endpoint_video_type(data, default=None)
    } | parse_song_runs(data["longBylineText"]["runs"])

    if extra_bs:
        # set the internal data

        for item in nav2.menu_items(data):
            if TOGGLE_MENU in item:
                track['library_status'] = parse_song_library_status(item)
                service = item[TOGGLE_MENU]["defaultServiceEndpoint"]
                if "feedbackEndpoint" in service:
                    track['feedback_tokens'] = parse_song_menu_tokens(item)
                if "likeEndpoint" in service:
                    track['like_status'] = parse_like_status(service)

    return track


def get_tab_browse_id(next_render, tab_id):
    if "unselectable" not in next_render["tabs"][tab_id]["tabRenderer"]:
        return next_render["tabs"][tab_id]["tabRenderer"]["endpoint"]["browseEndpoint"]["browseId"]
    else:
        return None
