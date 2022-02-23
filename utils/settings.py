import pygame
pygame.init()
pygame.font.init()

# Color contants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
BLACK = (0, 0, 0)
AZURE = (193, 205, 205)

# Framerate
FPS = 240

# Width and height of the window
WIDTH = 800
HEIGHT = 700

# Number of rows and columns in the grid
# each pixel size = grid height / rows
ROWS = COLS = 85

PIXEL_SIZE = HEIGHT // ROWS

TOOLBAR_WIDTH = WIDTH - HEIGHT

BG_COLOR = WHITE

DRAW_GRID_LINES = False


def get_font(size):
    return pygame.font.SysFont("comicsans", size)
