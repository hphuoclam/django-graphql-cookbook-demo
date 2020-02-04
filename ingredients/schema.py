import graphene

from graphene_django.types import DjangoObjectType

from ingredients.models import Category, Ingredient


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class AddCategoryMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String(required=True)

    # The class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    def mutate(self, info, **kwargs):
        name = kwargs.get('name')
        category = Category(name=name)
        category.save()
        # Notice we return an instance of this mutation
        return AddCategoryMutation(category=category)

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient


class Query(object):
    # Category
    get_all_categories = graphene.List(CategoryType)
    get_category = graphene.Field(CategoryType, id=graphene.Int())

    # Ingredient
    get_all_ingredients = graphene.List(IngredientType)
    get_ingredient = graphene.Field(IngredientType, id=graphene.Int())

    def resolve_get_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_get_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Category.objects.get(pk=id)
        return None

    def resolve_get_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()

    def resolve_get_ingredient(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Ingredient.objects.get(pk=id)
        return None


class Mutation(graphene.ObjectType):
    add_category = AddCategoryMutation.Field()