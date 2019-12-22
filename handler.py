import graphene
import query

schema = graphene.Schema(query= query.Query)

query = '''
    query SayHello {
      hello
    }
    '''
result = schema.execute(query)
print(result.data['hello'])