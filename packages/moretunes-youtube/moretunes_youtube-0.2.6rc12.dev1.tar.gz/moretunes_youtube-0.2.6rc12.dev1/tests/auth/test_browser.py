from unittest import mock

import moretunes.youtube.setup
from moretunes.youtube.setup import main


class TestBrowser:
    def test_setup_browser(self, config, browser_filepath: str):
        headers = moretunes.youtube.setup(browser_filepath, config["auth"]["headers_raw"])
        assert len(headers) >= 2
        headers_raw = config["auth"]["headers_raw"].split("\n")
        with (
            mock.patch("sys.argv", ["ytmusicapi", "browser", "--file", browser_filepath]),
            mock.patch("builtins.input", side_effect=(headers_raw + [EOFError()])),
        ):
            headers = main()
            assert len(headers) >= 2
