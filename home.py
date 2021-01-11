import random
import pygame
import math

if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = 1400, 800
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Home")

    startx = round((WIDTH - (WIDTH / 5.5 + WIDTH / 22) * 4) / 2)
    starty = 200
    WIDTH_2 = WIDTH - startx * 2
    space = WIDTH_2 / 20
    rectangle = WIDTH_2 / 5.5 + space

    LETTER_FONT = pygame.font.SysFont("arial", int(WIDTH / 55))
    TITLE_FONT = pygame.font.SysFont("arial", int(WIDTH / 35))


    class Person:  # all classes move before init
        def __init__(self, name):
            self.name = name


    # def create_inmates():
    #     name = input("What's your name ?")

    class Chore:
        def __init__(self, name, duration, frequency_per_week):
            self.name = name
            self.duration = duration
            self.frequency_per_week = frequency_per_week
            self.position = 0

        def __str__(self):
            return " {self.name} ".format(self=self)


    # def create_another_one():
    chores = []
    chores_2 = []
    vacuum_the_carpet = Chore("vacuum the carpet", 20, 2)
    walk_the_dog = Chore("walk the dog", 20, 7)
    dust_the_furniture = Chore("dust the furniture", 15, 3)
    do_the_ironing = Chore("do the ironing", 60, 2)
    wash_the_dishes = Chore("wash the dishes", 15, 7)
    take_out_the_rubbish = Chore("take out the rubbish", 15, 3)
    water_the_flowers = Chore("water the flowers", 15, 2)
    do_the_laundry = Chore("do the laundry", 20, 2)


    class Day:
        def __init__(self, name):
            self.name = name
            # self.total_time = total_time


    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUISH = "#BEE3DB"
    IND = "#555B6E"
    line_width = 2
    thin_line = 1

    m = Day("Monday")
    tu = Day("Tuesday")
    w = Day("Wednesday")
    th = Day("Thursday")
    f = Day("Friday")
    st = Day("Saturday")
    sn = Day("Sunday")

    chores = [
        vacuum_the_carpet,
        walk_the_dog,
        # dust_the_furniture,
        # do_the_ironing,
        # wash_the_dishes,
        # take_out_the_rubbish,
        # water_the_flowers,
        # do_the_laundry,
    ]


    def draw():
        win.fill(BLUISH)
        pygame.draw.rect(
            win,
            IND,
            pygame.Rect(
                20, 20, int(WIDTH - line_width - 20 * 2), int(HEIGHT - line_width - 20 * 2)
            ),
            line_width,
        )

        text = TITLE_FONT.render("HOME GAME", 1, IND)
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 20))

        shuffle = pygame.draw.rect(
            win,
            IND,
            pygame.Rect(
                WIDTH - 1000, HEIGHT - 180, 600, 80
            ),
            line_width,
        )

        text = TITLE_FONT.render("SHUFFLE", 1, IND)
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT - 166))

        for chore in chores:
            chore.x = startx + space + (rectangle * ((chores.index(chore)) % 4))
            chore.y = starty + (((chores.index(chore)) // 4) * (rectangle))
            if chore in chores_2:
                chore.position = pygame.draw.rect(
                    win, WHITE, pygame.Rect(chore.x, chore.y, int(rectangle), 80)
                )
            else:
                chore.position = pygame.draw.rect(
                    win, IND, pygame.Rect(chore.x, chore.y, int(rectangle), 80)
                )
            if chore in chores_2:
                text = LETTER_FONT.render(chore.name, 1, IND)
            else:
                text = LETTER_FONT.render(chore.name, 1, WHITE)
            win.blit(
                text, (chore.x + text.get_width() / 4, chore.y + text.get_height() / 1.5)
            )

        pygame.display.flip()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                for chore in chores:
                    if chore.position.collidepoint(pos):
                        # print('chores_2:', chores_2)
                        if chore not in chores_2:
                            chores_2.append(chore)
                            text = LETTER_FONT.render(chore.name, 1, BLACK)
                            win.blit(text, (chore.x + text.get_width() / 4, chore.y + text.get_height() / 1.5)
                                     )
                            pygame.display.update()

        draw()

    pygame.quit()
