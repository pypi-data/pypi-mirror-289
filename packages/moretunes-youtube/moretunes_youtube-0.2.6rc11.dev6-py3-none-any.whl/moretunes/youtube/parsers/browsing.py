from .songs import *
from .utils import *


def parse_list_meta(response: dict):
    data = response['contents']['twoColumnBrowseResultsRenderer']
    render = data['secondaryContents']['sectionListRenderer']

    meta = data['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents'][0]

    if 'musicEditablePlaylistDetailHeaderRenderer' in meta:
        meta = meta['musicEditablePlaylistDetailHeaderRenderer']['header']['musicResponsiveHeaderRenderer']
        playlist = {'own': True}
    else:
        meta = meta['musicResponsiveHeaderRenderer']
        playlist = {'own': False}

    play_nav = meta['buttons'][1]['musicPlayButtonRenderer']['playNavigationEndpoint']
    if not (we := play_nav.get('watchEndpoint')):
        we = play_nav['watchPlaylistEndpoint']

    playlist['id'] = we['playlistId']

    playlist["public"] = playlist['id'] != 'LM'

    if run1 := meta.get('subtitle'):
        run1 = run1['runs']
        if len(run1) == 1:
            t = run1[0]['text'].lower()
            if t in {'album', 'single', 'ep'}:
                playlist['type'] = t
                playlist['year'] = None
            else:
                try:
                    playlist['year'] = int(t)
                    playlist['type'] = None
                except ValueError:
                    playlist['type'] = t
                    playlist['year'] = None

        else:
            playlist['type'] = run1[0]['text'].lower()
            playlist['year'] = int(run1[-1]['text'])
            if len(run1) > 3:
                playlist['public'] = run1[2]['text'] == 'Public'

    if run2 := meta.get('secondSubtitle'):
        run2 = run2['runs']
        playlist['track_count'] = int(run2[-3]['text'].split()[0])
        playlist['runtime'] = run2[-1]['text']

        if len(run2) > 3:
            playlist['view_count'] = parse_real_count(run2[0])

    playlist["name"] = meta['title']['runs'][0]['text']
    playlist["thumbnail"] = meta['thumbnail']['musicThumbnailRenderer']['thumbnail']['thumbnails'][0][
        'url'].rsplit('=')[0]
    playlist['explicit'] = 'subtitleBadge' in meta

    if desc := meta.get('description'):
        playlist["description"] = desc['musicDescriptionShelfRenderer']['description']['runs'][0]['text']

    art_runs = meta['straplineTextOne'].get('runs', [])
    playlist['authors'] = [parse_id_name(art_runs[i]) for i in range(0, len(art_runs), 2)]
    if (t := meta.get('straplineThumbnail')) and art_runs:
        playlist['authors'][0]['thumbnail'] = t['musicThumbnailRenderer']['thumbnail']['thumbnails'][0]['url']

    return playlist, render


def parse_mixed_content(rows):
    items = []
    for row in rows:
        if DESCRIPTION_SHELF[0] in row:
            results = nav(row, DESCRIPTION_SHELF)
            title = nav(results, ["header"] + RUN_TEXT)
            contents = nav(results, DESCRIPTION)
        else:
            results = next(iter(row.values()))
            if "contents" not in results:
                continue
            title = nav(results, CAROUSEL_TITLE + ["text"])
            contents = []
            for result in results["contents"]:
                data = nav(result, [MTRIR], True)
                content = None
                if data:
                    page_type = nav(data, TITLE + NAVIGATION_BROWSE + PAGE_TYPE, True)
                    if page_type is None:  # song or watch_playlist
                        if nav(data, NAVIGATION_WATCH_PLAYLIST_ID, True) is not None:
                            content = parse_watch_playlist(data)
                        else:
                            content = parse_song(data)
                    elif page_type == "MUSIC_PAGE_TYPE_ALBUM":
                        content = parse_album(data)
                    elif page_type == "MUSIC_PAGE_TYPE_ARTIST":
                        content = parse_related_artist(data)
                    elif page_type == "MUSIC_PAGE_TYPE_PLAYLIST":
                        content = parse_playlist(data)
                else:
                    data = nav(result, [MRLIR], True)
                    if not data:
                        continue
                    content = parse_song_flat(data)

                contents.append(content)

        items.append({"name": title, "contents": contents})
    return items


def parse_content_list(results, parse_func, key=MTRIR):
    contents = []
    for result in results:
        contents.append(parse_func(result[key]))

    return contents


def parse_album(result):
    album = {
        "name": nav(result, TITLE_TEXT),
        "browse_id": nav(result, TITLE + NAVIGATION_BROWSE_ID),
        "playlist_id": nav(result, THUMBNAIL_OVERLAY, True),
        "thumbnail": pull_thumbnail(result, True),
        "explicit": 'subtitleBadges' in result,
    }
    runs = result['subtitle'].get('runs')
    if not runs:
        album['type'] = 'single'
        return album

    if len(runs) >= 2:
        album["type"] = runs[0]['text'].lower()

        if re.match(r'^\d{4}$', runs[2]['text']):
            album['year'] = runs[2]['text']
        else:
            album["artists"] = artists_from_runs(runs)

    # it's a single with just the year
    elif re.match(r'^\d{4}$', runs[0]['text']):
        album["type"] = "single"
        album["year"] = runs[0]['text']
    else:
        album['type'] = runs[0]['text']

    if album.get('year'):
        album['year'] = int(album['year'])
    else:
        album['year'] = None
    return album


def parse_song(result):
    song = {
        "name": nav(result, TITLE_TEXT),
        "video_id": nav(result, NAVIGATION_VIDEO_ID),
        "playlist_id": nav(result, NAVIGATION_PLAYLIST_ID, True),
        "thumbnail": pull_thumbnail(result, True),
    }
    song.update(parse_song_runs(nav(result, SUBTITLE_RUNS)))
    return song


def parse_song_flat(data):
    columns = [get_flex_column_item(data, i) for i in range(0, len(data["flexColumns"]))]
    song = {
        "name": nav(columns[0], TEXT_RUN_TEXT),
        "video_id": nav(columns[0], TEXT_RUN + NAVIGATION_VIDEO_ID, True),
        "artists": parse_pl_song_artists(data, 1),
        "thumbnail": pull_thumbnail(data),
        "explicit": nav(data, BADGE_LABEL, True) is not None,
    }
    if (
        len(columns) > 2
        and columns[2] is not None
        and "navigationEndpoint" in (targ := nav(columns[2], TEXT_RUN))
    ):
        song["album"] = parse_id_name(targ)
    else:
        song["views"] = nav(columns[1], ["text", "runs", -1, "text"]).split(" ")[0]

    return song


def parse_video(result):
    # runs = nav(result, SUBTITLE_RUNS)
    # artists_len = get_dot_separator_index(runs)

    # if not video_id:
    #     # I believe this
    #     video_id = next(
    #         (
    #             found
    #             for entry in nav(result, MENU_ITEMS)
    #             if (found := nav(entry, MENU_SERVICE + QUEUE_VIDEO_ID, True))
    #         ),
    #         None,
    #     )  # this won't match anything for episodes, None to catch iterator
    video = {'name': nav(result, TITLE_TEXT)}
    if endpoints := result['navigationEndpoint'].get('watchEndpoint'):
        video |= {
            "video_id": endpoints['videoId'],
            # "playlist_id": nav(result, NAVIGATION_PLAYLIST_ID, True),
            'video_type': endpoints['watchEndpointMusicSupportedConfigs']['watchEndpointMusicConfig']['musicVideoType'],
        }
    else:
        endpoints = result['navigationEndpoint']['browseEndpoint']
        video |= {
            'video_id': endpoints['browseId'][-11:],  # has "MPED" prefix when in browse_id form
            'video_type': 'MUSIC_VIDEO_TYPE_PODCAST_EPISODE'}

    video['thumbnail'] = f'https://i.ytimg.com/vi/{video['video_id']}'

    # it's an ~episode~ -> makes the first key a duration { "text": "%m min %s sec" } format
    # unsure if we should capture the duration for edge cases
    # could also be an unlinked artist
    runs = result['subtitle']['runs']
    if "navigationEndpoint" not in runs[0] and any(x in runs[0]["text"] for x in ["sec", "min"]):
        # result["type"] = "episode"
        # views are unavailable on episodes
        # result["views"] = None
        video["play_count"] = None
        video["artists"] = artists_from_runs(runs[2:], 0)
    else:
        # result["type"] = "song"
        # result["views"] = runs[-1]["text"].split(" ")[0]
        video["play_count"] = parse_real_count(runs[-1]) if len(runs) > 2 else -1
        video["artists"] = artists_from_runs(runs[:-2], 0)

    return video


def parse_playlist(data):
    playlist = {
        "name": nav(data, TITLE_TEXT),
        "playlist_id": nav(data, TITLE + NAVIGATION_BROWSE_ID)[2:],
        "thumbnail": pull_thumbnail(data, True),
    }
    runs = nav(data, SUBTITLE_RUNS)
    if runs:
        playlist["description"] = "".join([run["text"] for run in runs])
        if len(runs) == 3 and runs[1]["text"] == " • ":
            # genre charts from get_charts('US') are sent here...
            if runs[0]["text"] == "Chart" or runs[-1]["text"] == "YouTube Music":
                playlist["view_count"] = -1
                playlist["author"] = {"name": "YouTube Music", "id": None}
                playlist["featured_artists"] = None
            else:
                playlist["view_count"] = parse_real_count(runs[2])
                playlist["author"] = parse_id_name(runs[0])
                playlist["featured_artists"] = None
        else:
            playlist["featured_artists"] = nav(runs, ZTEXT, True)
            # fill default, maintain return format
            playlist["author"] = {"name": "YouTube Music", "id": None}
            playlist["view_count"] = -1

    return playlist


def parse_related_artist(data):
    return {
        "name": nav(data, TITLE_TEXT),
        "browse_id": nav(data, TITLE + NAVIGATION_BROWSE_ID),
        "sub_count": parse_real_count(nav(data, LAST_SUB_RUN, True)),
        "thumbnail": pull_thumbnail(data, True),
    }


def parse_watch_playlist(data):
    return {
        "name": nav(data, TITLE_TEXT),
        "playlist_id": nav(data, NAVIGATION_WATCH_PLAYLIST_ID),
        "thumbnail": pull_thumbnail(data, True),
    }
