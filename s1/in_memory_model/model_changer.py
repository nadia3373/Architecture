from abc import abstractmethod, ABC


class IModelChangedObserver(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def apply_update_model(self):
        pass
