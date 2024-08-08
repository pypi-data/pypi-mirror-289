"""protocol that defines the functions available to mixins"""
from typing import Dict, Optional, Protocol

from requests import Response

from ..auth.types import AuthType
from ..parsers.i18n import Parser


class MixinProtocol(Protocol):
    """protocol that defines the functions available to mixins"""

    auth_type: AuthType

    parser: Parser

    proxies: Optional[Dict[str, str]]

    warnings_enabled: bool

    def warning_print(self, *args) -> None:
        """prints if warnings are enabled for instance"""

    def _check_auth(self, specific_type: Optional[AuthType] = None) -> None:
        """checks if self has authentication"""

    def _send_request(self, endpoint: str, body: Dict, additional_params: str = "") -> Dict:
        """for sending post requests to YouTube Music"""

    def _send_get_request(self, url: str, params: Optional[Dict] = None) -> Response:
        """for sending get requests to YouTube Music"""

    @property
    def headers(self) -> Dict[str, str]:
        """property for getting request headers"""
