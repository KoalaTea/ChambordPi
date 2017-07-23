from pymongo import MongoClient

client = MongoClient()
db = client.ChambordPi

ingredients_col = db.Ingredients
past_orders_col = db.PastOrders
drinks_col = db.Drinks
orders_col = db.Orders
