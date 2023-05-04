from graphqlclient import GraphQLClient
import json
# Crea una instancia de GraphQLClient y configura la URL del servidor GraphQL
client = GraphQLClient('http://localhost:5000/graphql')
# Define la consulta GraphQL utilizando la clase gql
query = '''
query{
  heroById(id:1){
    name
  }
  
}
'''
# Envía la consulta al servidor GraphQL utilizando el cliente GraphQL
result = client.execute(query)

# Muestra la respuesta del servidor
data = json.loads(result)




print(data)
# Accede a la parte del diccionario que contiene el objeto heroById
# hero_data = data['data']['heroById']

# for hero in hero_data:
#     print(hero, ": ", hero_data[hero])

# Muestra el resultadoprint(hero_dat)