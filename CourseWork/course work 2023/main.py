import csv

attraction =[]
daySopen = []
category = []
height = []
visitors = []


def loadingCsvFile():
    filename="service.csv"
    with open(filename, 'r') as file: 
        reader = csv.reader(file) 
        next(reader)
        for row in reader:
            attraction.append(row[0])
            daySopen.append(int(row[1]))      
            category.append(row[2])           
            height.append(int(row[3]))      
            visitors.append(int(row[4])) 

            return attraction,daySopen,category, height,visitors


def find_max(myArray, attraction):
    max_value = myArray[0]
    max_index = 0
    for index in range(1, len(myArray)):
        if myArray[index] >= max_value:  
            max_value = myArray[index]
            max_index = index
    
    print("The most visited attraction: " + attraction[max_index] + " with " + str(max_value) + " visitors")


def find_min(myArray, attraction):
    min_value = myArray[0]
    min_index = 0
    for index in range(1, len(myArray)):
        if myArray[index] <= min_value:  
            min_value = myArray[index]
            min_index = index
    
    print("The least visited attraction: " + attraction[min_index] + " with " + str(min_value) + " visitors")


def rollerCoasters_needingService():
    with open('rollerCoasters_needingService.txt', 'w') as file:
        for index in range(len(attraction)):
            if category[index] == rollercoaster and daySopen[index] <= 7:
                file.write(attraction[index] + '\n')


#main
loadingCsvFile()  
find_max(visitors, attraction) 
find_min(visitors, attraction)  
rollerCoasters_needingService() 


