#Kyle
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
