import pygame
class std_button():
    def __init__(self,text = '',filled=0,fontScale= 20,colorFont = (0,0,0)):
        self.filled = filled
        self.fontScale = fontScale
        self.colorFont = colorFont
        self.text = text

#A Classe implementa o padrão Introduce Parameter Object
class button():

    def __init__(self, color, x, y, width, height, std):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.std = std

    def draw(self, win, outline=None):

        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), self.std.filled)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.std.filled)

        if self.std.text != '':
            font = pygame.font.SysFont('comicsans', self.std.fontScale)
            text = font.render(self.std.text, 1, self.std.colorFont)
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):

        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False