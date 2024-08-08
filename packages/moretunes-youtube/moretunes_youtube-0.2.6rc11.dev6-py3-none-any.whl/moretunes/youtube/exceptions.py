class APIException(Exception):
    """Error response from youtube api"""


class WrongAuthType(Exception):
    """Function call unavailable with current authentication type"""


class ArtistIsUserException(ValueError):
    """Requested channel appears to be a user rather than artist"""


class API404Exception(Exception):
    """Resource not found."""
