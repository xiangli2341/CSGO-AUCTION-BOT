import requests


class SteamInventory:
    def __init__(self):

        self.steam_dict = {
            "item_names": []
        }

        response_furkan = requests.get("https://steamcommunity.com/inventory/76561198893128342/730/2?l=english&count=5000").json()
        for item_furkan in response_furkan["descriptions"]:
            item_name = item_furkan["market_hash_name"]
            self.steam_dict["item_names"].append(item_name)

        response_ahmet = requests.get("https://steamcommunity.com/inventory/76561198346079540/730/2?l=english&count=5000").json()
        for item_ahmet in response_ahmet["descriptions"]:
            item_name = item_ahmet["market_hash_name"]
            self.steam_dict["item_names"].append(item_name)

        response_mehmet = requests.get(
            "https://steamcommunity.com/inventory/76561198328018727/730/2?l=english&count=5000").json()
        for item_mehmet in response_mehmet["descriptions"]:
            item_name = item_mehmet["market_hash_name"]
            self.steam_dict["item_names"].append(item_name)