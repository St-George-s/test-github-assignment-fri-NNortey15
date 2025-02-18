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

#Write "The prize winning members are:" to the results.txt file
    file.write("The prize winning members are:\n")

#Start loop for each record in members array
    for member in members:

#If the distance the member walked is greater than 0.7 * furthest
        if member.distance > 0.7 * furthest:

# Write the forename and surname to the results.txt file
            file.write(member.forename + " " + member.surname + "\n")
