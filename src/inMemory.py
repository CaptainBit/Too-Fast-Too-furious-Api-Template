from person import Person

myListPersons = []

def addPerson(person):
    global myListPersons
    myListPersons.append(person)

def getPersons():
    global myListPersons
    return myListPersons