import csv

class Country:
    def __init__ (self, rank , countryname , countryCode ,gold,silver,bronze,total):
        self.rank= rank
        self.countryname= countryname
        self.countryCode= countryCode
        self.gold= gold
        self.silver= silver
        self.bronze= bronze
        self.silver.total= total

def loadingCsvFile():
    filename="Starter act/olympics2024.csv"
    with open(filename, 'r') as file: 
        reader = csv.reader(file) 
        next(reader)
        countries = []
        for row in reader: 
            newRecord = Country(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )
            countries.append(newRecord)
            
    return countries


def medalCalcuclation(athletes):
   pass

def topCountryIdentification():
    pass

def goldMedalreport(athletes):
    pass

#main program
 
athletes = loadingCsvFile()
medalCalcuclation(athletes)
topCountryIdentification()
goldMedalreport()