import csv

# Declare parallel arrays
studentID = []
forename = []
surname = []
grades = []

# Function to read CSV data into parallel arrays
def getQualifyingData():
    with open("File handling/students.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header if it exists
        for row in reader:
            # Append data to parallel arrays
            studentID.append(row[0])
            forename.append(row[1])
            surname.append(row[2])
            grades.append(row[3])  # Convert jumps to integers
    
    print(studentID)
    print(forename)

    return studentID,  forename, surname, grades

# Main
getQualifyingData()