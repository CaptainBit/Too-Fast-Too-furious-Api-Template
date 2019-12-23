from graphene import ObjectType, String, InputObjectType

class Person(ObjectType) :
    firstName = String()
    lastName = String()

    def __init__(self, pFirstName, pLastName):
        self.firstName = pFirstName
        self.lastName = pLastName

    def getFullName(self):
        return self.firstName + ' ' + self.lastName

class PersonInput(InputObjectType):
    firstName = String(required = True)
    lastName = String(required = True)