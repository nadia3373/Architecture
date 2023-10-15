from gold_chest import GoldChest
from item_factory import ItemFactory


class GoldChestFactory(ItemFactory):
    def create_item(self):
        print("Создали сундук (золото)")
        return GoldChest()
