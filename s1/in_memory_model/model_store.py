from s1.in_memory_model.change_observer import IModelChanger
from s1.in_memory_model.model_changer import IModelChangedObserver
from s1.model_elements.camera import Camera
from s1.model_elements.flash import Flash
from s1.model_elements.polygonal_model import PolygonalModel
from s1.model_elements.scene import Scene


class ModelStore:
    def __init__(self, models: list[PolygonalModel], scenes: list[Scene],
                 flashes: list[Flash], cameras: list[Camera],
                 change_observers: list[IModelChangedObserver]):
        super().__init__()
        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras
        self._change_observers = change_observers

    def get_scene(self, scene_id: int):
        pass

    def notify_change(self, model_changer: IModelChanger):
        pass
