import pytest

from moretunes.youtube.exceptions import WrongAuthType


class TestLibrary:
    def test_get_library_playlists(self, config, yt_oauth, yt_empty):
        playlists = yt_oauth.get_library_playlists(50)
        assert len(playlists) > 25

        playlists = yt_oauth.get_library_playlists(None)
        assert len(playlists) >= config.getint("limits", "library_playlists")

        playlists = yt_empty.get_library_playlists()
        assert len(playlists) <= 1  # "Episodes saved for later"

    def test_get_library_songs(self, config, yt_oauth, yt_empty):
        with pytest.raises(Exception):
            yt_oauth.get_library_songs(None, True)
        songs = yt_oauth.get_library_songs(100)
        assert len(songs) >= 100
        songs = yt_oauth.get_library_songs(200, validate_responses=True)
        assert len(songs) >= config.getint("limits", "library_songs")
        songs = yt_oauth.get_library_songs(order="a_to_z")
        assert len(songs) >= 25
        with pytest.raises(Exception):
            yt_oauth.get_library_songs(order="upsidedown")

        songs = yt_empty.get_library_songs()
        assert len(songs) == 0

    def test_get_library_albums(self, yt_oauth, yt_brand, yt_empty):
        albums = yt_oauth.get_library_albums(100)
        assert len(albums) > 50
        for album in albums:
            assert "playlist_id" in album
        albums = yt_brand.get_library_albums(100, order="a_to_z")
        assert len(albums) > 50
        albums = yt_brand.get_library_albums(100, order="z_to_a")
        assert len(albums) > 50
        albums = yt_brand.get_library_albums(100, order="recently_added")
        assert len(albums) > 50
        albums = yt_empty.get_library_albums()
        assert len(albums) == 0

    def test_get_library_artists(self, config, yt_auth, yt_oauth, yt_brand, yt_empty):
        artists = yt_auth.get_library_artists(50)
        assert len(artists) > 40
        artists = yt_oauth.get_library_artists(order="a_to_z", limit=50)
        assert len(artists) > 40
        artists = yt_brand.get_library_artists(limit=None)
        assert len(artists) > config.getint("limits", "library_artists")
        artists = yt_empty.get_library_artists()
        assert len(artists) == 0

    def test_get_library_subscriptions(self, config, yt_brand, yt_empty):
        artists = yt_brand.get_library_subscriptions(50)
        assert len(artists) > 40
        artists = yt_brand.get_library_subscriptions(order="z_to_a")
        assert len(artists) > 20
        artists = yt_brand.get_library_subscriptions(limit=None)
        assert len(artists) > config.getint("limits", "library_subscriptions")
        artists = yt_empty.get_library_subscriptions()
        assert len(artists) == 0

    def test_get_liked_songs(self, yt_brand, yt_empty, yt_oauth, liked_song_id):
        songs = yt_oauth.get_liked_songs()
        assert len(songs["tracks"]) == 100  # no limit specified, defaults to 100, no continuations requested
        match = next((track for track in songs["tracks"] if track["video_id"] == liked_song_id), None)
        assert match is not None
        assert match["in_library"]
        assert match["like_status"] == "LIKE"
        assert match["album"]["id"] is not None

        songs = yt_brand.get_liked_songs(200)
        assert len(songs["tracks"]) > 100
        songs = yt_empty.get_liked_songs()
        assert songs["track_count"] == 0

    def test_get_history(self, yt_oauth):
        songs = yt_oauth.get_history()
        assert len(songs) > 0

    def test_manipulate_history_items(self, yt_auth, sample_video):
        song = yt_auth.get_song(sample_video)
        response = yt_auth.add_history_item(song)
        assert response.status_code == 204
        songs = yt_auth.get_history()
        assert len(songs) > 0
        response = yt_auth.remove_history_items([songs[0]["feedback_token"]])
        assert "feedbackResponses" in response

    def test_rate_song(self, yt_auth, sample_video):
        response = yt_auth.rate_song(sample_video, "LIKE")
        assert "actions" in response
        response = yt_auth.rate_song(sample_video, "DISLIKE")
        assert "actions" in response
        response = yt_auth.rate_song(sample_video, "HUH?")
        assert response is None
        response = yt_auth.rate_song(sample_video, "LIKE")
        assert "actions" in response
        response = yt_auth.rate_song(sample_video, "INDIFFERENT")
        assert "actions" in response

    def test_edit_song_library_status(self, yt_brand, sample_album):
        album = yt_brand.get_album(sample_album)
        response = yt_brand.edit_song_library_status(album["tracks"][0]["feedback_tokens"]["add"])
        album = yt_brand.get_album(sample_album)
        assert album["tracks"][0]["in_library"]
        assert response["feedbackResponses"][0]["isProcessed"]
        response = yt_brand.edit_song_library_status(album["tracks"][0]["feedback_tokens"]["remove"])
        album = yt_brand.get_album(sample_album)
        assert not album["tracks"][0]["in_library"]
        assert response["feedbackResponses"][0]["isProcessed"]

    def test_rate_playlist(self, yt_auth):
        response = yt_auth.rate_playlist("OLAK5uy_l3g4WcHZsEx_QuEDZzWEiyFzZl6pL0xZ4", "LIKE")
        assert "actions" in response
        response = yt_auth.rate_playlist("OLAK5uy_l3g4WcHZsEx_QuEDZzWEiyFzZl6pL0xZ4", "INDIFFERENT")
        assert "actions" in response

    def test_subscribe_artists(self, yt_auth, yt):
        yt_auth.subscribe_artists(["UCUDVBtnOQi4c7E8jebpjc9Q", "UCiMhD4jzUqG-IgPzUmmytRQ"])
        yt_auth.subscribe_artist("UCoIyS9hbe-yyxoDNwT4nvfw")
        yt_auth.unsubscribe_artists(["UCoIyS9hbe-yyxoDNwT4nvfw", "UCiMhD4jzUqG-IgPzUmmytRQ"])
        yt_auth.unsubscribe_artists(["UCUDVBtnOQi4c7E8jebpjc9Q"])

        with pytest.raises(WrongAuthType):
            yt.subscribe_artists(["UCUDVBtnOQi4c7E8jebpjc9Q"])
