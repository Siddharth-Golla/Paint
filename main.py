from utils import *
from utils.grid import draw_grid, init_grid

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAINT")


def draw(win, grid, buttons):
    # Draw the window
    win.fill(WHITE)

    # Draw the grid from grid.py
    draw_grid(win, grid)

    # Draw the buttons
    for button in buttons:
        button.draw(win)

    # Update the display
    pygame.display.update()


run = True
# Initialize time variable and grid
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, WHITE)
draw_color = BLACK

#  x-position of all buttons is same
button_row1_x = WIDTH - TOOLBAR_WIDTH/2 - 35
button_row2_x = WIDTH - TOOLBAR_WIDTH/2 + 5

# Create a list of button objects to be placed.
buttons = [
    Button(button_row1_x, 30, 30, 30, BLACK), Button(
        button_row2_x, 30, 30, 30, WHITE),
    Button(button_row1_x, 65, 30, 30, RED), Button(
        button_row2_x, 65, 30, 30, ORANGE),
    Button(button_row1_x, 100, 30, 30, GREEN), Button(
        button_row2_x, 100, 30, 30, LGREEN),
    Button(button_row1_x, 135, 30, 30, BLUE), Button(
        button_row2_x, 135, 30, 30, VIOLET),
    Button(button_row1_x, 170, 30, 30, YELLOW), Button(
        button_row2_x, 170, 30, 30, LYELLOW),
    Button(button_row1_x, 210, 30, 30, WHITE, "Erase", BLACK),
    Button(button_row1_x, 245, 30, 30, WHITE, "Clear", BLACK)
]

while run:
    clock.tick(FPS)

    # Check all events
    for event in pygame.event.get():
        # Check if the user has closed the window
        if event.type == pygame.QUIT:
            run = False

        # Check event to get position of left mouse click
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()

            # When button is pressed inside the grid change the pixel color to drawing color
            try:
                row, col = get_row_col_from_pos(position)
                grid[row][col] = draw_color

            except IndexError:
                # Check if any button was pressed on the toolbar
                for button in buttons:
                    if not button.clicked(position):
                        continue

                    # Change draw color to the color of the button if clicked.
                    draw_color = button.color

                    # If "Clear" button is pressed then reset the grid.
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        draw_color = BLACK

    draw(WIN, grid, buttons)

pygame.quit()
