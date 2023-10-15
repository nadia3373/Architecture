from game_item import GameItem


class FoodChest(GameItem):
    def open(self):
        print("Открыли сундук с продовольствием")
