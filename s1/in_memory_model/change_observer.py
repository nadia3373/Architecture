from abc import abstractmethod, ABC

from s1.in_memory_model.model_changer import IModelChangedObserver


class IModelChanger(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def notify_change(self, sender: IModelChangedObserver):
        pass
