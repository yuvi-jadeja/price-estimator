import json
import joblib
import numpy as np

__locations = None
__data_columns = None
__model = None

def loadSavedData():
    print("Loading data...")
    global __locations
    global __data_columns
    global __model

    with open('./model/columns.json', 'r') as json_file:
        __data_columns = json.load(json_file)['data_columns']
        __locations = __data_columns[3:]

    with open('./model/bangaluru_house_price_model', 'rb') as model_file:
        __model = joblib.load(model_file)
    
    print("Loaded successfully...")

def getLocationNames():
    return __locations

def getEstimatedPrice(location: str, sqft: float, bath: int, bed: int) -> float:
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bed
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)