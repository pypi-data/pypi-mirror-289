class TestWatch:
    def test_get_watch_playlist(self, config, yt, yt_brand, yt_oauth):
        playlist = yt_oauth.get_watch_playlist(
            playlist_id="RDAMPLOLAK5uy_l_fKDQGOUsk8kbWsm9s86n4-nZNd2JR8Q",
            radio=True,
            limit=90,
        )
        assert len(playlist["tracks"]) >= 90
        playlist = yt_oauth.get_watch_playlist("9mWr4c_ig54", limit=50)
        assert len(playlist["tracks"]) > 45
        playlist = yt_oauth.get_watch_playlist("UoAf_y9Ok4k")  # private track
        assert len(playlist["tracks"]) >= 25
        playlist = yt.get_watch_playlist(playlist_id=config["albums"]["album_browse_id"], shuffle=True)
        assert len(playlist["tracks"]) == config.getint("albums", "album_track_length")
        playlist = yt_brand.get_watch_playlist(playlist_id=config["playlists"]["own"], shuffle=True)
        assert len(playlist["tracks"]) == config.getint("playlists", "own_length")
