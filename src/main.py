#!/usr/bin/env python
import pygame
import sys

__author__ = 'xtofl'

from logging import info

def main():
    pygame.init()

    size = width, height = 320, 240

    speed = [1, 1]

    black = 0, 0, 0
    ball = pygame.image.load("ball.gif")

    screen = pygame.display.set_mode(size)

    ballrect = ball.get_rect()

    clock = pygame.time.Clock()

    while 1:
        delta_t = clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        ballrect = ballrect.move([s * delta_t for s in speed])

        if ballrect.left < 0 or ballrect.right > width:
           speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
           speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()



if __name__ == "__main__":
    info("starting")
    main()
    info("exit")
