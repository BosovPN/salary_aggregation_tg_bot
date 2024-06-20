from pymongo.mongo_client import MongoClient
from os import getenv


# Replace the placeholder with your Atlas connection string
PASSWORD = getenv("MONGODB_PASSWORD")
uri = f"mongodb+srv://user:{PASSWORD}@testcluster.ye0go0e.mongodb.net/?retryWrites=true&w=majority&appName=testCluster"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client['database']

coll = db['sample_collection']
