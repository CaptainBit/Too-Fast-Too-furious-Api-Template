import graphene
from person import Person, PersonInput

class CreatePersonMutation(graphene.Mutation):
    person = graphene.Field(Person)
    
    class Arguments:
        personData = PersonInput(required=True)


    def mutate(self, info, personData):
        person = Person(personData.firstName, personData.lastName)
        return CreatePersonMutation(person = person)

class Mutation(graphene.ObjectType):
    createPerson = CreatePersonMutation.Field()
    pass
