import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_USER = os.environ.get('MONGO_USER')
MONGO_USER_PASS = os.environ.get('MONGO_USER_PASS')
CLUSTER_URL = os.environ.get('CLUSTER_URL')


def connection_string():
    lab_uri = f'mongodb+srv://{MONGO_USER}:{MONGO_USER_PASS}@{CLUSTER_URL}?authMechanism=DEFAULT'
    print(lab_uri)

def connector_manager():
    connection_string()