import graphene
from person import Person, PersonInput
from inMemory import getPersons

class FindAllPersonQuery(graphene.AbstractType):
    findAllPerson = graphene.List(Person, description= 'get all persons')

    def resolve_findAllPerson(self, info):
        return getPersons()

class FindByNamePersonQuery(graphene.AbstractType):
    findByNamePerson = graphene.List(Person, description= 'filter by name', name = graphene.String())

    def resolve_findByNamePerson(self, info, name):
        lst = getPersons()
        return [person for person in lst if name in person.firstName]

class Query(FindAllPersonQuery, FindByNamePersonQuery, graphene.ObjectType):
    pass