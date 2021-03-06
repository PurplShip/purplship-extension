"""PurplShip freightcom connection settings."""

import attr
from purplship.providers.freightcom.utils import Settings as BaseSettings


@attr.s(auto_attribs=True)
class Settings(BaseSettings):
    """Freightcom connection settings."""

    username: str
    password: str
    id: str = None
    test: bool = False
    carrier_id: str = "freightcom"
