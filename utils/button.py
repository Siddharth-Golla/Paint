from .settings import *


class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=None):
        """Initialize button object.

        Args:
            x (int): x position where the button is to be placed.
            y (int): y position where the button is to be placed.
            width (int): Width of the button.
            height (int): Height of the button.
            color (str): Color of the button
            text (str, optional): Text to be placed on the button. Defaults to None.
            text_color (str, optional): Color of the text on the button. Defaults to None.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, win):
        # Draw the button by drawing two rectangle. One filled with color and other hollow outline

        # Initially draw the rectangle with color filled in
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))

        # Draw second hollow rectangle with only black outline
        pygame.draw.rect(
            win, BLACK, (self.x, self.y, self.width, self.height), 2)

        # Logic to draw button with text surface like "Clear" or "Erase"
        if self.text:
            button_font = get_font(10)
            text_surface = button_font.render(self.text, 1, self.text_color)
            win.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width()/2,
                     self.y + self.height / 2 - text_surface.get_height()/2))

    def clicked(self, pos):
        # Check x,y position to determine if button was clicked. Returns True only if clicked inside the dimensions of the button.
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True
