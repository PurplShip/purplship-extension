from purplship.core.utils import to_xml, request as http, Element
from purplship.package.proxy import Proxy as BaseProxy
from purplship.package.mappers.amazon.settings import Settings
from purplship.core.utils.serializable import Serializable, Deserializable


class Proxy(BaseProxy):
    settings: Settings
