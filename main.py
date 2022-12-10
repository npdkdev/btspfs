from user import User
from bot import Bot
from checkoutdata import PaymentInfo, PaymentChannel, PaymentChannelOptionInfo
from datetime     import datetime
from colorama     import Fore, Style, init
from time         import sleep, time
from datetime     import datetime, timedelta
from datetime import time as dtime
import os
import pytz
import urllib3
from npdk import Npdk 
urllib3.disable_warnings()

def payment_method():
    print(INFO, "Pilih metode pembayaran")
    payment_channels = dict(enumerate(PaymentChannel))
    for index, channel in payment_channels.items():
        print(Fore.GREEN + '[' + str(index) + ']' + Fore.BLUE, channel.name)
    print()
    selected_payment_channel = payment_channels[int(input(INPUT + " Pilihan: "))]
    print()

    selected_option_info = PaymentChannelOptionInfo.NONE
    if selected_payment_channel is PaymentChannel.TRANSFER_BANK:
        options_info = dict(enumerate(list(PaymentChannelOptionInfo)[1 if selected_payment_channel is
                            PaymentChannel.TRANSFER_BANK else 7:7]))
        for index, option_info in options_info.items():
            print(Fore.GREEN + '[' + str(index) + ']' + Fore.BLUE, option_info.name)
        print()
        selected_option_info = options_info[int(input(INPUT + " Pilihan: "))]
    return {"name":selected_payment_channel.name,"channel_id":selected_payment_channel.value,"option_name":selected_option_info.name,"option_info":selected_option_info.value if selected_option_info.value is not None else None }

if __name__ == "__main__":
    init()
    INFO = Fore.LIGHTBLUE_EX + "[*]" + Fore.BLUE
    INPUT = Fore.LIGHTGREEN_EX + "[?]" + Fore.GREEN
    PROMPT = Fore.LIGHTRED_EX + "[!]" + Fore.RED
    if os.name.lower() == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(INFO, "Mengambil informasi user...")
    cookie_file = "cookie.txt"
    cookie_content = ""
    with open(cookie_file,'r') as f:
        cookie_content = f.read()
    devices = {"user_agent":"","fingerprint":""}
    np = Npdk(cookie_content,devices)
    np.start()
    item = np.get_item()
    print(Fore.RESET, "-" * 32)
    print(Fore.LIGHTBLUE_EX, "Nama:", Fore.GREEN, item.name)
    print(Fore.LIGHTBLUE_EX, "Harga:", Fore.GREEN, item.get_price(item.price))
    print(Fore.LIGHTBLUE_EX, "Flashsale:", Fore.GREEN, "Bukan Product FlashSale" if not item.is_flash_sale else "Menunggu - "+
    datetime.fromtimestamp(item.flash_sale.start_time,pytz.timezone('Asia/Jakarta')).strftime("%H:%M:%S") if item.flash_sale.start_time > time() else "Berlangsung - "+
    datetime.fromtimestamp(item.flash_sale.end_time,pytz.timezone('Asia/Jakarta')).strftime("%H:%M:%S"))
    print(Fore.LIGHTBLUE_EX, "Brand:", Fore.GREEN, item.brand)
    print(Fore.LIGHTBLUE_EX, "Lokasi Toko:", Fore.GREEN, item.shop_location)
    print(Fore.RESET, "-" * 32)
    print()

    #shipping
    print(INFO, "Pilih Kurir")
    print(Fore.RESET, "-" * 32)
    for index, shipping in enumerate(np.get_shipping()):
        avail = "0" if shipping['channel_delivery_info']['has_edt'] is False else int(str(shipping['price_before_discount'])[:-5])
        kurir_avail = "TIDAK BISA DIGUNAKAN" if shipping['price_before_discount'] is None else ""
        print(Fore.GREEN + '[' + str(index) + ']' + Fore.BLUE, shipping['name'], "\t| ", avail, "\t| ", kurir_avail)
    print(Fore.RESET, "-" * 32)
    print()
    selected_kurir = int(input(INPUT + " Pilihan: "))
    kurir = np.get_shipping()[selected_kurir]
    np.set_buyer(buyer={"shipping_name":kurir['name'],"shipping_fee":kurir['price_before_discount'],"channel_id":kurir['channel_id']})
    print()

    print(INFO, "Pilih mode")
    print(Fore.RESET, "-" * 32)
    print('\t', Fore.LIGHTBLUE_EX, "1. AUTO CHECKOUT")
    print('\t', Fore.LIGHTBLUE_EX, "2. CEK HARGA")
    print(Fore.RESET, "-" * 32)
    selected_mode = int(input(INPUT + " Mode: "))
    print()

    if len(item.models) > 1:
        print(INFO, "Pilih model")
        print(Fore.RESET, "-" * 32)
        is_flashsale = False
        if item.flash_sale is not None: is_flashsale = np.get_bot().get_flashsale(item)
        for index, model in enumerate(item.models):
            print(Fore.GREEN + '[' + str(index) + ']' + Fore.BLUE, model.name, is_flashsale[index] if is_flashsale is not False  else "")
            print('\t', Fore.LIGHTBLUE_EX, "Harga:", Fore.GREEN, item.get_price(model.price))
            print('\t', Fore.LIGHTBLUE_EX, "Stok:", Fore.GREEN, model.stock)
            print('\t', Fore.LIGHTBLUE_EX, "ID Model:", Fore.GREEN, model.model_id)
            print(Fore.RESET, "-" * 32)
        print()
        selected_model = int(input(INPUT + " Pilihan: "))
        if not item.models[selected_model].is_available():
            pass
            #raise Exception("stock kosong")
        np.set_order({"model_id":item.models[selected_model].model_id})
        np.set_buyer({"model_id":item.models[selected_model].model_id})
        print()
    else:np.set_buyer({"model_id":item.models[0].model_id})

    payment = payment_method()
    stime = time()
    np.set_pay(payment)
    np.setup_bot()
    np.start_bot()
    print("time %s" % (time() - stime))

    #bot.checkout_get_quick()

    #url = input("url: ")
    #harga: int = int(input("Harga: "))
    #item = bot.fetch_item_from_url(url)
    
    # print(INFO, "Flash Sale telah tiba")
    # start = datetime.now()
    # print(INFO, "Menambah item ke cart...")
    # cart_item = bot.add_to_cart(item, selected_model)
    # print(INFO, "Checkout item...")
    # bot.checkout(PaymentInfo(
    #     channel=selected_payment_channel,
    #     option_info=selected_option_info
    # ), cart_item)
    # final = datetime.now() - start
    # print(INFO, "Item berhasil dibeli dalam waktu", Fore.YELLOW, final.seconds, "detik", final.microseconds // 1000,
    #       "milis")
    # print(Fore.GREEN + "[*]", "Sukses")
 
