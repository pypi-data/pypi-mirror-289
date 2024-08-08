import warnings
from random import randint
from typing import Dict, List, Optional

from ..continuations import *
from ..parsers.browsing import *
from ..parsers.library import *

from ._protocol import MixinProtocol
from ._utils import *


class LibraryMixin(MixinProtocol):
    def get_library_playlists(self, limit: int = 25) -> List[Dict]:
        """
        Retrieves the playlists in the user's library.

        :param limit: Number of playlists to retrieve. `None` retrieves them all.
        :return: List of owned playlists.

        Each item is in the following format::

            {
                'playlistId': 'PLQwVIlKxHM6rz0fDJVv_0UlXGEWf-bFys',
                'title': 'Playlist title',
                'thumbnails: [...],
                'count': 5
            }
        """
        self._check_auth()
        body = {"browseId": "FEmusic_liked_playlists"}
        endpoint = "browse"
        response = self._send_request(endpoint, body)

        results = get_library_contents(response, GRID)
        playlists = parse_content_list(results["items"][1:], parse_playlist)

        if "continuations" in results:
            request_func = lambda additional_params: self._send_request(endpoint, body, additional_params)
            parse_func = lambda contents: parse_content_list(contents, parse_playlist)
            remaining_limit = None if limit is None else (limit - len(playlists))
            playlists.extend(
                get_continuations(results, "gridContinuation", remaining_limit, request_func, parse_func)
            )

        return playlists

    def get_library_songs(
        self, limit: int = 25, validate_responses: bool = False, order: Optional[str] = None
    ) -> List[Dict]:
        """
        Gets the songs in the user's library (liked videos are not included).
        To get liked songs and videos, use :py:func:`get_liked_songs`

        :param limit: Number of songs to retrieve
        :param validate_responses: Flag indicating if responses from YTM should be validated and retried in case
            when some songs are missing. Default: False
        :param order: Order of songs to return. Allowed values: 'a_to_z', 'z_to_a', 'recently_added'. Default: Default order.
        :return: List of songs. Same format as :py:func:`get_playlist`
        """
        self._check_auth()
        body = {"browseId": "FEmusic_liked_videos"}
        validate_order_parameter(order)
        if order is not None:
            body["params"] = prepare_order_params(order)
        endpoint = "browse"
        per_page = 25

        request_func = lambda additional_params: self._send_request(endpoint, body)
        parse_func = lambda raw_response: parse_library_songs(raw_response)

        if validate_responses and limit is None:
            raise Exception("Validation is not supported without a limit parameter.")

        if validate_responses:
            validate_func = lambda parsed: validate_response(parsed, per_page, limit, 0)
            response = resend_request_until_parsed_response_is_valid(
                request_func, None, parse_func, validate_func, 3
            )
        else:
            response = parse_func(request_func(None))

        results = response["results"]
        songs = response["parsed"]
        if songs is None:
            return []

        if "continuations" in results:
            request_continuations_func = lambda additional_params: self._send_request(
                endpoint, body, additional_params
            )
            parse_continuations_func = lambda contents: parse_playlist_items(contents)

            if validate_responses:
                songs.extend(
                    get_validated_continuations(
                        results,
                        "musicShelfContinuation",
                        limit - len(songs),
                        per_page,
                        request_continuations_func,
                        parse_continuations_func,
                    )
                )
            else:
                remaining_limit = None if limit is None else (limit - len(songs))
                songs.extend(
                    get_continuations(
                        results,
                        "musicShelfContinuation",
                        remaining_limit,
                        request_continuations_func,
                        parse_continuations_func,
                    )
                )

        return songs

    def get_library_albums(self, limit: int = 25, order: Optional[str] = None) -> List[Dict]:
        """
        Gets the albums in the user's library.

        :param limit: Number of albums to return
        :param order: Order of albums to return. Allowed values: 'a_to_z', 'z_to_a', 'recently_added'. Default: Default order.
        :return: List of albums.

        Each item is in the following format::

            {
              "browseId": "MPREb_G8AiyN7RvFg",
              "playlistId": "OLAK5uy_lKgoGvlrWhX0EIPavQUXxyPed8Cj38AWc",
              "title": "Beautiful",
              "type": "Album",
              "thumbnails": [...],
              "artists": [{
                "name": "Project 46",
                "id": "UCXFv36m62USAN5rnVct9B4g"
              }],
              "year": "2015"
            }
        """
        self._check_auth()
        body = {"browseId": "FEmusic_liked_albums"}
        validate_order_parameter(order)
        if order is not None:
            body["params"] = prepare_order_params(order)

        endpoint = "browse"
        response = self._send_request(endpoint, body)
        return parse_library_albums(
            response, lambda additional_params: self._send_request(endpoint, body, additional_params), limit
        )

    def get_library_artists(self, limit: int = 25, order: Optional[str] = None) -> List[Dict]:
        """
        Gets the artists of the songs in the user's library.

        :param limit: Number of artists to return
        :param order: Order of artists to return. Allowed values: 'a_to_z', 'z_to_a', 'recently_added'. Default: Default order.
        :return: List of artists.

        Each item is in the following format::

            {
              "browseId": "UCxEqaQWosMHaTih-tgzDqug",
              "artist": "WildVibes",
              "subscribers": "2.91K",
              "thumbnails": [...]
            }
        """
        self._check_auth()
        body = {"browseId": "FEmusic_library_corpus_track_artists"}
        validate_order_parameter(order)
        if order is not None:
            body["params"] = prepare_order_params(order)
        endpoint = "browse"
        response = self._send_request(endpoint, body)
        return parse_library_artists(
            response, lambda additional_params: self._send_request(endpoint, body, additional_params), limit
        )

    def get_library_subscriptions(self, limit: int = 25, order: Optional[str] = None) -> List[Dict]:
        """
        Gets the artists the user has subscribed to.

        :param limit: Number of artists to return
        :param order: Order of artists to return. Allowed values: 'a_to_z', 'z_to_a', 'recently_added'. Default: Default order.
        :return: List of artists. Same format as :py:func:`get_library_artists`
        """
        self._check_auth()
        body = {"browseId": "FEmusic_library_corpus_artists"}
        validate_order_parameter(order)
        if order is not None:
            body["params"] = prepare_order_params(order)
        endpoint = "browse"
        response = self._send_request(endpoint, body)
        return parse_library_artists(
            response, lambda additional_params: self._send_request(endpoint, body, additional_params), limit
        )

    def get_history(self) -> List[Dict]:
        """
        Gets your play history in reverse chronological order

        :return: List of playlistItems, see :py:func:`get_playlist`
          The additional property ``played`` indicates when the playlistItem was played
          The additional property ``feedbackToken`` can be used to remove items with :py:func:`remove_history_items`
        """
        self._check_auth()

        response = self._send_request("browse", {"browseId": "FEmusic_history"})
        results = nav(response, SINGLE_COLUMN_TAB + SECTION_LIST)
        songs = []
        for content in results:
            data = nav(content, MUSIC_SHELF + ["contents"], True)
            if not data:
                error = nav(content, ["musicNotifierShelfRenderer"] + TITLE, True)
                raise Exception(error)

            song_list = parse_playlist_items(data, MENU_ENTRIES)
            for song in song_list:
                song["last_played"] = nav(content["musicShelfRenderer"], TITLE_TEXT)

            songs.extend(song_list)

        return songs

    def add_history_item(self, song):
        """
        Add an item to the account's history using the playbackTracking URI
        obtained from :py:func:`get_song`.

        :param song: Dictionary as returned by :py:func:`get_song`
        :return: Full response. response.status_code is 204 if successful
        """
        url = song["playbackTracking"]["videostatsPlaybackUrl"]["baseUrl"]
        CPNA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
        cpn = "".join((CPNA[randint(0, 256) & 63] for _ in range(0, 16)))
        params = {"ver": 2, "c": "WEB_REMIX", "cpn": cpn}
        return self._send_get_request(url, params)

    def remove_history_items(self, feedback_tokens: List[str]) -> Dict:  # pragma: no cover
        """
        Remove an item from the account's history. This method does currently not work with brand accounts

        :param feedback_tokens: Token to identify the item to remove, obtained from :py:func:`get_history`
        :return: Full response
        """
        self._check_auth()

        response = self._send_request("feedback", {"feedbackTokens": feedback_tokens})

        return response

    def rate_song(self, video_id: str, rating: str = "INDIFFERENT") -> Optional[Dict]:
        """
        Rates a song ("thumbs up"/"thumbs down" interactions on YouTube Music)

        :param video_id: Video id
        :param rating: One of 'LIKE', 'DISLIKE', 'INDIFFERENT'

          | 'INDIFFERENT' removes the previous rating and assigns no rating

        :return: Full response
        """
        self._check_auth()
        if not (endpoint := prepare_like_endpoint(rating)):
            return None

        return self._send_request(endpoint, {"target": {"videoId": video_id}})

    def edit_song_library_status(self, feedback_tokens: Optional[List[str]] = None) -> Dict:
        """
        Adds or removes a song from your library depending on the token provided.

        :param feedback_tokens: List of feedbackTokens obtained from authenticated requests
            to endpoints that return songs (i.e. :py:func:`get_album`)
        :return: Full response
        """
        self._check_auth()

        return self._send_request("feedback", {"feedbackTokens": feedback_tokens})

    def rate_playlist(self, playlist_id: str, rating: str = "INDIFFERENT") -> Optional[Dict]:
        """
        Rates a playlist/album ("Add to library"/"Remove from library" interactions on YouTube Music)
        You can also dislike a playlist/album, which has an effect on your recommendations

        :param playlist_id: Playlist id
        :param rating: One of 'LIKE', 'DISLIKE', 'INDIFFERENT'

          | 'INDIFFERENT' removes the playlist/album from the library

        :return: Full response
        """
        self._check_auth()
        if not (endpoint := prepare_like_endpoint(rating)):
            return None

        return self._send_request(endpoint, {"target": {"playlistId": playlist_id}})

    def subscribe_artist(self, channel_id: str) -> Dict:
        """
        Unsubscribe from artist. Removes the artist from your library.

        :param channel_id: Artist channel id
        :return: Full responses
        """

        self._check_auth()
        return self._send_request("subscription/subscribe", {"channelIds": [channel_id]})

    def subscribe_artists(self, channel_ids: List[str]) -> List[Dict]:
        """
        DEPRECIATED. Subscribe to artists. Adds the artists to your library.

        :param channel_ids: Artist channel ids
        :return: Full response
        """
        # self._check_auth()

        warnings.warn(
            "API no longer allows multiple subs/unsubs in a single request, " "performing sequentially.",
            DeprecationWarning,
        )

        return [self.subscribe_artist(channel_id) for channel_id in channel_ids]

    def unsubscribe_artist(self, channel_id: str) -> Dict:
        """
        Unsubscribe from artist. Removes the artist from your library

        :param channel_id: Artist channel id
        :return: Full response
        """
        self._check_auth()

        return self._send_request("subscription/unsubscribe", {"channelIds": [channel_id]})

    def unsubscribe_artists(self, channel_ids: List[str]) -> List[Dict]:
        """
        DEPRECIATED. Unsubscribe from artists. Removes the artists from your library

        :param channel_ids: Artist channel ids
        :return: Full responses
        """
        # self._check_auth()

        warnings.warn(
            "API no longer allows multiple subs/unsubs in a single request, " "performing sequentially.",
            DeprecationWarning,
        )

        return [self.unsubscribe_artist(channel_id) for channel_id in channel_ids]
