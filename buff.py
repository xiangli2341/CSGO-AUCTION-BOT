import gspread

service_account = gspread.service_account(filename="buff_keys.json")
sheet = service_account.open("Buff Data")
worksheet = sheet.worksheet("Sheet1")
all_records_buff = worksheet.get_all_records()


class Buff:
    def __init__(self):
        self.dict = {}
        self.item_finder()

    def item_finder(self):
        for item in all_records_buff:
            item_name = item["ITEM"]
            item_listing = item["LISTING"]
            item_buy_order = item["BUY ORDER"]
            self.dict[item_name] = {"listing": item_listing, "buy_order": item_buy_order}