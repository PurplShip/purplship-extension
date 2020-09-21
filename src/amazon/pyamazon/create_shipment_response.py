from jstruct import struct, JList, JStruct, REQUIRED
from typing import Optional, List


@struct
class Error:
    code: Optional[str] = None
    message: Optional[str] = None
    details: Optional[str] = None


@struct
class InsuranceType:
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
class Dimension:
    value: Optional[int] = None
    unit: Optional[str] = None


@struct
class WeightType:
    Value: Optional[int] = None
    Unit: Optional[str] = None


@struct
class SellerInput:
    DataType: Optional[str] = None
    ValueAsString: Optional[str] = None
    ValueAsBoolean: Optional[bool] = None
    ValueAsInteger: Optional[int] = None
    ValueAsTimestamp: Optional[str] = None
    ValueAsAddress: Optional[Address] = JStruct[Address]
    ValueAsWeight: Optional[WeightType] = JStruct[WeightType]
    ValueAsDimension: Optional[Dimension] = JStruct[Dimension]
    ValueAsCurrency: Optional[InsuranceType] = JStruct[InsuranceType]


@struct
class ItemLevelSellerInputsList:
    AdditionalInputFieldName: Optional[str] = None
    AdditionalSellerInput: Optional[SellerInput] = JStruct[SellerInput]


@struct
class Item:
    OrderItemId: Optional[str] = None
    Quantity: Optional[int] = None
    ItemWeight: Optional[WeightType] = JStruct[WeightType]
    ItemDescription: Optional[str] = None
    TransparencyCodeList: List[str] = []
    ItemLevelSellerInputsList: List[ItemLevelSellerInputsList] = None


@struct
class LabelDimensions:
    Length: Optional[int] = None
    Width: Optional[int] = None
    Unit: Optional[str] = None


@struct
class FileContent:
    Contents: Optional[str] = None
    FileType: Optional[str] = None
    Checksum: Optional[str] = None


@struct
class LabelType:
    CustomTextForLabel: Optional[str] = None
    Dimensions: Optional[LabelDimensions] = JStruct[LabelDimensions]
    FileContents: Optional[FileContent] = JStruct[FileContent]
    LabelFormat: Optional[str] = None
    StandardIdForLabel: Optional[str] = None


@struct
class Dimensions:
    Length: Optional[int] = None
    Width: Optional[int] = None
    Height: Optional[int] = None
    Unit: Optional[str] = None
    PredefinedPackageDimensions: Optional[str] = None


@struct
class AvailableFormatOption:
    IncludePackingSlipWithLabel: Optional[bool] = None
    LabelFormat: Optional[str] = None


@struct
class AvailableCarrierWillPickUpOption:
    CarrierWillPickUpOption: Optional[str] = None
    Charge: Optional[InsuranceType] = JStruct[InsuranceType]


@struct
class AvailableDeliveryExperienceOption:
    DeliveryExperienceOption: Optional[str] = None
    Charge: Optional[InsuranceType] = JStruct[InsuranceType]


@struct
class AvailableServiceOptions:
    AvailableCarrierWillPickUpOptions: List[AvailableCarrierWillPickUpOption] = JList[AvailableCarrierWillPickUpOption]
    AvailableDeliveryExperienceOptions: List[AvailableDeliveryExperienceOption] = JList[AvailableDeliveryExperienceOption]


@struct
class ServiceOptions:
    DeliveryExperience: Optional[str] = None
    DeclaredValue: Optional[InsuranceType] = JStruct[InsuranceType]
    CarrierWillPickUp: Optional[bool] = None
    CarrierWillPickUpOption: Optional[str] = None
    LabelFormat: Optional[str] = None


@struct
class Service:
    ShippingServiceName: Optional[str] = None
    CarrierName: Optional[str] = None
    ShippingServiceId: Optional[str] = None
    ShippingServiceOfferId: Optional[str] = None
    ShipDate: Optional[str] = None
    EarliestEstimatedDeliveryDate: Optional[str] = None
    LatestEstimatedDeliveryDate: Optional[str] = None
    Rate: Optional[InsuranceType] = None
    ShippingServiceOptions: Optional[ServiceOptions] = JStruct[ServiceOptions]
    AvailableShippingServiceOptions: Optional[AvailableServiceOptions] = JStruct[AvailableServiceOptions]
    AvailableLabelFormats: List[str] = []
    AvailableFormatOptionsForLabel: List[AvailableFormatOption] = JList[AvailableFormatOption]
    RequiresAdditionalSellerInputs: Optional[bool] = None


@struct
class Payload:
    ShipmentId: Optional[str] = None
    AmazonOrderId: Optional[str] = None
    SellerOrderId: Optional[str] = None
    ItemList: List[Item] = JList[Item]
    ShipFromAddress: Optional[Address] = JStruct[Address]
    ShipToAddress: Optional[Address] = JStruct[Address]
    PackageDimensions: Optional[Dimensions] = JStruct[Dimensions]
    Weight: Optional[WeightType] = JStruct[WeightType]
    Insurance: Optional[InsuranceType] = JStruct[InsuranceType]
    ShippingService: Optional[Service] = JStruct[Service]
    Label: Optional[LabelType] = JStruct[LabelType]
    Status: Optional[str] = None
    TrackingId: Optional[str] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None


@struct
class ShipmentResponse:
    payload: Optional[Payload] = JStruct[Payload]
    errors: List[Error] = JList[Error]
