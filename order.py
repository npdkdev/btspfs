from typing import List, Any, Dict, Optional
class AOAddOrder:
    client_id: int
    cart_type: int
    timestamp: int
    checkout_price_data: Dict[str, Optional[int]]
    order_update_info: dict
    dropshipping_info: dict
    promotion_data: dict
    selected_payment_channel_data: dict
    shoporders: List[dict]
    shipping_orders: List[dict]
    fsv_selection_infos: List[dict]
    client_event_info: dict
    buyer_txn_fee_info: dict
    disabled_checkout_info: dict
    can_checkout: bool
    buyer_service_fee_info: dict
    cft: List[int]
    captcha_version: int
    device_info: dict

    def __init__(self,
     timestamp: int, 
     checkout_price_data: Dict[str, Optional[int]], 
     promotion_data: dict, 
     selected_payment_channel_data: dict, 
     shoporders: List[dict], 
     shipping_orders: List[dict]) -> None:
        self.client_id = 0
        self.cart_type = 1
        self.timestamp = timestamp
        self.checkout_price_data = checkout_price_data
        self.order_update_info = {}
        self.dropshipping_info = {"enabled": False,"name": "","phone_number": ""}
        self.promotion_data = promotion_data
        self.selected_payment_channel_data = selected_payment_channel_data
        self.shoporders = shoporders
        self.shipping_orders = shipping_orders
        self.fsv_selection_infos = []
        self.client_event_info = {"is_platform_voucher_changed": False,"is_fsv_changed": False}
        self.buyer_txn_fee_info = {"title": "Biaya Penanganan","description": "Besar biaya penanganan adalah Rp1.000 dari total transaksi.","learn_more_url": "https://shopee.co.id/m/biaya-penanganan-transferbanklainnya"}
        self.disabled_checkout_info = {"description": "","auto_popup": False,"error_infos": []}
        self.can_checkout = True
        self.buyer_service_fee_info = {"learn_more_url": "https://shopee.co.id/m/biaya-layanan"}
        self.cft = 1236587
        self.captcha_version = 1
        self.device_info = {}
