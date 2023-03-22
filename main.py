from functions import checker
from hellcase import Hellcase
from empire_class import Empire
from steam_class import SteamInventory
from buff import Buff
import requests
import time

steam = SteamInventory()
steam_dict = steam.steam_dict
hellcase = Hellcase()
hellcase_dict = hellcase.dict
buff = Buff()
buff_dict = buff.dict

counter = 0
while True:
    counter += 1
    if counter == 750:
        hellcase = Hellcase()
        hellcase_dict = hellcase.dict
        print("HELLCASE HELLCASE HELLCASE HELLCASE HELLCASE HELLCASE HELLCASE HELLCASE")

        steam = SteamInventory()
        steam_dict = steam.steam_dict
        print("STEAM STEAM STEAM STEAM STEAM STEAM STEAM STEAM STEAM STEAM STEAM STEAM")

        buff = Buff()
        buff_dict = buff.dict
        print("BUFF BUFF BUFF BUFF BUFF BUFF BUFF BUFF BUFF BUFF BUFF BUFF BUFF BUFF BUFF")
        counter = 0

    try:
        empire = Empire()
        empire_dict = empire.dict
        checker(empire_dict, hellcase_dict, steam_dict, buff_dict)
    except requests.exceptions.ConnectionError:
        time.sleep(3)
    except IndexError:
        print(IndexError)
        time.sleep(1)
        pass
    except ValueError:
        print(ValueError)
        time.sleep(1)
        pass
    except KeyError:
        print(KeyError)
        time.sleep(2)
        pass
