from abc import ABC, abstractmethod


class ItemFactory(ABC):
    @abstractmethod
    def create_item(self):
        pass
