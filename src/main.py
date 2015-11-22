#!/usr/bin/env python
import pygame
import sys
import pymunk
import pymunk.pygame_util

__author__ = 'xtofl'

from logging import info

def main():
    pygame.init()
    space = pymunk.Space()

    size = width, height = 600, 600
    # walls - the left-top-right-bottom walls
    static_lines = [pymunk.Segment(space.static_body, (50, 50), (50, 550), 5)
                ,pymunk.Segment(space.static_body, (50, 550), (550, 550), 5)
                ,pymunk.Segment(space.static_body, (550, 550), (550, 50), 5)
                ,pymunk.Segment(space.static_body, (50, 50), (550, 50), 5)
                ]
    space.add(static_lines)

    gravity = pymunk.Vec2d(0, -9.81)

    speed = [1, 1]

    black = 0, 0, 0

    ph_ball = pymunk.Body(mass=10.0, moment=1.0)
    ph_ball.position = pymunk.Vec2d(200, 400)
    ph_ball.apply_force(gravity)

    space.add(ph_ball)

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("ball.gif")
    ballrect = ball.get_rect()

    clock = pygame.time.Clock()

    while 1:
        delta_t = clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        if ph_ball.position[1] < 0:
            ph_ball.velocity = (ph_ball.velocity[0], -ph_ball.velocity[1])
        space.step(delta_t)
        ballrect = ballrect.move(ph_ball.position)
        print(delta_t, ph_ball.position)
        pymunk.pygame_util.draw(screen, space)
        pygame.display.flip()



if __name__ == "__main__":
    info("starting")
    main()
    info("exit")
