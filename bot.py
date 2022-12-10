from urllib.parse import urlencode
from item import *
from user import User
from json import dumps
from re import search
from time import time
from checkoutdata import *
import requests
import random
class Bot:
    user: User

    def __init__(self, user: User):
        self.user = user

    def __default_headers(self, headers: dict = None) -> dict:
        default = {
                "Accept": "application/json",
                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                "Content-Type": "application/json",
                "Sec-Ch-Ua": "'Chromium';v='107', 'Not=A?Brand';v='24'",
                "Sec-Ch-Ua-Mobile": "?0",
                "X-API-SOURCE": "pc",
                "Host": "shopee.co.id",
                "X-Shopee-Language": "id",
                "Cookie": self.user.cookie.strip(),
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Origin": "https://shopee.co.id",
                "Referer": "https://shopee.co.id/flash_sale",
                "User-Agent": self.user.USER_AGENT.strip(),
                "if-none-match-": "*",
                "X-Requested-with": "XMLHttpRequest",
                "X-CSRFToken": self.user.csrf_token,
                "sec-gpc": "1",
                "af-ac-enc-dat":"AAYyLjIuMTEAAAGC8gGVGAAAAAABvQAAAAAAAAAABu4eZq0lL7h52o9f7CuwF3A5g75rqgouK+loN/v/p3MxkDpFZT2P2hfqZEDmHHFAmmlMQ+JYTMHF6kF68iRD85aWYi9ro3Wl9b3oSySuEOrgGKGQQJ836vmwS4evtiSZF+8hpeeDkMDl0WXkPHJxWSHdJSL2V2RgO7ZTdl2PzKj1IdJtmTKSF/iVRik4qQPHpZahF4xX9XDEQxZaMiy8FxB0KB/+Z3M6mcDhtM3PtZ2Jbb1Po1xg0v5d9YoE99A0++/hVcuScCn9rmuoaFPIkqb/QfQubeJxMPpEbOf8DabnB03ovh5/6rGSaxMR2cLpyWj3jrNNdgBj3inx/hFfmKOhu7fRXrcNo7k2Uxm8hdGVUZgOvo3vz+IOpcfuM8I9EjNXsEH8wiT/A0HZUldbYMxzhql0JPizgInzqYxo+JHfmbMMaYms5v/5YQyU5T1OK+dceLrCqZsizZTx6GyRUhRlbZfa0O93fHzTKbTBC9GRY7OMsPKRljZ2EI7Zp6aWkWOzjLDykZY2dhCO2aemlpkbjII7/J+vTHjkE+VsZsiRY7OMsPKRljZ2EI7Zp6aW1FalgcGI6E1yaFhUpEHhAw==",
            }
        if headers is not None:
            for key,val in headers.items():
                default[key] = val
        return default
        
    def fetch_item_from_url(self, url: str) -> Item:
        """
        :param url: the item url
        :return: Item object
        the url will definitely be one of these:
            - https://shopee.co.id/product/xxxx/xxxx
            - https://shopee.co.id/Item-Name.xxxx.xxxx
        """
        # https://shopee.co.id/product/xxxx/xxxx
        match = search(r".*/(?P<shopid>\d+)/(?P<itemid>\d+).*?", url)
        if match is not None:   
            return self.fetch_item(int(match.group("itemid")), int(match.group("shopid")))

        # https://shopee.co.id/Item-Name.xxxx.xxxx
        match = search(r".*\.(?P<shopid>\d+)\.(?P<itemid>\d+)", url)
        if match is None:
            raise ValueError("unexpected url")
        return self.fetch_item(int(match.group("itemid")), int(match.group("shopid")),url)

    def fetch_item(self, item_id: int, shop_id: int, url: str) -> Item:
        resp = requests.get(
            "https://shopee.co.id/api/v4/item/get?" + urlencode({
                "itemid": item_id,
                "shopid": shop_id
            }),
            headers=self.__default_headers({"Referer":url})
        )
        item_data = resp.json()['data']
        with open('test.txt','w') as fle:
            fle.write(resp.text)
        flashsl = item_data["upcoming_flash_sale"] if item_data["upcoming_flash_sale"] is not None else item_data["flash_sale"]
        if item_data is None:
            raise NameError("item not found")
        return Item(
            item_id=item_data["itemid"],
            shop_id=item_data["shopid"],
            models=[Model(
                # currency=model["currency"],
                item_id=model["itemid"],
                model_id=model["modelid"],
                promotion_id=model["promotionid"],
                name=model["name"],
                price=model["price"],
                stock=model["stock"]
            ) for model in item_data["models"]],
            name=item_data["name"],
            price=item_data["price"],
            price_before_discount=item_data["price_before_discount"],
            brand=item_data["brand"],
            shop_location=item_data["shop_location"],
            flash_sale=FlashSaleInfo(
                end_time=flashsl["end_time"],
                price=flashsl["price"],
                price_before_discount=flashsl["price_before_discount"],
                promotion_id=flashsl["promotionid"],
                start_time=flashsl["start_time"],
                stock=flashsl["stock"]
            ) if flashsl is not None else None,
            add_on_deal_info=AddOnDealInfo(
                add_on_deal_id=item_data["add_on_deal_info"]["add_on_deal_id"],
                add_on_deal_label=item_data["add_on_deal_info"]["add_on_deal_label"],
                sub_type=item_data["add_on_deal_info"]["sub_type"]
            ) if item_data["add_on_deal_info"] is not None else AddOnDealInfo(),
            price_min=item_data["price_min"],
            price_max=item_data["price_max"],
            stock=item_data["stock"],
            categories=[ catid['catid'] for catid in item_data['categories'] ],
            cb_option=item_data['cb_option'],
            image=item_data['image'],
            is_flash_sale=item_data["flash_sale"] is not None or item_data["upcoming_flash_sale"] is not None
        )

    def add_to_cart(self, item: Item, model_index: int) -> CartItem:
        if not item.models[model_index].is_available():
            raise Exception("out of stock")
        resp = requests.post(
            url="https://shopee.co.id/api/v2/cart/add_to_cart",
            headers=self.__default_headers(),
            data=dumps({
                "checkout": True,
                "client_source": 1,
                "donot_add_quantity": False,
                "itemid": item.item_id,
                "modelid": item.models[model_index].model_id,
                "quantity": 1,
                "shopid": item.shop_id,
                "source": "",
                "update_checkout_only": False
            })
        )
        data = resp.json()
        if data["error"] != 0:
            print("modelid:", item.models[0].model_id)
            print(resp.text)
            raise Exception(f"failed to add to cart {data['error']}")
        data = data["data"]["cart_item"]
        return CartItem(
            add_on_deal_id=item.add_on_deal_info.add_on_deal_id,
            item_group_id=str(data["item_group_id"]) if data["item_group_id"] != 0 else None,
            item_id=data["itemid"],
            model_id=data["modelid"],
            price=data["price"],
            shop_id=item.shop_id
        )

    def __checkout_get(self, payment: PaymentInfo, item: CartItem) -> CheckoutData:
        resp = requests.post(
            url="https://shopee.co.id/api/v2/checkout/get",
            headers=self.__default_headers(),
            # TODO: Implement data
            data=dumps({
                "cart_type": 0,
                "client_id": 0,
                "device_info": {
                    "buyer_payment_info": {},
                    "device_fingerprint": "",
                    "device_id": "",
                    "tongdun_blackbox": ""
                },
                "dropshipping_info": {

                    "enabled": False,
                    "name": "",
                    "phone_number": ""
                },
                "order_update_info": {},
                "promotion_data": {
                    "auto_apply_shop_voucher": False,
                    "check_shop_voucher_entrances": True,
                    "free_shipping_voucher_info": {
                        "disabled_reason": None,
                        "free_shipping_voucher_code": "",
                        "free_shipping_voucher_id": 0
                    },
                    "platform_voucher": [],
                    "shop_voucher": [],
                    "use_coins": False
                },
                "selected_payment_channel_data": {
                    "channel_id": payment.channel.value,
                    "channel_item_option_info": {"option_info": payment.option_info.value},
                    "version": 2
                },
                "shipping_orders": [{
                    "buyer_address_data": {
                        "address_type": 0,
                        "addressid": self.user.default_address.id,
                        "error_status": "",
                        "tax_address": ""
                    },
                    "buyer_ic_number": "",
                    "logistics": {
                        "recommended_channelids": None
                    },
                    "selected_preferred_delivery_instructions": {},
                    "selected_preferred_delivery_time_option_id": 0,
                    "selected_preferred_delivery_time_slot_id": None,
                    "shipping_id": 1,
                    "shoporder_indexes": [0],
                    "sync": True
                }],
                "shoporders": [{
                    "buyer_address_data": {
                        "address_type": 0,
                        "addressid": self.user.default_address.id,
                        "error_status": "",
                        "tax_address": ""
                    },
                    "items": [{
                        "add_on_deal_id": item.add_on_deal_id,
                        "is_add_on_sub_item": False,
                        "item_group_id": item.item_group_id,
                        "itemid": item.item_id,
                        "modelid": item.model_id,
                        "quantity": 1
                    }],
                    "logistics": {
                        "recommended_channelids": None
                    },
                    "selected_preferred_delivery_instructions": {},
                    "selected_preferred_delivery_time_option_id": 0,
                    "selected_preferred_delivery_time_slot_id": None,
                    "shipping_id": 1,
                    "shop": {"shopid": item.shop_id}
                }],
                "tax_info": {
                    "tax_id": ""
                },
                "timestamp": time()
            })
        )

        if not resp.ok:
            print(resp.status_code)
            print(resp.text)
            raise Exception("failed to get checkout info")
        data = resp.json()
        return CheckoutData(
            can_checkout=data["can_checkout"],
            cart_type=data["cart_type"],
            client_id=data["client_id"],
            shipping_orders=data["shipping_orders"],
            disabled_checkout_info=data["disabled_checkout_info"],
            checkout_price_data=data["checkout_price_data"],
            promotion_data=data["promotion_data"],
            dropshipping_info=data["dropshipping_info"],
            selected_payment_channel_data=data["selected_payment_channel_data"],
            shoporders=data["shoporders"],
            order_update_info=data["order_update_info"],
            buyer_txn_fee_info=data["buyer_txn_fee_info"],
            timestamp=data["timestamp"]
        )

    def place_order(self, data: dict):

        resp = requests.post(
            url="https://shopee.co.id/api/v4/checkout/place_order",
            headers=self.__default_headers({
                "Referer": "https://lite.shopee.co.id/",
                "Origin": "https://lite.shopee.co.id",
                "X-API-SRC-LIST": "pc,rweb,lite",
                "X-CV-ID": "106",
            }),
            data=dumps(data)
        )
        if resp.json()['error_msg'] is not None:
            print ("error: "+ resp.json()['error_msg'])
            resp = requests.post(
                url="https://shopee.co.id/api/v4/checkout/place_order",
                headers=self.__default_headers({
                    "Referer": "https://lite.shopee.co.id/",
                    "Origin": "https://lite.shopee.co.id",
                    "X-API-SRC-LIST": "pc,rweb,lite",
                    "X-CV-ID": "106",
                }),
                data=dumps(data)
            )
            
        print(resp.json())
    def get_shop_info(self, shop_id):
        resp = requests.get(
            url=f"https://shopee.co.id/api/v4/product/get_shop_info?shopid={shop_id}"
        )
        return resp.json()['data']
    def checkout_get_quick(self,data, quick=True, quantity=1):
        ranint = (random.randint(1,2001) - 1000)
        ctimestamp = int(time() + ranint)
        path = "get_quick" if quick else "get"
        resp = requests.post(
            url=f"https://shopee.co.id/api/v4/checkout/{path}",
            headers=self.__default_headers({"Referer":"https://lite.shopee.co.id","Origin":"https://lite.shopee.co.id","X-API-SRC-LIST":"pc,lite"}),
            verify=False,
            data=dumps({
                "timestamp": ctimestamp,
                "_cft": [
                    185963
                ],
                "shoporders": [
                    {
                        "shop": {
                            "shopid": data['shop_id']
                        },
                        "items": [
                            {
                                "itemid": data['item_id'],
                                "modelid": data['model_id'],
                                "quantity": quantity,
                                "insurances": []
                            }
                        ],
                        "logistics": {
                            "recommended_channelids": None
                        },
                        "selected_preferred_delivery_time_slot_id": None
                    }
                ],
                "selected_payment_channel_data": {},
                "promotion_data": {
                    "free_shipping_voucher_info": {
                        "free_shipping_voucher_id": None,
                        "free_shipping_voucher_code": None,
                        "signature": None
                    },
                    "platform_vouchers": [],
                    "shop_vouchers": [],
                    "check_shop_voucher_entrances": True,
                    "auto_apply_shop_voucher": True
                },
                "device_info": {
                    "device_id": "",
                    "device_fingerprint": "",
                    "tongdun_blackbox": "",
                    "buyer_payment_info": {}
                },
                "cart_type": 1,
                "client_id": 3,
                "tax_info": {
                    "tax_id": ""
                }
            })
        )
        if "error" in resp.json():
            print(resp.json()['error_msg'])
            return
        elif resp.status_code == 406:
            print(resp.text)
            raise Exception("response not acceptable, maybe the item has run out")
        elif not resp.ok:
            print(resp.status_code)
            print(resp.text)
            raise Exception(f"failed to checkout, response not ok: {resp.status_code}")
        else:
            return resp.json()
    def checkout(self, payment: PaymentInfo, item: CartItem):
        """
        :param payment: payment method like COD/Alfamart
        :param item: the item to checkout
        checkout an item that has been added to cart
        """
        data = self.__checkout_get(payment, item)
        resp = requests.post(
            url="https://shopee.co.id/api/v2/checkout/place_order",
            headers=self.__default_headers(),
            data=dumps({
                "status": 200,
                "headers": {},
                "cart_type": data.cart_type,
                "shipping_orders": data.shipping_orders,
                "disabled_checkout_info": data.disabled_checkout_info,
                "timestamp": data.timestamp,
                "checkout_price_data": data.checkout_price_data,
                "client_id": data.client_id,
                "promotion_data": data.promotion_data,
                "dropshipping_info": data.dropshipping_info,
                "selected_payment_channel_data": data.selected_payment_channel_data,
                "shoporders": data.shoporders,
                "can_checkout": data.can_checkout,
                "order_update_info": data.order_update_info,
                "buyer_txn_fee_info": data.buyer_txn_fee_info
            })
        )
        if "error" in resp.json():
            print(resp.text)
            raise Exception("failed to checkout")
        elif resp.status_code == 406:
            print(resp.text)
            raise Exception("response not acceptable, maybe the item has run out")
        elif not resp.ok:
            raise Exception(f"failed to checkout, response not ok: {resp.status_code}")

    def buy(self, item: Item, model_index: int, payment: PaymentInfo):
        """
        :param item: the item to buy
        :param model_index: selected model
        :param payment: payment method
        just another way to add item to cart and checkout
        """
        cart_item = self.add_to_cart(item, model_index)
        self.checkout(payment, cart_item)
    def get_shop_info(self, shopid):
        resp = requests.get(
            url=f"https://shopee.co.id/api/v4/product/get_shop_info?shopid={shopid}",
            headers=self.__default_headers()
        )
        return resp.json()['data']
    def get_shipping(self, url, item, user):
        address = user.default_address
        payload = f"buyer_zipcode=&city={address.city}&district={address.district}&itemid={item.item_id}&shopid={item.shop_id}&state={address.state}&town="
        resp = requests.get(
            url=f"https://shopee.co.id/api/v4/pdp/get_shipping?{payload}",
            headers=self.__default_headers({"Referer":url}),
        )
        return resp.json()['data']

    def get_current_item(self, url, shopId, models):
        payload = f"itemId={models.item_id}&modelId={models.model_id}&quantity=1&shopId={shopId}"
        resp = requests.get(
            url=f"https://shopee.co.id/api/v4/product/get_purchase_quantities_for_selected_model?{payload}",verify=False
        )
        return resp.json()['selected_price_and_stock']

    def get_flashsale(self, item):
        itemids = item.item_id
        model = item.models
        promoid = item.flash_sale.promotion_id
        resp = requests.post(
            url="https://shopee.co.id/api/v4/flash_sale/flash_sale_batch_get_items",
            headers=self.__default_headers(),
            verify=False,
            data=dumps({
                "promotionid": promoid,
                "itemids":[itemids],
                "limit":12,
                "with_dp_items": True,
                "sort_soldout":False,
            })
        )
        modelids = resp.json()["data"]["items"][0]["modelids"]
        if modelids is None: return False
        return [ "[FLASHSALE]" if mod.model_id in modelids else "[NOT]" for mod in model ]

    def remove_item_from_cart(self, cart_item: CartItem):
        """
        :param cart_item: cart item to be removed
        remove item from cart
        """
        resp = requests.post(
            url="https://shopee.co.id/api/v4/cart/update",
            headers=self.__default_headers(),
            data=dumps({
                "action_type": 2,
                "updated_shop_order_ids": [
                    {
                        "item_briefs": [
                            {
                                "add_on_deal_id": cart_item.add_on_deal_id,
                                "checkout": False,
                                "item_group_id": cart_item.item_group_id,
                                "itemid": cart_item.item_id,
                                "modelid": cart_item.model_id,
                                "price": cart_item.price,
                                "shopid": cart_item.shop_id
                            }
                        ],
                        "shopid": cart_item.shop_id
                    }
                ]
            })
        )
        if resp.json()["error"] != 0:
            raise Exception("failed to remove item from cart")
