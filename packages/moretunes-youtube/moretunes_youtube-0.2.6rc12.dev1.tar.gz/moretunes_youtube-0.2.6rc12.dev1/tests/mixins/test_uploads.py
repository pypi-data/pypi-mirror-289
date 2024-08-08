import tempfile

import pytest

from tests.conftest import get_resource
from moretunes.youtube.exceptions import WrongAuthType


class TestUploads:
    def test_get_library_upload_songs(self, yt_oauth, yt_empty):
        results = yt_oauth.get_library_upload_songs(50, order="z_to_a")
        assert len(results) > 25

        results = yt_empty.get_library_upload_songs(100)
        assert len(results) == 0

    def test_get_library_upload_albums(self, config, yt_oauth, yt_empty):
        results = yt_oauth.get_library_upload_albums(50, order="a_to_z")
        assert len(results) > 40

        albums = yt_oauth.get_library_upload_albums(None)
        assert len(albums) >= config.getint("limits", "library_upload_albums")

        results = yt_empty.get_library_upload_albums(100)
        assert len(results) == 0

    def test_get_library_upload_artists(self, config, yt_oauth, yt_empty):
        artists = yt_oauth.get_library_upload_artists(None)
        assert len(artists) >= config.getint("limits", "library_upload_artists")

        results = yt_oauth.get_library_upload_artists(50, order="recently_added")
        assert len(results) >= 25

        results = yt_empty.get_library_upload_artists(100)
        assert len(results) == 0

    def test_upload_song_exceptions(self, config, yt_auth, yt_oauth):
        with pytest.raises(FileNotFoundError, match="The provided file does not exist."):
            yt_auth.upload_song("song.wav")
        with tempfile.NamedTemporaryFile(suffix="wav") as temp, pytest.raises(
            TypeError, match="The provided file type is not supported"
        ):
            yt_auth.upload_song(temp.name)
        with pytest.raises(WrongAuthType, match="Please provide BROWSER authentication"):
            yt_oauth.upload_song(config["uploads"]["file"])

    def test_upload_song(self, config, yt_auth):
        response = yt_auth.upload_song(get_resource(config["uploads"]["file"]))
        assert response.status_code == 409

    @pytest.mark.skip(reason="Do not delete uploads")
    def test_delete_upload_entity(self, yt_oauth):
        results = yt_oauth.get_library_upload_songs()
        response = yt_oauth.delete_upload_entity(results[0]["entity_id"])
        assert response == "STATUS_SUCCEEDED"

    def test_get_library_upload_album(self, config, yt_oauth):
        album = yt_oauth.get_library_upload_album(config["uploads"]["private_album_id"])
        assert len(album["tracks"]) > 0

    def test_get_library_upload_artist(self, config, yt_oauth):
        tracks = yt_oauth.get_library_upload_artist(config["uploads"]["private_artist_id"], 100)
        assert len(tracks) > 0
