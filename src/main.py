#!/usr/bin/env python
import pygame
import sys
import pymunk
import pymunk.pygame_util
from Ball import Ball
from View import View

__author__ = 'xtofl'

from logging import info

def main():
    pygame.init()
    space = pymunk.Space()

    size = width, height = 600, 600
    view = View(world=((0, 0), (10, 10)), screen=((0, size[0]), (size[1], 0)))
    # walls - the left-top-right-bottom walls
    static_lines = [pymunk.Segment(space.static_body, (1, 1), (1, 11), .1)
                ,pymunk.Segment(space.static_body, (1, 11), (11, 11), .1)
                ,pymunk.Segment(space.static_body, (11, 11), (11, 1), .1)
                ,pymunk.Segment(space.static_body, (1, 1), (1, 1), .1)
                ]
    space.add(static_lines)

    gravity = pymunk.Vec2d(0, -9.81)

    black = 0, 0, 0

    ball = Ball()
    ball.set_pos(pymunk.Vec2d(2.0, 4.0))
    ball.body.velocity = pymunk.Vec2d(1.0, 1.0)
    ball.forces.append(gravity)

    space.add(ball.body)

    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    while 1:
        delta_t = clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        ball.update()
        space.step(delta_t / 100.0)

        #pymunk.pygame_util.draw(screen, space)
        screen.fill(black)
        s = view.to_screen(ball.body.position)
        screen.blit(ball.image, s)
        pygame.display.flip()



if __name__ == "__main__":
    info("starting")
    main()
    info("exit")
