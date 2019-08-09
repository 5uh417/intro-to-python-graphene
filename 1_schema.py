"""
A VERY BASIC HELLO WORLD IMPLEMENTATION WITH GRAPHQL(python-graphene).
"""

import graphene
import json


class Query(graphene.ObjectType):
    """
    Root operation class for Querying. Will hold all the fields that is needed
    to be returned. Additional parameters that needs to be part of the resolver
    function needs to be decalred with the field.
    """
    user = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_user(self, info):
        """
        Resolver function should prepend with the name resolve. followed by
        the query parameter and should follow snake casing.
        """
        return "Benjamin Button"

    def resolve_is_admin(self, info):
        return True


# All root operations should be registered under schema.
schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        user
        isAdmin
    }
    '''
)

dictResult = dict(result.data.items())
print(json.dumps(dictResult, indent=2))
