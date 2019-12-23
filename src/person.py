from graphene import ObjectType, String, InputObjectType

class Person(ObjectType) :
    firstName = String()
    lastName = String()

class PersonInput(InputObjectType):
    firstName = String(required = True)
    lastName = String(required = True)