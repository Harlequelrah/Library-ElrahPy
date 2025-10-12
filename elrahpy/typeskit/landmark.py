from typing import Any


class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x: int):
        self.__x = x

    @y.setter
    def y(self, y: int):
        self.__y = y

    def __str__(self):
        return f"({self.__x},{self.__y})"


class LandMark:

    def __init__(self, type_land_mark: type = Any):
        self.__marks: dict[Point, type_land_mark:type] = {}
        self.__type_land_mark = type_land_mark

    def get_point_value(self, point: Point):
        return self.__marks[point]

    def set_point_value(self, point: Point, obj):
        if self.exist_point(point) and self.is_valid_obj(obj):
            self.__marks[point] = obj
        else:
            raise ValueError("Point doesn't exist or value is not valid")

    def add_point(self, point: Point, obj):
        if self.is_valid_obj(obj):
            self.__marks[point] = obj
        else:
            raise ValueError(
                f"The object is not valid and must be {self.__type_land_mark}"
            )

    def is_valid_obj(self, obj) -> bool:
        return (
            self.__type_land_mark is not Any
            and isinstance(obj, self.__type_land_mark)
            or self.__type_land_mark is Any
        )

    def exist_point(self, point: Point) -> bool:
        return next(
            (True for p in self.__marks.keys() if point.x == p.x and point.y == p.y),
            False,
        )

    def remove_point(self, point: Point):
        if self.exist_point(point):
            del self.__marks[point]

    def list_marks(self):
        for point, value in self.__marks.items():
            print(f"({point.x},{point.y}) -> {value}")

    @property
    def marks(self):
        return self.__marks
