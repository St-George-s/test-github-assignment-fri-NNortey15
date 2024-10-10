import csv 

#declare parallel arrays 
gamesTitles=[]
genre=[]
ageRatings =[]


def readGameDataFromCSV():
    with open("Class test /game_data.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header if it exists
        for row in reader:
            # Append data to parallel arrays
            gamesTitles.append(row[0])
            genre.append(row[1])
            ageRatings.append(row[2])


    return gamesTitles, genre, ageRatings
 #check genre positon
genre_to_check = genre[0]

def countSuitableGames(genre_to_check,gameTitles,genre ,ageRatings ):
        counter = 0
        for index in gamesTitles:
             if genre == genre_to_check and ageRatings < int(18):
                  print (gamesTitles[index])
                  counter = counter + 1 

             


 

#main 

readGameDataFromCSV()
countSuitableGames(gamesTitles)