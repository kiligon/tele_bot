import requests 
from config import *
from tabulate import tabulate


def get_games(lang):
    par = {'seller_id': seller_id}
    r = requests.get("https://api.digiseller.ru/api/categories", params=par, headers={'Accept': 'application/json'})
    ids = []
    print(r.json())
    for i in r.json()["category"]:
        if int(i["cnt"])>0:
            ids.append(i["id"])
    games  = []

    for cat_id in ids:
        g = requests.get("https://api.digiseller.ru/api/shop/products?seller_id={}&category_id={}&lang={}".format(seller_id, cat_id, lang), headers={'Accept': 'application/json'})
        print(g.json().keys())
        for game in g.json()["product"]:
            games.append((game["id"], game["name"], game["base_price"])) #game["num_in_stock"]))

    if lang == "en-US":
        table = tabulate(games, [["ID"][0], ["Game"][0], ["Price"][0]],tablefmt="fancy_grid")
    else:
        table = tabulate(games, [["ID"][0], ["Игра"][0], ["Цена"][0]],tablefmt="fancy_grid")
    return table


def add_to_cart(product_id=3341854, product_cnt=1, typecurr="WMZ",email="ilay01@list.ru", lang="ru-RU", cart_uid=""):
    param = {"product_id": product_id,"product_cnt": product_cnt, "typecurr": typecurr, "email": email, "lang": lang, "cart_uid": cart_uid,  }

    r = requests.post('https://shop.digiseller.ru/xml/shop_cart_add.asp', data = param)
    print(r.json())
    return r.json()["cart_uid"]

def print_cart(cart_uid, lang):
    param = {"cart_uid": cart_uid, "cart_curr": "USD", "lang": lang}
    products = []
    r = requests.post('https://shop.digiseller.ru/xml/shop_cart_lst.asp', data = param)
    print(r.json())
    amount = r.json()["amount"]
    for product in r.json()["products"]:
        products.append((product["name"], product["price"], product["cnt_item"]))

    if lang == "en-US":
        table = tabulate(products, [["Игрa"][0], ["Цена"][0], ["Количесво"][0]], tablefmt="fancy_grid")
    else:
        table = tabulate(products, [["Game"][0], ["Price"][0], ["Count"][0]], tablefmt="fancy_grid")
    return amount, table


def payment(cart_uid, lang):
    return "https://oplata.info/asp2/pay.asp?cart_uid={}&email={}&lang={}".format(cart_uid, "ilay01@list.ru", lang)


payment("0FBE79006C844491B403FDFEFABCE155", "ru-RU")
    
