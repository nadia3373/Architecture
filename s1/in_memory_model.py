from abc import ABC, abstractmethod

from s1.model_elements import PolygonalModel, Scene, Flash, Camera


class IModelChangedObserver(ABC):
    @abstractmethod
    def apply_update_model(self):
        pass


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self, sender: IModelChangedObserver):
        pass


class ModelStore(IModelChanger, ABC):
    def __init__(
            self, models: PolygonalModel, scenes: Scene,
            flashes: Flash, cameras: Camera, change_observers: list[IModelChangedObserver]
    ):
        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras
        self._change_observers = change_observers

    def get_scene(self, scene_id: int):
        pass
