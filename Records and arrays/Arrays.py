frameSizes = [20, 22]
brand = ["Giant", "Trek"]
Model = ["Escape 2", "Marlin 5"]
type = ["Hybrid ", "Mountain"]
price = [450.000, 370.000]
electricAssit = [False, False]

myFirstcar = Car("yellow", "honda", 200, 1999)
mySecondcar = Car("blue", "Audi", 3000, 2005)
myThirdcar = Car("red", "tesla", 4000, 1980)

Bicycles = [
    Bicycle("Giant", "Escape 2", 20, "Hybrid", 450.00, False),
    Bicycle("Trek", "Marlin 5", 22, "Mountain", 370.00, False)
]

cars = [
    Car("yellow", "honda", 200, 1999),
    Car("blue", "Audi", 3000, 2005),
    Car("red", "tesla", 4000, 1980)
]

brand = ["Purina", "Pedigree"]
animalType = ["Cat", "Dog"]
weight = [1.5, 2.0]
price = [24.99, 18.99]
inStock = [10, 20]

stockedPetFoods = [
    PetFood("Purina", "Cat", 1.5, 24.99, 10),
    PetFood("Pedigree", "Dog", 2.0, 18.99, 20)
]

print(stockedPetFoods[0].brand,"is the a brand of a ",stockedPetFoods[0].animalType, ".Cats weigh about", stockedPetFoods[0].weight, "Kg.They cost ", stockedPetFoods[0].price, "but there are only", stockedPetFoods[0].inStock, "left in stock")
print(stockedPetFoods[1].brand, "is the a brand of a ", stockedPetFoods[1].animalType, ".Cats weigh about", stockedPetFoods[1].weight, "Kg.They cost ", stockedPetFoods[1].price, "but there are only",  stockedPetFoods[1].inStock, "left in stock")
# for stockedPetFood in stockedPetFoods:
print(stockedPetFood.animalType)
print()

materials = ["Acrylic Yarn", "Beading Wire"]
colors = ["Red", "Silver"]
quantities = [150, 75]
pricesPerunit = [5.50, 3.75]
ecoFriendly = [True, False]


brands = ["Samsung", "Apple", "Motorola"]
models = ["Galaxy S21", "iPhone 12", "Brick"]
storages = ["128GB", "64GB", "500MB"]
prices = [799.00, 699.00, 50.50]
waterProof = [True, False, False]

titles = ["To Kill a Mockingbird", "Sapiens"]
authors = ["Harper Lee", "Yuval Noah Harari"]
publishedYears = [1960, 2011]
genres = ["Fiction", "Non-Fiction"]
hardCovers = [True, False]