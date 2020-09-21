"""PurplShip freightcom connection settings."""

import attr
from purplship.providers.amazon.utils import Settings as BaseSettings


@attr.s(auto_attribs=True)
class Settings(BaseSettings):
    """Amazon connection settings."""

    id: str = None
    test: bool = False
    carrier_id: str = "amazon"
