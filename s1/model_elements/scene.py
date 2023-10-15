from s1.model_elements.camera import Camera
from s1.model_elements.flash import Flash
from s1.model_elements.polygonal_model import PolygonalModel


class Scene:
    def __init__(self, scene_id: int, models: list[PolygonalModel], flashes: list[Flash], cameras: list[Camera]):
        self.id = scene_id

        if len(models) < 1:
            raise ValueError("Должна быть хотя бы одна модель")

        if len(cameras) < 1:
            raise ValueError("Должна быть хотя бы одна камера")

        self.models = models
        self.flashes = flashes
        self.cameras = cameras

    def method1(self, obj):
        pass

    def method2(self, obj1, obj2):
        pass
