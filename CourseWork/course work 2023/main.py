import csv

# Define parallel arrays
attraction =[]
daySopen = []
category = []
height = []
visitors = []

# Load the service.csv file into parallel arrays
def loadingCsvFile():
    # Store file name in variable called filename
    filename="service.csv"

    # Opening and reading csv file into variable called file
    with open(filename, 'r') as file: 
        # Converts CSV file into 2D (rows -> arrays)
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # For each row, add the data from each column to its corresponding parallel array
        # e.g Add data in column 1 to attraction array
        for row in reader:
            attraction.append(row[0])
            daySopen.append(int(row[1]))      
            category.append(row[2])           
            height.append(int(row[3]))      
            visitors.append(int(row[4])) 

            return attraction,daySopen,category, height,visitors

# Finds the attraction with the most number of visitors and print
def find_max(visitors, attraction):
    max_value = myArray[0]
    max_index = 0

    # Loop over each index and compare number of visitors to max
    for index in range(1, len(visitors)):
        if visitors[index] >= max_value:  
            # Updates max value and index if bigger
            max_value = visitors[index]
            max_index = index
    
    print("The most visited attraction: " + attraction[max_index] + " with " + str(max_value) + " visitors")

# Finds the attraction with the least number of visitors and print
def find_min(visitors, attraction):
    min_value = myArray[0]
    min_index = 0
    for index in range(1, len(visitors)):
        if visitors[index] <= min_value:  
            min_value = visitors[index]
            min_index = index
    
    print("The least visited attraction: " + attraction[min_index] + " with " + str(min_value) + " visitors")

# Write the roller coasters that need a service within 7 days to a file
def rollerCoasters_needingService(attraction, category, daySopen):
    with open('service.csv', 'w') as file:
        for index in range(len(attraction)):
            if category[index] == "rollercoaster":
                # Divide current days open by 90 and store remainder 
                days =  daySopen[i] % 90
                if 90 - days <= 7:
                    file.write(attraction[index] + '\n')


#main
loadingCsvFile()  
find_max(visitors, attraction) 
find_min(visitors, attraction)  
rollerCoasters_needingService(attraction, category, daySopen) 


