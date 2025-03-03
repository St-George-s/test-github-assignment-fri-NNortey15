import csv

# Declare class Orders to represent each order's details
class Orders:
    def __init__(self, orderNum, date, email, option, cost, rating):
        # Initialize the attributes for the order
        self.orderNum = orderNum
        self.date = date
        self.email = email
        self.option = option
        self.cost = float(cost)  # making sure cost is a float for calculations
        self.rating = float(rating)  # making sure rating is a float


def readOrdersfromCSV():
    orders = []
     # Open the file with orders
    with open("2025 CourseWork /orders.txt", 'r') as file: 
         # CSV reader to read the file content
        reader = csv.reader(file) 
        for row in reader:
            # Create an Orders object for each row and append it to the orders list
            orderNum, date, email, option, cost, rating = row
            orders.append(Orders(orderNum, date, email, option, cost, rating))
  
    return orders


def customerPosition(orders):
    #Set position to -1
    position = -1  
    #Set index to 0
    index = 0
    #Ask user to enter month to search for
    UsersChosenMonth = input("Enter month to search for: ") 
    # Loop through all orders and find the one with the given month and 5-star rating
    while position == -1 and index < len(orders):
    #If current month is equal to searched month and current rating is 5 then
        if orders[index].date[3:6] == UsersChosenMonth and orders[index].rating == 5:
    #Set position to index
            position = index  
            #Add 1 to index
            index += 1
            #Return position
            return position
            

def openNewFile(orders, position):
#Open new file ‘winningCustomer.txt’
    file = open("winningCustomer.txt", 'w')
# If position is 0 or above then
    if position >= 0:
    #Write winning order number, email and cost to ‘winningCustomer.txt’
                file.write(orders.orderNum + " " + orders.email + " " + str(orders.cost) + "\n")
    #    Else
    else:
    #        Write ‘No winner’ to ‘winningCustomer.txt’
                file.write("No winner\n")    
    #    End if
    #Close ‘winningCustomer.txt


def countOption(orders):
    #Counts the number of orders that match a specific option 
    count = 0
    for order in orders:
        if order.option() == order.option.lower():
            count =+ 1
            
    return count 


def totalNumOfOrders(orders):
#Call countOption function to return the number of orders delivered
    deliveredCount = countOption(orders.option, "Delivery")
    #Call countOption function to return the number of orders collected
    collectedCount = countOption(orders.option, "Collection")
    #Output the total number of orders delivered
    print("Total number of orders delivered: " + str(deliveredCount))
    #Output the total number of orders collected
    print("Total number of orders collected: " + str(collectedCount))

# Main execution

orders = readOrdersfromCSV()
position = customerPosition(orders)
openNewFile(orders, position) 
countOption(orders) 
totalNumOfOrders(orders)
