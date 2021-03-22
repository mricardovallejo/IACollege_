# A simple class

class Contact:
    def __init__(self, firstname, lastname, phonenumber=0): #Constructor
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber

    def setphonenumber(self, phonenumber):
        self.phonenumber = phonenumber

    def defineSex(self, currentValue):
        if currentValue == 'M':
            return 'Masculine'
        else:
            return 'Femenine'

#Instance of class

m = Contact('Ricardo','Vallejo','13123')
n = Contact('Pedro', 'Perez', '13123')
del m #Delete class instance
n.setphonenumber('111111111111111')
print(n.phonenumber)

# Using methodes of class
print(n.defineSex('F'))


# A child class - Inheritance
class ContactStudent(Contact): #Contact est parent de Contact Student
    # DONT CONSTRUCTOR IN CHILD!
    # def __init__(self, level=0, categStudent='STANDARD'):
    #    self.level = level
    #    self.categStudent = categStudent # Child dont have constructors

    def setcategStudent(self, categStudent):
        self.categStudent = categStudent

#Inheritance
x  = ContactStudent("Pipe", "Pelaez")
x.setcategStudent('CAT')
x.setphonenumber('3245234523')
print ( x.firstname )
print ( x.defineSex('M') )

# A child class - Inheritance
class ContactStudent(Contact): #Contact est parent de Contact Student
    def setcategStudent(self, categStudent):
        self.categStudent = categStudent

#Multi-inheritance

class ContactSports(): #Contact est parent de Contact Student

    def setSportsList(self, sports_list):
        self.sports_lists = sports_list

    def updateSportList(self, item):
        self.sports_lists.append(item)

class ContactStudent2(Contact, ContactSports):
    def f(self,a):
        a=a+2

x2 = ContactStudent2('Peter','Cereza')
x2.setSportsList(['Gggg','hhhh'])
print(x2.sports_lists)
x2.updateSportList('Basket')
print(x2.sports_lists)


# Another example inheritance
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# Overiding

class OverrideContactMethod(Contact):

    def defineSex(self, currentValue):
        if currentValue == 'M':
            return 'M'
        else:
            return 'F'

#Another example overridding

class Robot:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):

    def say_hi(self):
        print("Everything will be okay! ")
        print(self.name + " takes care of you!")


