import graphene
from person import Person, PersonInput
from inMemory import addPerson

class CreatePersonMutation(graphene.Mutation):
    person = graphene.Field(Person)
    
    class Arguments:
        personData = PersonInput(required=True)


    def mutate(self, info, personData):
        person = Person(firstName = personData.firstName, lastName = personData.lastName)
        addPerson(person)
        return CreatePersonMutation(person = person)

class Mutation(graphene.ObjectType):
    createPerson = CreatePersonMutation.Field()
    pass
