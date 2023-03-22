import requests
from empire_class import USER_TOKEN

BUFF_RATE = 1.025


def checker(empire_dict, hellcase_dict, steam_dict, buff_dict):
    for item in empire_dict["item_name"]:
        if item in hellcase_dict:
            empire_index = empire_dict["item_name"].index(item)
            price = empire_dict["item_current_price"][empire_index]
            empire_id = empire_dict["wear"][empire_index]

            hellcase_price = hellcase_dict[item]
            discount = (100 - ((price * 0.615) / hellcase_price * 100)).__round__(2)

            if discount >= 32:
                shadow_data = requests.get(f"https://api.shadowpay.com/api/v2/user/items?token={USER_TOKEN}&steam_market_hash_name={item}").json()
                if len(shadow_data["data"]) == 0:
                    if item not in steam_dict["item_names"]:
                        if empire_checker(item, price, empire_id):
                            item_url = empire_dict["url"][empire_index]
                            buff_listing = buff_dict[item]["listing"]
                            buff_rate = float(1 - (price * 0.615) / (buff_listing * BUFF_RATE)).__round__(2)
                            requests.get(f"https://api.telegram.org/bot1997676317:AAF-EMTXHXcqTE20ZJQansGD2KbL9-8xxyI"
                                         f"/sendPhoto?chat_id=-535146829&photo=https://community.cloudflare.steamstatic.com/economy/"
                                         f"image/{item_url}&caption= SC: 0 {item}, Buff: {buff_rate}, Current Price: {price}, Disc: {discount}")
                        else:
                            item_url = empire_dict["url"][empire_index]
                            buff_listing = buff_dict[item]["listing"]
                            buff_rate = float(1 - (price * 0.615) / (buff_listing * BUFF_RATE)).__round__(2)
                            requests.get(f"https://api.telegram.org/bot1997676317:AAF-EMTXHXcqTE20ZJQansGD2KbL9-8xxyI"
                                         f"/sendPhoto?chat_id=-535146829&photo=https://community.cloudflare.steamstatic.com/economy/"
                                         f"image/{item_url}&caption= SC: 0 MARKETTE DAHA UCUZU VAR! {item}, Buff: {buff_rate}, Current Price: {price}, Disc: {discount} ")
                else:
                    if discount >= 33:
                        if len(shadow_data["data"]) == 1:
                            if item not in steam_dict["item_names"]:
                                if empire_checker(item, price, empire_id):
                                    item_url = empire_dict["url"][empire_index]
                                    buff_listing = buff_dict[item]["listing"]
                                    buff_rate = float(1 - (price * 0.615) / (buff_listing * BUFF_RATE)).__round__(2)
                                    rate_shadow = float(1 - (shadow_data["data"][0]["price"] / hellcase_price)).__round__(2)
                                    requests.get(
                                        f"https://api.telegram.org/bot1997676317:AAF-EMTXHXcqTE20ZJQansGD2KbL9-8xxyI"
                                        f"/sendPhoto?chat_id=-535146829&photo=https://community.cloudflare.steamstatic.com/economy/"
                                        f"image/{item_url}&caption= SC: 1 {item}, Buff: {buff_rate}, Rate: {rate_shadow}, Current Price: {price}, Disc: {discount}")
                                else:
                                    item_url = empire_dict["url"][empire_index]
                                    buff_listing = buff_dict[item]["listing"]
                                    buff_rate = float(1 - (price * 0.615) / (buff_listing * BUFF_RATE)).__round__(2)
                                    rate_shadow = float(1 - (shadow_data["data"][0]["price"] / hellcase_price)).__round__(2)
                                    requests.get(
                                        f"https://api.telegram.org/bot1997676317:AAF-EMTXHXcqTE20ZJQansGD2KbL9-8xxyI"
                                        f"/sendPhoto?chat_id=-535146829&photo=https://community.cloudflare.steamstatic.com/economy/"
                                        f"image/{item_url}&caption= SC: 1 MARKETTE DAHA UCUZU VAR! {item}, Buff: {buff_rate}, Rate: {rate_shadow}, Current Price: {price}, Disc: {discount}")
                        else:
                            if discount >= 33:
                                if len(shadow_data["data"]) == 2:
                                    if item not in steam_dict["item_names"]:
                                        if empire_checker(item, price, empire_id):
                                            item_url = empire_dict["url"][empire_index]
                                            buff_listing = buff_dict[item]["listing"]
                                            buff_rate = float(1 - (price * 0.615) / (buff_listing * BUFF_RATE)).__round__(2)
                                            rate_shadow = float(
                                                (1 - (shadow_data["data"][0]["price"] / hellcase_price)) * 100).__round__(2)
                                            if rate_shadow <= 13:
                                                requests.get(
                                                    f"https://api.telegram.org/bot1997676317:AAF-EMTXHXcqTE20ZJQansGD2KbL9-8xxyI"
                                                    f"/sendPhoto?chat_id=-535146829&photo=https://community.cloudflare.steamstatic.com/economy/"
                                                    f"image/{item_url}&caption= SC: 1 {item}, Buff: {buff_rate}, Rate: {rate_shadow}, Current Price: {price}, Disc: {discount}")
                                        else:
                                            item_url = empire_dict["url"][empire_index]
                                            buff_listing = buff_dict[item]["listing"]
                                            buff_rate = float(1 - (price * 0.615) / (buff_listing * BUFF_RATE)).__round__(2)
                                            rate_shadow = float(
                                                (1 - (shadow_data["data"][0]["price"] / hellcase_price)) * 100).__round__(2)
                                            if rate_shadow <= 13:
                                                requests.get(
                                                    f"https://api.telegram.org/bot1997676317:AAF-EMTXHXcqTE20ZJQansGD2KbL9-8xxyI"
                                                    f"/sendPhoto?chat_id=-535146829&photo=https://community.cloudflare.steamstatic.com/economy/"
                                                    f"image/{item_url}&caption= SC: 2 MARKETTE DAHA UCUZU VAR! {item}, Buff: {buff_rate}, Rate: {rate_shadow}, Current Price: {price}, Disc: {discount}")


def empire_checker(item_name, current_price, item_wear):
    response = requests.get(f"https://csgoempire.gg/api/v2/trading/items?per_page=160&page=1&price_max_above=999999"
                            f"&search={item_name}&sort=asc&order=market_value").json()
    if len(response["data"]) == 1 and response["data"][0]["wear"] == item_wear:
        return True
    else:
        cheapest_item_in_market = response["data"][0]["market_value"]
        if len(str(cheapest_item_in_market)) == 4:
            cheapest_item_in_market = float(
                f"{str(cheapest_item_in_market)[:2]}." + f"{str(cheapest_item_in_market)[2:]}")
        elif len(str(cheapest_item_in_market)) == 5:
            cheapest_item_in_market = float(
                f"{str(cheapest_item_in_market)[:3]}." + f"{str(cheapest_item_in_market)[3:]}")
        else:
            cheapest_item_in_market = float(
                f"{str(cheapest_item_in_market)[:4]}." + f"{str(cheapest_item_in_market)[4:]}")

        if cheapest_item_in_market > current_price:
            return True
        elif current_price > cheapest_item_in_market and response["data"][0]["wear"] != item_wear:
            return False
        else:
            return True
