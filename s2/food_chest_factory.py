from food_chest import FoodChest
from item_factory import ItemFactory


class FoodChestFactory(ItemFactory):
    def create_item(self):
        print("Создали сундук (продовольствие)")
        return FoodChest()
