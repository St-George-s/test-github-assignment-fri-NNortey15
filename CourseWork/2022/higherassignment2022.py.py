import csv

# Declare record class
class Sightings:
    def __init__(self, town, mammal, date, age):
        self.town = town
        self.mammal = mammal
        self.date = date
        self.age = int(age)  

# Read sightings from a CSV file
def readOrdersfromCSV():
    # Array for storing list of sighting records
    sightings = []

    # Opening file in read mode
    with open("CourseWork/2022/mammals.txt", 'r') as file:
        reader = csv.reader(file)
        # Skip header
        next(reader)

        # Read each row and create a Sightings object
        for row in reader:
            town, mammal, date, age = row
            sightings.append(Sightings(town, mammal, date, age))

    return sightings

# # Find the maximum age of the oldest walker
# def findMaxAge(sightings):
    
#     max_sighting = sightings[0]

#     # Loop over the remaining orders using the index
#     for current_index in range(1, len(sightings)):
#         if sightings[current_index].age > max_sighting.age:
#             max_sighting = sightings[current_index]

#     print("The oldest walker is " + str(max_sighting.age) + " years old.")

# # # Find and display the dates of sightings of a chosen mammal in a particular town
# def displayDates(sightings, chosenTown, chosenMammal):
#     print("Sightings of " + chosenMammal + " in " + chosenTown )

# #     # Filter records matching the chosen town and mammal
#     for sighting in sightings:
#         if sighting.town.upper() == chosenTown.upper() and sighting.mammal.upper() == chosenMammal.upper():
#             print( "The dates of sightings were :" sighting.date)


# Count and display the number of sightings for each date
# def countAndDisplayNumOfSightings(sightings):
#     print("Number of sightings for each date:")

    
  

# Loop through each date and count occurrences
    DayToCount = sightings[0].date
    count = 1
    for dayToCount in count:
        count = 1
        for sighting in sightings:
            if DayToCoount == sightings.date:
                count += 1
        print( dayToCount + Count)

# Main program

    # Read the data from the CSV file
sightings = readOrdersfromCSV()

    # Find and display the age of the oldest walker
findMaxAge(sightings)

    # Display the dates of sightings for a chosen mammal and town
chosenTown = input("Enter the town ")
chosenMammal = input("Enter the mammal")
displayDates(sightings, chosenTown, chosenMammal)

    # # Count and display the number of sightings for each date
countAndDisplayNumOfSightings(sightings)
