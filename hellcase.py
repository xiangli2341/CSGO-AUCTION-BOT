import gspread

service_account = gspread.service_account(filename="hellcase_keys.json")
sheet = service_account.open("Hellcase Data")
worksheet = sheet.worksheet("Sheet1")
all_records_hellcase = worksheet.get_all_records()


class Hellcase:
    def __init__(self):
        self.dict = {}
        self.item_finder()

    def item_finder(self):
        for item in all_records_hellcase:
            item_name = item["ITEM"]
            item_price = item["PRICE"]
            self.dict[item_name] = item_price