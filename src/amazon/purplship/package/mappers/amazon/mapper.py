from typing import List, Tuple
from purplship.package.mapper import Mapper as BaseMapper
from purplship.package.mappers.amazon.settings import Settings
from purplship.core.models import (
    RateRequest,
    ShipmentRequest,
    ShipmentDetails,
    RateDetails,
    Message,
)


class Mapper(BaseMapper):
    settings: Settings
