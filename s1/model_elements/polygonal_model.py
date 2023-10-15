from s1.model_elements.polygon import Polygon
from s1.model_elements.texture import Texture


class PolygonalModel:
    def __init__(self, polygons: list[Polygon], textures: list[Texture]):
        self.polygons = polygons
        self.textures = textures
