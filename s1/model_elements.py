class Texture:
    pass


class Polygon:
    def __init__(self, points: list[Point3D]):
        self.points = points


class PolygonalModel:
    def __init__(self, polygons: Polygon, textures: list[Texture]):
        self.polygons = polygons
        self.textures = textures


class Flash:
    def __init__(self, location: Point3D, angle: Angle3D, color: Color, power: float):
        self.location = location
        self.angle = angle
        self.color = color
        self.power = power

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Camera:
    def __init__(self, location, angle):
        self.location = location
        self.angle = angle

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Scene:
    def __init__(self, scene_id: int, models: PolygonalModel, flashes: list[Flash], camera: Camera):
        self.id = scene_id
        self.models = models
        self.flashes = flashes
        self.camera = camera

    def method1(self, obj):
        pass

    def method2(self, obj1, obj2):
        pass
