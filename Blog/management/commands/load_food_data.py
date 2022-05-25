import ssl

from django.core.management.base import BaseCommand
from django.utils import timezone
from Blog.models import Food, FoodNutrients, Nutrients
import json


class Command(BaseCommand):
    help = 'Add data from FoodData'

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)

        file_path = options["file_path"]

        with open(file_path) as file:
            data = json.loads(file.read())

            for foodElement in data["SurveyFoods"]:
                description = foodElement["description"]
                foodClass = foodElement["foodClass"]
                inputFoods = foodElement["inputFoods"][0]["ingredientDescription"]

                NewFood = Food.objects.filter(food_name=description)

                for index, Nutrient in enumerate(foodElement["foodNutrients"]):
                    foodnutr = FoodNutrients.objects.create(
                        amount=Nutrient["amount"],
                        nutrientInfo=Nutrients.objects.get(pk=index + 4),
                        food=NewFood.first()
                    )
                    # foodnutr.food.add(NewFood)
                print(description)
                # break
