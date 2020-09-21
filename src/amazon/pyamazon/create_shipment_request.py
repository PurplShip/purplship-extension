from jstruct import struct, JList, JStruct, REQUIRED
from typing import List, Optional


@struct
class LabelFormat:
    IncludePackingSlipWithLabel: Optional[bool] = None


@struct
class Address:
    City: str
    Name: str
    Email: str
    Phone: str
    PostalCode: str
    CountryCode: str
    AddressLine1: str

    AddressLine2: Optional[str] = None
    AddressLine3: Optional[str] = None
    DistrictOrCounty: Optional[str] = None
    StateOrProvinceCode: Optional[str] = None


@struct
class DeclaredValue:
    CurrencyCode: str
    Amount: int


@struct
class Dimension:
    value: Optional[int] = None
    unit: Optional[str] = None


@struct
class Weight:
    Value: int
    Unit: str


@struct
class AdditionalSellerInput:
    DataType: Optional[str] = None
    ValueAsString: Optional[str] = None
    ValueAsBoolean: Optional[bool] = None
    ValueAsInteger: Optional[int] = None
    ValueAsTimestamp: Optional[str] = None
    ValueAsAddress: Address = JStruct[Address]
    ValueAsWeight: Weight = JStruct[Weight]
    ValueAsDimension: Dimension = JStruct[Dimension]
    ValueAsCurrency: DeclaredValue = JStruct[DeclaredValue]


@struct
class LevelSellerInputsList:
    AdditionalInputFieldName: str
    AdditionalSellerInput: AdditionalSellerInput = JStruct[AdditionalSellerInput, REQUIRED]


@struct
class Item:
    Quantity: int
    OrderItemId: str

    ItemDescription: Optional[str] = None
    TransparencyCodeList: List[str] = []
    ItemWeight: Weight = JStruct[Weight]
    ItemLevelSellerInputsList: List[LevelSellerInputsList] = JList[LevelSellerInputsList]


@struct
class Label:
    CustomTextForLabel: str
    StandardIdForLabel: str


@struct
class PackageDimensions:
    Length: Optional[int] = None
    Width: Optional[int] = None
    Height: Optional[int] = None
    Unit: Optional[str] = None
    PredefinedPackageDimensions: Optional[str] = None


@struct
class ShippingServiceOption:
    DeliveryExperience: str
    CarrierWillPickUp: bool

    DeclaredValue: DeclaredValue = JStruct[DeclaredValue]
    CarrierWillPickUpOption: Optional[str] = None
    LabelFormat: Optional[str] = None


@struct
class ShipmentRequestDetails:
    AmazonOrderId: str
    Weight: Weight = JStruct[Weight, REQUIRED]
    ItemList: List[Item] = JList[Item, REQUIRED]
    ShipFromAddress: Address = JStruct[Address, REQUIRED]
    PackageDimensions: PackageDimensions = JStruct[PackageDimensions, REQUIRED]
    ShippingServiceOptions: ShippingServiceOption = JStruct[ShippingServiceOption, REQUIRED]
    
    ShipDate: Optional[str] = None
    SellerOrderId: Optional[str] = None
    MustArriveByDate: Optional[str] = None
    LabelCustomization: Label = JStruct[Label]


@struct
class ShipmentRequest:
    ShippingServiceId: str
    ShipmentRequestDetails: ShipmentRequestDetails = JStruct[ShipmentRequestDetails, REQUIRED]

    ShippingServiceOfferId: Optional[str] = None
    HazmatType: Optional[str] = None
    LabelFormatOption: LabelFormat = JStruct[LabelFormat]
    ShipmentLevelSellerInputsList: List[LevelSellerInputsList] = JList[LevelSellerInputsList]
