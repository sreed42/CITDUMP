#Jared Thompson

class salesperson(object):  # creating salesperson class

    def __init__(self, name, idnum, gender, age):
        self.name = name
        self.idnum = idnum
        self.gender = gender
        self.age = age

    def getname(self):
        return self.name

    def getID(self):
        return self.idnum

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age
