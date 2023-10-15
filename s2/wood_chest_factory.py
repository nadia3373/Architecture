from item_factory import ItemFactory
from wood_chest import WoodChest


class WoodChestFactory(ItemFactory):
    def create_item(self):
        print("Создали сундук (древесина)")
        return WoodChest()
