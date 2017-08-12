from pymongo import MongoClient

client = MongoClient()
db_obj = client.ChambordPi

ingredients_col = db_obj.Ingredients
past_orders_col = db_obj.PastOrders
drinks_col = db_obj.Drinks
orders_col = db_obj.Orders
