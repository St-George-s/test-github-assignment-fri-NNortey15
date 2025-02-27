import csv 

#Declare class record 
class Orders:
     def __init__(self,orderNum, date, email, option , cost, rating):
         self.orderNum = orderNum
         self.date = date
         self.email = email
         self.option = option
         self.cost = float(cost)
         self.rating = float(rating)  

        
def readOrdersfromCSV():

    orders = []

    with open("2025 CourseWork /orders.txt", 'r') as file:
        reader = csv.reader(file)
        
    for row in reader:
        orderNum, date, email, option , cost, rating= row
        orders.append(orders(orderNum, date, email, option , cost, rating))
    return orders

def customerPosition(orders):
    #Set position to -1
    position = -1
    #Set index to 0
    index = 0

    orders = readOrdersfromCSV()
    #While position is -1 and index is less than the length of the array
    while position and index == len(1,orders):
    #If current month is equal to searched month and current rating is 5 then
        if UsersChosenMonth == orders.date[3:5] and orders.rating == 5:
            position = index
    index = index + 1

    return position

def openNewFile(orders):
#Open new file ‘winningCustomer.txt’
    with open("winningCustomer.txt", 'w') as file:
        position = 
#If position is 0 or above then
        if position >= 0 :
#Write winning order number, email and cost to ‘winningCustomer.txt’
            file.write(orders.orderNum + "" + orders.email + "" + orders.cost + "\n")
        else:
#Write ‘No winner’ to ‘winningCustomer.txt’
         file.write("No winner\n")



def countOption(orders,option):
    count = 0 
    for order in orders:
        if order.option.lower() == option.lower(): 
            count += 1 
        
        return count 
    

# #main 
orders = openNewFile(Orders)
#Ask user to enter month to search for
UsersChosenMonth = (" Enter month to search for")
deliveredCount = (orders , "delivered") 
collectedCount = (orders , "collected") 
#Output the total number of orders delivered
print("Total number of orders delivered: ", deliveredCount) 
#Output the total number of orders collected
print("Total number of orders collected: ", collectedCount)
