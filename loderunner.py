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

    def time_tick(self, tick_ms):
        self.step_ms_cnt += tick_ms

    def move(self, lr_game, screen_size, direction) -> Tuple[bool, bool, bool]:
        if self.step_ms_cnt < self.step_ms:
            return False, False, False
        self.step_ms_cnt -= self.step_ms

        x, y = self.pos
        tile_attrs = lr_game.tile_attrs

        fall = self._check_fall(tile_attrs, screen_size)
        if fall:
            direction = LodeRunner.DIR_DOWN

        (off_x, off_y), tiles = self._get_tiles((x, y))
        if off_x or off_y:
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
    def __init__(self, sprites, size, tile_size, scale, pos, group, step_ms):
        super().__init__(sprites, size, tile_size, scale, pos, group, step_ms)

    def move(self, lr_game, screen_size, direction) -> Tuple[bool, bool, bool]:
        x, y = self.pos
        tile_attrs = lr_game.tile_attrs

        moved, tile_change, exit_game = super().move(lr_game, screen_size, direction)

        if not moved:
            return moved, tile_change, exit_game

        _, tiles = self._get_tiles((x, y))
        dir_ids = [0, 1, 2, 3]
        for i in dir_ids:
            tx, ty = tiles[i]
            if tile_attrs[tx][ty] & LodeRunner.MASK_GOLD:
                lr_game.replace_tile(tx, ty, 0)
                lr_game.gold_count -= 1

        tx, ty = self.tile_pos

        return moved, tile_change, tile_attrs[tx][ty] & LodeRunner.MASK_EXIT != 0


class MinerEnemy(MinerBase):
    def __init__(self, sprites, size, tile_size, scale, pos, group, step_ms):
        super().__init__(sprites, size, tile_size, scale, pos, group, step_ms)

    def move(self, lr_game, screen_size, direction) -> Tuple[bool, bool, bool]:
        return super().move(lr_game, screen_size, direction)


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

        # for y in range(0, height):
        #     for x in range(0, width):
        #         print("%x " % cells[x][y], end='')
        #     print('')

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

    def __init__(self):
        self.gold_count = 0
        self.graph = {}
        screen = screen1
        self.background = self._draw_screen(screen, 3)
        self.exit_ladder = screen['exit_ladder']

        self._create_graph()

        self.display = pygame.display.set_mode(self.background.get_size())
        pygame.display.set_caption('Lode Runner')
        pygame.Surface.blit(self.display, self.background, (0, 0))

        colors = [(0, 0, 0, 0), (255, 101, 0, 255), (255, 255, 99, 255)]

        self.miner_images = []
        for _ in [self.SPRITE_WALK, self.SPRITE_CLIMB, self.SPRITE_HANG]:
            self.miner_images.append([])

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
            self.miner_images[sprite_type].append(images)

        self.group = pygame.sprite.Group()
        self.player = MinerPlayer(self.miner_images, (8, 11), self.tile_size, 3, (4, 0), self.group, 20)
        self.enemies = []
        for (x, y), step_ms in screen.get('enemies', []):
            self.enemies.append(MinerEnemy(self.miner_images, (8, 11), self.tile_size, 3, (x, y), self.group, step_ms))

    def mainloop(self, tick_ms: int):
        key_map = {pygame.K_RIGHT: self.DIR_RIGHT,
                   pygame.K_LEFT: self.DIR_LEFT,
                   pygame.K_UP: self.DIR_UP,
                   pygame.K_DOWN: self.DIR_DOWN,
                   }
        pygame.init()

        pygame.time.set_timer(self.TIMER_REFRESH, tick_ms)
        game_over = False
        direction = self.DIR_NONE
        self._find_paths()

        cur_time = pygame.time.get_ticks()
        while not game_over:
            if not self.gold_count:
                self.gold_count = -1
                self._draw_exit_ladder()

            self.group.clear(self.display, self.background)
            self.group.draw(self.display)
            event = pygame.event.wait()
            if event.type == self.TIMER_REFRESH:
                new_time = pygame.time.get_ticks()
                tick_ms = new_time - cur_time
                cur_time = new_time

                self.player.time_tick(tick_ms)
                for enemy in self.enemies:
                    enemy.time_tick(tick_ms)
                moving = True
                while moving and not game_over:
                    moving = False
                    moved, tile_change, exit_game = self.player.move(self, self.size, direction)
                    if moved:
                        moving = True
                    if tile_change:
                        self._find_paths()
                    if exit_game:
                        game_over = True
                    for enemy in self.enemies:
                        edir = self.paths.get(enemy.tile_pos, LodeRunner.DIR_NONE)
                        moved, _, _ = enemy.move(self, self.size, edir)
                        if moved:
                            moving = True
                        if pygame.sprite.collide_rect(self.player.sprite, enemy.sprite):
                            pygame.time.wait(5000)
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


screen1 = {'tiles': [(nothing, 0),
                     (bricks, LodeRunner.MASK_SOLID),
                     (ladder, LodeRunner.MASK_STAND | LodeRunner.MASK_CLIMB),
                     (line, LodeRunner.MASK_HANG),
                     (gold_pile, LodeRunner.MASK_GOLD),
                     (ladder, LodeRunner.MASK_STAND | LodeRunner.MASK_CLIMB | LodeRunner.MASK_EXIT),
                     ],
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
           'enemies': [((24, 14), 24), ((14, 14), 28)],
           'exit_ladder': {'x': 20,
                           'top_tile': 5,
                           'rest_tile': 2,
                           }
           }

parser = argparse.ArgumentParser(description='Start game')
parser.add_argument('--tick-ms', type=int,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
tick_ms = args.tick_ms if args.tick_ms else 20
sg = LodeRunner()
sg.mainloop(tick_ms)
