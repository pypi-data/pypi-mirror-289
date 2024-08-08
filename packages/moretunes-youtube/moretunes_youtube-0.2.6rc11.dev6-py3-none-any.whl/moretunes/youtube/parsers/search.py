from .songs import *
from .utils import *


def get_search_result_type(result_type_local, result_types_local):
    if not result_type_local:
        return None
    result_types = ["artist", "playlist", "song", "video", "station", "profile", "podcast", "episode"]
    result_type_local = result_type_local.lower()
    # default to album since it's labeled with multiple values ('Single', 'EP', etc.)
    if result_type_local not in result_types_local:
        result_type = "album"
    else:
        result_type = result_types[result_types_local.index(result_type_local)]

    return result_type


def parse_top_result(data, search_result_types):
    result_type = get_search_result_type(nav(data, SUBTITLE), search_result_types)
    search_result = {"category": nav(data, CARD_SHELF_TITLE), "result_type": result_type}
    if result_type == "artist":
        subscribers = nav(data, SUBTITLE2, True)
        if subscribers:
            search_result["subscribers"] = subscribers.split(" ")[0]

        artist_info = parse_song_runs(nav(data, ["title", "runs"]))
        search_result.update(artist_info)

    if result_type in ["song", "video"]:
        on_tap = data.get("onTap")
        if on_tap:
            search_result["video_id"] = nav(on_tap, WATCH_VIDEO_ID)
            search_result["video_type"] = nav(on_tap, NAVIGATION_VIDEO_TYPE)

    if result_type in ["song", "video", "album"]:
        if result_type != "album":
            search_result["video_id"] = nav(data, ["onTap"] + WATCH_VIDEO_ID, True)
            search_result["video_type"] = nav(data, ["onTap"] + NAVIGATION_VIDEO_TYPE, True)

        search_result["title"] = nav(data, TITLE_TEXT)
        runs = nav(data, ["subtitle", "runs"])
        song_info = parse_song_runs(runs, search_result=True)
        search_result.update(song_info)

    if result_type in ["album"]:
        search_result["browse_id"] = nav(data, TITLE + NAVIGATION_BROWSE_ID, True)

    search_result["thumbnails"] = nav(data, THUMBNAILS, True)
    return search_result


def parse_search_result(data, search_result_types, result_type, category):
    default_offset = (not result_type or result_type == "album") * 2
    search_result = {"category": category}
    video_type = nav(data, PLAY_BUTTON + ["playNavigationEndpoint"] + NAVIGATION_VIDEO_TYPE, True)
    if not result_type and video_type:
        result_type = "song" if video_type == "MUSIC_VIDEO_TYPE_ATV" else "video"

    result_type = (
        get_search_result_type(get_item_text(data, 1), search_result_types)
        if not result_type
        else result_type
    )
    search_result["result_type"] = result_type

    if result_type != "artist":
        search_result["name"] = get_item_text(data, 0)

    if result_type == "artist":
        search_result["artist"] = get_item_text(data, 0)
        parse_menu_playlists(data, search_result)

    elif result_type == "album":
        search_result["type"] = get_item_text(data, 1)

    elif result_type == "playlist":
        flex_item = get_flex_column_item(data, 1)["text"]["runs"]
        has_author = len(flex_item) == default_offset + 3
        search_result["item_count"] = get_item_text(data, 1, default_offset + has_author * 2).split(" ")[0]
        search_result["author"] = None if not has_author else get_item_text(data, 1, default_offset)

    elif result_type == "station":
        search_result["video_id"] = nav(data, NAVIGATION_VIDEO_ID)
        search_result["playlist_id"] = nav(data, NAVIGATION_PLAYLIST_ID)

    elif result_type == "profile":
        search_result["name"] = get_item_text(data, 1, 2, True)

    elif result_type == "song":
        search_result["album"] = None
        if "menu" in data:
            toggle_menu = find_object_by_key(nav(data, MENU_ITEMS), TOGGLE_MENU)
            if toggle_menu:
                search_result["in_library"] = parse_song_library_status(toggle_menu)
                search_result["feedback_tokens"] = parse_song_menu_tokens(toggle_menu)

    elif result_type == "upload":
        browse_id = nav(data, NAVIGATION_BROWSE_ID, True)
        if not browse_id:  # song result
            flex_items = [nav(get_flex_column_item(data, i), ["text", "runs"], True) for i in range(2)]
            if flex_items[0]:
                search_result["video_id"] = nav(flex_items[0][0], NAVIGATION_VIDEO_ID, True)
                search_result["playlist_id"] = nav(flex_items[0][0], NAVIGATION_PLAYLIST_ID, True)
            if flex_items[1]:
                search_result.update(parse_song_runs(flex_items[1]))
            search_result["result_type"] = "song"

        else:  # artist or album result
            search_result["browse_id"] = browse_id
            if "artist" in search_result["browse_id"]:
                search_result["result_type"] = "artist"
            else:
                flex_item2 = get_flex_column_item(data, 1)
                runs = [run["text"] for i, run in enumerate(flex_item2["text"]["runs"]) if i % 2 == 0]
                if len(runs) > 1:
                    search_result["artist"] = runs[1]
                if len(runs) > 2:  # date may be missing
                    search_result["release_date"] = runs[2]
                search_result["result_type"] = "album"

    if result_type in ["song", "video"]:
        search_result["video_id"] = nav(
            data, PLAY_BUTTON + ["playNavigationEndpoint", "watchEndpoint", "videoId"], True
        )
        search_result["video_type"] = video_type

    if result_type in ["song", "video", "album"]:
        # search_result["duration"] = None
        # search_result["year"] = None
        flex_item = get_flex_column_item(data, 1)
        search_result |= parse_song_runs(flex_item["text"]["runs"])

    if result_type in ["artist", "album", "playlist", "profile"]:
        search_result["browse_id"] = nav(data, NAVIGATION_BROWSE_ID, True)

    if result_type in ["song", "album"]:
        search_result["explicit"] = 'badges' in data

    search_result["thumbnail"] = pull_thumbnail(data)

    return search_result


def parse_search_results(results, search_result_types, result_type=None, category=None):
    return [
        parse_search_result(result[MRLIR], search_result_types, result_type, category) for result in results
    ]


def get_search_params(param_filter, scope, ignore_spelling):
    filtered_param1 = "EgWKAQ"
    params = None
    if param_filter is None and scope is None and not ignore_spelling:
        return params

    if scope == "uploads":
        params = "agIYAw%3D%3D"

    if scope == "library":
        if param_filter:
            param1 = filtered_param1
            param2 = _get_param2(param_filter)
            param3 = "AWoKEAUQCRADEAoYBA%3D%3D"
        else:
            params = "agIYBA%3D%3D"

    if scope is None and param_filter:
        if param_filter == "playlists":
            params = "Eg-KAQwIABAAGAAgACgB"
            if not ignore_spelling:
                params += "MABqChAEEAMQCRAFEAo%3D"
            else:
                params += "MABCAggBagoQBBADEAkQBRAK"

        elif "playlists" in param_filter:
            param1 = "EgeKAQQoA"
            if param_filter == "featured_playlists":
                param2 = "Dg"
            else:  # community_playlists
                param2 = "EA"

            if not ignore_spelling:
                param3 = "BagwQDhAKEAMQBBAJEAU%3D"
            else:
                param3 = "BQgIIAWoMEA4QChADEAQQCRAF"

        else:
            param1 = filtered_param1
            param2 = _get_param2(param_filter)
            if not ignore_spelling:
                param3 = "AWoMEA4QChADEAQQCRAF"
            else:
                param3 = "AUICCAFqDBAOEAoQAxAEEAkQBQ%3D%3D"

    if not scope and not param_filter and ignore_spelling:
        params = "EhGKAQ4IARABGAEgASgAOAFAAUICCAE%3D"

    return params if params else f'{param1}{param2}{param3}'


def _get_param2(param_filter):
    filter_params = {
        "songs": "II",
        "videos": "IQ",
        "albums": "IY",
        "artists": "Ig",
        "playlists": "Io",
        "profiles": "JY",
        "podcasts": "JQ",
        "episodes": "JI",
    }
    return filter_params[param_filter]


def parse_search_suggestions(results, detailed_runs):
    if not results.get("contents", [{}])[0].get("searchSuggestionsSectionRenderer", {}).get("contents", []):
        return []

    raw_suggestions = results["contents"][0]["searchSuggestionsSectionRenderer"]["contents"]
    suggestions = []

    for raw_suggestion in raw_suggestions:
        if "historySuggestionRenderer" in raw_suggestion:
            suggestion_content = raw_suggestion["historySuggestionRenderer"]
            from_history = True
        else:
            suggestion_content = raw_suggestion["searchSuggestionRenderer"]
            from_history = False

        text = suggestion_content["navigationEndpoint"]["searchEndpoint"]["query"]
        runs = suggestion_content["suggestion"]["runs"]

        if detailed_runs:
            suggestions.append({"text": text, "runs": runs, "fromHistory": from_history})
        else:
            suggestions.append(text)

    return suggestions
