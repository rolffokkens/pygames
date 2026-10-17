import pygame
import argparse
from typing import Tuple

nothing = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], ]

bricks = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, ],
          [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
          [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
          [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
          [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
          [2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, ],
          [1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, ],
          [1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, ],
          [1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, ],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], ]

gold_pile = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
             [0, 0, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, ],
             [0, 0, 0, 0, 2, 2, 3, 3, 0, 0, 0, 0, ],
             [0, 0, 0, 2, 2, 2, 3, 3, 3, 0, 0, 0, ],
             [0, 0, 2, 2, 2, 2, 3, 3, 3, 3, 0, 0, ],
             [0, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 0, ], ]

ladder = [[0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, ],
          [0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, ],
          [0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, ],
          [0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, ],
          [0, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 0, ],
          [0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, ],
          [0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, ],
          [0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, ],
          [0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, ],
          [0, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 0, ],
          [0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, ], ]

line = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], ]

dummy = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, ],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, ],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, ],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, ],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, ],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, ],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, ],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, ],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, ],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ], ]

miner1 = [[0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, ],
          [0, 0, 1, 2, 0, 0, 2, 2, 0, 2, 1, ],
          [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 0, 1, 1, 2, 2, ],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, ], ]

miner2 = [[0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, ],
          [0, 0, 1, 2, 2, 1, 1, 2, 2, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, ], ]

miner3 = [[0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, ],
          [0, 0, 1, 0, 2, 2, 2, 2, 0, 0, 0, ],
          [0, 0, 2, 2, 2, 2, 0, 2, 1, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, ],
          [0, 0, 2, 2, 0, 0, 0, 1, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, ], ]

miner4 = [[0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, ],
          [0, 0, 1, 2, 2, 2, 1, 2, 2, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, ], ]

miner5 = [[0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, ],
          [0, 0, 2, 0, 2, 1, 2, 0, 0, 2, 0, ],
          [0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 0, ],
          [0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 0, ],
          [0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, ],
          [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, ],
          [0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, ], ]

miner6 = [[0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, ],
          [0, 0, 2, 0, 2, 1, 2, 0, 0, 2, 0, ],
          [0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 0, ],
          [0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 0, ],
          [0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, ], ]

miner7 = [[0, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, ],
          [0, 0, 0, 2, 2, 1, 2, 0, 2, 0, 0, ],
          [0, 0, 0, 2, 1, 1, 1, 0, 2, 0, 0, ],
          [0, 0, 0, 2, 1, 2, 2, 2, 2, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, ], ]

miner8 = [[0, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 2, 1, 2, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, ], ]

miner9 = [[0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, ],
          [0, 0, 0, 0, 2, 1, 2, 0, 0, 2, 0, ],
          [0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 0, ],
          [0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 0, ],
          [0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, ],
          [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 0, 2, 2, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, ],
          [0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, ], ]

miner10 = [[0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, ],
           [0, 0, 2, 0, 2, 1, 2, 0, 0, 0, 0, ],
           [0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 0, ],
           [0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 0, ],
           [0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, ],
           [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, ],
           [0, 0, 0, 2, 2, 1, 1, 1, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, ],
           [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, ], ]

miner11 = [[0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, ],
           [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, ],
           [0, 0, 0, 2, 1, 2, 2, 1, 2, 0, 0, ],
           [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, ],
           [0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 0, ],
           [0, 0, 2, 0, 0, 1, 1, 0, 0, 2, 0, ],
           [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, ],
           [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, ],
           [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, ],
           [0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, ], ]


def _init_surface(pattern, colors, scale, flip, clip):
    height = len(pattern)
    width = len(pattern[0])

    if clip:
        r_margin = 0
        l_margin = width

        for row in pattern:
            for i in range(0, width):
                if colors[row[i]][3]:
                    if i < l_margin:
                        l_margin = i
                    break
            for i in reversed(range(0, width)):
                if colors[row[i]][3]:
                    if i > r_margin:
                        r_margin = i
                    break
        r_margin = width - r_margin - 1
    else:
        r_margin = 0
        l_margin = 0

    width -= l_margin + r_margin

    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pix_array = pygame.PixelArray(surface)

    for y in range(0, height):
        for x in range(0, width):
            pix_array[x, y] = colors[pattern[y][x + l_margin]]

    if flip:
        surface = pygame.transform.flip(surface, flip, False)
        l_margin = r_margin

    return l_margin, pygame.transform.scale(surface, (scale * width, scale * height))


class MinerBase:
    def _set_sprite_image(self, pos, sprite_type, sprite_dir, inc_id):
        x, y = pos

        images = self.sprite_images[sprite_type]

        if inc_id:
            self.sprite_id += 1
        if self.sprite_id // 8 >= len(images[sprite_dir]):
            self.sprite_id = 0

        x_off, image = images[sprite_dir][self.sprite_id // 8]

        self.sprite.image = image
        self.sprite.rect = image.get_rect()

        self.sprite.rect.x = (x + x_off) * self.scale
        self.sprite.rect.y = y * self.scale

    def __init__(self, sprite_images, size, tile_size, scale, tile_pos, group, step_ms):
        self.sprite_images = sprite_images
        self.sprite_dir = 0
        self.sprite_id = 0
        self.sprite = pygame.sprite.Sprite()

        self.group = group
        self.step_ms = step_ms
        self.step_ms_cnt = 0

        self.size = size
        self.tile_size = tile_size
        self.scale = scale

        pos = self._tile_pos2pos(tile_pos)
        self._set_sprite_image(pos, LodeRunner.SPRITE_WALK, self.sprite_dir, False)

        self.hang = False
        self.stand = False

        self.tile_pos = tile_pos
        self.pos = pos

        x, y = pos
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = x * self.scale
        self.sprite.rect.y = y * self.scale

        self.sprite.add(self.group)

    def _tile_pos2pos(self, tile_pos):
        x, y = tile_pos
        tile_width, tile_height = self.tile_size
        return x * tile_width, y * tile_height

    def _pos2tile_pos(self, pos):
        x, y = pos
        tile_width, tile_height = self.tile_size
        return x // tile_width, y // tile_height

    def _get_tiles(self, pos):
        x, y = pos

        tile_width, tile_height = self.tile_size

        tiles = []
        for dx, dy in (0, 0), (tile_width - 1, 0), (tile_width - 1, tile_height - 1), (0, tile_height - 1):
            tiles.append(self._pos2tile_pos((x + dx, y + dy)))
        off_x = x - (tiles[0][0] * tile_width)
        off_y = y - (tiles[0][1] * tile_height)
        return (off_x, off_y), tiles

    def _check_hit_solid(self, tile_attrs, screen_size, pos, direction, mask):
        dir_ids = LodeRunner.DIR_CHECKS[direction]
        dx, dy = LodeRunner.DIRS[direction]

        x, y = pos

        x += dx
        y += dy

        _, tiles = self._get_tiles((x, y))
        screen_width, screen_height = screen_size

        mask &= ~LodeRunner.MASK_HANG

        for i in dir_ids:
            tx, ty = tiles[i]
            if tx < 0 or tx >= screen_width or ty < 0 or ty >= screen_height:
                return x, y, True
            if tile_attrs[tx][ty] & mask:
                return x, y, True
        return x, y, False

    def _check_fall(self, tile_attrs, screen_size):
        x, y = self.pos

        (off_x, off_y), tiles = self._get_tiles((x, y))

        self.hang = False
        if off_y == 0:
            for i in [0, 1]:
                tx, ty = tiles[i]
                if tile_attrs[tx][ty] & LodeRunner.MASK_HANG:
                    self.hang = True

        _, _, self.stand = self._check_hit_solid(tile_attrs, screen_size, (x, y + 1), LodeRunner.DIR_DOWN,
                                                 LodeRunner.MASK_SOLID | LodeRunner.MASK_STAND)
        return not self.hang and not self.stand

    def _check_climb(self, tile_attrs):
        x, y = self.pos

        _, tiles = self._get_tiles((x, y))

        for i in [0, 1, 2, 3]:
            tx, ty = tiles[i]
            attrs = tile_attrs[tx][ty]
            if attrs & LodeRunner.MASK_CLIMB:
                return True

        return False

    def time_tick(self, elapsed_ms):
        self.step_ms_cnt += elapsed_ms

    def move(self, lr_game, screen_size, direction) -> Tuple[bool, bool, bool]:
        # Returns (acted, tile_change, exit_game). acted is True whenever
        # enough time had accumulated for a step, even if the step was
        # blocked by solid tiles.
        if self.step_ms_cnt < self.step_ms:
            return False, False, False
        self.step_ms_cnt -= self.step_ms

        x, y = self.pos
        tile_attrs = lr_game.tile_attrs

        fall = self._check_fall(tile_attrs, screen_size)
        if fall:
            direction = LodeRunner.DIR_DOWN

        (off_x, off_y), tiles = self._get_tiles((x, y))
        # While mid-tile, the current step must be finished first (a new
        # direction only takes effect after a turn-around). Never let this
        # override a fall, and never apply it when there is no pending step
        # (sprite_dir = NONE): otherwise a held UP key on the landing tick
        # of a fall turns into a failed climb, freezing the mover with
        # sprite_dir = NONE at a sub-tile position, from which no input can
        # ever recover (this happened when entering a level still holding UP).
        if (off_x or off_y) and not fall and self.sprite_dir != LodeRunner.DIR_NONE:
            if direction != self.sprite_dir ^ 2:
                direction = self.sprite_dir

        if direction == LodeRunner.DIR_UP:
            if not self._check_climb(tile_attrs):
                direction = LodeRunner.DIR_NONE

        up_ok = False
        if direction == LodeRunner.DIR_UP:
            for i in [0, 1, 2, 3]:
                tx, ty = tiles[i]
                attrs = tile_attrs[tx][ty]
                if attrs & LodeRunner.MASK_CLIMB:
                    up_ok = True
                    break

        if not up_ok and direction == LodeRunner.DIR_UP:
            for i in [0, 1]:
                tx, ty = tiles[i]
                attrs = tile_attrs[tx][ty]
                if attrs & LodeRunner.MASK_HANG:
                    direction = LodeRunner.DIR_DOWN
                    break

        self.sprite_dir = direction

        nx, ny, solid = self._check_hit_solid(tile_attrs, screen_size, (x, y), direction, LodeRunner.MASK_SOLID)
        if solid:
            return True, False, False

        if self.stand or not self.hang:
            sprite_type = LodeRunner.SPRITE_WALK if (direction in [LodeRunner.DIR_LEFT, LodeRunner.DIR_RIGHT,
                                                                   LodeRunner.DIR_NONE]) else LodeRunner.SPRITE_CLIMB
        else:
            sprite_type = LodeRunner.SPRITE_HANG

        sprite_dir = LodeRunner.DIR_NONE if fall else self.sprite_dir

        self._set_sprite_image((nx, ny), sprite_type, sprite_dir, self.pos != (nx, ny))

        old_tile_pos = self.tile_pos

        self.pos = nx, ny
        self.tile_pos = self._pos2tile_pos((nx, ny))

        return True, old_tile_pos != self.tile_pos, False


class MinerPlayer(MinerBase):
    def move(self, lr_game, screen_size, direction) -> Tuple[bool, bool, bool]:
        x, y = self.pos
        tile_attrs = lr_game.tile_attrs

        acted, tile_change, exit_game = super().move(lr_game, screen_size, direction)

        if not acted:
            return acted, tile_change, exit_game

        _, tiles = self._get_tiles((x, y))
        dir_ids = [0, 1, 2, 3]
        for i in dir_ids:
            tx, ty = tiles[i]
            if tile_attrs[tx][ty] & LodeRunner.MASK_GOLD:
                lr_game.replace_tile(tx, ty, 0)
                lr_game.gold_count -= 1

        tx, ty = self.tile_pos

        return acted, tile_change, tile_attrs[tx][ty] & LodeRunner.MASK_EXIT != 0


class MinerEnemy(MinerBase):
    pass


class LodeRunner:
    right_arrow = [(-50, -25), (0, -25), (0, -50), (50, 0), (0, 50), (0, 25), (-50, 25)]

    DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1), (0, 0)]
    DIR_RIGHT = 0
    DIR_UP = 1
    DIR_LEFT = 2
    DIR_DOWN = 3
    DIR_NONE = 4

    DIRMASK_RIGHT = 1
    DIRMASK_UP = 2
    DIRMASK_LEFT = 4
    DIRMASK_DOWN = 8

    DIRMASK_ALL = DIRMASK_RIGHT | DIRMASK_UP | DIRMASK_LEFT | DIRMASK_DOWN

    MASK_SOLID = 1
    MASK_STAND = 2
    MASK_HANG = 4
    MASK_CLIMB = 8
    MASK_GOLD = 16
    MASK_EXIT = 32

    SPRITE_WALK = 0
    SPRITE_CLIMB = 1
    SPRITE_HANG = 2

    DIR_CHECKS = [[1, 2], [0, 1], [0, 3], [2, 3], []]

    TIMER_REFRESH = 0

    def _update_graph(self, pos1, direction, pos2):
        dests = self.graph.get(pos1, {})
        if direction in dests:
            return
        dests.update({direction: pos2})
        self.graph[pos1] = dests

    def _create_graph(self):
        width, height = self.size
        cells = [[0 for _ in range(0, height)] for _ in range(0, width)]
        for y in range(0, height):
            for x in range(0, width):
                hor_move = False
                if y < height - 1 and self.tile_attrs[x][y + 1] & (LodeRunner.MASK_SOLID | LodeRunner.MASK_STAND):
                    hor_move = True
                if self.tile_attrs[x][y] & LodeRunner.MASK_HANG:
                    hor_move = True

                if hor_move:
                    mask = (LodeRunner.DIRMASK_RIGHT if x < width - 1 else 0) | \
                           (LodeRunner.DIRMASK_LEFT if x > 0 else 0)
                else:
                    mask = 0
                cells[x][y] = mask | \
                              (LodeRunner.DIRMASK_DOWN if y < height - 1 else 0) | \
                              (LodeRunner.DIRMASK_UP if self.tile_attrs[x][y] & LodeRunner.MASK_CLIMB else 0)

        for y in range(0, height):
            for x in range(0, width):
                if self.tile_attrs[x][y] & LodeRunner.MASK_SOLID:
                    cells[x][y] = 0
                    if y > 0:
                        cells[x][y - 1] &= ~LodeRunner.DIRMASK_DOWN
                    if y < height - 1:
                        cells[x][y + 1] &= ~LodeRunner.DIRMASK_UP
                    if x > 0:
                        cells[x - 1][y] &= ~LodeRunner.DIRMASK_RIGHT
                    if x < width - 1:
                        cells[x + 1][y] &= ~LodeRunner.DIRMASK_LEFT

        for y in range(0, height):
            for x in range(0, width):
                if cells[x][y] & LodeRunner.DIRMASK_RIGHT:
                    self._update_graph((x + 1, y), LodeRunner.DIR_RIGHT, (x, y))
                if cells[x][y] & LodeRunner.DIRMASK_LEFT:
                    self._update_graph((x - 1, y), LodeRunner.DIR_LEFT, (x, y))
                if cells[x][y] & LodeRunner.DIRMASK_DOWN:
                    self._update_graph((x, y + 1), LodeRunner.DIR_DOWN, (x, y))
                if cells[x][y] & LodeRunner.DIRMASK_UP:
                    self._update_graph((x, y - 1), LodeRunner.DIR_UP, (x, y))

    def _find_paths(self):
        black = {}
        grey = [(LodeRunner.DIR_NONE, self.player.tile_pos)]

        while grey:
            direction, pos = grey[0]
            grey = grey[1:]
            black.update({pos: direction})

            for direction, orig in self.graph.get(pos, {}).items():
                if orig in black:
                    continue
                grey.append((direction, orig))
        self.paths = black

    def _draw_tile(self, surface, x, y, tile):
        tile_width, tile_height = self.tile_size
        # solid, tile = self.tiles[tile_id]
        pygame.Surface.blit(surface, tile, (x * tile_width * self.scale, y * tile_height * self.scale))

    def _draw_screen(self, screen, scale):
        self.scale = scale
        self.size = screen['size']
        self.colors = screen['colors']
        self.tile_size = screen['tile_size']
        width, height = self.size
        tile_width, tile_height = self.tile_size

        self.tiles = []
        for (tile, solid) in screen['tiles']:
            x_off, surface = _init_surface(tile, self.colors, scale, False, False)
            self.tiles.append((surface, solid))

        self.layout = screen['layout']
        self.tile_attrs = [[0 for _ in range(0, height)] for _ in range(0, width)]
        surface = pygame.Surface((scale * tile_width * width, scale * tile_height * height))
        self.gold_count = 0
        for y in range(0, height):
            for x in range(0, width):
                tile_id = self.layout[y][x]
                tile, solid = self.tiles[tile_id]
                self._draw_tile(surface, x, y, tile)
                self.tile_attrs[x][y] = solid
                if solid & LodeRunner.MASK_GOLD:
                    self.gold_count += 1

        return surface

    def replace_tile(self, x, y, tile_id):
        tile, solid = self.tiles[tile_id]
        self.tile_attrs[x][y] = solid
        self._draw_tile(self.background, x, y, tile)
        self._draw_tile(self.display, x, y, tile)

    def _draw_exit_ladder(self):
        width, height = self.size
        x = self.exit_ladder['x']
        top_tile_id = self.exit_ladder['top_tile']
        rest_tile_id = self.exit_ladder['rest_tile']

        for y in range(0, height):
            if self.tile_attrs[x][y]:
                break
            self.replace_tile(x, y, rest_tile_id if y else top_tile_id)
        self._create_graph()

    def _create_miner_images(self, colors):
        miner_images = []
        for _ in [self.SPRITE_WALK, self.SPRITE_CLIMB, self.SPRITE_HANG]:
            miner_images.append([])

        for sprite_type, flip, sprites, in [(self.SPRITE_WALK, True, [miner3, miner2, miner1]),
                                            (self.SPRITE_WALK, False, [dummy]),
                                            (self.SPRITE_WALK, False, [miner1, miner2, miner3]),
                                            (self.SPRITE_WALK, False, [dummy]),
                                            (self.SPRITE_WALK, False, [miner11]),
                                            (self.SPRITE_CLIMB, False, [dummy]),
                                            (self.SPRITE_CLIMB, False, [miner9, miner10]),
                                            (self.SPRITE_CLIMB, False, [dummy]),
                                            (self.SPRITE_CLIMB, False, [miner9, miner10]),
                                            (self.SPRITE_CLIMB, False, [miner5]),
                                            (self.SPRITE_HANG, False, [miner6, miner8]),
                                            (self.SPRITE_HANG, False, [miner5]),
                                            (self.SPRITE_HANG, True, [miner6, miner8]),
                                            (self.SPRITE_HANG, False, [miner5]),
                                            (self.SPRITE_HANG, False, [miner5]),
                                            ]:
            images = [_init_surface(image, colors, 3, flip, True) for image in sprites]
            miner_images[sprite_type].append(images)

        return miner_images

    def __init__(self, screens, start_level=0):
        self.screens = screens
        self.screen_idx = start_level
        self.load_screen(screens[start_level])

    def load_screen(self, screen):
        self.gold_count = 0
        self.graph = {}
        self.background = self._draw_screen(screen, 3)
        self.exit_ladder = screen['exit_ladder']

        self._create_graph()

        size = self.background.get_size()
        if getattr(self, 'display', None) is None or self.display.get_size() != size:
            self.display = pygame.display.set_mode(size)
        pygame.display.set_caption('Lode Runner')
        pygame.Surface.blit(self.display, self.background, (0, 0))

        self.group = pygame.sprite.Group()
        player_pos, player_step_ms = screen['player']
        self.player = MinerPlayer(self._create_miner_images(screen['player_colors']),
                                  (8, 11), self.tile_size, 3, player_pos, self.group,
                                  player_step_ms)
        miner_images = self._create_miner_images(screen['miner_colors'])
        self.enemies = []
        for (x, y), step_ms in screen.get('enemies', []):
            self.enemies.append(MinerEnemy(miner_images, (8, 11), self.tile_size, 3, (x, y), self.group, step_ms))

    def load_next_screen(self):
        if self.screen_idx + 1 >= len(self.screens):
            return False
        self.screen_idx += 1
        self.load_screen(self.screens[self.screen_idx])
        self._find_paths()
        return True

    def mainloop(self, tick_ms: int):
        key_map = {pygame.K_RIGHT: self.DIR_RIGHT,
                   pygame.K_LEFT: self.DIR_LEFT,
                   pygame.K_UP: self.DIR_UP,
                   pygame.K_DOWN: self.DIR_DOWN,
                   }
        pygame.init()

        pygame.time.set_timer(self.TIMER_REFRESH, tick_ms)
        game_over = False
        died = False
        direction = self.DIR_NONE
        self._find_paths()

        cur_time = pygame.time.get_ticks()
        while not game_over:
            if not self.gold_count:
                self.gold_count = -1
                self._draw_exit_ladder()
                self._find_paths()

            self.group.clear(self.display, self.background)
            self.group.draw(self.display)
            event = pygame.event.wait()
            if event.type == self.TIMER_REFRESH:
                new_time = pygame.time.get_ticks()
                # Clamp the elapsed time to a few ticks, so that one badly
                # delayed tick cannot turn into a huge multi-step catch-up
                # (entities teleporting and passing through each other).
                elapsed_ms = min(new_time - cur_time, 4 * tick_ms)
                cur_time = new_time

                self.player.time_tick(elapsed_ms)
                for enemy in self.enemies:
                    enemy.time_tick(elapsed_ms)
                moving = True
                while moving and not game_over:
                    moving = False
                    acted, tile_change, exit_game = self.player.move(self, self.size, direction)
                    if acted:
                        moving = True
                    if tile_change:
                        self._find_paths()
                    if exit_game:
                        # advance to the next level; only truly done after the last one
                        game_over = not self.load_next_screen()
                        break
                    for enemy in self.enemies:
                        if game_over:
                            break
                        edir = self.paths.get(enemy.tile_pos, LodeRunner.DIR_NONE)
                        acted, _, _ = enemy.move(self, self.size, edir)
                        if acted:
                            moving = True
                        if pygame.sprite.collide_rect(self.player.sprite, enemy.sprite):
                            pygame.time.wait(5000)
                            died = True
                            game_over = True
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key in key_map:
                    direction = key_map[event.key]
            if event.type == pygame.KEYUP:
                if event.key in key_map:
                    dir2 = key_map[event.key]
                    if direction == dir2:
                        direction = LodeRunner.DIR_NONE
            if event.type == pygame.QUIT:
                game_over = True

        # True when the player was caught: the caller returns to the
        # welcome screen. False when the game was won or the window closed.
        return died


class IntroScreen:
    """Animated title screen shown before the game starts.

    A strip of bricks with gold piles and an escape ladder forms the
    floor, miners walk back and forth over it and a blinking prompt
    waits for the player. run() returns True when the game should start,
    False when the player quits.
    """

    SCALE = 3
    FPS = 30
    WALK_DELAY_MS = 200
    BLINK_DELAY_MS = 500

    BG_COLOR = (0, 0, 0)
    TITLE_COLOR = (255, 255, 99)
    SUBTITLE_COLOR = (255, 101, 0)
    TEXT_COLOR = (170, 170, 170)
    PROMPT_COLOR = (255, 255, 255)

    START_KEYS = [pygame.K_SPACE, pygame.K_RETURN, pygame.K_KP_ENTER]

    INSTRUCTIONS = ['Collect every gold pile to make the escape ladder appear',
                    'Climb the ladder to reach the next level',
                    'Avoid the guards - move with the arrow keys']

    def __init__(self, screen):
        tiles_w, tiles_h = screen['size']
        tile_w, tile_h = screen['tile_size']
        self.width = tiles_w * tile_w * self.SCALE
        self.height = tiles_h * tile_h * self.SCALE
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Lode Runner')
        self.floor_y = self.height - tile_h * self.SCALE

        self.background = pygame.Surface((self.width, self.height))
        self.background.fill(self.BG_COLOR)
        self._draw_tiles(screen)
        self._draw_texts()
        self.miners = [self._create_miner(screen['player_colors'], self.width * 0.12, 3),
                       self._create_miner(screen['miner_colors'], self.width * 0.45, 2),
                       self._create_miner(screen['miner_colors'], self.width * 0.72, 2)]

    def _draw_tiles(self, screen):
        colors = screen['colors']
        brick = _init_surface(bricks, colors, self.SCALE, False, False)[1]
        for x in range(0, self.width, brick.get_width()):
            self.background.blit(brick, (x, self.floor_y))

        gold = _init_surface(gold_pile, colors, self.SCALE, False, False)[1]
        for fraction in [0.07, 0.3, 0.66, 0.91]:
            self.background.blit(gold, (int(self.width * fraction), self.floor_y - gold.get_height()))

        ladder_tile = _init_surface(ladder, colors, self.SCALE, False, False)[1]
        ladder_x = self.width // 2 - ladder_tile.get_width() // 2
        for rungs in range(1, 5):
            self.background.blit(ladder_tile, (ladder_x, self.floor_y - rungs * ladder_tile.get_height()))

    def _draw_texts(self):
        title_font = pygame.font.SysFont('monospace', 72, bold=True)
        text_font = pygame.font.SysFont('monospace', 24, bold=True)
        self._draw_text('LODE RUNNER', title_font, self.TITLE_COLOR, self.height * 0.2)
        self._draw_text('Can you outsmart the guards?', text_font, self.SUBTITLE_COLOR, self.height * 0.32)
        for i, line in enumerate(self.INSTRUCTIONS):
            self._draw_text(line, text_font, self.TEXT_COLOR, self.height * (0.47 + 0.07 * i))
        self.prompt = text_font.render('Press SPACE to start - ESC to quit', True, self.PROMPT_COLOR)
        self.prompt_rect = self.prompt.get_rect(center=(self.width // 2, int(self.height * 0.78)))

    def _draw_text(self, text, font, color, bottom):
        surface = font.render(text, True, color)
        self.background.blit(surface, surface.get_rect(midbottom=(self.width // 2, int(bottom))))

    def _create_miner(self, colors, start_x, step_px):
        # same orientation as in-game: DIR_RIGHT uses the flipped sprites,
        # DIR_LEFT the unflipped ones (see _create_miner_images)
        frames = {right: [_init_surface(image, colors, self.SCALE, right, True)[1]
                          for image in images]
                  for right, images in [(True, [miner3, miner2, miner1]),
                                        (False, [miner1, miner2, miner3])]}
        return {'frames': frames, 'right': True, 'frame': 0, 'step_px': step_px,
                'x': start_x, 'y': self.floor_y - 11 * self.SCALE}

    def _step_miners(self):
        for miner in self.miners:
            miner['frame'] = (miner['frame'] + 1) % len(miner['frames'][miner['right']])
            miner['x'] += miner['step_px'] if miner['right'] else -miner['step_px']
            # clamp against the width of the frame that will be drawn next
            if miner['x'] + miner['frames'][miner['right']][miner['frame']].get_width() > self.width:
                miner['right'] = False
                miner['x'] = self.width - miner['frames'][False][miner['frame']].get_width()
            elif miner['x'] < 0:
                miner['right'] = True
                miner['x'] = 0

    def _draw(self, show_prompt):
        self.display.blit(self.background, (0, 0))
        for miner in self.miners:
            self.display.blit(miner['frames'][miner['right']][miner['frame']], (int(miner['x']), miner['y']))
        if show_prompt:
            self.display.blit(self.prompt, self.prompt_rect)
        pygame.display.update()

    def run(self):
        # drop stale events (e.g. keys pressed at the moment the player
        # died) so they cannot dismiss the welcome screen right away
        pygame.event.clear()
        clock = pygame.time.Clock()
        walk_timer = 0
        blink_timer = self.BLINK_DELAY_MS
        show_prompt = False
        while True:
            elapsed_ms = clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return False
                if event.type == pygame.KEYDOWN and event.key in self.START_KEYS:
                    return True
            walk_timer += elapsed_ms
            if walk_timer >= self.WALK_DELAY_MS:
                walk_timer -= self.WALK_DELAY_MS
                self._step_miners()
            blink_timer += elapsed_ms
            if blink_timer >= self.BLINK_DELAY_MS:
                blink_timer -= self.BLINK_DELAY_MS
                show_prompt = not show_prompt
            self._draw(show_prompt)


# Tile definitions shared by all levels: (bitmap, solid/behavior mask)
tiles_def = [(nothing, 0),
             (bricks, LodeRunner.MASK_SOLID),
             (ladder, LodeRunner.MASK_STAND | LodeRunner.MASK_CLIMB),
             (line, LodeRunner.MASK_HANG),
             (gold_pile, LodeRunner.MASK_GOLD),
             (ladder, LodeRunner.MASK_STAND | LodeRunner.MASK_CLIMB | LodeRunner.MASK_EXIT),
             ]

screen1 = {'tiles': tiles_def,
           'colors': [(0, 0, 0, 255), (99, 0, 0, 255), (255, 101, 0, 255), (255, 255, 99, 255)],
           'size': (26, 16),
           'tile_size': (12, 11),
           'layout': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                      [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 4, 0, 0, 0, ],
                      [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, ],
                      [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, ],
                      [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 4, 0, 2, 0, 0, ],
                      [1, 1, 2, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, ],
                      [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, ],
                      [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 0, 0, 0, 0, 4, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 4, 0, 0, 0, ],
                      [0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, ],
                      [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, ],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
                      ],
           'player': ((4, 0), 20),
           'miner_colors': [(0, 0, 0, 0), (255, 101, 0, 255), (255, 255, 99, 255)],
           'player_colors': [(0, 0, 0, 0), (255, 255, 255, 255), (170, 170, 170, 255)],
           'enemies': [((24, 14), 24), ((14, 14), 28)],
           'exit_ladder': {'x': 20,
                           'top_tile': 5,
                           'rest_tile': 2,
                           }
           }

# Level 2: '.'=nothing, '#'=bricks, '='=ladder, '-'=rope, 'o'=gold
# Four floors plus a bottom level, deliberately asymmetric (rule 3.7):
# every slab has its own gap rhythm, no two slab rows match, and no
# feature column mirrors another across the centre. Long ladders (cols 4
# and 22) span floors 1-4; the floor-3 hole (col 16) drops onto the rope
# (row 9), which shuffles sideways and drops onto floor 4 at either end.
# The bottom level has three unevenly spaced escape ladders (cols 2, 12,
# 21); its single gold pile is the risky reward. Column 24 at row 1 is
# kept clear as the escape-ladder column.
screen2_layout_ascii = [
    "..........................",
    ".o.....................o..",
    "####=#####=#.###=##.##=###",
    "....=.....=-----=.....=...",
    "....=.....=...o.=.....=...",
    "####=##=###..=####.=##=###",
    "....=..=.....=.....=..=...",
    "..o.=..=.....=.....=..=...",
    "####=##=######=#.#####=###",
    "....=..=......=-------=...",
    "....=..=......=.......=o..",
    "##=#########=####=...=####",
    "..=.........=....=...=....",
    "..=.........=....=...=....",
    "..=.........=..o.=...=....",
    "##########################",
]
char2tile = {'.': 0, '#': 1, '=': 2, '-': 3, 'o': 4}

screen2 = {'tiles': tiles_def,
           'colors': screen1['colors'],
           'size': (26, 16),
           'tile_size': (12, 11),
           'layout': [[char2tile[c] for c in row] for row in screen2_layout_ascii],
           'player': ((15, 0), 20),  # spawn on row 0: drops into the level, as in level 1
           'miner_colors': screen1['miner_colors'],
           'player_colors': screen1['player_colors'],
           'enemies': [((10, 14), 24), ((16, 14), 28), ((21, 7), 26)],
           'exit_ladder': {'x': 24,
                           'top_tile': 5,
                           'rest_tile': 2,
                           }
           }


screens = [screen1, screen2]


def tick_ms_arg(value):
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not an integer")
    if ivalue < 1:
        raise argparse.ArgumentTypeError('the tick interval must be at least 1 ms')
    return ivalue


def level_arg(value):
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not an integer")
    if not 1 <= ivalue <= len(screens):
        raise argparse.ArgumentTypeError(f'the level must be between 1 and {len(screens)}')
    return ivalue


parser = argparse.ArgumentParser(description='Start game')
parser.add_argument('--tick-ms', type=tick_ms_arg, default=20,
                    help='number of milliseconds between clock-ticks, i.e. the refresh rate '
                         '(default: 20)')
parser.add_argument('--level', type=level_arg, default=1, metavar='LEVEL',
                    help=f'level to start on, 1 to {len(screens)} (default: 1)')

args = parser.parse_args()
pygame.init()
show_intro = True
while show_intro:
    if not IntroScreen(screens[0]).run():
        break
    sg = LodeRunner(screens, args.level - 1)
    # back to the welcome screen when the player dies, exit otherwise
    show_intro = sg.mainloop(args.tick_ms)
pygame.quit()
