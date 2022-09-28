import pygame
import random
import time
import copy

class SnakeGame:
    right_arrow=[(-50,-25),(0,-25),(0,-50),(50,0),(0,50),(0,25),(-50,25)]
    rotate_matrices=[((1,0),(0,1)),((0,-1),(1,0)),((-1,0),(0,-1)),((0,1),(-1,0))]

    SNAKE_NONE=0
    SNAKE_HEAD=1
    SNAKE_TAIL=2
    SNAKE_FOOD=3

    def _init_arrows(self) -> list[list]:
        arrows=[]
        for (m00, m01), (m10, m11) in self.rotate_matrices:
            arrow=[]
            for x0, x1 in self.right_arrow:
                arrow.append((x0*m00 + x1*m10, x0*m01 + x1*m11))
            arrows.append(arrow)
        self.arrows = arrows

    @staticmethod
    def _init_board(width, height, value = None) -> list[list]:
        return [ [value for x in range(0, height)] for y in range(0, width) ]

    # A Hamlitonian path visits all cells exacty once
    # https://en.wikipedia.org/wiki/Hamiltonian_path
    # By making this an infinite loop, we have a safe path for the snake to traverse
    # the board
    #
    def _init_hamiltonian(self, width, height):
        hamildir = self._init_board(width, height)

        hamildir[0][0]=3

        for x in range(1, width):
            hamildir[x][0] = 2
        for x in range(0, width, 2):
            hamildir[x][height-1]=0
            hamildir[x+1][height-1]=1
            hamildir[x][1]=3
            hamildir[x+1][1] = 0 if x < width - 2 else 1

            for y in range(2, height-1):
                hamildir[x][y] = 3
                hamildir[x+1][y] = 1

        self.hamildir = hamildir

    def _init_freecells(self):
        self.freecells = []
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.freecells.append((x,y))

    def _update_cell(self, x, y, val, idx):
        curval = self.board[x][y]
        if (val is None) == (curval is None):
            raise Exception(f'Error ({x}, {y}): {curval} -> {val}')
        self.board[x][y] = val
        self.board_idx[x][y] = idx
        self._draw_cell(x,y)
        if val is None:
            self.freecells.append((x, y))
        else:
            self.freecells.remove((x, y))

    def _create_arrow(self, dir, scale):
        scale = scale * self.cell_size / 100
        arrow = [(x * scale + self.cell_size/2, y * scale + self.cell_size/2) for x, y in self.arrows[dir]]
        surface = pygame.Surface((self.cell_size, self.cell_size))
        pygame.draw.polygon(surface, (32, 32, 32), arrow)
        return surface

    def _create_head(self, dir):
        surface = pygame.Surface((self.cell_size, self.cell_size))
        pygame.draw.circle(surface, (0,255,0), (self.cell_size/2, self.cell_size/2), self.cell_size/2)
        return surface

    def _create_tail(self, prvdir, newdir):
        dir_pos = [(1,0),(0,-1),(-1,0),(0,1)]
        surface = pygame.Surface((self.cell_size, self.cell_size))
        for x, y in [dir_pos[prvdir ^ 2], dir_pos[newdir]]:
            x, y = (x + 1) * self.cell_size/2, (y + 1) * self.cell_size/2
            pygame.draw.line(surface, (0,255,0), (self.cell_size/2, self.cell_size/2), (x, y), 5)
        return surface

    def _create_food(self, dir):
        surface = pygame.Surface((self.cell_size, self.cell_size))
        pygame.draw.circle(surface, (255,0,0), (self.cell_size/2, self.cell_size/2), self.cell_size/2)
        return surface

    def _create_surfaces(self):
        self.surfaces = {}
        surfaces = []
        for i in range(0, 4):
            surfaces.append(self._create_arrow(i, 0.8))
        self.surfaces[self.SNAKE_NONE] = surfaces

        surfaces = []
        for prvdir in range(0, 4):
            for newdir in range(0, 4):
                surfaces.append(self._create_tail(prvdir, newdir))
        self.surfaces[self.SNAKE_TAIL] = surfaces

        self.surfaces[self.SNAKE_HEAD] = [self._create_head(0)]
        self.surfaces[self.SNAKE_FOOD] = [self._create_food(0)]

    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self._init_arrows()
        self._init_hamiltonian(width, height)
        self.board = self._init_board(width, height)
        self.board_idx = copy.deepcopy(self.hamildir)
        self._init_freecells()

        self.display = pygame.display.set_mode((self.cell_size*self.width,self.cell_size*self.height))
        pygame.display.set_caption('Snake solver')

        self._create_surfaces()

        self.snake_dir  = 0
        self.snake_tail = []
        x, y = int(width/2), int(height/2)
        self.snake_head = x, y
        self._update_cell(x, y, self.SNAKE_HEAD, 0)

        self.food = None

        self.blue=(0,0,255)
        self.red=(255,0,0)

    def _draw_arrow(self, x, y, col, dir, scale = 0.8):
        surface = self._create_arrow(dir, scale)
        pygame.Surface.blit(self.display, surface, (self.cell_size*x, self.cell_size*y))

    def __draw_arrow(self, x, y, col, dir, scale = 0.8):
        scale = scale * self.cell_size / 100
        off_x = self.cell_size*x + self.cell_size/2
        off_y = self.cell_size*y + self.cell_size/2
        arrow = [(x * scale + off_x, y * scale + off_y) for x, y in self.arrows[dir]]
        # pygame.draw.polygon(self.display, col, arrow)

        arrow = [(x * scale + self.cell_size/2, y * scale + self.cell_size/2) for x, y in self.arrows[dir]]
        surface = pygame.Surface((self.cell_size, self.cell_size))
        pygame.draw.polygon(surface, col, arrow)

        pygame.Surface.blit(self.display, surface, (self.cell_size*x, self.cell_size*y))
        #self.display.blit(surface, (x,y))

    def _draw_cell(self, x, y):
        cell_colors = {self.SNAKE_HEAD: (0, 255, 0),
                       self.SNAKE_TAIL: (0, 192, 0),
                       self.SNAKE_FOOD: (255, 0, 0)}

        item = self.board[x][y]
        if item is None:
            item = self.SNAKE_NONE
        if item in self.surfaces:
            idx = self.board_idx[x][y]
            pygame.Surface.blit(self.display, self.surfaces[item][idx], (self.cell_size*x, self.cell_size*y))
        else:
            self._draw_arrow(x, y, cell_colors[self.board[x][y]], self.hamildir[x][y])

    def _draw_board(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self._draw_cell(x, y)

    def _clear_cell(self, x, y):
        self._update_cell(x, y, None, self.hamildir[x][y])

    def _gen_food(self):
        nfree = len(self.freecells)
        if nfree == 0:
            raise Exception('No more free cells')
        x2, y2 = self.freecells[random.randint(0, nfree - 1)]

        if self.food != None:
            x1, y1 = self.food
            if self.board[x1][y1] == self.SNAKE_FOOD:
                self._clear_cell(x1, y1)

        self.food = x2, y2
        self._update_cell(x2, y2, self.SNAKE_FOOD, 0)

    def _update_tail(self, resize, prvdir, newdir):
        tail_size = len(self.snake_tail)
        x, y = self.snake_head
        self.snake_tail.insert(0, (x, y))
        self._update_cell(x, y, self.SNAKE_TAIL, prvdir * 4 + newdir)
        if resize or tail_size == 0:
            return
        x, y = self.snake_tail[tail_size]
        self.snake_tail.pop()
        self._clear_cell(x, y)

    def _get_minmax(self):
        min_x = self.width
        max_x = -1
        min_y = self.height
        max_y = -1

        for x, y in self.snake_tail:
            if y == 0:
                continue
            if (x, y) == self.snake_head:
                continue
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

        return min_x, min_y, max_x, max_y

    def _get_snake_dir(self):
        dir_offset = [(1,0),(0,-1),(-1,0),(0,1)]

        min_x, min_y, max_x, max_y = self._get_minmax()
        fx, fy = self.food

        x, y = self.snake_head
        dir = self.hamildir[x][y]
        dx, dy = dir_offset[dir]

        ddir = 3
        ddx, ddy = dir_offset[ddir]

        if y == 0:
            if x == 0:
                return dir, dx, dy
            x2 = x + ddx
            y2 = y + ddy
            dir2 = self.hamildir[x + ddx][y + ddy]

            # top edge?
            if x < min_x and x < fx and dir2 == 3:
                # food below?
                # cut short
                return ddir, ddx, ddy
            # otherwise just follow standard path
            return dir, dx, dy

        if x == self.width - 1:
            # right edge?
            # just follow standard path
            return dir, dx, dy

        x2 = x + dx
        y2 = y + dy
        dir2 = self.hamildir[x + dx][y + dy]

        rdir = 0
        rdx, rdy = dir_offset[rdir]

        if x >= max_x and fx < x:
            if y == 1 and self.board[x][0] is None:
                udir = 1
                udx, udy = dir_offset[udir]
                return udir, udx, udy

            if dir == 1:
                return dir, dx, dy

            return rdir, rdx, rdy

        if x >= max_x and max_x < fx:
            # food is on our right, and no tail on or right
            # Time for a short cut
            if fy == y:
                # same hight? move right
                return rdir, rdx, rdy

            if fy < y and dir2 == 3:
                # Food above us, but hamildir moves us down?
                # Move right, saves time...
                return rdir, rdx, rdy

            if fy > y and dir2 == 1:
                # Food below us, but hamlpath moves us up?
                # Move right, saves time...
                return rdir, rdx, rdy

        return dir, dx, dy

    def _move_snake(self):
        x, y = self.snake_head
        dir, dx, dy = self._get_snake_dir()
        self._clear_cell(x, y)

        x2 = x + dx
        y2 = y + dy

        if self.food == (x2, y2):
            self._update_tail(True, self.snake_dir, dir)
            self._gen_food()
        else:
            self._update_tail(False, self.snake_dir, dir)

        self.snake_head = x2, y2
        self._update_cell(x2, y2, self.SNAKE_HEAD, 0)

        self.snake_dir = dir

        return

    def mainloop(self):
        pygame.init()

        self._draw_board()
        self._gen_food()

        pygame.time.set_timer(0, 200)
        delay = 0.1
        game_over=False
        while not game_over:
            event = pygame.event.wait()
            if event.type == 0:
                self._move_snake()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pygame.time.set_timer(0, 200)
                if event.key == pygame.K_UP:
                    pygame.time.set_timer(0, 1)
                    delay = None
            if event.type==pygame.QUIT:
                game_over=True
            pygame.display.update()
#            if delay:
#                time.sleep(delay)

sg = SnakeGame(32, 32, 30)
sg.mainloop()
