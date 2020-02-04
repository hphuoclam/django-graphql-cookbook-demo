import graphene
import graphql_jwt

import ingredients.schema 
from ingredients.schema import AddCategoryMutation

class Query(
    ingredients.schema.Query, 
    graphene.ObjectType
    ):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(
    ingredients.schema.Mutation, # Add your Mutation objects here
    graphene.ObjectType
):
    pass
    # add_category = AddCategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
