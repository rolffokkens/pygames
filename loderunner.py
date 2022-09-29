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

miner1 = [[0, 0, 0, 2, 0, 0, 0, 0, 0, ],
          [0, 0, 1, 1, 2, 0, 0, 0, 0, ],
          [0, 0, 1, 1, 1, 0, 0, 0, 0, ],
          [0, 0, 0, 2, 1, 2, 0, 0, 0, ],
          [0, 0, 2, 2, 2, 2, 2, 2, 0, ],
          [1, 2, 0, 0, 2, 2, 0, 2, 1, ],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, ],
          [0, 0, 0, 1, 0, 1, 0, 0, 0, ],
          [0, 0, 1, 1, 0, 1, 1, 2, 2, ],
          [0, 0, 1, 1, 0, 0, 0, 0, 0, ],
          [0, 0, 2, 2, 0, 0, 0, 0, 0, ], ]

miner2 = [[0, 0, 0, 2, 0, 0, 0, ],
          [0, 0, 1, 1, 2, 0, 0, ],
          [0, 0, 1, 1, 1, 0, 0, ],
          [0, 0, 0, 2, 2, 2, 0, ],
          [0, 0, 2, 2, 2, 2, 2, ],
          [1, 2, 2, 1, 1, 2, 2, ],
          [0, 0, 1, 1, 1, 0, 0, ],
          [0, 0, 0, 1, 1, 0, 0, ],
          [0, 0, 0, 1, 1, 0, 0, ],
          [0, 0, 0, 1, 1, 2, 0, ],
          [0, 0, 0, 2, 2, 0, 0, ], ]

miner3 = [[0, 0, 2, 0, 0, 0, 0, ],
          [0, 1, 1, 2, 0, 0, 0, ],
          [0, 1, 1, 1, 0, 0, 0, ],
          [0, 0, 1, 1, 0, 0, 0, ],
          [1, 0, 2, 2, 2, 2, 0, ],
          [2, 2, 2, 2, 0, 2, 1, ],
          [0, 0, 2, 2, 0, 0, 0, ],
          [0, 1, 1, 1, 1, 0, 0, ],
          [1, 1, 0, 0, 1, 1, 0, ],
          [2, 2, 0, 0, 0, 1, 0, ],
          [0, 0, 0, 0, 0, 2, 2, ], ]

miner4 = [[0, 0, 0, 2, 0, 0, 0, ],
          [0, 0, 1, 1, 2, 0, 0, ],
          [0, 0, 1, 1, 1, 0, 0, ],
          [0, 0, 0, 1, 1, 0, 0, ],
          [0, 0, 0, 2, 2, 2, 0, ],
          [0, 0, 2, 2, 2, 2, 2, ],
          [1, 2, 2, 2, 1, 2, 2, ],
          [0, 0, 0, 1, 1, 1, 0, ],
          [0, 0, 1, 1, 0, 1, 0, ],
          [0, 0, 1, 1, 0, 1, 1, ],
          [0, 0, 2, 2, 0, 2, 2, ], ]


miner5 = [[2, 0, 0, 2, 0, 0, 0, 2, ],
          [2, 0, 2, 1, 2, 0, 0, 2, ],
          [2, 0, 1, 1, 1, 0, 0, 2, ],
          [2, 2, 1, 2, 2, 1, 2, 2, ],
          [0, 2, 2, 2, 2, 2, 2, 0, ],
          [0, 0, 0, 2, 2, 0, 0, 0, ],
          [0, 0, 0, 1, 1, 0, 0, 0, ],
          [0, 0, 1, 1, 1, 0, 0, 0, ],
          [0, 1, 1, 1, 1, 1, 1, 0, ],
          [0, 1, 1, 0, 1, 1, 0, 0, ],
          [0, 2, 2, 0, 2, 2, 0, 0, ], ]


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


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pattern, colors, size, tile_size, scale, pos, flip):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = _init_surface(pattern, colors, scale, flip)
        self.size = size
        self.tile_size = tile_size
        self.scale = scale

        self.rect = pos
        # self.pos = pos


class Miner:
    def __init__(self, sprites, size, tile_size, scale, pos, group):
        self.sprites = sprites
        self.sprite_dir = 0
        self.sprite_id = 0
        self.sprite = self.sprites[self.sprite_dir][self.sprite_id]
        self.group = group

        self.size = size
        self.tile_size = tile_size
        self.scale = scale

        self.sprite.rect = pos
        self.pos = pos

        self.sprite.add(self.group)

    def _get_tiles(self, pos):
        x, y = pos

        width, height = self.size
        tile_width, tile_height = self.tile_size

        tiles = []
        for dx, dy in (0, 0), (width-1, 0), (width-1, height-1), (0, height-1):
            tiles.append(((x + dx) // tile_width, (y + dy) // tile_height))
        off_y = y - (tiles[0][1]*tile_height)
        return off_y, tiles

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

        off_y, tiles = self._get_tiles((x, y))

        if off_y == 0:
            for i in [0, 1]:
                tx, ty = tiles[i]
                if tile_attrs[tx][ty] & LodeRunner.MASK_HANG:
                    return False

        for i in [2, 3]:
            tx, ty = tiles[i]
            if not tile_attrs[tx][ty] & LodeRunner.MASK_FALL:
                continue
            tx, ty, solid = self._check_hit_solid(tile_attrs, screen_size, (x, y), LodeRunner.DIR_DOWN,
                                                  LodeRunner.MASK_SOLID | LodeRunner.MASK_STAND)
            if not solid:
                return True

        return False

    def _check_climb(self, tile_attrs):
        x, y = self.pos

        off_y, tiles = self._get_tiles((x, y))

        for i in [0, 1, 2, 3]:
            tx, ty = tiles[i]
            attrs = tile_attrs[tx][ty]
            if attrs & LodeRunner.MASK_CLIMB:
                return True

        return False

    def move(self, tile_attrs, screen_size, direction):
        x, y = self.pos

        if direction != LodeRunner.DIR_DOWN:
            if self._check_fall(tile_attrs, screen_size):
                direction = LodeRunner.DIR_DOWN

        off_y, tiles = self._get_tiles((x, y))

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

        self.sprite_dir = direction-1

        tx, ty, solid = self._check_hit_solid(tile_attrs, screen_size, (x, y), direction, LodeRunner.MASK_SOLID)
        if solid:
            return

        self.sprite_id += 1
        if self.sprite_id // 8 >= len(self.sprites[self.sprite_dir]):
            self.sprite_id = 0

        self.sprite.kill()
        self.sprite = self.sprites[self.sprite_dir][self.sprite_id // 8]
        self.sprite.add(self.group)

        self.pos = tx, ty
        self.sprite.rect = tx * self.scale, ty * self.scale


class LodeRunner:
    right_arrow = [(-50, -25), (0, -25), (0, -50), (50, 0), (0, 50), (0, 25), (-50, 25)]

    DIRS = [(0, 0), (1, 0), (0, -1), (-1, 0), (0, 1)]
    DIR_NONE = 0
    DIR_RIGHT = 1
    DIR_UP = 2
    DIR_LEFT = 3
    DIR_DOWN = 4

    MASK_SOLID = 1
    MASK_STAND = 2
    MASK_HANG = 4
    MASK_CLIMB = 8
    MASK_FALL = 16

    # DIR_CHECKS=[([],0), ([1,2],MASK_RIGHT),([0,1],MASK_UP),([0,3],MASK_LEFT),([2,3],MASK_DOWN)]
    DIR_CHECKS = [[], [1, 2], [0, 1], [0, 3], [2, 3]]

    TIMER_REFRESH = 0

    def _draw_screen(self, screen, scale):
        # self.width, self.height = screen['size']
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
                pygame.Surface.blit(surface, self.tiles[tile_id], (x*tile_width*scale, y*tile_height*scale))
                _, attrs = screen['tiles'][tile_id]
                self.tile_attrs[x][y] = attrs

        return surface

    def __init__(self):
        self.background = self._draw_screen(screen1, 3)

        self.display = pygame.display.set_mode(self.background.get_size())
        pygame.display.set_caption('Snake solver')
        pygame.Surface.blit(self.display, self.background, (0, 0))

        colors = [(0, 0, 0, 0), (255, 101, 0, 255), (255, 255, 99, 255)]

        self.miner_sprites = []
        for flip, sprites, in [(True, [miner3, miner2, miner1]),
                               (False, [miner5]),
                               (False, [miner1, miner2, miner3]),
                               (False, [miner5]),
                               ]:
            self.miner_sprites.append([Sprite(i, colors, (8, 11), self.tile_size, 3, (80, 0), flip) for i in sprites])

        self.group = pygame.sprite.Group()
        self.miner = Miner(self.miner_sprites, (8, 11), self.tile_size, 3, (80, 0), self.group)

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
                self.miner.move(self.tile_attrs, self.size, direction)
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key in key_map:
                    direction = key_map[event.key]
            if event.type == pygame.QUIT:
                game_over = True


screen1 = {'tiles': [(nothing, LodeRunner.MASK_FALL),
                     (bricks, LodeRunner.MASK_SOLID),
                     (ladder, LodeRunner.MASK_STAND | LodeRunner.MASK_CLIMB),
                     (line, LodeRunner.MASK_FALL | LodeRunner.MASK_HANG)
                     ],
           'colors': [(0, 0, 0, 255), (99, 0, 0, 255), (255, 101, 0, 255)],
           'size': (26, 16),
           'tile_size': (12, 11),
           'layout': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                      [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, ],
                      [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, ],
                      [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, ],
                      [1, 1, 2, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, ],
                      [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, ],
                      [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0, ],
                      [0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, ],
                      [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, ],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
                      ]
           }

sg = LodeRunner()
sg.mainloop()
