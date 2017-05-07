#Erick
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
        return("\n"
              "SALESPERSON INFORMATION:" + "\n"
              "NAME: " + str(self.empName) + "\n"
              "ID: " + str(self.empID) + "\n"
              "SPECIALTY: " + str(self.empSpecial) + "\n"
              "GENDER: " + str(self.empGender) + "\n"
              "AGE: " + str(self.empAge))

    def printCustomerInfo(self):
        return("\n"
              "CUSTOMER INFORMATION:\n"
              "FIRST NAME: " + str(self.custFirstName) + "\n"
              "LAST NAME: " + str(self.custLastName) + "\n"
              "GENDER: " + str(self.custGender) + "\n"
              "AGE: " + str(self.custAge) + "\n"
              "MARITAL STATUS: " + str(self.custMarital))

    def printVehicleInfo(self):
        return("\n"
              "VEHICLE INFORMATION:"+"\n"
              "ID: " + str(self.carID) + "\n"
              "TYPE: " + str(self.carType) + "\n"
              "CONDITION: " + str(self.carCondition) + "\n"
              "YEAR: " + str(self.carYear) + "\n"
              "COLOR: " + str(self.carColor) + "\n"
              "PRICE: " + str(self.carPrice))
