from typing import List
from pyeshipper.quote_reply import CarrierErrorMessageType
from purplship.core.models import Message
from purplship.core.utils.xml import Element
from purplship.carriers.eshipper.utils import Settings


def parse_error_response(response: Element, settings: Settings) -> List[Message]:
    errors = response.xpath(".//*[local-name() = $name]", name="CarrierErrorMessage")
    return [_extract_error(node, settings) for node in errors]


def _extract_error(error_node: Element, settings: Settings) -> Message:
    error = CarrierErrorMessageType()
    error.build(error_node)
    return Message(
        code="",
        message=error.errorMessage0,
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id
    )