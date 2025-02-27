import csv

#array of records 
class Country:
    def __init__ (self, rank , countryName , countryCode ,gold,silver,bronze,total):
        self.rank= rank
        self.countryName= countryName
        self.countryCode= countryCode
        self.gold= gold
        self.silver= silver
        self.bronze= bronze
        self.total= total

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
                int(row[3]),
                int(row[4]),
                int(row[5]),
                int(row[6])
            )
            countries.append(newRecord)
            
    return countries


def medalCalcuclation(countries):
   total=0
   for country in countries:
    total = total + country.total
    
    print(total)
       

def topCountryIdentification(countries):
    max = countries[0]

    for index in range(1, len(countries)):
        if countries[index].total >= max.total:
            max = countries[index]
    print(max.countryName)

def goldMedalreport(countries):
  with open('countries.txt', 'w') as file: 
      for country in countries:
         if country.gold > 30:
            file.write(str(country.gold) )
            file.write(country.countryName + "\n")
     


#main program
countries = loadingCsvFile()
medalCalcuclation(countries)
topCountryIdentification(countries)
goldMedalreport(countries)



