#!/usr/bin/env python
import pygame
import sys
import pymunk
import pymunk.pygame_util
from Ball import Ball

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

    speed = [100, 0.1]

    black = 0, 0, 0

    ball = Ball()
    ball.set_pos(pymunk.Vec2d(200, 400))
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

        print(delta_t, ball.body.position)
        #pymunk.pygame_util.draw(screen, space)
        screen.fill(black)
        screen.blit(ball.image, ball.rect)
        pygame.display.flip()



if __name__ == "__main__":
    info("starting")
    main()
    info("exit")
