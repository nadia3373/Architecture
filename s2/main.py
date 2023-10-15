from random import randint

from artifact_chest_factory import ArtifactChestFactory
from food_chest_factory import FoodChestFactory
from gem_chest_factory import GemChestFactory
from gold_chest_factory import GoldChestFactory
from potions_chest_factory import PotionsChestFactory
from wood_chest_factory import WoodChestFactory

if __name__ == "__main__":
    factories = [GoldChestFactory(), GemChestFactory(), ArtifactChestFactory(),
                 WoodChestFactory(), FoodChestFactory(), PotionsChestFactory()]

    for _ in range(20):
        index = randint(0, len(factories) - 1)
        factory = factories[index]
        item = factory.create_item()
        item.open()
