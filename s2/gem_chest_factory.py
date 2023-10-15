from gem_chest import GemChest
from item_factory import ItemFactory


class GemChestFactory(ItemFactory):
    def create_item(self):
        print("Создали сундук (изумруды)")
        return GemChest()
