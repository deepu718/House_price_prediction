import json
import pickle
import numpy as np
from functools import lru_cache
__locations = None
__data_columns = None
__model = None
@lru_cache
def get_estimated_price(location,sqft,bhk,bath,balcony):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns)) 
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_index >= 0:
        x[loc_index]  = 1
    return round(__model.predict([x])[0],2)
def get_location_names():
    return __locations
@lru_cache
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model
    with open("C:/Users/deepu/Documents/house_price_prediction/server/artifacts/columns.json","r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[4:]

    with open("C:/Users/deepu/Documents/house_price_prediction/server/artifacts/bengaluru_house_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts..done")

if __name__ == "__main__":
    print(get_estimated_price('1st phase jp nagar',1000,2,2,2))