import pygame

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


class player():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        # faster to draw character
        self.rect = (x, y, width, height)
        self.vel = 3


    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)


    def move(self):
        # 2 keys, 1 or 0, 1 is pressing the key, 2 is not pressing the key
        keys = pygame.key.get_pressed()
        # left arrow key
        if keys[pygame.K_LEFT]:
            # subtract x value
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(win, player):
    # the colour for the window
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()


def main():
    run = True
    p = player(50,50,100,100,(0,255,0))
    # clock = pygame.time.Clock()

    while run:
        # clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p)

main()
