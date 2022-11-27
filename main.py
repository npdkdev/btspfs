from user import User
from bot import Bot

if __name__ == "__main__":
    cookie_file = "cookie.txt"
    cookie_content = ""
    with open(cookie_file,'r') as f:
        cookie_content = f.read()
    user = User.exec(cookie_content)
    
    print("WELCOME: ",user.name)
    print("Masukan url barang yang akan dibeli")
    bot = Bot(user)
    item = bot.fetch_item_from_url(input(" url: "))
    print(item)
 
