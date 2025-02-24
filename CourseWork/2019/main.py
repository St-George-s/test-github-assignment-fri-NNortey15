class Member:
    def __init__(self, forename, surname, distance):
        self.forename = forename
        self.surname = surname
        self.distance = float(distance)

#  Open members.txt file and initialize members array
members = []

#with open('members.txt', 'r') as file:
#   for row in header:
        #  Get member forename, surname, and distance
       
        # Store member forename, surname, and distance in members array
#        members.append(Member(forename, surname, distance))


# Step 2: Find the furthest distance walked
furthest = members[0].distance

#Start fixed loop from second member to end of array
for member in members[1:]:

    #If distance the current member walked is greater than furthest
    if member.distance > furthest:
        
        #Set furthest to current distance
        furthest = member.distance

# Display the furthest distance walked
print("The furthest distance walked is: " + str(furthest))


# Write club prize winners to file
# Open results.txt file
with open('results.txt', 'w') as file:
#Find the position of the customer who gave the first 5-star rating in a given month.
#def customerPosition(Orders):

# 2.1	Set position to -1
#orders = -1
# 2.2	Set index to 0
#index = 0
# 2.3	Ask user to enter month to search for
#UsersChosenMonth = (" Enter month to search for")
# 2.4	While position is -1 and index is less than the length of the array
#for x in range (1, len(Orders)
# 2.5	    If current month is equal to searched month and current rating is 5 then
#if orders[x].date and orders[x].rating == int(5):
# 2.6	        Set position to index
#orders = index
# 2.7	    End if

# 2.8	    Add 1 to index
 #index = index + 1
# 2.9	End while

# 2.10	Return position
#	return orders
    
# 3.1	Open new file ‘winningCustomer.txt’
# with open("winningCustomer,txt", 'w') as file:
        
# 3.2	    If position is 0 or above then
#if index >= 0 ;
# 3.3	        Write winning order number, email and cost to ‘winningCustomer.txt’
#file.write(Orders.orderNum + "" + Orders.email + Orders.cost + "\n")
# 3.4	    Else
# 3.5	        Write ‘No winner’ to ‘winningCustomer.txt’
#file.write("No winner\n")
# 3.6	    End if
# 3.7	Close ‘winningCustomer.txt’
#file.close()
	
# 4.1	Call countOption function to return the number of orders delivered
# 4.2	Call countOption function to return the number of orders collected
# 4.3	Output the total number of orders delivered
# 4.4	Output the total number of orders collected





#Write "The prize winning members are:" to the results.txt file
    file.write("The prize winning members are:\n")

#Start loop for each record in members array
    for member in members:

#If the distance the member walked is greater than 0.7 * furthest
        if member.distance > 0.7 * furthest:

# Write the forename and surname to the results.txt file
            file.write(member.forename + " " + member.surname + "\n")
