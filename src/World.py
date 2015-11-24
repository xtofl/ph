__author__ = 'xtofl'
import pymunk
import pygame

from View import View

black = 0, 0, 0


class World:

    def __init__(self, screen_size=(600, 600), one_second=500.):
        size = screen_size

        space = pymunk.Space()
        view = View(world=((0, 0), (10, 10)), screen=((0, size[0]), (size[1], 0)))
        # walls - the left-top-right-bottom walls
        static_lines = [pymunk.Segment(space.static_body, (1, 1), (1, 11), .1)
                ,pymunk.Segment(space.static_body, (1, 11), (11, 11), .1)
                ,pymunk.Segment(space.static_body, (11, 11), (11, 1), .1)
                ,pymunk.Segment(space.static_body, (1, 1), (1, 1), .1)
                ]
        space.add(static_lines)

        self.screen = pygame.display.set_mode(size)
        self.view = view
        self.space = space
        self.gravity = pymunk.Vec2d(0, -9.81)
        self.objects = []
        self.clock = pygame.time.Clock()
        self.one_second = one_second

    def add(self, obj):
        self.objects.append(obj)
        self.space.add(obj.body)
        obj.body.apply_force(self.gravity)

    def step(self):
        delta_t = self.clock.tick()

        for o in self.objects:
            o.update()

        self.space.step(delta_t / self.one_second)

    def draw(self):
        #pymunk.pygame_util.draw(screen, space)
        self.screen.fill(black)
        for o in self.objects:
            s = self.view.to_screen(o.body.position)
            self.screen.blit(o.image, s)
        pygame.display.flip()

