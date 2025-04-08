from typing import List

class Point:
    def __init__(self,x:int,y:int):
        self.__x = x
        self.__y=y
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self,x:int):
        self.__x=x

    @y.setter
    def y(self,y:int):
        self.__y=y


class LandMark:

    def __init__(self,count_rows:int,count_columns:int):
        self.__points:List[Point]=self.filled_land_mark(count_rows,count_columns)

    def filled_land_mark(self,count_rows:int,count_columns:int):
        points:List[Point]=[]
        for i in range(1,count_rows+1):
            for j in range(1,count_columns+1):
                point = Point(i,j)
                points.append(point)
        return points


    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self,points:List[Point]):
        self.__points=points

    def print_points(self):
        for p in  self.__points:
            print(f"{p.x=} {p.y=}")



my_land = LandMark(count_rows=5,count_columns=5)

my_land.print_points()
