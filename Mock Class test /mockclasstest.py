import csv

# Declaring a record called Order
class Order:
    def __init__(self,customer_ID,customer_Name,product_Purchsed,amount_Spent, categoryOfProduct):
        self.customer_ID = customer_ID
        self.customer_Name = customer_Name
        self.product_Purchsed= product_Purchsed
        self.amount_Spent = amount_Spent
        self.categoryOfProduct =categoryOfProduct

def readOrdersfromCSV():
    # Array for storing list of order records
    orders =[]

    # Opening file in read mode
    with open("Mock Class test /orders.csv", 'r') as file: 
        reader = csv.reader(file) 
        #skip header 
        next(reader)

        # Loop over each row in the file treating each row as an array
        for row in reader:
            # Create an instance (copy) of the record Order for the current row
            newOrder = Order(row[0],row[1],row[2])
            # Add the new record to the end of the array orders
            orders.append(newOrders)

    return orders

# Find the maximum order where the product is a TV
def findMaxorderWithtv(orders):
    # Set the max to the record at position 0
    max = orders[0]
    # Loop over the remaining orders using the index
    for current_index in range(1, len(orders)):
        # If the order at the current index is bigger than max, update max to the current order
        if orders[current_index].amount_Spent > max.amount_Spent and "TV" in orders[current_index].product_Purchsed :
            max = orders[current_index]
    print("The product with max orders that is a TV is " + max.product_Purchsed)

#main

orders = readOrdersfromCSV()
findMaxorderWithtv(orders)