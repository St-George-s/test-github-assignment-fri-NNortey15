import random

def generate_username(firstName, surName):
    #takes the first few letters in an word 
    firstName=firstName[0:3]
    surName=surName[0:3]
    #chooses a number from random between 100 and 999
    randomnum= random.randint(100,999 )
    uname=firstName+surName+str(randomnum)
    #passes back a result so that its available when you call it 
    return uname
    
firstName=input("What is your first name?")
surName=input("What is your surname?")
age=input("How old are you?")
dofeAward=input("Enter what level of Dofe you are doing:")

#passing through firstname and surname to generate a username 
uname = generate_username(firstName,surName)
print(uname)