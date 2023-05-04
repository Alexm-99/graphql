from flask import Flask
from flask_graphql import GraphQLView
import graphene

class Post(graphene.ObjectType):
    title = graphene.String()
    content = graphene.String()

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    post = graphene.Field(lambda: Post)

    def mutate(self, info, title, content):
        post = Post(title=title, content=content)
        return CreatePost(post=post)

class Query(graphene.ObjectType):
    hello = graphene.String() #TypesDefs

    def resolve_hello(self, info):#resolves
        return 'Hola desde GraphQL! soy Alex Medranda' #data

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

# Crea una instancia de Flask y configura la vista GraphQL
app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Arranca el servidor en el puerto 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
