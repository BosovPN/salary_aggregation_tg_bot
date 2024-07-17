from pymongo.mongo_client import MongoClient
from os import getenv


# Replace the placeholder with your Atlas connection string
CONNECTION_STRING = getenv("MONGODB_CONNECTION_STRING")
uri = f"{CONNECTION_STRING}"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client['database']

coll = db['sample_collection']


def get_values_in_time_interval(dt_from: str, dt_upto: str):
    try:
        query = {'dt': {'$gte':dt_from, '$lte':dt_upto}}
        result = coll.find(query)
        return result
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)
