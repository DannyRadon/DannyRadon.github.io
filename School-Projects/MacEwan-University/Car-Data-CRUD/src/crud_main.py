#-------------------------------------------------------------------------------
# Name: Danny Radon
# Course: CMPT 103-AS02
# Work: Project - Car Data CRUD Program
# 
#
# Academic Integrity Pledge: I, Danny Radon, hereby pledge the work done in this
#                          laboratory is that of my own and no one elses.
#                                                                  D.R.
#-------------------------------------------------------------------------------

# Variable containing file name created for use by main function
filename = "data/carData.csv"

# Load Data Function
def loadData(filename):

# Data List created for processing lines from File
    data = []

# File is opened and read line by line
    carFile = open(filename)
    fileLine = carFile.readline()


# Lines read from File is stripped of new space characters '\n' and added to data list
    while fileLine is not "":
        
        fileLine = fileLine.strip()
        data.append(fileLine)
        fileLine = carFile.readline()

# Data containing processed information is returned to caller.
    return data


# Add Car to Data Function
def addCar(data):

# Input prompts to gain full information on new car (make, year, model, cost, etc)
    carMake = input("\nPlease enter the make of the car: ")
    carModel = input("Please enter the model of the car: ")
    carYear= input("Please enter the year of the car: ")
    carCost = input("Please enter the cost of the car: ")
    carRange = input("Please enter the range of the car: ")
    carComment = input("Please enter any comment of the car: ")

# Variable created to make list of info. about new car
    newCar = [carMake, carModel, carYear, carCost, carRange, carComment]

# Data of new car is appended to data list.
    data.append(newCar)

# Updated data list is returned to caller
    return data


# Modify Car in Data Function
def modifyCar(data): 

# User-Prompt to select which car in data list to modify (not remove/not add)
    print("\nWhich car would you like to modify? ")

# Counter established for sub-menu creation 
    i = 1

# For-Loop created to process each car from data list
    for car in data[1::]:

# Menu printed for user prompt. Counter increases by the amount of cars in data list.
        print(str(i) + ")", car[0], car[1], sep = " ")

# Counter Increment (from 1 to how many cars are in data list)
        i = i + 1

# User Prompt to choose which car in data list to modify
    carSelect = int(input("Please enter an option (number): "))

# Error-Proofing; ensuring chosen option matches menu options
    while carSelect not in range(1,i):
        carSelect = int(input("Please enter a valid option: "))

# If Statements created, dependant on user's choice of option
    if carSelect == 1:

# Variables established to store original data about chosen car in menu position before modifying
        ogCar = data[1]

# Original Make of Chosen Car Stored
        ogMake = ogCar[0]

# Original Model of Chosen Car Stored
        ogModel = ogCar[1]

# Original Year of Chosen Car Stored
        ogYear = ogCar[2]

# Original Cost of Chosen Car Stored
        ogCost = ogCar[3]

# Original Range of Chosen Car Stored
        ogRange = ogCar[4]

# Original Comment of Chosen Car Stored
        ogComment = ogCar[5]

# User inputs for creating/storing modified data. Replaces car data in menu position
        modMake = input("\nWhat is the new make of the car?: ")
        modModel = input("What is the model of the car?: ")
        modYear = input("What is the year of the car?: ")
        modCost = input("What is the cost of the car?: ")
        modRange = input("What is the range of the car?: ")
        modComment = input("Please type the comment of the new car: ")

# Original Car Make Data Swapped for Modified Make Data
        ogCar.remove(ogMake)
        ogCar.insert(0, modMake)

# Original Car Model Data Swapped for Modified Model Data
        ogCar.remove(ogModel)
        ogCar.insert(1, modModel)

# Original Car Year Data Swapped for Modified Year Data
        ogCar.remove(ogYear)
        ogCar.insert(2, modYear)

# Original Car Cost Data Swapped for Modified Cost Data
        ogCar.remove(ogCost)
        ogCar.insert(3, modCost)

# Original Car Range Data Swapped for Modified Range Data
        ogCar.remove(ogRange)
        ogCar.insert(4, modRange)

# Original Car Comment Data Swapped for Modified Comment Data
        ogCar.remove(ogComment)
        ogCar.insert(5, modComment)        

# Process repeated for each option in sub-menu
    elif carSelect == 2:
        ogCar = data[2]
        
        ogMake = ogCar[0]
        ogModel = ogCar[1]
        ogYear = ogCar[2]
        ogCost = ogCar[3]
        ogRange = ogCar[4]
        ogComment = ogCar[5]
        
        modMake = input("What is the new make of the car?: ")
        modModel = input("What is the model of the car?: ")
        modYear = input("What is the year of the car?: ")
        modCost = input("What is the cost of the car?: ")
        modRange = input("What is the range of the car?: ")
        modComment = input("Please type the comment of the new car: ")
        
        ogCar.remove(ogMake)
        ogCar.insert(0, modMake)
        
        ogCar.remove(ogModel)
        ogCar.insert(1, modModel)
        
        ogCar.remove(ogYear)
        ogCar.insert(2, modYear)
        
        ogCar.remove(ogCost)
        ogCar.insert(3, modCost)
        
        ogCar.remove(ogRange)
        ogCar.insert(4, modRange)
        
        ogCar.remove(ogComment)
        ogCar.insert(5, modComment)        
        
        
    elif carSelect == 3:
        
        ogCar = data[3]
        
        ogMake = ogCar[0]
        ogModel = ogCar[1]
        ogYear = ogCar[2]
        ogCost = ogCar[3]
        ogRange = ogCar[4]
        ogComment = ogCar[5] 
        
        modMake = input("What is the new make of the car?: ")
        modModel = input("What is the model of the car?: ")
        modYear = input("What is the year of the car?: ")
        modCost = input("What is the cost of the car?: ")
        modRange = input("What is the range of the car?: ")
        modComment = input("Please type the comment of the new car: ")
        
        ogCar.remove(ogMake)
        ogCar.insert(0, modMake)
        
        ogCar.remove(ogModel)
        ogCar.insert(1, modModel)
        
        ogCar.remove(ogYear)
        ogCar.insert(2, modYear)
        
        ogCar.remove(ogCost)
        ogCar.insert(3, modCost)
        
        ogCar.remove(ogRange)
        ogCar.insert(4, modRange)
        
        ogCar.remove(ogComment)
        ogCar.insert(5, modComment)        
           
    elif carSelect == 4:
        ogCar = data[4]
        
        ogMake = ogCar[0]
        ogModel = ogCar[1]
        ogYear = ogCar[2]
        ogCost = ogCar[3]
        ogRange = ogCar[4]
        ogComment = ogCar[5]  
        
        modMake = input("What is the new make of the car?: ")
        modModel = input("What is the model of the car?: ")
        modYear = input("What is the year of the car?: ")
        modCost = input("What is the cost of the car?: ")
        modRange = input("What is the range of the car?: ")
        modComment = input("Please type the comment of the new car: ")
        
        ogCar.remove(ogMake)
        ogCar.insert(0, modMake)
        
        ogCar.remove(ogModel)
        ogCar.insert(1, modModel)
        
        ogCar.remove(ogYear)
        ogCar.insert(2, modYear)
        
        ogCar.remove(ogCost)
        ogCar.insert(3, modCost)
        
        ogCar.remove(ogRange)
        ogCar.insert(4, modRange)
        
        ogCar.remove(ogComment)
        ogCar.insert(5, modComment)        
    
    elif carSelect == 5:
        
        ogCar = data[5]
        
        ogMake = ogCar[0]
        ogModel = ogCar[1]
        ogYear = ogCar[2]
        ogCost = ogCar[3]
        ogRange = ogCar[4]
        ogComment = ogCar[5]
        
        modMake = input("What is the new make of the car?: ")
        modModel = input("What is the model of the car?: ")
        modYear = input("What is the year of the car?: ")
        modCost = input("What is the cost of the car?: ")
        modRange = input("What is the range of the car?: ")
        modComment = input("Please type the comment of the new car: ")
        
        ogCar.remove(ogMake)
        ogCar.insert(0, modMake)
        
        ogCar.remove(ogModel)
        ogCar.insert(1, modModel)
        
        ogCar.remove(ogYear)
        ogCar.insert(2, modYear)
        
        ogCar.remove(ogCost)
        ogCar.insert(3, modCost)
        
        ogCar.remove(ogRange)
        ogCar.insert(4, modRange)
        
        ogCar.remove(ogComment)
        ogCar.insert(5, modComment)        

# Updated data list is returned to caller
    return data



# Delete Car from Data Function
def deleteCar(data):

# Prompt for user input to choose which car to remove from data list
    print("\nWhich car would you like to delete? ")

# Counter established for sub-menu creation
    i = 1

# For-Loop created to process data from each car
    for car in data[1::]:

# Sub-Menu options created, counter increments with amount of cars in data list
        print(str(i) + ")", car[0], car[1], sep = " ")
        i = i + 1

# User chosen option saved in variable
    carSelect = int(input("Please enter an option (number): ")) 

# Error-Proofing; ensure user's chosen option is an option from sub-menu
    while carSelect not in range(1, i):
        carSelect = int(input("Please enter a valid option(number): "))

# Variable of user-chosen option is used to select car from data list
    car = data[carSelect]

# Chosen car is deleted from data list
    data.remove(car)

# Updated data list is returned to caller
    return data


# Display Main Menu Function
def displayMenu():

# True condition established for menu-looping until 'quit'/break
    while True:

# Available user options on main menu is displayed
        print("\nMenu:")
        print("1) Load Car Data")
        print("2) Add a Car")
        print("3) Modify a Car")
        print("4) Delete a Car")
        print("5) Save Data")
        print("6) Report on Top Three Cars")
        print("7) Quit")

# User input is saved to variable
        choice = int(input("\nPlease choose an option: "))
        
# Error-Proofing; ensure user's chosen option is an option from main menu
        while choice not in range(1, 8):
            choice = int(input("Please enter a valid option(number): ")) 

# Stored information on user input is returned to caller 
        return choice        
    

# Top 3 Cars from Data with Information Function
def top3Cars(data):

# Rankings List created for use in ratings calculation with car
    rankings_list = []

# For-Loop established to process each car from data list
    for car in data[1::]:

# Variables created to store specific information (cost, range) from current car in processing
        carCost = car[3]
        carRange = car[4]

# String variables converted to integer variables for use in mathematical calcution of ratings
        carCost = int(carCost)
        carRange = int(carRange)

# Formula for calculating car ratings is created
        carRating = (carCost / 10000) - (carRange / 100)

# Car Year of current car in processing is saved for printing purposes
        carYear = car[2]

# Car Make and Model strings of current car in processing is joined to form full name for print
        carName = car[0], car[1]
        carName = " ".join(carName)

# Current car in processing has rating saved along with car's data in list of lists
        rankings_list.append([carRating, carName, carYear, carCost, carRange])

# Car ratings appended first to sort list for lowest value of car rating (Lower=Better)
        rankings_list.sort()

# First place car in rankings is saved to variable along with the year, cost, range
    car1 = rankings_list[0][1]
    car1Year = rankings_list[0][2]
    car1Cost = rankings_list[0][3]
    car1Range = rankings_list[0][4]

# Second place car in rankings is saved to variable along with year, cost, range
    car2 = rankings_list[1][1]
    car2Cost = rankings_list[1][3]
    car2Year = rankings_list[1][2]
    car2Range = rankings_list[1][4]

# Third place car in rankings is saved to variable along with year, cost, range
    car3 = rankings_list[2][1]
    car3Year = rankings_list[2][2]
    car3Cost = rankings_list[2][3]
    car3Range = rankings_list[2][4]
    
# Ranking and Data of Top Three Cars are Printed:
    print("\nThe Top Three Cars are: ")

# First Ranked Place Car Displayed
    print("\n1)", car1Year, car1)
    print("   Cost: $" + str(car1Cost),"  Range: " + str(car1Range) + "km")

# Second Ranked Place Car Displayed
    print("\n2)", car2Year, car2)
    print("   Cost: $" + str(car2Cost),"  Range: " + str(car2Range) + "km")

# Third Ranked Place Car Displayed
    print("\n3)", car3Year, car3)
    print("   Cost: $" + str(car3Cost),"  Range: " + str(car3Range) + "km")


# Load Car Data Function
def getCarInfo(data, fmt="all"):

# If statement for display formats. If format is 'all' then full data displayed
    if fmt == "all":

# Counter created for printing purposes
        i = 0
        
# Cars in data list is processed
        for car in data[1::]:

# Information on each car is displayed with Make, Model, Year, Cost, Range, Comment
            print("\n", str(i + 1) + ")", car[0],car[1])
            print("    Year:", car[2], " Cost: $" +  str(car[3]), " Range: " + str(car[4]), " Comment: " + str(car[5]))

# Counter increments up to amount of cars in data list
            i = i + 1

# If format is not 'all' only partial data is displayed      
    elif fmt != "all":
        
        i = 0
        
        for car in data[1::]:
            
            print("\n", str(i + 1) + ")", car[0],car[1])
            print("    Year:", car[2])           
        
            i = i + 1
    

# Save File Function
def saveFile(filename, data):

# List generated for processing of data to save
    saveData_list = []

# File is opened for writing
    saveData = open(filename, 'w')
    
# For-Loop Generated to process data list of lists and create single list
    for carInfo in data:
        carInfo = ",".join(carInfo)
        saveData_list.append(carInfo)

# Single list of data is converted to string with newline '\n' at end of each line
    saveInfo = "\n".join(saveData_list)

# Each line of data up to newline is written to file
    saveData.write(saveInfo)

# File is closed from writing
    saveData.close()

    return


# Main Function
def main(filename):

# Raw Data List Created from File Contents
    data = loadData(filename)

# List created for data refinement from raw data
    refined_data = []

# List for car dictionaries created
    dictData = []

# Processing loop to seperate comma values in data list as elements in their own list
    for entry in data:
        
        entry = entry.split(',')

# Processed data is appended to refined data list
        refined_data.append(entry)

# Data list is now refined data.
    data = refined_data

# Headers from .CSV file saved as variable
    categories = data[0]
    

# Booleon condition made for menu-looping and data updating/saving
    while True:
        choice = displayMenu()

# User input to initialize the 'getCarInfo(data, fmt)' function
        if choice == 1:
            getCarInfo(data, fmt="all")

# User input to initialize the 'addCar(data)' function
        elif choice == 2:
            data = addCar(data)

# User input to initialize the 'modifyCar(data)' function
        elif choice == 3:
            data = modifyCar(data)

# User input to initialize the 'deleteCar(data)' function
        elif choice == 4:
            data = deleteCar(data)

# User input to initialie the 'saveFile(filename, data)' function
        elif choice == 5:
            saveFile(filename, data)

# User input to initialize the 'top3Cars(data)' function
        elif choice == 6:
            top3Cars(data)

# User input to break Boolean condition and terminate program
        elif choice == 7:
            break    
        

# Main Function Call/Start of Program
main(filename)