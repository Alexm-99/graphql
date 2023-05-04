from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, List, Field, Int, Schema
from src.graphql.resolvers import resolve_heroes, resolve_hero_by_id, resolve_villains, resolve_villain_by_id
from src.graphql.typesDefs import Hero, Villain

app = Flask(__name__)

class Query(ObjectType):
    heroes = List(Hero, description="List of all heroes")
    hero_by_id = Field(Hero, id=Int(required=True), description="Get a hero by its ID")
    villains = List(Villain, description="List of all villains")
    villain_by_id = Field(Villain, id=Int(required=True), description="Get a villain by its ID")

    def resolve_heroes(self, info):
        return resolve_heroes()

    def resolve_hero_by_id(self, info, id):
        return resolve_hero_by_id(id)

    def resolve_villains(self, info):
        return resolve_villains()

    def resolve_villain_by_id(self, info, id):
        return resolve_villain_by_id(id)

schema = Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
