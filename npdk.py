from user import User
from bot import Bot
from placeorderdata import *
from order import AOAddOrder
from checkoutdata import PaymentInfo, PaymentChannel, PaymentChannelOptionInfo
from datetime     import datetime
from colorama     import Fore, Style, init
from time         import sleep, time
from datetime     import datetime, timedelta
from datetime import time as dtime
import os,sys
import pytz
import urllib3
from helper import place_order, Dpo
import random

class Npdk:
    shop: list
    user: list
    cookies: str
    devices: dict
    bot = None
    order:  dict = {}
    pay: dict = {}
    buyer: dict = {}
    shipping: dict = {}
    checkout: AOAddOrder
    

    def __init__(self, cookie, devices):
        self.cookies = cookie
        self.devices = devices
        try:
            self.user = User.exec(self.cookies)
            self.bot = bot = Bot(self.user)
            self.buyer.update({"address_id":self.user.default_address.id,"service_fee":100000000,"fingerprint":self.devices['fingerprint']})
            print("WELCOME: ",self.user.name)
        except Exception as e:
            self.log(e)
            self.stop()

    def start(self):
        print("Masukan url barang yang akan dibeli")
        self.link = str(input("url product: "))
        #harga = int(input("harga: "))
        #link = "https://shopee.co.id/Sweater-Hoodie-Original-Polos-Pria-Wanita-Jaket-Hodie-Polos-Cowok-Cewek-OverSize-Distro-Bandung-Switer-Polos-Kekinian-Warna-Bulgandi-Bisa-COD-i.22604926.12940184066"
        self.harga = 139900
        self.cekPrice = True
        try:
            self.item = self.bot.fetch_item_from_url(self.link)
            if not self.item.is_flash_sale:
                self.log("BUKAN PRODUCT FLASH SALE!!")
                self.stop()
            self.get_shipping(url=self.link)
            self.order.update({"shop_id":self.item.shop_id,"item_id":self.item.item_id})
        except Exception as e:
            self.log(e)
            self.stop()
    def start_bot(self):
        tz = pytz.timezone('Asia/Jakarta')
        #start_time_bot = datetime.fromtimestamp(1670663640,tz)
        start_time_bot = datetime.fromtimestamp(self.item.flash_sale.start_time,tz)
        time_start_bot = start_time_bot - timedelta(seconds=1)
        second_coutndown = start_time_bot - timedelta(seconds=5)
        print("WAKTU SEKARANG", datetime.now(tz).strftime("%H:%M:%S"))
        print("Waktu Flash Sale: ", start_time_bot.strftime("%H:%M:%S"))
        while True:
            if start_time_bot < datetime.now(tz): break
            print( "Menunggu Flash Sale... [{}]".format(str((time_start_bot - datetime.now(tz)).total_seconds())), end='\r')
        getItem = None
        nowPrice = self.item.price
        if (time_start_bot - datetime.now(tz)).total_seconds() > 0:
            sleep((time_start_bot - datetime.now(tz)).total_seconds())
        print("BOT RUNNING")
        while True:
            getItem = self.bot.get_current_item(self.link,self.item.shop_id,self.item.models[0])
            nowPrice = int(str(getItem['display_price'])[:-5])
            stock = int(getItem['display_stock'])
            print(f"[{datetime.now(tz).strftime('%H:%M:%S:%f')}] HARGA NOW: {nowPrice} | HARGA MAX: {self.harga}", end="\r")
            if self.cekPrice and nowPrice <= self.harga:
                print()
                print(f"[PLACE_ORDER] HARGA: {nowPrice}")
                #cq = self.bot.checkout_get_quick(data={"shop_id":self.item.shop_id,"item_id":self.item.item_id,"model_id":self.buyer['model_id']},quick=False)
                # self.checkout.checkout_price_data.update({
                #     "merchandise_subtotal":nowPrice,
                print(cq)
                #     })
                # self.bot.place_order(self.checkout.__dict__)
                break
            elif not self.cekPrice and nowPrice == self.harga:
                print()
                print(f"[PLACE_ORDER_2] HARGA: {nowPrice}")
                break
        print("HARGA ASLI: ",int(str(self.item.price)[:-5]))
        print("HARGA AKHIR:", nowPrice)
    def setup_bot(self):
        ranint = (random.randint(1,2001) - 1000)
        ctimestamp = int(time() + ranint)
        shop = self.bot.get_shop_info(self.item.shop_id)
        cq = self.bot.checkout_get_quick(data={"shop_id":self.item.shop_id,"item_id":self.item.item_id,"model_id":self.buyer['model_id']},quick=False)
        print(cq)
        #
        #self.bot.place_order(self.checkout.__dict__)
        # dataplaceo = Dpo(
        #     timestamp=ctimestamp,
        #     dataharga={
        #         "price":1000,
        #         "shipping_fee":9000,
        #         "order_total":10000,
        #         ""
        #     },
        #     payment_data={"txn_fee":self.buyer['txn_fee'],"version":2,"channel_id":self.pay['channel_id'],"option_info":self.pay['option_info'] if self.pay['option_info'] is not None else ""},
        #     shoporders=cq['shoporders'],
        #     shipping_orders=cq['shipping_orders']
        # )
        # print(dataplaceo)
        #print(place_order(data=dataplaceo))
        # data_place_order = DataPlaceOrder(
        #     timestamp=int(time()),
        #     price=cq['shoporders'][0]['items'][0]['price'],
        #     order_total=cq['checkout_price_data'],
        #     image=cq['shoporders'][0]['items'][0]['image'],
        #     cat_ids=cq['shoporders'][0]['items'][0]['image']['categories'][0]['catids'],
        #     pay=DataPayment(
        #         version=2,
        #         channel_id=self.pay['channel_id'],
        #         option_info=self.pay['option_info'] if self.pay['option_info'] is not None else ""
        #     ),
        #     shop=cq['shoporders'][0]['shop'],
        #     item=cq['shoporders'][0]['items'][0],
        #     buyer=DataBuyer(
        #         model_id=cq['shoporders'][0]['items'][0]['modelid'],
        #         shipping_fee=cq['shoporders'][0]['shipping_fee'],
        #         channel_id=self.buyer['channel_id'],
        #         address_id=self.buyer['address_id'],
        #         service_fee=self.buyer['service_fee'],
        #         fingerprint=self.buyer['fingerprint'],
        #         txn_fee=self.buyer['txn_fee']
        #     )
        # )
        #self.bot.place_order(data=place_order(data=data_place_order))
    def set_order(self, order: dict):
        self.order.update(order)
    def set_pay(self, pay: dict):
        self.pay.update(pay)
        txn_fee = 0
        if "SHOPEEPAY" in pay['name']:txn_fee = 0
        elif "ALFAMART" in pay['name'] or "INDOMART_ISAKU" in pay['name']:txn_fee = 250000000
        elif "COD_BAYAR_DI_TEMPAT" in pay['name']:txn_fee = 0
        elif "TRANSFER_BANK" in pay['name']:
            txn_fee = 1000
            if "TRANSFER_BANK_SEA_AUTO" in pay['option_name']:txn_fee = 0
        self.buyer.update({"txn_fee": txn_fee})
    def set_buyer(self, buyer: dict):
        self.buyer.update(buyer)
    def get_order(self):
        return self.order
    def get_checkout(self):
        checkout = self.bot.checkout_get_quick(data=self.order)
    def get_item(self):
        return self.item
    def get_bot(self):
        return self.bot
    def get_shipping(self, url=None):
        if url is not None:
            self.ship = self.bot.get_shipping(url, self.item, self.user)['ungrouped_channel_infos']
            return
        return self.ship
    
    def get_models(self):
        pass

    def log(self, msg: str, debug=False, level: int = 0):
        log_level = "[ERROR] " if level is 0 else "[WARNING]"
        print(log_level,msg)
        if debug:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
    def stop(self):
        print("BOT BERHENTI")
        exit(1)