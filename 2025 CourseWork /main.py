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


#Read from file into array of records.
def readOrdersfromCSV():
    orders = []

    # Open the file with orders
    with open("2025 CourseWork /orders.txt", 'r') as file: 
        # CSV reader to read the file content
        reader = csv.reader(file) 

        # Read each row and create a Orders object
        for row in reader:
            orderNum, date, email, option, cost, rating = row
            orders.append(Orders(orderNum, date, email, option, cost, rating))
    
    return orders


#Find the position of the customer who gave the first 5-star rating in a given month.
def customerPosition(orders):
    # Set position to -1
    position = -1  
    # Set index to 0
    index = 0

    # Ask user to enter month to search for
    UsersChosenMonth = input("Enter month to search for: ") 

    # While position is -1 and index is less than the length of the array
    while position == -1 and index < len(orders):
        # If current month is equal to searched month and current rating is 5 then
        if orders[index].date[3:6] == UsersChosenMonth and orders[index].rating == 5:
            # Set position to index
            position = index  
         #Add 1 to index
        index += 1 

    #Return position 
    return position


#Write details of the winning customer, or ‘no winner’ message, to a text file.
def openNewFile(orders, position):
    #Open new file ‘winningCustomer.txt’
    with open("winningCustomer.txt", "w") as file:

        # If position is 0 or above then
        if position >= 0:
            # Write winning order number, email and cost to ‘winningCustomer.txt’
            file.write("Order Number: " + orders[position].orderNum +"\n")
            file.write("Email: " + orders[position].email + "\n")
            file.write("Cost: " + str(orders[position].cost) + "\n")
        else:
            #Write ‘No winner’ to ‘winningCustomer.txt’
            file.write("No winner\n")
            
    #Close ‘winningCustomer.txt’
    file.close()  


def countOption(orders, optionType):
    # Count the number of orders based on the given option type (Delivery or Collection)
    count = 0
    for order in orders:
        if order.option.lower() == optionType.lower():
            count += 1
    return count


#Display the total number of orders delivered and the total number of orders collected.
def displayTotals(orders):
    # Call countOption function to return the number of orders delivered
    deliveredCount = countOption(orders, "Delivery")
    # Call countOption function to return the number of orders collected
    collectedCount = countOption(orders, "Collection")
    # Output the total number of orders delivered
    print("Total number of orders delivered: " + str(deliveredCount))
    # Output the total number of orders collected
    print("Total number of orders collected: " + str(collectedCount))


# Main 
orders = readOrdersfromCSV()
position = customerPosition(orders)
openNewFile(orders, position)
displayTotals(orders)
