import graphene
from query import Query
from mutation import Mutation
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query, mutation= Mutation)))