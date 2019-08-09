"""
1) VARIABLES IN ACTION WITH QUERIES
2) NAMING YOUR GRAPH QL QUERIES
"""

import graphene
import json
import uuid
from datetime import datetime


class User(graphene.ObjectType):
    """
    Passing arguments to queries by creating a class sub classed from
    `graphene.ObjectType`, also can hold default values.
    """
    id = graphene.ID(default_value=str(uuid.uuid4()))
    username = graphene.String()
    created_at = graphene.DateTime(default_value=datetime.now())


class Query(graphene.ObjectType):
    """
    Root operation class for Querying. Will hold all the fields that is needed
    to be returned. Additional parameters that needs to be part of the resolver
    function needs to be decalred with the field.
    """
    users = graphene.List(User, limit=graphene.Int())
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_hello(self, info):
        """
        Resolver function should prepend with the name resolve. followed by
        the query parameter and should follow snake casing.
        """
        return "Benjamin Button"

    def resolve_is_admin(self, info):
        return True

    def resolve_users(self, info, limit=None):
        return [
            User(id="1", username="Fred", created_at=datetime.now()),
            User(id="2", username="Doug", created_at=datetime.now()),
        ][:limit]


class CreateUser(graphene.Mutation):
    """
    Will have the fields defined below and sub fields if any.

    In the below example user is a Field parameter which has sub field that
    gets inherited from User class.
    """
    user = graphene.Field(User)

    class Arguments:
        """
        Arguments needs to be passed as a class within a class under
        mutation unlike Query arguments.
        """
        username = graphene.String()

    def mutate(self, info, username):
        """
        Resolver function for mutation create_user.
        This name will always be mutate.
        """
        user = User(username=username)
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    """
    The root mutation operation class.
    """
    create_user = CreateUser.Field()


# All root operations should be registered under schema.
schema = graphene.Schema(query=Query, mutation=Mutation)

result = schema.execute(
    # You can give a name to your query like GetUsersQuery
    # variable and type of the variable needs to be decalred before
    # passing it with the query `query getUsersQuery ($limit: Int)`
    '''
    query getUsersQuery ($limit: Int) {
        users(limit: $limit) {
           id
           username
           createdAt
        }
    }
    ''',
    variable_values={'limit': 2}
)

dictResult = dict(result.data.items())
print(json.dumps(dictResult, indent=2))
