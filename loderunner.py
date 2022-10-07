import pygame

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

goldpile = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
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

miner2 = [[0, 0, 0, 0, 0, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 2, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, ],
          [0, 0, 0, 0, 0, 2, 2, 2, 0, ],
          [0, 0, 0, 0, 2, 2, 2, 2, 2, ],
          [0, 0, 1, 2, 2, 1, 1, 2, 2, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 2, 0, ],
          [0, 0, 0, 0, 0, 2, 2, 0, 0, ], ]

miner3 = [[0, 0, 0, 0, 2, 0, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 2, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 1, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, ],
          [0, 0, 1, 0, 2, 2, 2, 2, 0, ],
          [0, 0, 2, 2, 2, 2, 0, 2, 1, ],
          [0, 0, 0, 0, 2, 2, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 1, 1, 0, 0, ],
          [0, 0, 1, 1, 0, 0, 1, 1, 0, ],
          [0, 0, 2, 2, 0, 0, 0, 1, 0, ],
          [0, 0, 0, 0, 0, 0, 0, 2, 2, ], ]

miner4 = [[0, 0, 0, 0, 0, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 2, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, ],
          [0, 0, 0, 0, 0, 2, 2, 2, 0, ],
          [0, 0, 0, 0, 2, 2, 2, 2, 2, ],
          [0, 0, 1, 2, 2, 2, 1, 2, 2, ],
          [0, 0, 0, 0, 0, 1, 1, 1, 0, ],
          [0, 0, 0, 0, 1, 1, 0, 1, 0, ],
          [0, 0, 0, 0, 1, 1, 0, 1, 1, ],
          [0, 0, 0, 0, 2, 2, 0, 2, 2, ], ]


miner5 = [[0, 0, 2, 0, 0, 2, 0, 0, 0, 2, ],
          [0, 0, 2, 0, 2, 1, 2, 0, 0, 2, ],
          [0, 0, 2, 0, 1, 1, 1, 0, 0, 2, ],
          [0, 0, 2, 2, 1, 2, 2, 1, 2, 2, ],
          [0, 0, 0, 2, 2, 2, 2, 2, 2, 0, ],
          [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, ],
          [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, ],
          [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, ],
          [0, 0, 0, 2, 2, 0, 2, 2, 0, 0, ], ]

miner6 = [[0, 0, 2, 0, 0, 2, 0, 0, 0, 2, ],       
          [0, 0, 2, 0, 2, 1, 2, 0, 0, 2, ],       
          [0, 0, 2, 0, 1, 1, 1, 0, 0, 2, ],       
          [0, 0, 2, 2, 1, 2, 2, 1, 2, 2, ],
          [0, 0, 0, 2, 2, 2, 2, 2, 2, 0, ],
          [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, ],       
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, ],
          [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, ],
          [0, 0, 2, 2, 0, 2, 2, 0, 0, 0, ], ]

miner7 = [[0, 0, 0, 2, 0, 2, 0, 0, 2, 0, ],
          [0, 0, 0, 2, 2, 1, 2, 0, 2, 0, ],       
          [0, 0, 0, 2, 1, 1, 1, 0, 2, 0, ],       
          [0, 0, 0, 2, 1, 2, 2, 2, 2, 0, ], 
          [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, ], 
          [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, ],       
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, ], 
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, ], 
          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, ], 
          [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, ], 
          [0, 0, 2, 2, 0, 2, 2, 0, 0, 0, ], ]

miner8 = [[0, 0, 0, 0, 2, 2, 0, 2, 0, 0, ],
          [0, 0, 0, 0, 2, 1, 2, 2, 0, 0, ],
          [0, 0, 0, 0, 2, 1, 1, 2, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, ],
          [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, ],
          [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, ],
          [0, 0, 2, 2, 0, 2, 2, 0, 0, 0, ], ]

miner9 = [[0, 0, 0, 0, 0, 2, 0, 0, 0, 2, ],
          [0, 0, 0, 0, 2, 1, 2, 0, 0, 2, ], 
          [0, 0, 2, 0, 1, 1, 1, 0, 0, 2, ], 
          [0, 0, 2, 2, 1, 2, 2, 1, 2, 2, ], 
          [0, 0, 2, 2, 2, 2, 2, 2, 2, 0, ], 
          [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, ], 
          [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, ], 
          [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, ], 
          [0, 0, 0, 1, 1, 0, 2, 2, 0, 0, ], 
          [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, ], 
          [0, 0, 0, 2, 2, 0, 0, 0, 0, 0, ], ]

miner10 = [[0, 0, 2, 0, 0, 2, 0, 0, 0, 0, ],
           [0, 0, 2, 0, 2, 1, 2, 0, 0, 0, ], 
           [0, 0, 2, 0, 1, 1, 1, 0, 0, 2, ], 
           [0, 0, 2, 2, 1, 2, 2, 1, 2, 2, ], 
           [0, 0, 0, 2, 2, 2, 2, 2, 2, 0, ], 
           [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, ], 
           [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, ], 
           [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, ], 
           [0, 0, 0, 2, 2, 1, 1, 1, 0, 0, ], 
           [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, ], 
           [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, ], ]

miner11 = [[0, 0, 0, 0, 0, 2, 0, 0, 0, 0, ], 
           [0, 0, 0, 0, 2, 1, 2, 0, 0, 0, ], 
           [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, ], 
           [0, 0, 0, 2, 1, 2, 2, 1, 2, 0, ], 
           [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, ], 
           [0, 0, 2, 0, 0, 2, 2, 0, 0, 2, ], 
           [0, 0, 2, 0, 0, 1, 1, 0, 0, 2, ], 
           [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, ], 
           [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, ], 
           [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, ], 
           [0, 0, 0, 2, 2, 0, 2, 2, 0, 0, ], ]


def _init_surface(pattern, colors, scale, flip):
    height = len(pattern)
    width = len(pattern[0])

    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pix_array = pygame.PixelArray(surface)

    for y in range(0, height):
        for x in range(0, width):
            pix_array[x, y] = colors[pattern[y][x]]

    if flip:
        surface = pygame.transform.flip(surface, flip, False)

    return pygame.transform.scale(surface, (scale*width, scale*height))


class MinerBase:
    def __init__(self, sprite_images, size, tile_size, scale, tpos, group, speed):
        self.sprite_images = sprite_images
        self.sprite_dir = 0
        self.sprite_id = 0
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.sprite_images[LodeRunner.SPRITE_WALK][self.sprite_dir][self.sprite_id]
        self.group = group
        self.speed = speed
        self.speedcnt = 0

        self.hang = False
        self.stand = False

        self.size = size
        self.tile_size = tile_size
        self.scale = scale

        pos = self._tilepos2pos(tpos)

        self.tpos = tpos
        self.pos = pos
        self.sprite.rect = pos

        self.sprite.add(self.group)

    def _tilepos2pos(self, tpos):
        x, y = tpos
        tile_width, tile_height = self.tile_size
        return x * tile_width, y * tile_height

    def _pos2tilepos(self, pos):
        x, y = pos
        tile_width, tile_height = self.tile_size
        return x // tile_width, y // tile_height

    def _get_tiles(self, pos):
        x, y = pos

        width, height = self.size
        tile_width, tile_height = self.tile_size

        tiles = []
        for dx, dy in (0, 0), (width-1, 0), (width-1, height-1), (0, height-1):
            tiles.append(self._pos2tilepos((x + dx, y + dy)))
        off_x = x - (tiles[0][0]*tile_width)
        off_y = y - (tiles[0][1]*tile_height)
        return (off_x, off_y), tiles

    def _check_hit_solid(self, tile_attrs, screen_size, pos, direction, mask):
        dir_ids = LodeRunner.DIR_CHECKS[direction]
        dx, dy = LodeRunner.DIRS[direction]

        x, y = pos

        x += dx
        y += dy

        off_y, tiles = self._get_tiles((x, y))
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

        _, _, self.stand = self._check_hit_solid(tile_attrs, screen_size, (x, y+1), LodeRunner.DIR_DOWN,
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

    def _move(self, lr_game, screen_size, direction) -> bool:
        self.speedcnt += 1
        if self.speedcnt < self.speed:
            return False
        self.speedcnt = 0

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
            return False

        if self.stand or not self.hang:
            sprite_type = LodeRunner.SPRITE_WALK if (direction in [LodeRunner.DIR_LEFT, LodeRunner.DIR_RIGHT, LodeRunner.DIR_NONE]) else LodeRunner.SPRITE_CLIMB
        else:
            sprite_type = LodeRunner.SPRITE_HANG

        sprite_dir = LodeRunner.DIR_NONE if fall else self.sprite_dir

        images = self.sprite_images[sprite_type]

        self.sprite.kill()
        if self.pos != (nx, ny):
            self.sprite_id += 1
        if self.sprite_id // 8 >= len(images[sprite_dir]):
            self.sprite_id = 0

        old_tpos = self.tpos

        self.pos = nx, ny
        self.tpos = self._pos2tilepos((nx, ny))

        self.sprite.image = images[sprite_dir][self.sprite_id // 8]
        self.sprite.add(self.group)
        self.sprite.rect = nx * self.scale, ny * self.scale

        return old_tpos != self.tpos


class MinerPlayer(MinerBase):
    def __init__(self, sprites, size, tile_size, scale, pos, group, speed):
        super().__init__(sprites, size, tile_size, scale, pos, group, speed)

    def move(self, lr_game, screen_size, direction):
        x, y = self.pos
        tile_attrs = lr_game.tile_attrs

        ret = super()._move(lr_game, screen_size, direction)

        _, tiles = self._get_tiles((x, y))
        dir_ids = [0, 1, 2, 3]
        for i in dir_ids:
            tx, ty = tiles[i]
            if tile_attrs[tx][ty] & LodeRunner.MASK_GOLD:
                lr_game.replace_tile(tx, ty, 0)
                tile_attrs[tx][ty] &= ~LodeRunner.MASK_GOLD

        return ret


class MinerEnemy(MinerBase):
    def __init__(self, sprites, size, tile_size, scale, pos, group, speed):
        super().__init__(sprites, size, tile_size, scale, pos, group, speed)

    def move(self, lr_game, screen_size, direction):
        return super()._move(lr_game, screen_size, direction)


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
                        cells[x][y-1] &= ~LodeRunner.DIRMASK_DOWN
                    if y < height-1:
                        cells[x][y+1] &= ~LodeRunner.DIRMASK_UP
                    if x > 0:
                        cells[x-1][y] &= ~LodeRunner.DIRMASK_RIGHT
                    if x < width-1:
                        cells[x+1][y] &= ~LodeRunner.DIRMASK_LEFT

        for y in range(0, height):
            for x in range(0, width):
                print("%x " % cells[x][y], end='')
            print('')

        for y in range(0, height):
            for x in range(0, width):
                if cells[x][y] & LodeRunner.DIRMASK_RIGHT:
                    self._update_graph((x+1, y), LodeRunner.DIR_RIGHT, (x, y))
                if cells[x][y] & LodeRunner.DIRMASK_LEFT:
                    self._update_graph((x-1, y), LodeRunner.DIR_LEFT, (x, y))
                if cells[x][y] & LodeRunner.DIRMASK_DOWN:
                    self._update_graph((x, y+1), LodeRunner.DIR_DOWN, (x, y))
                if cells[x][y] & LodeRunner.DIRMASK_UP:
                    self._update_graph((x, y-1), LodeRunner.DIR_UP, (x, y))

    def _find_paths(self):
        black = {}
        grey = [(LodeRunner.DIR_NONE, self.miner.tpos)]

        while grey:
            direction, pos = grey[0]
            grey = grey[1:]
            black.update({pos: direction})

            for direction, orig in self.graph.get(pos, {}).items():
                if orig in black:
                    continue
                grey.append((direction, orig))
        self.paths = black

    def _draw_tile(self, surface, x, y, tile_id):
        tile_width, tile_height = self.tile_size
        pygame.Surface.blit(surface, self.tiles[tile_id], (x*tile_width*self.scale, y*tile_height*self.scale))

    def _draw_screen(self, screen, scale):
        self.scale = scale
        self.size = screen['size']
        self.colors = screen['colors']
        self.tile_size = screen['tile_size']
        width, height = self.size
        tile_width, tile_height = self.tile_size

        self.tiles = []
        for (tile, solid) in screen['tiles']:
            self.tiles.append(_init_surface(tile, self.colors, scale, False))

        self.layout = screen['layout']
        self.tile_attrs = [[0 for _ in range(0, height)] for _ in range(0, width)]
        surface = pygame.Surface((scale*tile_width*width, scale*tile_height*height))
        for y in range(0, height):
            for x in range(0, width):
                tile_id = self.layout[y][x]
                self._draw_tile(surface, x, y, tile_id)
                _, attrs = screen['tiles'][tile_id]
                self.tile_attrs[x][y] = attrs

        return surface

    def replace_tile(self, x, y, tile_id):
        self._draw_tile(self.background, x, y, tile_id)
        self._draw_tile(self.display, x, y, tile_id)

    def __init__(self):
        self.graph = {}
        screen = screen1
        self.background = self._draw_screen(screen, 3)

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
            images = [_init_surface(i, colors, 3, flip) for i in sprites]
            self.miner_images[sprite_type].append(images)

        self.group = pygame.sprite.Group()
        self.miner = MinerPlayer(self.miner_images, (8, 11), self.tile_size, 3, (4, 0), self.group, 6)
        self.enemies = []
        for (x, y), speed in screen.get('enemies', []):
            self.enemies.append(MinerEnemy(self.miner_images, (8, 11), self.tile_size, 3, (x, y), self.group, speed))

    def mainloop(self):
        key_map = {pygame.K_RIGHT: self.DIR_RIGHT,
                   pygame.K_LEFT: self.DIR_LEFT,
                   pygame.K_UP: self.DIR_UP,
                   pygame.K_DOWN: self.DIR_DOWN,
                   }
        pygame.init()

        pygame.time.set_timer(self.TIMER_REFRESH, 5)
        game_over = False
        direction = self.DIR_NONE
        self._find_paths()
        while not game_over:
            self.group.clear(self.display, self.background)
            self.group.draw(self.display)
            event = pygame.event.wait()
            if event.type == self.TIMER_REFRESH:
                if self.miner.move(self, self.size, direction):
                    self._find_paths()
                for enemy in self.enemies:
                    edir = self.paths.get(enemy.tpos, LodeRunner.DIR_NONE)
                    enemy.move(self, self.size, edir)
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
                     (goldpile, LodeRunner.MASK_GOLD),
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
           'enemies': [((24, 14), 7), ((14, 14), 8)],
           }

sg = LodeRunner()
sg.mainloop()
