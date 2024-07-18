from models.User import User_Model

import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener variables de entorno
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_HOST=os.getenv('MONGO_HOST')
MONGO_DB_URI = os.getenv('MONGO_DB_URI')
MONGO_DB = os.getenv('MONGO_DB')
