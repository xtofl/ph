__author__ = 'xtofl'


def transform(x0, x1, y0, y1):

    dx = float(x1) - float(x0)
    dy = float(y1) - float(y0)
    r = dy/dx

    def f(x):
        return ((x)-float(x0)) * r + y0
    return f

class View:

    def __init__(self, world, screen):
        def x_axis(rect):
            return rect[0][0], rect[1][0]
        def y_axis(rect):
            return rect[0][1], rect[1][1]

        self._to_screen_x = transform(*(x_axis(world) + x_axis(screen)))
        self._to_screen_y = transform(*(y_axis(world) + y_axis(screen)))

    def to_screen(self, w):
        return self._to_screen_x(w[0]), self._to_screen_y(w[1])

    def to_world(self, s):
        return s


from unittest import TestCase

class TestTransform(TestCase):
    def test_SimpleScaling(self):
        scale = transform(0, 1, 0, 100)
        self.assertEqual(0, scale(0))
        self.assertEqual(100, scale(1))
        self.assertEqual(50, scale(0.5))

    def test_Shift(self):
        scale = transform(0, 1, 2, 3)
        self.assertEqual(2, scale(0))
        self.assertEqual(3, scale(1))
        self.assertEqual(2.5, scale(0.5))

    def test_screenToWorld(self):
        size = 600, 600
        view = View(world=((0, 0), (10, 10)), screen=((0, size[0]), (size[1], 0)))

        self.assertEqual((0, 600), view.to_screen((0, 0)))
        self.assertEqual(((60, 480)), view.to_screen((1, 2)))
        self.assertEqual(((66, 479.4)), view.to_screen((1.1, 2.01)))

        from pymunk import Vec2d
        self.assertEqual(((120, 363)), view.to_screen(Vec2d(2.0, 3.95)))
