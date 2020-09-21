from jstruct import struct, JList, JStruct, REQUIRED
from typing import List, Optional


@struct
class Address:
    Name: str
    City: str
    Phone: str
    Email: str
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
    value: int
    unit: str


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
class ItemLevelSellerInputs:
    AdditionalInputFieldName: str
    AdditionalSellerInput: AdditionalSellerInput = JStruct[AdditionalSellerInput]


@struct
class Item:
    Quantity: int
    OrderItemId: str
    ItemWeight: Weight = JStruct[Weight]
    ItemDescription: Optional[str] = None
    TransparencyCodeList: List[str] = []
    ItemLevelSellerInputsList: List[ItemLevelSellerInputs] = JList[ItemLevelSellerInputs]


@struct
class Label:
    CustomTextForLabel: str
    StandardIdForLabel: str


@struct
class PackageDimensions:
    Length: Optional[int] = None
    Width: Optional[int] = None
    Height: Optional[int] = None
    Unit: Optional[int] = None
    PredefinedPackageDimensions: Optional[str] = None


@struct
class ServiceOptions:
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
    ShippingServiceOptions: ServiceOptions = JStruct[ServiceOptions, REQUIRED]

    ShipDate: Optional[str] = None
    SellerOrderId: Optional[str] = None
    MustArriveByDate: Optional[str] = None
    LabelCustomization: Label = JStruct[Label]


@struct
class ShippingOfferingFilter:
    IncludePackingSlipWithLabel: bool
    IncludeComplexShippingOptions: bool
    CarrierWillPickUp: str
    DeliveryExperience: str


@struct
class EligibleShipmentServices:
    ShipmentRequestDetails: ShipmentRequestDetails = JStruct[ShipmentRequestDetails, REQUIRED]
    ShippingOfferingFilter: ShippingOfferingFilter = JStruct[ShippingOfferingFilter]
