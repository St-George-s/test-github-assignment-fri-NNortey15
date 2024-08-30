def get_destination():
    destination= input("Enter the travel destination (type 'END' to stop): ")
    return destination 

def getNumberofPeople():
    numberOfpeople= input("Enter the amount of people going on the trip:")
    return numberOfpeople

def getTravelmethod():
    travelMethod= input("What method of travel do you use?")
    return travelMethod

def print_travel_details(destination, numberOfpeople, travelMethod):
    print(destination + numberOfpeople + travelMethod)

#MAIN PROGRAM
destination=get_destination()   
while destination != "END":
    numberOfpeople=getNumberofPeople()
    travelMethod=getTravelmethod()

    print( "Your destination is" + destination + "and you plan on getting there by "+ travelMethod + "with " + numberOfpeople + "people")
    destination=get_destination()   
print("Bye")