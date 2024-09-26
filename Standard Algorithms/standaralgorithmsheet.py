times_spent = [5,3,4,6,5]

def find_max(myArray):
    max = myArray[0]

    for index in range(1, len(myArray)):
        if myArray[index] >= max:
            max = myArray[index]
    print(max)

find_max(times_spent)
find_max([100.200,400])
find_max([-10, -90, 500])
find_max(["A", "B", "C"])

def find_min(myArray):
    min = myArray[0]
    for index in range(len(myArray)):
        if myArray[index] <= min:
            min = myArray[index]
    print(min)

find_min(times_spent)

def linear_search(myArray, target):
    found = False
    for index in myArray:
        if index == target:
            found = True
            
    if found:
        print( target , " is found in the array.")
    else: 
        print( target , " is not found in the array.")

def count_occurrences(myArray, item_to_find):
    number_found = 0

    for index in myArray:
        if index == item_to_find:
            number_found += 1

    print("There were", number_found, "occurrences of", item_to_find, "in the list") 