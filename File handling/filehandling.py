import csv

# Declare record
class Student:
    def __init__(self,studentID,forename,surname,grades):
        self.studentID = studentID
        self.forname = forename
        self.surname = surname
        self.grades = grades


# Function to read CSV data into parallel arrays
def getQualifyingData():
    with open("File handling/students.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header if it exists
        students=[]
        for row in reader:
           newStudent=Student(row[0], row[1], row[2],row[3])
           students.append(newStudent)

    return students

# Main
students = getQualifyingData()
print(students[3].grades)