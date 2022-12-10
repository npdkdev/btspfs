from dataclasses import dataclass
from typing      import List

@dataclass
class DataPayment:
    version: int
    channel_id: int
    option_info: int

@dataclass
class DataBuyer:
    model_id: int
    shipping_fee: int
    channel_id: int
    address_id: int
    service_fee: int
    fingerprint: str
    txn_fee: int

@dataclass
class DataPlaceOrder:
    timestamp: int
    price: int
    order_total: int
    image: str
    cat_ids: list
    pay: DataPayment
    shop: dict
    item: dict
    buyer: DataBuyer
    

