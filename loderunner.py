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

    print("mx", surface)

    return pygame.transform.scale(surface, (scale*width, scale*height))


class _Sprite(pygame.sprite.Sprite):
    def __init__(self, pattern, colors, size, tile_size, scale, pos, flip):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = _init_surface(pattern, colors, scale, flip)
        self.size = size
        self.scale = scale

        self.rect = pos


class Miner:
    def __init__(self, sprite_images, size, tile_size, scale, pos, group):
        self.sprite_images = sprite_images
        # print("m0", sprite_images)
        self.sprite_dir = 0
        self.sprite_id = 0
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.sprite_images[LodeRunner.SPRITE_WALK][self.sprite_dir][self.sprite_id]
        print("m1", type(self.sprite.image), self.sprite.image)
        self.group = group

        self.hang = False
        self.stand = False

        self.size = size
        self.tile_size = tile_size
        self.scale = scale

        self.sprite.rect = pos
        self.pos = pos

        self.sprite.add(self.group)

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

        (off_x, off_y), tiles = self._get_tiles((x, y))

        for i in [0, 1, 2, 3]:
            tx, ty = tiles[i]
            attrs = tile_attrs[tx][ty]
            if attrs & LodeRunner.MASK_CLIMB:
                return True

        return False

    def move(self, lr_game, screen_size, direction):
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
            return

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

        self.pos = nx, ny

        self.sprite.image = images[sprite_dir][self.sprite_id // 8]
        self.sprite.add(self.group)
        self.sprite.rect = nx * self.scale, ny * self.scale

        (off_x, off_y), tiles = self._get_tiles((x, y))
        dir_ids = [0, 1, 2, 3]
        for i in dir_ids:
            tx, ty = tiles[i]
            if tile_attrs[tx][ty] & LodeRunner.MASK_GOLD:
                lr_game._replace_tile(tx, ty, 0)
                tile_attrs[tx][ty] &= ~LodeRunner.MASK_GOLD

class MinerEnemy(Miner):
    def __init__(self, sprites, size, tile_size, scale, pos, group):
        super().__init__(sprites, size, tile_size, scale, pos, group)

class LodeRunner:
    right_arrow = [(-50, -25), (0, -25), (0, -50), (50, 0), (0, 50), (0, 25), (-50, 25)]

    DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1), (0,0)]
    DIR_RIGHT = 0
    DIR_UP = 1
    DIR_LEFT = 2
    DIR_DOWN = 3
    DIR_NONE = 4

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

    def _replace_tile(self, x, y, tile_id):
        self._draw_tile(self.background, x, y, tile_id)
        self._draw_tile(self.display, x, y, tile_id)

    def __init__(self):
        self.background = self._draw_screen(screen1, 3)

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
            print("m2", type(images), type(images[0]))
            self.miner_images[sprite_type].append(images)

        self.group = pygame.sprite.Group()
        self.miner = Miner(self.miner_images, (8, 11), self.tile_size, 3, (80, 0), self.group)
        self.enemy = MinerEnemy(self.miner_images, (8, 11), self.tile_size, 3, (40, 0), self.group)

    def mainloop(self):
        key_map = {pygame.K_RIGHT: self.DIR_RIGHT,
                   pygame.K_LEFT: self.DIR_LEFT,
                   pygame.K_UP: self.DIR_UP,
                   pygame.K_DOWN: self.DIR_DOWN,
                   }
        pygame.init()

        pygame.time.set_timer(self.TIMER_REFRESH, 30)
        game_over = False
        direction = self.DIR_NONE
        while not game_over:
            self.group.clear(self.display, self.background)
            self.group.draw(self.display)
            event = pygame.event.wait()
            if event.type == self.TIMER_REFRESH:
                self.miner.move(self, self.size, direction)
                self.enemy.move(self, self.size, LodeRunner.DIR_NONE)
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key in key_map:
                    direction = key_map[event.key]
            if event.type == pygame.KEYUP:
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
                      ]
           }

sg = LodeRunner()
sg.mainloop()
