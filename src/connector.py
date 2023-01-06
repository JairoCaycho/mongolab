import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_USER = os.environ.get('MONGO_USER')
MONGO_USER_PASS = os.environ.get('MONGO_USER_PASS')
CLUSTER_URL = os.environ.get('CLUSTER_URL')
LAB_URI = f'mongodb+srv://{MONGO_USER}:{MONGO_USER_PASS}@{CLUSTER_URL}?authMechanism=DEFAULT'
DATABASE = os.environ.get('DATABASE')

lab_client = MongoClient(LAB_URI)

database = lab_client.get_database(name=DATABASE)

collection_planets = database.get_collection(name='planets')
collection_comets = database.get_collection(name='comets')

