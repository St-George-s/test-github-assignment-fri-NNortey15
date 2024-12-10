class Competitor:
    def __init__(name,category,number,score):
        self.name = name
        self.category = category
        self.number = number
        self.score = score

def getdetails():
    # Array for storing list of sighting records
    competitors =[]

    # Opening file in read mode
    with open("file", 'r') as file: 
        reader = csv.reader(file) 
        #skip header 
        next(reader)

        # Loop over each row in the file treating each row as an array
        for row in reader:
            # Create an instance (copy) of the record Order for the current row
            newCompetitor = Competitor(row[0],row[1],row[2],row[3],row[4])
            # Add the new record to the end of the array sightings
            competitors.append(newCompetitor)

    return competitors

def searchUser(competitors):
    pass

def findelitemax(competitors):
    pass

def findaverage(competitors):
    return 

def displayandwritefile(competitors):
    with open('qualifying.txt', 'w')
      for competitor in competitors:
         if competitor :
            file.write(str() )
            file.write( + "\n")
     
