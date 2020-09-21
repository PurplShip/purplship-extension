import math
from typing import Optional
from purplship.core import Settings as BaseSettings
from purplship.core.utils import Element, export


class Settings(BaseSettings):
    """Amazon connection settings."""

    @property
    def carrier_name(self):
        return "amazon"
