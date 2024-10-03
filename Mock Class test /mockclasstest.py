import csv

# Declaring a record called Order
class Order:
    def __init__(self,customer_ID,customer_Name,product_Purchsed,amount_Spent, categoryOfProduct):
        self.customer_ID = customer_ID
        self.customer_Name = customer_Name
        self.product_Purchsed= product_Purchsed
        self.amount_Spent = amount_Spent
        self.categoryOfProduct =categoryOfProduct

def  readOrdersfromCSV():
    orders =[]
    # Opening file in read mode
    with open("Mock Class test /orders.csv", 'r') as file: 
        reader = csv.reader(file) 
        #skip header 
        next(reader)
        for row in reader: 
            newOrders = Order(row[0],row[1],row[2])
            orders.append(newOrders)

    return orders


def findMaxorderWithtv(orders):
    max = orders[0]
    for current_index in range(1, len(orders)):
        if orders[current_index].amount_Spent > max.amount_Spent:
            max = orders[current_index]
    print(max.orders )

#main

orders = readOrdersfromCSV()
findMaxorderWithtv(orders)