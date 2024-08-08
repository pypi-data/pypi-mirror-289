import re

from .utils import *
from ..speed_nav import nav2


def parse_pl_song_artists(data, index, as_album=None):
    flex_item = get_flex_column_item(data, index)
    if not flex_item:
        # when it's an album and no per-track artists are displayed,
        # assume album artists == track artists
        return None if as_album is None else as_album["artists"]

    artists = artists_from_runs(flex_item["text"]["runs"], 0)
    # check if track came from album without linked artists
    if (
        len(artists) == 1
        and artists[0]["id"] is None
        and ("&" in artists[0]["name"] or "," in artists[0]["name"])
    ):
        # rsplit and pray that artist doesn't have an ampersand in their name
        seperated = artists[0]["name"].rsplit(" & ", 1)
        if len(seperated) == 1:
            parsed = seperated[0]
        else:
            parsed = [item.rstrip().lstrip() for item in seperated[0].split(",") if item] + [seperated[-1]]

        # try to fill with name and id from album artists when possible
        return [
            next((f for f in as_album["artists"] if f["name"].lower() == x.lower()), {"name": x, "id": None})
            if as_album
            else {"name": x, "id": None}
            for x in parsed
        ]

    return artists


def parse_id_name(sub_run):
    """Return id and name from an artist or user subtitle runs"""
    return {
        "id": nav2.navigation_browse_id(sub_run, default=None),
        "name": raw.replace('\u200b', '') if (raw := nav2.text(sub_run, default=None)) else None,
    }


def artists_from_runs(runs, offset=2):
    """Parse artists name and id from runs WITH separators"""
    if not runs:
        return []

    return [parse_id_name(runs[idx]) for idx in range(offset, len(runs), 2)]


def parse_song_runs(runs, search_result=False):
    parsed = {"artists": []}
    for i, run in enumerate(runs):
        if i % 2:  # uneven items are always separators
            continue

        if "navigationEndpoint" in run:  # artist or album
            item = parse_id_name(run)

            if item["id"] and (
                    item["id"].startswith("MPRE") or    # album
                    "release_detail" in item["id"] or   # something
                    item['id'].startswith('MPSPPL')     # podcast "album"(?)    ie 'omgoQzKyLJw'
            ):  # album
                parsed["album"] = item
            else:  # artist
                parsed["artists"].append(item)

        else:
            # note: YT uses non-breaking space \xa0 to separate number and magnitude
            if re.match(r"^\d([^ ])* [^ ]*$", run["text"]) and i > 0:
                parsed["view_count"] = parse_real_count(run)

            elif re.match(r"^(\d+:)*\d+:\d+$", run["text"]):
                parsed["duration_s"] = parse_duration(run["text"])

            elif re.match(r"^\d{4}$", run["text"]):
                parsed["year"] = int(run["text"])

            elif not search_result:  # artist without id unless search result -> result type
                parsed["artists"].append({"name": run["text"], "id": None})

    return parsed


def parse_song_album(data, index):
    flex_item = get_flex_column_item(data, index)
    if not flex_item:
        return {"id": None, "name": None}
    else:
        return {"name": get_item_text(data, index), "id": get_browse_id(flex_item, 0)}


def parse_song_library_status(item) -> bool:
    """Returns True if song is in the library"""
    return nav2.icon_type(item, default=None) == "LIBRARY_SAVED"


def parse_song_menu_tokens(item):
    toggle_menu = item[TOGGLE_MENU]

    library_add_token = nav2.default_token(toggle_menu, default=None)
    library_remove_token = nav2.toggled_token(toggle_menu, default=None)

    in_library = parse_song_library_status(item)
    if in_library:
        library_add_token, library_remove_token = library_remove_token, library_add_token

    return {"add": library_add_token, "remove": library_remove_token}


# todo: ensure this works with disliked
def parse_like_status(service):
    if service is None:
        return None
    return next((x for x in ["LIKE", "INDIFFERENT"] if x != service["likeEndpoint"]["status"]), None)
