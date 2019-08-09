"""
1) QUERIES THAT HAVE FIELDS WITH SUBFIELDS (ARGUMENTS)
2) PAGINATION IN GRAPHQL AND HOW IT IS DONE
3) MORE INTO RESOLVER FUNCTIONS
"""

import graphene
import json
from datetime import datetime


class User(graphene.ObjectType):
    """
    Passing arguments to queries by creating a class sub classed from
    `graphene.ObjectType`, also can hold default values.
    """
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()


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


# All root operations should be registered under schema.
schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        users(limit: 1) {
           id
           username
           createdAt
        }
    }
    '''
)

dictResult = dict(result.data.items())
print(json.dumps(dictResult, indent=2))
