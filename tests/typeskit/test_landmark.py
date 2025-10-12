import pytest
from elrahpy.typeskit.landmark import LandMark, Point


def test_point():
    p = Point(x=2, y=3)
    assert str(p) == "(2,3)"


def test_should_add_point():
    a = Point(x=0, y=2)
    land_mark = LandMark(str)
    land_mark.add_point(a, "Hello")
    assert land_mark.exist_point(Point(0, 2))


def test_should_return_point_value():
    a = Point(x=0, y=2)
    land_mark = LandMark(str)
    land_mark.add_point(a, "Hello")
    assert land_mark.get_point_value((a)) == "Hello"


def test_should_set_point_value():
    a = Point(x=0, y=2)
    land_mark = LandMark(str)
    land_mark.add_point(a, "Hello")
    land_mark.set_point_value(a, "Hi")
    assert land_mark.get_point_value((a)) == "Hi"


def test_should_remote_point():
    a = Point(x=0, y=2)
    land_mark = LandMark(str)
    land_mark.add_point(a, "Hello")
    land_mark.remove_point(a)
    assert land_mark.exist_point(a) is False
