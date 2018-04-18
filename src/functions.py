import pygame
import random
import levels
import public
import sprites
import dictionaries


def generate_level():
    public.all_sprites.empty()

    for i, l in enumerate(levels.LEVELS[public.level]['Top']):
        for _i, c in enumerate(l):
            if c == 'A':
                block = sprites.Block(
                    (_i * 20, i * 20), public.WHITE)
            elif c == 'B':
                block = sprites.Block(
                    (_i * 20, i * 20), public.BLACK)
            elif c == 'B':
                block = sprites.Block(
                    (_i * 20, i * 20), public.GREY)
            elif c == 'G':
                player = sprites.Player(
                    (_i * 20, i * 20), public.all_sprites)

    return player


def clamp(x, low, high):
    if x < low:
        return low
    elif x > high:
        return high
    return x
