"""
Json based easy data handler.

Version -> 0.0.1

Last Modification -> None

"""

import json
import json.decoder

def on_change(path : str ) :
    """
    Determines where shall be the target data holder file will be.
    :param path: Path to set as new.
    """
    with open("data.json","rb") as json_f:
        json_f = json.load(json_f)
    json_f["target"] = path
    with open('data.json','w+') as json_f2:
        json.dump(obj=json_f,fp=json_f2)


def save_data_1(key_list : list , value_list : list):
    """
    Saves data of the parameter!

    Note that Save Data 1 is meant to save your data with lists with given indexes being same.
    """
    with open("data.json","rb") as json_1:
        json_1 = json.load(json_1)
    with open(json_1["target"],"rb") as json_2:
        json_2 = json.load(json_2)
    for v in key_list:
        if type(v) == str:
            json_2[v] = value_list[key_list.index(v)]
        else:
            print("ERROR")
            break
    with open(json_1["target"],"w+") as json_3:
        json.dump(obj=json_2,fp=json_3)
        