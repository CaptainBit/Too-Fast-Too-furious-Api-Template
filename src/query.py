import graphene
from person import Person, PersonInput

class PersonQuery(graphene.AbstractType):
    findPerson = graphene.String(description= 'find person by name', name=graphene.String())

    def resolve_findPerson(self, info, name):
        return 'Bye ' + name

class Query(PersonQuery, graphene.ObjectType):
    pass