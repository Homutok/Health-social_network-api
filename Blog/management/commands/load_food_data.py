
import ssl
from django.core.management.base import BaseCommand
from django.utils import timezone
from Recipe.models import Food
from Nutrients.models import FoodNutrients, Nutrients
import json


class Command(BaseCommand):
    help = 'Add data from FoodData'

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)

        file_path = options["file_path"]
        # with open(file_path) as file:
        #     data = json.loads(file.read())
        #     for foodElement in data["SurveyFoods"]:
        #         for index, Nutrient in enumerate(foodElement["foodNutrients"]):
        #             name = Nutrient['nutrient']['name']
        #             unitName = Nutrient['nutrient']['unitName']
        #             rank = Nutrient['nutrient']['rank']
        #
        #             Nutrients.objects.create(
        #                 nutrient_name=name,
        #                 nutrient_unitName=unitName,
        #                 nutrient_rank=rank
        #             )
        #         break
        with open(file_path) as file:
            data = json.loads(file.read())

            for foodElement in data["SurveyFoods"]:
                description = foodElement["description"]
                foodClass = foodElement["foodClass"]
                inputFoods = foodElement["inputFoods"][0]["ingredientDescription"]

                NewFood = Food.objects.create(food_name=description,
                                              food_summary=foodClass,
                                              food_ingredient_summary=inputFoods
                                              )

                for index, Nutrient in enumerate(foodElement["foodNutrients"]):
                    foodnutr = FoodNutrients.objects.create(
                        amount=Nutrient["amount"],
                        nutrientInfo=Nutrients.objects.get(pk=index+1),
                        food=NewFood
                    )
                print(description)

