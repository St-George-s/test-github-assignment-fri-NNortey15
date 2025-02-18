import csv

# Declare record class
class Orders:
    def __init__(orderNum, date, email, option , cost, rating):
        self.orderNum = orderNum
        self.date = date
        self.email = email
        self.option = option
        self.cost = cost 
        self.rating = float(rating)  


# Read Orders from a CSV file
def readOrdersfromCSV():
    # Array for storing list of sighting records
    Orders = []

    # Opening file in read mode
    with open("2025 CourseWork /orders.txt", 'r') as file:
        reader = csv.reader(file)
     
        # Read each row and create a Orders object
        for row in reader:
            orderNum, date, email, option , cost, rating= row
            Orders.append(Orders(orderNum, date, email, option , cost, rating))

    return Orders

# 2.1	Set position to -1
orders =[-1] 
# 2.2	Set index to 0
index = 0
# 2.3	Ask user to enter month to search for
UsersChosenMonth = (" Enter month to search for")
# 2.4	While position is -1 and index is less than the length of the array
for x in range(1, len(Orders)
# 2.5	    If current month is equal to searched month and current rating is 5 then
if orders[x].date and orders[x].rating == int(5):
# 2.6	        Set position to index
orders = index
# 2.7	    End if

# 2.8	    Add 1 to index
 index = index + 1
# 2.9	End while

# 2.10	Return position
	
# 3.1	Open new file ‘winningCustomer.txt’
# 3.2	    If position is 0 or above then
# 3.3	        Write winning order number, email and cost to ‘winningCustomer.txt’
# 3.4	    Else
# 3.5	        Write ‘No winner’ to ‘winningCustomer.txt’
# 3.6	    End if
# 3.7	Close ‘winningCustomer.txt’
	
# 4.1	Call countOption function to return the number of orders delivered
# 4.2	Call countOption function to return the number of orders collected
# 4.3	Output the total number of orders delivered
# 4.4	Output the total number of orders collected
