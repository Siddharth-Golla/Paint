from .settings import *

# Initialize the grid
def init_grid(rows, cols, color):

    # Grid is 2-D list containing color value of each pixel eg. [[(255,255,255)],[(255,255,255)]]
    grid = []

    for i in range(rows):
        # Add list for every row
        grid.append([])

        for j in range(cols):
            # Add color in each row as many as columns
            grid[i].append(color)

    return grid


def draw_grid(win, grid):
    # Loop thru all the rows and columns of the grid and color
    for y, row in enumerate(grid):
        for x, pixel_color in enumerate(row):
            pygame.draw.rect(win, pixel_color, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))


def get_row_col_from_pos(pos):
    """Return the row and col in the grid where mouse is clicked

    Args:
        pos ([type]): Mouse click postion

    Raises:
        IndexError: Raise error when clicked outside grid on toolbar

    Returns:
        [type]: The row and column in the grid
    """
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if col >= COLS:
        raise IndexError
    return row, col