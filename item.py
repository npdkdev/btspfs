from dataclasses import dataclass
from typing      import List


@dataclass
class Model:
    item_id: int
    model_id: int
    promotion_id: int
    name: str
    price: int
    stock: int
    
    def is_flashsale(self):
        pass

    def is_available(self):
        return self.stock != 0


@dataclass
class FlashSaleInfo:
    end_time: int
    price: int
    price_before_discount: int
    promotion_id: int
    start_time: int
    stock: int


@dataclass
class AddOnDealInfo:
    add_on_deal_id: int = None
    add_on_deal_label: str = None
    sub_type: int = None

@dataclass
class Item:
    item_id: int
    shop_id: int
    models: List[Model]
    name: str
    price: int
    price_before_discount: int
    brand: str
    shop_location: str

    # prepared for the future (if needed)
    flash_sale: FlashSaleInfo
    add_on_deal_info: AddOnDealInfo
    price_min: int
    price_max: int
    stock: int
    categories: dict
    image: str
    cb_option: int
    is_flash_sale: bool

    @staticmethod
    def get_price(price) -> int:
        return int(str(price)[:-5])


@dataclass
class CartItem:
    add_on_deal_id: int
    item_group_id: str
    item_id: int
    model_id: int
    price: int
    shop_id: int
