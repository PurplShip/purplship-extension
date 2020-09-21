from jstruct import struct, JList, JStruct, REQUIRED
from typing import List, Optional


@struct
class Error:
    code: Optional[str] = None
    message: Optional[str] = None
    details: Optional[str] = None


@struct
class Insurance:
    CurrencyCode: Optional[str] = None
    Amount: Optional[int] = None


@struct
class Address:
    Name: Optional[str] = None
    AddressLine1: Optional[str] = None
    AddressLine2: Optional[str] = None
    AddressLine3: Optional[str] = None
    DistrictOrCounty: Optional[str] = None
    Email: Optional[str] = None
    City: Optional[str] = None
    StateOrProvinceCode: Optional[str] = None
    PostalCode: Optional[str] = None
    CountryCode: Optional[str] = None
    Phone: Optional[str] = None


@struct
class ValueAsDimension:
    value: Optional[int] = None
    unit: Optional[str] = None


@struct
class Weight:
    Value: Optional[int] = None
    Unit: Optional[str] = None


@struct
class AdditionalSellerInput:
    DataType: Optional[str] = None
    ValueAsString: Optional[str] = None
    ValueAsBoolean: Optional[bool] = None
    ValueAsInteger: Optional[int] = None
    ValueAsTimestamp: Optional[str] = None
    ValueAsAddress: Address = JStruct[Address]
    ValueAsWeight: Weight = JStruct[Weight]
    ValueAsDimension: ValueAsDimension = JStruct[ValueAsDimension]
    ValueAsCurrency: Insurance = JStruct[Insurance]


@struct
class ItemLevelSellerInputs:
    AdditionalInputFieldName: Optional[str] = None
    AdditionalSellerInput: AdditionalSellerInput = JStruct[AdditionalSellerInput]


@struct
class Item:
    OrderItemId: Optional[str] = None
    Quantity: Optional[int] = None
    ItemWeight: Weight = JStruct[Weight]
    ItemDescription: Optional[str] = None
    TransparencyCodeList: List[str] = []
    ItemLevelSellerInputsList: List[ItemLevelSellerInputs] = JList[ItemLevelSellerInputs]


@struct
class Dimensions:
    Length: Optional[int] = None
    Width: Optional[int] = None
    Unit: Optional[str] = None


@struct
class FileContents:
    Contents: Optional[str] = None
    FileType: Optional[str] = None
    Checksum: Optional[str] = None


@struct
class Label:
    CustomTextForLabel: Optional[str] = None
    Dimensions: Dimensions = JStruct[Dimensions]
    FileContents: FileContents = JStruct[FileContents]
    LabelFormat: Optional[str] = None
    StandardIdForLabel: Optional[str] = None


@struct
class PackageDimensions:
    Length: Optional[int] = None
    Width: Optional[int] = None
    Height: Optional[int] = None
    Unit: Optional[str] = None
    PredefinedPackageDimensions: Optional[str] = None


@struct
class AvailableFormatOptions:
    IncludePackingSlipWithLabel: bool
    LabelFormat: Optional[str] = None


@struct
class AvailableCarrierWillPickUpOption:
    CarrierWillPickUpOption: Optional[str] = None
    Charge: Insurance = JStruct[Insurance]


@struct
class AvailableDeliveryExperienceOption:
    DeliveryExperienceOption: Optional[str] = None
    Charge: Insurance = JStruct[Insurance]


@struct
class AvailableShippingServiceOptions:
    AvailableCarrierWillPickUpOptions: List[AvailableCarrierWillPickUpOption] = JList[AvailableCarrierWillPickUpOption]
    AvailableDeliveryExperienceOptions: List[AvailableDeliveryExperienceOption] = JList[AvailableDeliveryExperienceOption]


@struct
class ShippingServiceOptions:
    DeliveryExperience: Optional[str] = None
    DeclaredValue: Insurance = JStruct[Insurance]
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
    Rate: Insurance = JStruct[Insurance]
    ShippingServiceOptions: ShippingServiceOptions = JStruct[ShippingServiceOptions]
    AvailableShippingServiceOptions: AvailableShippingServiceOptions = JStruct[AvailableShippingServiceOptions]
    AvailableLabelFormats: List[str] = []
    AvailableFormatOptionsForLabel: List[AvailableFormatOptions] = JList[AvailableFormatOptions]
    RequiresAdditionalSellerInputs: Optional[bool] = None


@struct
class Payload:
    ShipmentId: Optional[str] = None
    AmazonOrderId: Optional[str] = None
    SellerOrderId: Optional[str] = None
    ItemList: List[Item] = JList[Item]
    ShipFromAddress: Address = JStruct[Address]
    ShipToAddress: Address = JStruct[Address]
    PackageDimensions: PackageDimensions = JStruct[PackageDimensions]
    Weight: Weight = JStruct[Weight]
    Insurance: Insurance = JStruct[Insurance]
    ShippingService: ShippingService = JStruct[ShippingService]
    Label: Label = JStruct[Label]
    Status: Optional[str] = None
    TrackingId: Optional[str] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None


@struct
class CancelShipementRequest:
    payload: Payload = JStruct[Payload]
    errors: List[Error] = JList[Error]
