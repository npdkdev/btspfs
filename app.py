from user import User
from bot import Bot
from placeorderdata import *
from checkoutdata import PaymentInfo, PaymentChannel, PaymentChannelOptionInfo
from datetime     import datetime
from colorama     import Fore, Style, init
from time         import sleep, time
from datetime     import datetime, timedelta
from datetime import time as dtime
import os
import pytz
import urllib3
import asyncio

urllib3.disable_warnings()

init()
INFO = Fore.LIGHTBLUE_EX + "[*]" + Fore.BLUE
INPUT = Fore.LIGHTGREEN_EX + "[?]" + Fore.GREEN
PROMPT = Fore.LIGHTRED_EX + "[!]" + Fore.RED
mode = None
selected_model = 0

async def start_bot(url, bot, item):
    data = DataPlaceOrder(
        timestamp=int(time.time()),
        price=item.price,
        
    )
    
async def shipping(bot, url, item, user):
    shipp = bot.get_shipping(url, item, user)['ungrouped_channel_infos']
    print(INFO, "Pilih Kurir")
    print(Fore.RESET, "-" * 32)
    for index, shipping in enumerate(shipp):
        avail = "0" if shipping['channel_delivery_info']['has_edt'] is False else int(str(shipping['price_before_discount'])[:-5])
        kurir_avail = "TIDAK BISA DIGUNAKAN" if shipping['price_before_discount'] is None else ""
        print(Fore.GREEN + '[' + str(index) + ']' + Fore.BLUE, shipping['name'], "\t| ", avail, "\t| ", kurir_avail)
    print(Fore.RESET, "-" * 32)
    print()
    selected_kurir = int(input(INPUT + " Pilihan: "))
    kuririd = shipp[selected_kurir]["channel_id"]
    print(kuririd)
    print()

async def checkout():
    print(INFO, "Flash Sale telah tiba")
    start = datetime.now()
    print(INFO, "Menambah item ke cart...")
    cart_item = bot.add_to_cart(item, selected_model)
    print(INFO, "Checkout item...")
    bot.checkout(PaymentInfo(
        channel=selected_payment_channel,
        option_info=selected_option_info
    ), cart_item)
    final = datetime.now() - start
    print(INFO, "Item berhasil dibeli dalam waktu", Fore.YELLOW, final.seconds, "detik", final.microseconds // 1000,
          "milis")
    print(Fore.GREEN + "[*]", "Sukses")

async def check_flash_sale(item):
    if not item.is_flash_sale:
        if item.upcoming_flash_sale is not None:
            flash_sale_start = datetime.fromtimestamp(item.upcoming_flash_sale.start_time)
            flash_sale_id = datetime.fromtimestamp(item.upcoming_flash_sale.start_time,pytz.timezone('Asia/Jakarta'))
            time_to_start_bot = flash_sale_start - timedelta(seconds=60)
            print(time_to_start_bot)
            print(INFO, "WAKTU SEKARANG", datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%H:%M:%S"))
            print(INFO, "Waktu Flash Sale: ", flash_sale_id.strftime("%H:%M:%S"))
            print(INFO, "BOT BERJALAN: ", (flash_sale_id - timedelta(seconds=2)).strftime("%H:%M:%S"))
            print(INFO, "Menunggu Flash Sale...", end='\r')
            print((time_to_start_bot - datetime.now()).total_seconds())
            sleep(2.735685)
            print(INFO, "BOT SEDANG BERJALAN", end='\r')
            print(INFO, "CEK HARGA:", "1000")
            while True:
                citem = bot.get_current_item(url,item.shop_id,item.models[0])
                price = int(str(citem['display_price'])[:-5])
                stock = int(citem['display_stock'])
                if price <= harga:
                    print("checkout:", price)
                    break
                else: print("normal price")

            sleep((datetime.fromtimestamp(item.upcoming_flash_sale.start_time) - datetime.now()).total_seconds())
        else:
            print(PROMPT, "Flash Sale telah Lewat!")
            exit(1)
    else:
        pass

async def payment_method():
    print(INFO, "Pilih metode pembayaran")
    payment_channels = dict(enumerate(PaymentChannel))
    for index, channel in payment_channels.items():
        print(Fore.GREEN + '[' + str(index) + ']' + Fore.BLUE, channel.name)
    print()
    selected_payment_channel = payment_channels[int(input(INPUT + " Pilihan: "))]
    print()

    selected_option_info = PaymentChannelOptionInfo.NONE
    if selected_payment_channel is PaymentChannel.TRANSFER_BANK or \
            selected_payment_channel is PaymentChannel.AKULAKU:
        options_info = dict(enumerate(list(PaymentChannelOptionInfo)[1 if selected_payment_channel is
                            PaymentChannel.TRANSFER_BANK else 7:None if selected_payment_channel is
                            PaymentChannel.AKULAKU else 7]))
        for index, option_info in options_info.items():
            print(Fore.GREEN + '[' + str(index) + ']' + Fore.BLUE, option_info.name)
        print()
        selected_option_info = options_info[int(input(INPUT + " Pilihan: "))]

async def models(item, bot):
    is_flashsale = bot.get_flashsale(item)
    print(INFO, "Pilih model")
    print(Fore.RESET, "-" * 32)
    for index, model in enumerate(item.models):
        print(Fore.GREEN + '[' + str(index) + ']' + Fore.BLUE, model.name, is_flashsale[index] if not item.is_flash_sale else "")
        print('\t', Fore.LIGHTBLUE_EX, "Harga:", Fore.GREEN, item.get_price(model.price))
        print('\t', Fore.LIGHTBLUE_EX, "Stok:", Fore.GREEN, model.stock)
        print('\t', Fore.LIGHTBLUE_EX, "ID Model:", Fore.GREEN, model.model_id)
        print(Fore.RESET, "-" * 32)
    print()
    selected_model = int(input(INPUT + " Pilihan: "))
    print()
        

async def main():
    print(INFO, "Mengambil informasi user...", end='\r')
    cookie_file = "cookie.txt"
    cookie_content = ""
    with open(cookie_file,'r') as f:
        cookie_content = f.read()
    user = User.exec(cookie_content)
    bot = Bot(user)
    print("WELCOME: ",user.name)
    url = input("url: ")
    harga: int = int(input("Harga: "))
    item = bot.fetch_item_from_url(url)
    print(Fore.RESET, "-" * 32)
    print(Fore.LIGHTBLUE_EX, "Nama:", Fore.GREEN, item.name)
    print(Fore.LIGHTBLUE_EX, "Harga:", Fore.GREEN, item.get_price(item.price))
    print(Fore.LIGHTBLUE_EX, "Flashsale:", Fore.GREEN, "Sedang berlangsung" if item.is_flash_sale else "Menunggu - "+ datetime.fromtimestamp(item.upcoming_flash_sale.start_time,pytz.timezone('Asia/Jakarta')).strftime("%H:%M:%S"))
    print(Fore.LIGHTBLUE_EX, "Brand:", Fore.GREEN, item.brand)
    print(Fore.LIGHTBLUE_EX, "Lokasi Toko:", Fore.GREEN, item.shop_location)
    print(Fore.RESET, "-" * 32)
    print()
    await shipping(bot, url, item, user)
    print(INFO, "Pilih mode")
    print(Fore.RESET, "-" * 32)
    print('\t', Fore.LIGHTBLUE_EX, "1. MODE CHECKOUT:")
    print('\t', Fore.LIGHTBLUE_EX, "2. CEK HARGA")
    print(Fore.RESET, "-" * 32)
    selected_mode = int(input(INPUT + " Mode: "))
    print()
    if len(item.models) > 1: await models(item,bot)
    await payment_method()

print("Starting...")
asyncio.run(main())
print("Screenshot has been taken")
