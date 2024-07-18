
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from utils.utils import MONGO_USER, MONGO_PASSWORD, MONGO_HOST, MONGO_DB_URI,MONGO_DB

# URL de conexión a MongoDB
mongo_url = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}{MONGO_HOST}/{MONGO_DB_URI}"


# Create a new client and connect to the server
client = MongoClient(mongo_url, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)