class salesperson():
    name = ''
    idnum = 0
    special = ''
    gender = ''
    age = 0

    def __init__(self, newname, newidnum, newspecial, newgender, newage):
        self.name = newname
        self.idnum = newidnum
        self.special = newspecial
        self.gender = newgender
        self.age = newage

    def getName(self):
        return self.name

    def getID(self):
        return self.idnum

    def getSpecial(self):
        return self.special

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

class purchaseOrder():
    # Employee Information
    empName = ''
    empID = 0
    empSpecial = ''
    empGender = ''
    empAge = 0

    # Customer Information
    custFirstName = ''
    custLastName = ''
    custGender = ''
    custAge = 0
    custMarital = ''

    # Vehicle Information
    carID = 0
    carColor = ''
    carType = ''
    carCondition = ''
    carPrice = 0
    carYear = 0

    def insertEmpInfo(self, newEmpName, newEmpID, newEmpSpecial, newEmpGender, newEmpAge):
        self.empName = newEmpName
        self.empID = newEmpID
        self.empSpecial = newEmpSpecial
        self.empGender = newEmpGender
        self.empAge = newEmpAge

    def insertCustInfo(self, newCustFirstName, newCustLastName, newCustGender, newCustAge, newCustMarital):
        self.custFirstName = newCustFirstName
        self.custLastName = newCustLastName
        self.custGender = newCustGender
        self.custAge = newCustAge
        self.custMarital = newCustMarital

    def insertCarInfo(self, newCarID, newCarColor, newCarType, newCarCondition, newCarPrice, newCarYear):
        self.carID = newCarID
        self.carColor = newCarColor
        self.carType = newCarType
        self.carCondition = newCarCondition
        self.carPrice = newCarPrice
        self.carYear = newCarYear

    def printEmployeeInfo(self):
        print("\n"
              "SALESPERSON INFORMATION:\n"
              "NAME: " + str(self.empName), "\n"
              "ID: " + str(self.empID), "\n"
              "SPECIALTY: " + str(self.empSpecial), "\n"
              "GENDER: " + str(self.empGender), "\n"
              "AGE: " + str(self.empAge))

    def printCustomerInfo(self):
        print("\n"
              "CUSTOMER INFORMATION:\n"
              "FIRST NAME: " + str(self.custFirstName), "\n"
              "LAST NAME: " + str(self.custLastName), "\n"
              "GENDER: " + str(self.custGender), "\n"
              "AGE: " + str(self.custAge), "\n"
              "MARITAL STATUS: " + str(self.custMarital))

    def printVehicleInfo(self):
        print("\n"
              "VEHICLE INFORMATION:\n"
              "ID: " + str(self.carID), "\n"
              "TYPE: " + str(self.carType), "\n"
              "CONDITION: " + str(self.carCondition), "\n"
              "YEAR: " + str(self.carYear), "\n"
              "COLOR: " + str(self.carColor), "\n"
              "PRICE: " + str(self.carPrice))

class customer:
    FirstName = ''
    LastName = ''
    Age = 0
    Gender = ''
    MaritalStatus = ''

    def __init__(self, FirstName, LastName, Age, Gender, MaritalStatus):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age
        self.Gender = Gender
        self.MaritalStatus = MaritalStatus

    def getFirstName(self):
        return self.FirstName

    def getLastName(self):
        return self.LastName

    def getAge(self):
        return self.Age

    def getGender(self):
        return self.Gender

    def getMaritalStatus(self):
        return self.MaritalStatus

class vehicle:
    ID = 0
    Color = ''
    Type = ''
    Condition = ''
    Year = ''
    Price = 0

    def __init__(self, ID, Color, Type, Condition, Year, Price):
        self.ID = ID
        self.Color = Color
        self.Type = Type
        self.Condition = Condition
        self.Year = Year
        self.Price = Price

    def getID(self):
        return self.ID

    def getColor(self):
        return self.Color

    def getType(self):
        return self.Type

    def getCondition(self):
        return self.Condition

    def getYear(self):
        return self.Year

    def getPrice(self):
        return self.Price


###############
# Employees List
###############
Rick = salesperson("Rick James", 213, "Compact Cars", "Male", 48)
Jenny = salesperson("Jenny TuTone", 8675309, "Diesel Trucks", "Female", 15)
Craig = salesperson("Craig Michaels", 656, "Motorcycles", "Male", 25)

Employees = list()
Employees.append(Rick)
Employees.append(Jenny)
Employees.append(Craig)

##########
# Cars List
##########
Car1 = vehicle(101, "White", "Sedan", "New", 2017, 22999)
Car2 = vehicle(102, "Yellow", "Coupe", "Used", 2007, 20197)
Car3 = vehicle(103, "Black", "Sedan", "Used", 2009, 15999)
Car4 = vehicle(104, "Green", "Coupe", "New", 2016, 25199)
Truck1 = vehicle(201, "Silver", "Crew Cab", "New", 2017, 32999)
Truck2 = vehicle(202, "Brown", "Regular Cab", "Used", 2011, 25999)
Truck3 = vehicle(203, "Red", "Crew Cab", "Used", 2013, 26999)
Truck4 = vehicle(204, "Blue", "Regular Cab", "New", 2017, 30999)
Motor1 = vehicle(301, "Black", "Sport", "New", 2017, 19999)
Motor2 = vehicle(302, "White", "Sport", "Used", 2012, 15987)

Vehicles = list()
Vehicles.append(Car1)
Vehicles.append(Car2)
Vehicles.append(Car3)
Vehicles.append(Car4)
Vehicles.append(Truck1)
Vehicles.append(Truck2)
Vehicles.append(Truck3)
Vehicles.append(Truck4)
Vehicles.append(Motor1)
Vehicles.append(Motor2)

#########################
# Start of actual program
#########################

count = 1
while count == 1:
    choiceCount = 1
    while choiceCount ==1:
        print("\n"
              "What would you like to do today?\n"
              "\n"
              "1. Print new purchase order.\n"
              "2. Look up employee information.\n"
              "3. Look up car information.\n"
              "4. Exit.")
        choice = input()
        try:
            choice = int(choice)
            choiceCount = 0
        except:
            print("Please enter a number 1 through 4")

    if choice == 1:
        custFirstName = str(input("What is the customer's first name?"))
        custLastName = str(input("What is the customer's last name?"))

        ageCount = 1
        while ageCount == 1:
            custAge = input("What is the customer's age?")
            try:
                custAge = int(custAge)
                ageCount = 0
            except ValueError:
                print("Please enter a number.")

        genderCount = 1
        while genderCount == 1:
            custGender = str(input("Is the customer male or female? (Enter 'm' or 'f')"))
            if custGender == 'm':
                genderCount = 0
            elif custGender == 'f':
                genderCount = 0
            else:
                print("Please enter either 'm' or 'f'")

        maritalCount = 1
        while maritalCount == 1:
            custMarital = str(input("What is the customer's marital status? (single, married, n/a)"))
            if custMarital == "single":
                maritalCount = 0
            elif custMarital == "married":
                maritalCount = 0
            elif custMarital == "n/a":
                maritalCount = 0
            else:
                print("Please enter 'single', 'married', or 'n/a'")

        newCust = customer(custFirstName, custLastName, custAge, custGender, custMarital)

        purchaseOrder1 = purchaseOrder()
        purchaseOrder1.insertCustInfo(newCust.getFirstName(), newCust.getLastName(), newCust.getAge(),newCust.getGender(), newCust.getMaritalStatus())

        empCount = 1
        while empCount == 1:
            employeeInput = input("\n"
                                  "Which employee sold the vehicle?\n"
                                  "1. Rick James\n"
                                  "2. Jenny Tutone\n"
                                  "3. Craig Michaels\n")

            try:
                employeeInput = int(employeeInput)
            except ValueError:
                pass

            if employeeInput == 1:
                purchaseOrder1.insertEmpInfo(Rick.getName(), Rick.getID(), Rick.getSpecial(), Rick.getGender(),Rick.getAge())
                empCount = 0
            elif employeeInput == 2:
                purchaseOrder1.insertEmpInfo(Jenny.getName(), Jenny.getID(), Jenny.getSpecial(), Jenny.getGender(),Jenny.getAge())
                empCount = 0
            elif employeeInput == 3:
                purchaseOrder1.insertEmpInfo(Craig.getName(), Craig.getID(), Craig.getSpecial(), Craig.getGender(),Craig.getAge())
                empCount = 0
            else:
                print("Please enter a number 1 through 3.")

        carCount = 1
        while carCount == 1:
            vehicleInput = input("\n"
                                 "Which vehicle did the customer purchase?\n"
                                 "1. 2017 White Sedan\n"
                                 "2. 2007 Yellow Coupe\n"
                                 "3. 2009 Black Sedan\n"
                                 "4. 2016 Green Coupe\n"
                                 "5. 2017 Silver Crew Cab Truck\n"
                                 "6. 2011 Brown Regular Cab Truck\n"
                                 "7. 2013 Red Crew Cab Truck\n"
                                 "8. 2017 Blue Regular Cab Truck\n"
                                 "9. 2017 Black Sport Motorcycle\n"
                                 "10. 2012 White Sport Motorcycle\n")

            try:
                vehicleInput = int(vehicleInput)
            except:
                pass
            if vehicleInput == 1:
                purchaseOrder1.insertCarInfo(Car1.getID(), Car1.getColor(), Car1.getType(), Car1.getCondition(),
                                             Car1.getPrice(), Car1.getYear())
                carCount = 0
            elif vehicleInput == 2:
                purchaseOrder1.insertCarInfo(Car2.getID(), Car2.getColor(), Car2.getType(), Car2.getCondition(),
                                             Car2.getPrice(), Car2.getYear())
                carCount = 0
            elif vehicleInput == 3:
                purchaseOrder1.insertCarInfo(Car3.getID(), Car3.getColor(), Car3.getType(), Car3.getCondition(),
                                             Car3.getPrice(), Car3.getYear())
                carCount = 0
            elif vehicleInput == 4:
                purchaseOrder1.insertCarInfo(Car4.getID(), Car4.getColor(), Car4.getType(), Car4.getCondition(),
                                             Car4.getPrice(), Car4.getYear())
                carCount = 0
            elif vehicleInput == 5:
                purchaseOrder1.insertCarInfo(Truck1.getID(), Truck1.getColor(), Truck1.getType(), Truck1.getCondition(),
                                             Truck1.getPrice(), Truck1.getYear())
                carCount = 0
            elif vehicleInput == 6:
                purchaseOrder1.insertCarInfo(Truck2.getID(), Truck2.getColor(), Truck2.getType(), Truck2.getCondition(),
                                             Truck2.getPrice(), Truck2.getYear())
                carCount = 0
            elif vehicleInput == 7:
                purchaseOrder1.insertCarInfo(Truck3.getID(), Truck3.getColor(), Truck3.getType(), Truck3.getCondition(),
                                             Truck3.getPrice(), Truck3.getYear())
                carCount = 0
            elif vehicleInput == 8:
                purchaseOrder1.insertCarInfo(Truck4.getID(), Truck4.getColor(), Truck4.getType(), Truck4.getCondition(),
                                             Truck4.getPrice(), Truck4.getYear())
                carCount = 0
            elif vehicleInput == 9:
                purchaseOrder1.insertCarInfo(Motor1.getID(), Motor1.getColor(), Motor1.getType(), Motor1.getCondition(),
                                             Motor1.getPrice(), Motor1.getYear())
                carCount = 0
            elif vehicleInput == 10:
                purchaseOrder1.insertCarInfo(Motor2.getID(), Motor2.getColor(), Motor2.getType(), Motor2.getCondition(),
                                             Motor2.getPrice(), Motor2.getYear())
                carCount = 0
            else:
                print("Please enter a number 1 through 10.")

        print("\n"
              "\n"
              "PURCHASE ORDER:")
        purchaseOrder1.printVehicleInfo()
        purchaseOrder1.printCustomerInfo()
        purchaseOrder1.printEmployeeInfo()
        input("\n"
              "PRESS ENTER TO CONTINUE..."
              "\n")

    if choice == 2:
        salesCount = 1
        while salesCount == 1:
            salesInput = input("\n"
                               "Employee List:\n"
                               "\n"
                               "1. Rick James\n"
                               "2. Jenny Tutone\n"
                               "3. Craig Michaels\n")
            try:
                salesInput = int(salesInput)
            except:
                pass
            if salesInput == 1:
                print("Information:")
                print("Name: Rick James")
                print("ID Number: 213")
                print("Specialty: Compact Cars")
                print("Gender: Male")
                print("Age: 48")
                salesCount = 0

            elif salesInput == 2:
                print("Information:")
                print("Name: Jenny Tutone")
                print("ID Number: 8675309")
                print("Specialty: Diesel Trucks")
                print("Gender: Female")
                print("Age: 15")
                salesCount = 0

            elif salesInput == 3:
                print("Information:")
                print("Name: Craig Michaels")
                print("ID Number: 656")
                print("Specialty: Motorcycles")
                print("Gender: Male")
                print("Age: 25")
                salesCount = 0

            else:
                print("Please enter a number 1 through 3.")

    elif choice == 3:
        vehCount = 1
        while vehCount == 1:
            vehicleInput = input("\n"
                                 "Vehicle List:\n"
                                 "\n"
                                 "1. White Sedan\n"
                                 "2. Yellow Coupe\n"
                                 "3. Black Sedan\n"
                                 "4. Green Coupe\n"
                                 "5. Silver crew\n"
                                 "6. Brown Regular\n"
                                 "7. Red Crew\n"
                                 "8. Blue Regular\n"
                                 "9. Black Sport\n"
                                 "10. White Sport\n")
            try:
                vehicleInput = int(vehicleInput)
            except:
                pass
            if vehicleInput == 1:
                print("Information:")
                print("Vehicle ID: 101")
                print("Vehcile Type: Car")
                print("Color: White")
                print("Series: Sedan")
                print("Condition: New")
                print("Year: 2017")
                print("Price: $22,999")
                vehCount = 0

            elif vehicleInput == 2:
                print("Information: ")
                print("Vehicle ID: 102")
                print("Vehcile Type: Car")
                print("Color: Yellow")
                print("Series: Coupe")
                print("Condition: Used")
                print("Year: 2007")
                print("Price: $20,197")
                vehCount = 0

            elif vehicleInput == 3:
                print("Information:")
                print("Vehicle ID: 103")
                print("Vehcile Type: Car")
                print("Color: Black")
                print("Series: Sedan")
                print("Condition: Used")
                print("Year: 2009")
                print("Price: $15,999")
                vehCount = 0

            elif vehicleInput == 4:
                print("Information:")
                print("Vehicle ID: 104")
                print("Vehcile Type: Car")
                print("Color: Green")
                print("Series: Coupe")
                print("Condition: New")
                print("Year: 2017")
                print("Price: $25,199")
                vehCount = 0

            elif vehicleInput == 5:
                print("Information:")
                print("Vehicle ID: 201")
                print("Vehcile Type: Truck")
                print("Color: Silver")
                print("Cab Size: Crew Cab")
                print("Condition: New")
                print("Year: 2017")
                print("Price: $32,999")
                vehCount = 0

            elif vehicleInput == 6:
                print("Information:")
                print("Vehicle ID: 202")
                print("Vehcile Type: Truck")
                print("Color: Brown")
                print("Cab Size: Regular Cab")
                print("Condition: Used")
                print("Year: 2011")
                print("Price: $25,197")
                vehCount = 0

            elif vehicleInput == 7:
                print("Information:")
                print("Vehicle ID: 203")
                print("Vehcile Type: Truck")
                print("Color: Red")
                print("Cab Size: Crew Cab")
                print("Condition: Used")
                print("Year: 2013")
                print("Price: $26,999")
                vehCount = 0

            elif vehicleInput == 8:
                print("Information:")
                print("Vehicle ID: 204")
                print("Vehcile Type: Truck")
                print("Color: Blue")
                print("Cab Size: Regular Cab")
                print("Condition: New")
                print("Year: 2017")
                print("Price: $30,999")
                vehCount = 0

            elif vehicleInput == 9:
                print("Information:")
                print("Vehicle ID: 301")
                print("Vehcile Type: Motorcycle")
                print("Color: Black")
                print("Series: Sport")
                print("Condition: New")
                print("Year: 2017")
                print("Price: $19,999")
                vehCount = 0

            elif vehicleInput == 10:
                print("Information:")
                print("Vehicle ID: 302")
                print("Vehcile Type: Motorcycle")
                print("Color: White")
                print("Series: Sport")
                print("Condition: Used")
                print("Year: 2012")
                print("Price: $15,987")
                vehCount = 0

    elif choice == 4:
        count = 0

    else:
        print("Please enter a number 1 through 4.")
