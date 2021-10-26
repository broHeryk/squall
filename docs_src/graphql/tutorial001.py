import strawberry
from strawberry.asgi import GraphQL

from squall import Squall


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)


schema = strawberry.Schema(query=Query)


graphql_app = GraphQL(schema)

app = Squall()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
