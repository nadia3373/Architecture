from s2.game_item import GameItem


class PotionsChest(GameItem):
    def open(self):
        print("Открыли сундук с зельями")
