from pymongo import MongoClient

DB_NAME = "ChambordPi"
DB = MongoClient().get_database(DB_NAME)
