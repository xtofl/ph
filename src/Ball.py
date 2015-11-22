__author__ = 'xtofl'


import pygame, pymunk


class Ball:

    def __init__(self):
        self.sprite = pygame.sprite.Sprite()
        self.image = pygame.image.load("ball.gif")
        self.rect = self.image.get_rect()
        self.body = pymunk.Body(mass=10.0, moment=1.0)
        self.forces = []

    def set_pos(self, pos):
        self.body.position = pos

    def update(self):
        if self.body.position[1] < 0:
            self.body.velocity[1] *= -1

        self.body.reset_forces()
        for f in self.forces:
            self.body.apply_force(f)
        self.rect.x, self.rect.y = self.body.position / 100
