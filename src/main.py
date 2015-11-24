#!/usr/bin/env python
import pygame
import sys
import pymunk
import pymunk.pygame_util
from Ball import Ball
from View import View
from World import World

__author__ = 'xtofl'

from logging import info

def main():
    pygame.init()
    world = World()

    ball = Ball()
    ball.set_pos(pymunk.Vec2d(2.0, 4.0))
    ball.body.velocity = pymunk.Vec2d(1.0, 1.0)

    world.add(ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        world.step()
        world.draw()


if __name__ == "__main__":
    info("starting")
    main()
    info("exit")
