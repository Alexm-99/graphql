from graphene import ObjectType, String, List, Field, Float

class Hero(ObjectType):
    id = String(required=True)
    name = String(required=True)
    height = Float()
    alias = String(required=True)
    powers = List(String, required=True)
    team = String(required=True)
    archenemy = List(String, required=True)

class Villain(ObjectType):
    id = String(required=True)
    name = String(required=True)
    height = Float()
    alias = String(required=True)
    powers = List(String, required=True)
    archenemy = List(String, required=True)




