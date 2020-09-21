from jstruct import struct, JList, JStruct, REQUIRED
from typing import List, Optional


@struct
class Error:
    code: Optional[str] = None
    message: Optional[str] = None
    details: Optional[str] = None


@struct
class RejectedShippingService:
    CarrierName: Optional[str] = None
    ShippingServiceName: Optional[str] = None
    ShippingServiceId: Optional[str] = None
    RejectionReasonCode: Optional[str] = None
    RejectionReasonMessage: Optional[str] = None


@struct
class AvailableFormatOptions:
    IncludePackingSlipWithLabel: Optional[bool] = None
    LabelFormat: Optional[str] = None


@struct
class Rate:
    CurrencyCode: Optional[str] = None
    Amount: Optional[int] = None


@struct
class AvailableCarrierWillPickUpOption:
    CarrierWillPickUpOption: Optional[str] = None
    Charge: Rate = JStruct[Rate]


@struct
class AvailableDeliveryExperienceOption:
    DeliveryExperienceOption: Optional[str] = None
    Charge: Rate = JStruct[Rate]


@struct
class AvailableServiceOptions:
    AvailableCarrierWillPickUpOptions: List[AvailableCarrierWillPickUpOption] = JList[AvailableCarrierWillPickUpOption]
    AvailableDeliveryExperienceOptions: List[AvailableDeliveryExperienceOption] = JList[AvailableDeliveryExperienceOption]


@struct
class ServiceOptions:
    DeliveryExperience: Optional[str] = None
    DeclaredValue: Rate = JStruct[Rate]
    CarrierWillPickUp: Optional[bool] = None
    CarrierWillPickUpOption: Optional[str] = None
    LabelFormat: Optional[str] = None


@struct
class ShippingService:
    ShippingServiceName: Optional[str] = None
    CarrierName: Optional[str] = None
    ShippingServiceId: Optional[str] = None
    ShippingServiceOfferId: Optional[str] = None
    ShipDate: Optional[str] = None
    EarliestEstimatedDeliveryDate: Optional[str] = None
    LatestEstimatedDeliveryDate: Optional[str] = None
    Rate: Rate = JStruct[Rate]
    ShippingServiceOptions: ServiceOptions = JStruct[ServiceOptions]
    AvailableShippingServiceOptions: AvailableServiceOptions = JStruct[AvailableServiceOptions]
    AvailableLabelFormats: List[str] = []
    AvailableFormatOptionsForLabel: List[AvailableFormatOptions] = JList[AvailableFormatOptions]
    RequiresAdditionalSellerInputs: Optional[bool] = None


@struct
class Carrier:
    CarrierName: Optional[str] = None


@struct
class Payload:
    ShippingServiceList: List[ShippingService] = JList[ShippingService]
    RejectedShippingServiceList: List[RejectedShippingService] = JList[RejectedShippingService]
    TemporarilyUnavailableCarrierList: List[Carrier] = JList[Carrier]
    TermsAndConditionsNotAcceptedCarrierList: List[Carrier] = JList[Carrier]


@struct
class EligibleShipmentServicesResponse:
    payload: Payload = JStruct[Payload]
    errors: List[Error] = JList[Error]


@struct
class API:
    EligibleShipmentServicesResponse: EligibleShipmentServicesResponse = JStruct[EligibleShipmentServicesResponse]
