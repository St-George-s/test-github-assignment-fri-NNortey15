import csv 

#declare parallel arrays 
gamesTitles=[]
genre=[]
ageRatings =[]
platform =[]


def readGameDataFromCSV():
    with open("Class test /game_data.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header if it exists
        for row in reader:
            # Append data to parallel arrays
            gamesTitles.append(row[0])
            genre.append(row[1])
            ageRatings.append(row[2])
            platform.append(row[3])

    return gamesTitles, genre, ageRatings,platform 
 #check genre positon
genre_to_check = genre[0]

def countSuitableGames(genre_to_check,gameTitles,genre ,ageRatings ):
        counter = 0
        for index in gamesTitles:
             if genre == genre_to_check and ageRatings < int(18):
                  print (gamesTitles[index])
                  counter = counter + 1 

#finding specfic genre that has games under the age of 18             
def findgamesSpeficgenre(gamesTitles,genre,ageRatings,Platform):
    with open('Platform_suitable_games.txt', 'w') as file:
        for index in range(len(gamesTitles)):

            if genre[index] == "Horror" , "Sci-Fi" , "Fanatsy" and ageRatings < int(18):
                #write the game titles and genre and platform to the file  
                    file.write(gamesTitles[index],genre[index] + "-" + platform[index]+ '\n')


 

#main 

readGameDataFromCSV()
countSuitableGames(gamesTitles)
findgamesSpeficgenre(gamesTitles,genre,ageRatings,platform)