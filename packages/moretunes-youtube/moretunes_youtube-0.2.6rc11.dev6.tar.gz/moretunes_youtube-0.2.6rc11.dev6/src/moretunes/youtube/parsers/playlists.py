from typing import List, Optional

from .songs import *


def parse_playlist_items(results, menu_entries: Optional[List[List]] = None, context=None, extra_bs=True):
    songs = []
    for result in results:
        if not (data := result.get(MRLIR, {})):
            continue
        if (name := get_item_text(data, 0) if "menu" in data else None) == "Song deleted":
            continue

        song = {
            "video_id": None,
            "name": name,
            "artists": parse_pl_song_artists(data, 1, as_album=context),
            "like_status": None,
            "in_library": None,
            "available": data.get("musicItemRendererDisplayPolicy", "GOOD_TO_GO") != UNAVAILABLE,
            "explicit": 'badges' in data,
            "video_type": None,
            "feedback_tokens": None,
        }

        if not song['available']:
            song['video_type'] = 'MUSIC_VIDEO_TYPE_UNAVAILABLE'
            if song["name"] is None:
                try:
                    song["name"] = data["flexColumns"][0][MRLIFCR]["text"]["runs"][0]["text"]
                except KeyError:
                    pass
        else:
            song["video_type"] = nav(
                data,
                MENU_ITEMS + [0, "menuNavigationItemRenderer", "navigationEndpoint"] + NAVIGATION_VIDEO_TYPE,
                True,
            )

        flex = data["flexColumns"]
        if context is None:
            song["album"] = parse_song_album(data, -1)  # liked=2 songs=3
            if "thumbnail" in data:
                # song["thumbnails"] = nav(data, THUMBNAILS)
                song["thumbnail"] = nav2.thumbnails(data)[0]['url'].rsplit('=')[0]

        # album contexts skip per-track album and thumbnail spec, but add track_numbers
        else:
            song["track_number"] = int(data['index']['runs'][0]['text']) if song["available"] else None

            if song['available']:
                song['play_count'] = parse_real_count(flex[-1][MRLIFCR]['text']['runs'][0])

        if len(flex) == 4:
            song['play_count'] = parse_real_count(flex[-2][MRLIFCR]['text']['runs'][0])

        # if the item has a menu, find its setVideoId
        if extra_bs and "menu" in data:
            song["like_status"] = nav(data, MENU_LIKE_STATUS, True)
            # playlist specific
            if context is None:
                for item in nav(data, MENU_ITEMS):
                    if "menuServiceItemRenderer" in item:
                        menu_service = nav(item, MENU_SERVICE)
                        if "playlistEditEndpoint" in menu_service:
                            song["set_video_id"] = nav(
                                menu_service, ["playlistEditEndpoint", "actions", 0, "setVideoId"], True
                            )
                            song["video_id"] = nav(
                                menu_service, ["playlistEditEndpoint", "actions", 0, "removedVideoId"], True
                            )

                    if TOGGLE_MENU in item:
                        song["feedback_tokens"] = parse_song_menu_tokens(item)
                        song["in_library"] = parse_song_library_status(item)

            # albums just search for present keys
            elif targ := next((x for x in nav(data, MENU_ITEMS) if TOGGLE_MENU in x), None):
                song["feedback_tokens"] = parse_song_menu_tokens(targ)
                song["in_library"] = parse_song_library_status(targ)

        # if item is not playable, the videoId was retrieved above
        if song["video_id"] is None:
            if (play := nav2.play_button(data, default=None)) is not None and "playNavigationEndpoint" in play:
                song["video_id"] = play["playNavigationEndpoint"]["watchEndpoint"]["videoId"]

        if "fixedColumns" in data:
            # two variations
            if "simpleText" in (fork := get_fixed_column_item(data, 0)["text"]):
                song["duration_s"] = parse_duration(fork["simpleText"])
            else:
                song["duration_s"] = parse_duration(fork["runs"][0]["text"])

        if menu_entries:
            for menu_entry in menu_entries:
                if menu_entry[-1] == "feedbackToken":
                    song["feedback_token"] = nav(data, MENU_ITEMS + menu_entry)
                else:
                    song[menu_entry[-1]] = nav(data, MENU_ITEMS + menu_entry)

        songs.append(song)

    return songs
