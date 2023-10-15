from artifact_factory import ArtifactChest
from item_factory import ItemFactory


class ArtifactChestFactory(ItemFactory):
    def create_item(self):
        print("Создали сундук (артефакты)")
        return ArtifactChest()
