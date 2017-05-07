#Erick
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
