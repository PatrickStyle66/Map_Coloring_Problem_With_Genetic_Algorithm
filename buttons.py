import pygame
from constants import Constants


class StdButton():

    def __init__(self, text='', filled=0, font_scale=20, font_color=Constants.BLACK) -> None:
        self.filled = filled
        self.font_scale = font_scale
        self.font_color = font_color
        self.text = text


#A Classe implementa o padrão Introduce Parameter Object
class Button():

    def __init__(self, color, x, y, width, height, std) -> None:
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.std = std

    def draw(self, win, outline=None) -> None:

        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), self.std.filled)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.std.filled)

        if self.std.text != '':
            font = pygame.font.SysFont('comicsans', self.std.font_scale)
            text = font.render(self.std.text, 1, self.std.font_color)
            win.blit(
                text,
                (
                    self.x + (self.width / 2 - text.get_width() / 2),
                    self.y + (self.height / 2 - text.get_height() / 2)
                )
            )

    def hover(self, pos) -> bool:

        if pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height:
            self.color = Constants.GREEN
            return True

        self.color = Constants.DARK_GREEN
        return False
