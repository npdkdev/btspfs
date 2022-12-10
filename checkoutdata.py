from dataclasses import dataclass
from enum import Enum


class PaymentChannel(Enum):
    SHOPEEPAY = 8001400
    ALFAMART = 8003200
    INDOMART_ISAKU = 8003001
    TRANSFER_BANK = 8005200
    COD_BAYAR_DI_TEMPAT = 89000


class PaymentChannelOptionInfo(Enum):
    NONE = None
    # Transfer Bank
    TRANSFER_BANK_BCA_AUTO = "89052001"
    TRANSFER_BANK_SEA_AUTO = "89052007"
    TRANSFER_BANK_MANDIRI_AUTO = "89052002"
    TRANSFER_BANK_BNI_AUTO = "89052003"
    TRANSFER_BANK_BRI_AUTO = "89052004"
    TRANSFER_BANK_SYARIAH_AUTO = "89052005"
    TRANSFER_BANK_PERMATA_AUTO = "89052006"
    TRANSFER_BANK_LAINYA_AUTO = "89052902"


@dataclass
class PaymentInfo:
    channel: PaymentChannel
    option_info: PaymentChannelOptionInfo = PaymentChannelOptionInfo.NONE


@dataclass
class CheckoutData:
    can_checkout: bool
    cart_type: int
    client_id: int
    shipping_orders: list
    disabled_checkout_info: dict
    checkout_price_data: dict
    promotion_data: dict
    dropshipping_info: dict
    selected_payment_channel_data: dict
    shoporders: list
    order_update_info: dict
    buyer_txn_fee_info: dict
    timestamp: int
