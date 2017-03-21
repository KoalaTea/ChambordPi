from pymongo import MongoClient

client = MongoClient()
db = client.ChambordPi

ingredientsCol = db.Ingredients
pastOrdersCol = db.PastOrders
drinksCol = db.Drinks
ordersCol = db.Orders
