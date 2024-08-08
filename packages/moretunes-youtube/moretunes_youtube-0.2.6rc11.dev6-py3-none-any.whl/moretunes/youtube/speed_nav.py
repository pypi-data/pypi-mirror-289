from typing import Any, Dict, List, Literal, Optional, overload
from types import FunctionType
from functools import wraps
from inspect import isclass



CONTENT = ["contents", 0]
ZTEXT = [0, "text"]
TTEXT = [2, "text"]
RUN_TEXT = ["runs"] + ZTEXT
TAB_CONTENT = ["tabs", 0, "tabRenderer", "content"]
TAB_1_CONTENT = ["tabs", 1, "tabRenderer", "content"]
SINGLE_COLUMN = ["contents", "singleColumnBrowseResultsRenderer"]
SINGLE_COLUMN_TAB = SINGLE_COLUMN + TAB_CONTENT
SECTION = ["sectionListRenderer"]
SECTION_LIST = SECTION + ["contents"]
SECTION_LIST_ITEM = SECTION + CONTENT
ITEM_SECTION = ["itemSectionRenderer"] + CONTENT
MUSIC_SHELF = ["musicShelfRenderer"]
GRID = ["gridRenderer"]
GRID_ITEMS = GRID + ["items"]
MENU = ["menu", "menuRenderer"]
MENU_ITEMS = MENU + ["items"]
MENU_LIKE_STATUS = MENU + ["topLevelButtons", 0, "likeButtonRenderer", "likeStatus"]
MENU_SERVICE = ["menuServiceItemRenderer", "serviceEndpoint"]
TOGGLE_MENU = "toggleMenuServiceItemRenderer"
OVERLAY_RENDERER = ["musicItemThumbnailOverlayRenderer", "content", "musicPlayButtonRenderer"]
PLAY_BUTTON = ["overlay"] + OVERLAY_RENDERER
NAVIGATION_BROWSE = ["navigationEndpoint", "browseEndpoint"]
NAVIGATION_BROWSE_ID = NAVIGATION_BROWSE + ["browseId"]
PAGE_TYPE = ["browseEndpointContextSupportedConfigs", "browseEndpointContextMusicConfig", "pageType"]
WATCH_VIDEO_ID = ["watchEndpoint", "videoId"]
NAVIGATION_VIDEO_ID = ["navigationEndpoint"] + WATCH_VIDEO_ID
QUEUE_VIDEO_ID = ["queueAddEndpoint", "queueTarget", "videoId"]
NAVIGATION_PLAYLIST_ID = ["navigationEndpoint", "watchEndpoint", "playlistId"]
WATCH_PID = ["watchPlaylistEndpoint", "playlistId"]
NAVIGATION_WATCH_PLAYLIST_ID = ["navigationEndpoint"] + WATCH_PID
NAVIGATION_VIDEO_TYPE = [
    "watchEndpoint",
    "watchEndpointMusicSupportedConfigs",
    "watchEndpointMusicConfig",
    "musicVideoType",
]
TITLE = ["title", "runs", 0]
TITLE_TEXT = ["title"] + RUN_TEXT
TEXT_RUNS = ["text", "runs"]
TEXT_RUN = TEXT_RUNS + [0]
TEXT_RUN_TEXT = TEXT_RUN + ["text"]
SUBTITLE = ["subtitle"] + RUN_TEXT
SUBTITLE_RUNS = ["subtitle", "runs"]
LAST_RUN = ["runs", -1]
TEXT_LAST_RUN = ["text"] + LAST_RUN
LAST_SUB_RUN = ["subtitle"] + LAST_RUN
SUBTITLE2 = SUBTITLE_RUNS + TTEXT
SUBTITLE3 = SUBTITLE_RUNS + [4, "text"]
THUMBNAIL = ["thumbnail", "thumbnails"]
THUMBNAILS = ["thumbnail", "musicThumbnailRenderer"] + THUMBNAIL
THUMBNAIL_RENDERER = ["thumbnailRenderer", "musicThumbnailRenderer"] + THUMBNAIL
THUMBNAIL_OVERLAY = ["thumbnailOverlay"] + OVERLAY_RENDERER + ["playNavigationEndpoint"] + WATCH_PID
THUMBNAIL_CROPPED = ["thumbnail", "croppedSquareThumbnailRenderer"] + THUMBNAIL
FEEDBACK_TOKEN = ["feedbackEndpoint", "feedbackToken"]
MENU_ENTRIES = [[-1] + MENU_SERVICE + FEEDBACK_TOKEN]
BADGE_PATH = [0, "musicInlineBadgeRenderer", "accessibilityData", "accessibilityData", "label"]
BADGE_LABEL = ["badges"] + BADGE_PATH
SUBTITLE_BADGE_LABEL = ["subtitleBadges"] + BADGE_PATH
CATEGORY_TITLE = ["musicNavigationButtonRenderer", "buttonText"] + RUN_TEXT
CATEGORY_PARAMS = ["musicNavigationButtonRenderer", "clickCommand", "browseEndpoint", "params"]
UNAVAILABLE = "MUSIC_ITEM_RENDERER_DISPLAY_POLICY_GREY_OUT"
MRLIR = "musicResponsiveListItemRenderer"
MTRIR = "musicTwoRowItemRenderer"
MRLIFCR = "musicResponsiveListItemFlexColumnRenderer"
TASTE_PROFILE_ITEMS = ["contents", "tastebuilderRenderer", "contents"]
TASTE_PROFILE_ARTIST = ["title", "runs"]
SECTION_LIST_CONTINUATION = ["continuationContents", "sectionListContinuation"]
MENU_PLAYLIST_ID = MENU_ITEMS + [0, "menuNavigationItemRenderer"] + NAVIGATION_WATCH_PLAYLIST_ID
MULTI_SELECT = ["musicMultiSelectMenuItemRenderer"]
HEADER_DETAIL = ["header", "musicDetailHeaderRenderer"]
HEADER_SIDE = ["header", "musicSideAlignedItemRenderer"]
DESCRIPTION_SHELF = ["musicDescriptionShelfRenderer"]
DESCRIPTION = ["description"] + RUN_TEXT
CAROUSEL = ["musicCarouselShelfRenderer"]
IMMERSIVE_CAROUSEL = ["musicImmersiveCarouselShelfRenderer"]
CAROUSEL_CONTENTS = CAROUSEL + ["contents"]
CAROUSEL_TITLE = ["header", "musicCarouselShelfBasicHeaderRenderer"] + TITLE
CARD_SHELF_TITLE = ["header", "musicCardShelfHeaderBasicRenderer"] + TITLE_TEXT
FRAMEWORK_MUTATIONS = ["frameworkUpdates", "entityBatchUpdate", "mutations"]


def try_wrap(func):
    @wraps(func)
    def wrapped(*args, default=Exception, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, IndexError) as err:

            # allows special errors to be provided to wrap the vanilla keyerror
            if default is Exception:
                raise err
            elif isclass(default) and issubclass(default, Exception):
                # default just re-throws the error
                raise default(*err.args)
            # gives default value ie None
            return default

    return wrapped


class NavWrapper(type):
    def __new__(cls, classname, bases, class_dict):
        return type.__new__(cls, classname, bases, {
            name: (try_wrap(attr) if isinstance(attr, FunctionType) else attr)
            for name, attr in class_dict.items()
        })


class KeyNavigator(metaclass=NavWrapper):
    unavailable = "MUSIC_ITEM_RENDERER_DISPLAY_POLICY_GREY_OUT"
    MRLIR = "musicResponsiveListItemRenderer"
    MTRIR = "musicTwoRowItemRenderer"
    MRLIFCR = "musicResponsiveListItemFlexColumnRenderer"

    def content(self, root):
        return root['contents'][0]

    def text(self, root):
        return root['text']

    def ztext(self, root):
        return root[0]['text']

    def ttext(self, root):
        return root[2]['text']

    def run_text(self, root):
        # return self.ztext(root['runs'])
        return root['runs'][0]['text']

    def length_text(self, root):
        return root['lengthText']['runs'][0]['text']

    def tab_content(self, root, n=0):
        return root['tabs'][n]['tabRenderer']['content']

    def panel_render(self, root):
        # return self.tab_content(root)['musicQueueRenderer']['content']['playlistPanelRenderer']
        return root['tabs'][0]['tabRenderer']['content']['musicQueueRenderer']['content']['playlistPanelRenderer']

    def single_column(self, root):
        return root['contents']['singleColumnBrowseResultsRenderer']

    def single_column_tab(self, root):
        # return self.tab_content(self.single_column(root))
        return root['contents']['singleColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']

    def watch_next(self, root):
        return root['contents']['singleColumnMusicWatchNextResultsRenderer']['tabbedRenderer'][
            'watchNextTabbedResultsRenderer']

    def section(self, root):
        return root['sectionListRenderer']

    def section_list(self, root):
        # return self.section(root)['contents']
        return root['sectionListRenderer']['contents']

    def section_list_item(self, root):
        # return self.content(self.section(root))
        return root['sectionListRenderer']['contents'][0]

    def item_section(self, root):
        # return self.content(root['itemSectionRenderer'])
        return root['itemSectionRenderer']['contents'][0]

    def music_shelf(self, root):
        return root['musicShelfRenderer']

    def content_music_shelf(self, root):
        # return self.music_shelf(self.content(root))
        return root['contents'][0]['musicShelfRenderer']

    def grid(self, root):
        return root['gridRenderer']

    def grid_items(self, root):
        return root['gridRenderer']['items']

    def menu(self, root):
        return root['menu']['menuRenderer']

    def menu_items(self, root):
        # return self.menu(root)['items']
        return root['menu']['menuRenderer']['items']

    def menu_like_status(self, root):
        return root['menu']['menuRenderer']['topLevelButtons'][0]['likeButtonRenderer']['likeStatus']

    def menu_service(self, root):
        return root['menuServiceItemRenderer']['serviceEndpoint']

    def toggle_menu(self, root):
        return root['toggleMenuServiceItemRenderer']

    def overlay_renderer(self, root):
        return root['musicItemThumbnailOverlayRenderer']['content']['musicPlayButtonRenderer']

    def play_button(self, root):
        # return self.overlay_renderer(root['overlay'])
        return root['overlay']['musicItemThumbnailOverlayRenderer']['content']['musicPlayButtonRenderer']

    def navigation_browse(self, root):
        return root['navigationEndpoint']['browseEndpoint']

    def navigation_browse_id(self, root):
        # return self.navigation_browse(root)['browseId']
        return root['navigationEndpoint']['browseEndpoint']['browseId']

    def panel_pid(self, root):
        # return self.navigation_browse_id(root['playlistPanelVideoRenderer'])
        return root['playlistPanelVideoRenderer']['navigationEndpoint']['browseEndpoint']['browseId']

    def page_type(self, root):
        return root['browseEndpointContextSupportedConfigs']['browseEndpointContextMusicConfig']['pageType']

    def watch_video_id(self, root):
        return root['watchEndpoint']['videoId']

    def navigation_video_id(self, root):
        # return self.watch_video_id(root['navigationEndpoint'])
        return root['navigationEndpoint']['watchEndpoint']['videoId']

    def queue_video_id(self, root):
        return root['queueAddEndpoint']['queueTarget']['videoId']

    def navigation_playlist_id(self, root):
        return root['navigationEndpoint']['watchEndpoint']['playlistId']

    def watch_pid(self, root):
        return root['watchPlaylistEndpoint']['playlistId']

    def navigation_watch_playlist_id(self, root):
        # return self.watch_pid(root['navigationEndpoint'])
        return root['navigationEndpoint']['watchPlaylistEndpoint']['playlistId']

    def navigation_video_type(self, root):
        return root['watchEndpoint']['watchEndpointMusicSupportedConfigs']['watchEndpointMusicConfig']['musicVideoType']

    def nav_endpoint_video_type(self, root):
        # return self.navigation_video_type(root['navigationEndpoint'])
        return root['navigationEndpoint']['watchEndpoint']['watchEndpointMusicSupportedConfigs'][
            'watchEndpointMusicConfig']['musicVideoType']

    def title(self, root):
        return root['title']['runs'][0]

    def title_text(self, root):
        # return self.run_text(root['title'])
        return root['title']['runs'][0]['text']

    def text_runs(self, root):
        return root['text']['runs']

    def text_run(self, root):
        # return self.text_runs(root)[0]
        return root['text']['runs'][0]

    def text_run_text(self, root):
        # return self.text_run(root)['text']
        return root['text']['runs']['text']

    def subtitle(self, root):
        # return self.run_text(root['subtitle'])
        return root['subtitle']['runs'][0]['text']

    def subtitle_runs(self, root):
        return root['subtitle']['runs']

    def last_run(self, root):
        return root['runs'][-1]

    def text_last_run(self, root):
        # return self.last_run(root['text'])
        return root['text']['runs'][-1]

    def last_sub_run(self, root):
        # return self.last_run(root['subtitle'])
        return root['subtitle']['runs'][-1]

    def subtitle_n(self, root, n):
        return root['subtitle']['runs'][n]['text']

    def thumbnail(self, root):
        return root['thumbnail']['thumbnails']

    def thumbnails(self, root):
        # return self.thumbnail(root['thumbnail']['musicThumbnailRenderer'])
        return root['thumbnail']['musicThumbnailRenderer']['thumbnail']['thumbnails']

    def thumbnail_render(self, root):
        # return self.thumbnail(root['thumbnailRenderer']['musicThumbnailRenderer'])
        return root['thumbnailRenderer']['musicThumbnailRenderer']['thumbnail']['thumbnails']

    def thumbnail_overlay(self, root):
        # return self.watch_pid(self.overlay_renderer(root['thumbnailOverlay'])['playNavigationEndpoint'])
        return root['thumbnailOverlay']['watchPlaylistEndpoint']['playlistId']['playNavigationEndpoint'][
            'musicItemThumbnailOverlayRenderer']['content'][
            'musicPlayButtonRenderer']

    def thumbnail_cropped(self, root):
        # return self.thumbnail(root['thumbnail']['croppedSquareThumbnailRenderer'])
        return root['thumbnail']['croppedSquareThumbnailRenderer']['thumbnail']['thumbnails']

    def default_token(self, root):
        # return self.feedback_token(root['defaultServiceEndpoint'])
        return root['defaultServiceEndpoint']['feedbackEndpoint']['feedbackToken']

    def toggled_token(self, root):
        # return self.feedback_token(root['toggledServiceEndpoint'])
        return root['toggledServiceEndpoint']['feedbackEndpoint']['feedbackToken']

    def feedback_token(self, root):
        return root['feedbackEndpoint']['feedbackToken']

    def icon_type(self, root):
        # return self.toggle_menu(root)['defaultIcon']['iconType']
        return root['toggleMenuServiceItemRenderer']['defaultIcon']['iconType']

    def menu_entries(self, root):
        # return self.feedback_token(self.menu_service(root[-1]))
        return root[-1]['menuServiceItemRenderer']['serviceEndpoint']['feedbackEndpoint']['feedbackToken']

    def badge_path(self, root):
        return root[0]['musicInlineBaderRenderer']['accessibilityData']['accessibilityData']['label']

    def badge_label(self, root):
        # return self.badge_path(root['badges'])
        return root['badges'][0]['musicInlineBaderRenderer']['accessibilityData']['accessibilityData']['label']

    def subtitle_badge_label(self, root):
        # return self.badge_path(root['subtitleBadges'])
        return root['subtitleBadges'][0]['musicInlineBaderRenderer']['accessibilityData']['accessibilityData']['label']

    def category_title(self, root):
        # return self.run_text(root['musicNavigationButtonRenderer']['buttonText'])
        return root['musicNavigationButtonRenderer']['buttonText']['runs'][0]['text']

    def category_params(self, root):
        return root['musicNavigationButtonRenderer']['clickCommand']['browseEndpoint']['params']

    def taste_profile_items(self, root):
        return root['contents']['tastebuilderRenderer']['contents']

    def taste_profile_artist(self, root):
        return root['title']['runs']

    def section_list_continuation(self, root):
        return root['continuationContents']['sectionListContinuation']

    def menu_playlist_id(self, root):
        # return self.navigation_watch_playlist_id(self.menu_items(root)[0]['menuNavigationItemRenderer'])
        return root['menu']['menuRenderer']['items'][0]['menuNavigationItemRenderer']['navigationEndpoint'][
            'watchPlaylistEndpoint']['playlistId']

    def multi_select(self, root):
        return root['musicMultiSelectMenuItemRenderer']

    def header_detail(self, root):
        return root['header']['musicDetailHeaderRenderer']

    def header_side(self, root):
        return root['header']['musicSideAlignedItemRenderer']

    def description_shelf(self, root):
        return root['musicDescriptionShelfRenderer']

    def description(self, root):
        # return self.run_text(root['description'])
        return root['description']['runs'][0]['text']

    def carousel(self, root):
        return root['musicCarouselShelfRenderer']

    def immersive_carousel(self, root):
        return root['musicImmersiveCarouselShelfRenderer']

    def carousel_contents(self, root):
        return root['musicCarouselShelfRenderer']['contents']

    def carousel_title(self, root):
        # return self.title(root['header']['musicCarouselShelfBasicHeaderRenderer'])
        return root['header']['musicCarouselShelfBasicHeaderRenderer']['title']['runs'][0]

    def card_shelf_title(self, root):
        # return self.title_text(root['header']['musicCardShelfHeaderBasicRenderer'])
        return root['header']['musicCardShelfHeaderBasicRenderer']['title']['runs'][0]['text']

    def framework_mutations(self, root):
        return root['frameworkUpdates']['entityBatchUpdate']['mutations']
    
    def playlist_results(self, root):
        # return self.section_list_item(self.single_column_tab(root))['musicPlaylistShelfRenderer']
        return root['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content'][
            'sectionListRenderer']['contents'][0]['musicPlaylistShelfRenderer']


class Navigator(KeyNavigator):
    def __call__(self, root: Dict, items: List[Any], none_if_absent: bool = False) -> Optional[Any]:
        """ reverse compatability with old nav"""
        try:
            for k in items:
                root = root[k]
            return root
        except Exception as err:
            if none_if_absent:
                return None
            else:
                raise err

    def find_object_by_key(self, obj_list, key, nested=None, is_key=False):
        for item in obj_list:
            if nested:
                item = item[nested]
            if key in item:
                return item[key] if is_key else item
        return None

    def find_objects_by_key(self, obj_list, key, nested=None):
        objects = []
        for item in obj_list:
            if nested:
                item = item[nested]
            if key in item:
                objects.append(item)
        return objects


nav2 = Navigator()
