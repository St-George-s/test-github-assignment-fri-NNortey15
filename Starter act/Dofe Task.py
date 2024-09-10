import random

def generate_username(firstName, surName):
    firstName=(firstName[0:3])
    surName=(surName[0:3])
    randomnum= random.randint(100,999 )
    print(firstName+surName+str(randomnum))
    return generate_username

firstName=input("What is your first name?")
surName=input("What is your surname?")
age=input("How old are you?")
dofeAward=input("Enter what level of Dofe you are doing:")

generate_username(firstName,surName)
