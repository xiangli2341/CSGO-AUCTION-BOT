import requests
import gspread

service_account = gspread.service_account(filename="configs.json")
sheet = service_account.open("CONFIGS")
worksheet = sheet.worksheet("Sheet1")
all_records_config = worksheet.get_all_records()
USER_TOKEN = all_records_config[0]["USER"]
EMPIRE_COOKIE = all_records_config[0]["EMPIRE COOKIE"]

headers = {
    'authority': 'csgoempire.gg',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Yandex";v="22"',
    'accept': 'application/json, text/plain, */*',
    'x-empire-device-identifier': '9a5d9d9a-efb0-409a-b52e-8b3f93d3cb67',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.3.852 Yowser/2.5 Safari/537.36',
    'referer': 'https://csgoempire.gg/withdraw',
    'accept-language': 'tr,en;q=0.9',
    'cookie': EMPIRE_COOKIE
}
ENDPOINT = "https://csgoempire.gg/api/v2/trading/items?per_page=2500&page=1&auction=yes&price_max_above=9999&sort=desc&order=market_value"


class Empire:
    def __init__(self):
        self.response = requests.get(ENDPOINT, headers=headers).json()
        self.dict = {
            "item_name": [],
            "item_current_price": [],
            "url": [],
            "wear": []
        }

        for item in self.response["data"]:
            self.item_name = item["name"]
            self.item_base_price = item["market_value"]
            self.item_highest_bid = item["auction_highest_bid"]
            self.item_wear = item["wear"]
            self.url = item["icon_url"]

            if self.item_highest_bid is not None and self.item_highest_bid >= self.item_base_price:
                self.item_price = self.item_highest_bid
            else:
                self.item_price = self.item_base_price

            if self.item_price > 6000:
                self.dict["item_name"].append(self.item_name)
                self.dict["url"].append(self.url)
                self.dict["wear"].append(self.item_wear)

                if len(str(self.item_price)) == 3:
                    self.item_price = f"{str(self.item_price)[:1]}." + f"{str(self.item_price)[1:]}"
                    self.dict["item_current_price"].append(float(self.item_price))
                elif len(str(self.item_price)) == 4:
                    self.item_price = f"{str(self.item_price)[:2]}." + f"{str(self.item_price)[2:]}"
                    self.dict["item_current_price"].append(float(self.item_price))
                elif len(str(self.item_price)) == 5:
                    self.item_price = f"{str(self.item_price)[:3]}." + f"{str(self.item_price)[3:]}"
                    self.dict["item_current_price"].append(float(self.item_price))
                elif len(str(self.item_price)) == 6:
                    self.item_price = f"{str(self.item_price)[:4]}." + f"{str(self.item_price)[4:]}"
                    self.dict["item_current_price"].append(float(self.item_price))
                elif len(str(self.item_price)) == 7:
                    self.item_price = f"{str(self.item_price)[:5]}." + f"{str(self.item_price)[5:]}"
                    self.dict["item_current_price"].append(float(self.item_price))
                elif len(str(self.item_price)) == 8:
                    self.item_price = f"{str(self.item_price)[:6]}." + f"{str(self.item_price)[6:]}"
                    self.dict["item_current_price"].append(float(self.item_price))