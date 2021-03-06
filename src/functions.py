import pygame
import random
import public
import sprites
import dictionaries


def generate_clouds():
    for i in range(15):
        generated_int = random.randint(0, 1)
        cloud = sprites.Cloud(
            (random.randint(0, public.SWIDTH),
                random.randint(0, public.SHEIGHT)), generated_int)


def generate_level(show_title):
    for sprite in public.all_sprites:
        if sprite.type != 'Cloud':
            sprite.kill()

    level_data = dictionaries.LEVELS[public.level]
    public.bg_type = level_data[1]
    public.wrapping = level_data[2]

    platform = sprites.Platform()

    if show_title:
        title = sprites.Title(level_data[0])

    for i, row in enumerate(level_data[3]):
        for _i, col in enumerate(row):
            if col in 'ABC':
                color = color_return('ABC', col)
                block = sprites.Block((_i * 20, i * 20), color)

            elif col in 'DEF':
                color = color_return('DEF', col)
                exit = sprites.Exit((_i * 20, i * 20), color)

            elif col in 'GHI':
                color = color_return('GHI', col)
                pit = sprites.Pit((_i * 20, i * 20), color, 'U')

            elif col in 'JKL':
                color = color_return('JKL', col)
                pit = sprites.Pit((_i * 20, i * 20), color, 'D')

            elif col in 'MNO':
                color = color_return('MNO', col)
                jumpad = sprites.Jumpad((_i * 20, i * 20), color, 'U')

            elif col in 'PQR':
                color = color_return('PQR', col)
                jumpad = sprites.Jumpad((_i * 20, i * 20), color, 'D')

            elif col in 'STU':
                color = color_return('STU', col)
                breakable = sprites.Breakable((_i * 20, i * 20), color, 'U')

            elif col in 'VWX':
                color = color_return('VWX', col)
                breakable = sprites.Breakable((_i * 20, i * 20), color, 'D')

            elif col in '123':
                color = color_return('123', col)
                flipad = sprites.Flipad((_i * 20, i * 20), color, 'U')

            elif col in '456':
                color = color_return('456', col)
                flipad = sprites.Flipad((_i * 20, i * 20), color, 'D')

            elif col in '><':
                public.spawn = (_i * 20, i * 20)

                if col == '>':
                    public.player = sprites.Ox(public.spawn, 'R')

                elif col == '<':
                    public.player = sprites.Ox(public.spawn, 'L')

            elif col == '.':
                sphere = sprites.RGBSphere((_i * 20, i * 20), 192)

    for sprite in public.blocks:
        if sprite.type == 'Block':
            sprite.image = block_return(sprite, sprite.color)

        elif sprite.type == 'Pit':
            pit_return(sprite, sprite.color)

        elif sprite.type == 'Breakable':
            sprite.image = breakable_return(sprite, sprite.color)

            if sprite.direction == 'D':
                sprite.image = pygame.transform.flip(sprite.image, 0, 1)


def clamp(x, low, high):
    if x < low:
        return low

    elif x > high:
        return high

    else:
        return x


def center(surface):
    return ((
        public.SWIDTH / 2) - surface.get_width() // 2, (
        public.SHEIGHT / 2) - surface.get_height() // 2)


def ppc(surface, color_black, color_white):
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            r, g, b, a = surface.get_at((x, y))

            if (r, g, b) == (0, 0, 0):
                r, g, b = [color_black] * 3

            elif (r, g, b) == (255, 255, 255):
                r, g, b = [color_white] * 3

            surface.set_at((x, y), (r, g, b, a))

    return surface


def block_check(block, list_index):
    arr = ['Exit', 'Jumpad', 'Flipad', 'RGBSphere']

    if block.type not in arr[0:list_index]:
        return True

    return False


def anim_check(obj):
    prep_anim = 'Idle'

    if obj.accelerating:
        prep_anim = 'Walk'

    if not obj.on_ground:
        if obj.flipped:
            if obj.vel.y > 0:
                prep_anim = 'Jump'

            elif obj.vel.y < 0:
                prep_anim = 'Fall'

        elif not obj.flipped:
            if obj.vel.y < 0:
                prep_anim = 'Jump'

            elif obj.vel.y > 0:
                prep_anim = 'Fall'

    if obj.vel.y > 1 or obj.super_jump:
        prep_anim = 'Fall'

    if obj.died:
        prep_anim = 'Die'

    if obj.won:
        prep_anim = 'Win'

    return prep_anim


def image_return(color, index):
    if color == 0:
        return dictionaries.IMAGES[index]

    elif color == 255:
        return dictionaries.I_IMAGES[index]

    return dictionaries.G_IMAGES[index]


def block_return(obj, color):
    corners = {
        'LEFTUP': 1,
        'RIGHTUP': 1,
        'RIGHTDOWN': 1,
        'LEFTDOWN': 1,
    }
    x = obj.rect.center[0]
    y = obj.rect.center[1]

    LEFT = -11
    UP = -11

    RIGHT = 11
    DOWN = 11

    # LEFTUP
    pos = (x + LEFT, y + UP)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            corners['LEFTUP'] = 0
            break

    if pos[0] < 0:
        corners['LEFTUP'] = 0
        corners['LEFTDOWN'] = 0

    if pos[1] > public.SHEIGHT:
        corners['LEFTUP'] = 0
        corners['RIGHTUP'] = 0

    # UP
    pos = (x, y + UP)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            corners['LEFTUP'] = 0
            corners['RIGHTUP'] = 0
            break

    if pos[1] > public.SHEIGHT:
        corners['LEFTUP'] = 0
        corners['RIGHTUP'] = 0

    # RIGHTUP
    pos = (x + RIGHT, y + UP)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            corners['RIGHTUP'] = 0
            break

    if pos[0] > public.SWIDTH:
        corners['RIGHTUP'] = 0
        corners['RIGHTDOWN'] = 0

    if pos[1] > public.SHEIGHT:
        corners['LEFTUP'] = 0
        corners['RIGHTUP'] = 0

    # RIGHT
    pos = (x + RIGHT, y)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            corners['RIGHTUP'] = 0
            corners['RIGHTDOWN'] = 0

            break

    if pos[0] > public.SWIDTH:
        corners['RIGHTUP'] = 0
        corners['RIGHTDOWN'] = 0

    # RIGHTDOWN
    pos = (x + RIGHT, y + DOWN)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            corners['RIGHTDOWN'] = 0
            break

    if pos[0] > public.SWIDTH:
        corners['RIGHTUP'] = 0
        corners['RIGHTDOWN'] = 0

    if pos[1] < 0:
        corners['LEFTDOWN'] = 0
        corners['RIGHTDOWN'] = 0

    # DOWN
    pos = (x, y + DOWN)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            corners['LEFTDOWN'] = 0
            corners['RIGHTDOWN'] = 0
            break

    if pos[1] < 0:
        corners['LEFTDOWN'] = 0
        corners['RIGHTDOWN'] = 0

    # LEFTDOWN
    pos = (x + LEFT, y + DOWN)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            corners['LEFTDOWN'] = 0
            break

    if pos[0] < 0:
        corners['LEFTUP'] = 0
        corners['LEFTDOWN'] = 0

    if pos[1] < 0:
        corners['LEFTDOWN'] = 0
        corners['RIGHTDOWN'] = 0

    # LEFT
    pos = (x + LEFT, y)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            corners['LEFTUP'] = 0
            corners['LEFTDOWN'] = 0
            break

    if pos[0] < 0:
        corners['LEFTUP'] = 0
        corners['LEFTDOWN'] = 0

    binary = int(''.join(map(str, corners.values())), 2)

    return image_return(color, 'Block')[binary]


def breakable_return(obj, color):
    sides = {'LEFT': 1, 'RIGHT': 1}

    LEFT = -11
    RIGHT = 11
    x = obj.rect.center[0]
    y = obj.rect.center[1]

    # LEFT

    pos = (x + LEFT, y)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            sides['LEFT'] = 0
            break

    if pos[0] < 0:
        sides['LEFT'] = 0

    # RIGHT

    pos = (x + RIGHT, y)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            sides['RIGHT'] = 0
            break

    if pos[0] > public.SWIDTH:
        sides['RIGHT'] = 0

    binary = int(''.join(map(str, sides.values())), 2)

    return image_return(color, 'Breakable')[binary]


def pit_return(obj, color):
    sides = {'LEFT': 1, 'RIGHT': 1}

    LEFT = -11
    RIGHT = 11
    x = obj.rect.center[0]
    y = obj.rect.center[1]

    # LEFT

    pos = (x + LEFT, y)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            sides['LEFT'] = 0

    if pos[0] < 0:
        sides['LEFT'] = 0

    # RIGHT

    pos = (x + RIGHT, y)

    for sprite in public.all_sprites:
        if sprite.type not in ['Cloud', 'Exit'] and \
                sprite.rect.collidepoint(pos):

            sides['RIGHT'] = 0
            break

    if pos[0] > public.SWIDTH:
        sides['RIGHT'] = 0

    binary = int(''.join(map(str, sides.values())), 2)

    obj.image = image_return(color, 'Pit')[binary]

    if obj.direction == 'D':
        if type(obj.image) is list:
            obj.image = \
                [pygame.transform.flip(image, 0, 1) for image in obj.image]

        elif not type(obj.image) is list:
            obj.image = pygame.transform.flip(obj.image, 0, 1)


def color_return(options, value):
    prep_color = list(options)

    if prep_color[0] == value:
        return 255

    elif prep_color[1] == value:
        return 0

    return 192


def flip_check(obj):
    if obj.direction == 'U':
        obj.rect.y += 10

    elif obj.direction == 'D':
        if type(obj.image) is list:
            obj.image = \
                [pygame.transform.flip(image, 0, 1) for image in obj.image]

        elif not type(obj.image) is list:
            obj.image = pygame.transform.flip(obj.image, 0, 1)


def generate_blank():
    to_return = []
    print

    for i in range(int((public.SHEIGHT - 3) / 20)):
        s = ''

        for i in range(int(public.SWIDTH / 20)):
            s += ' '

        to_return.append(s)

    return to_return
