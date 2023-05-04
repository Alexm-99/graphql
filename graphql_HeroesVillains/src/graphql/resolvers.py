from src.db.data import heroes, villains
from src.graphql.typesDefs import Hero, Villain

def resolve_heroes():
    return [Hero(
        id=hero["id"],
        name=hero["name"],
        height=hero["height"],
        alias=hero["alias"],
        powers=hero["powers"],
        team=hero["team"],
        archenemy=hero["archenemy"]
    ) for hero in heroes]

def resolve_hero_by_id(id):
    for hero in heroes:
        if hero["id"] == str(id):
            return Hero(
                id=hero["id"],
                name=hero["name"],
                height=hero["height"],
                alias=hero["alias"],
                powers=hero["powers"],
                team=hero["team"],
                archenemy=hero["archenemy"]
            )
    return None

def resolve_villains():
    return [Villain(
        id=villain["id"],
        name=villain["name"],
        height=villain["height"],
        alias=villain["alias"],
        powers=villain["powers"],
        archenemy=villain["archenemy"]
    ) for villain in villains]

def resolve_villain_by_id(id):
    for villain in villains:
        if villain["id"] == str(id):
            return Villain(
                id=villain["id"],
                name=villain["name"],
                height=villain["height"],
                alias=villain["alias"],
                powers=villain["powers"],
                archenemy=villain["archenemy"]
            )
    return None
