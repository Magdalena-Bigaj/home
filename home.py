import random
import pygame

if __name__ == "__main__":
    pygame.init()
    WIDTH = 1400
    HEIGHT = int(0.57 * WIDTH)
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Home")
    number_of_days = 7
    line_width = 2
    margin = 20
    gap_day = 10
    gap_chore = 30
    rectangle_chore = (
        WIDTH - margin * 2 * 2 - ((margin + line_width) * 2) - gap_chore * 3
    ) / 4
    rectangle_chore_1 = 180
    rectangle_height = WIDTH * 0.0428
    startx = WIDTH - margin * 4 - line_width * 2 - gap_chore * 3 - rectangle_chore * 4
    starty = 320
    starty2 = 150

    rectangle_day = (
        WIDTH
        - rectangle_chore_1
        - gap_day
        - margin * 2
        - (margin + line_width) * 2
        - gap_day * number_of_days
    ) / number_of_days
    startx1 = round(
        WIDTH
        - margin * 2
        - line_width
        - rectangle_chore_1
        - rectangle_day * number_of_days
        - gap_day * number_of_days
    )
    global shuffle
    shuffle = 0
    one = True
    LETTER_FONT = pygame.font.SysFont("arial", int(WIDTH / 60))
    CHORES_FONT = pygame.font.SysFont("arial", int(WIDTH / 70))
    TITLE_FONT = pygame.font.SysFont("arial", int(WIDTH / 35))
    text1 = ""
    active = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUISH = "#BEE3DB"
    IND = "#555B6E"
    APRICOT = "#FFD6BA"

    thin_line = 1
    color = APRICOT
    input_box = pygame.Rect(startx + margin, 150, WIDTH - startx * 2, margin * 4)

    class Chore:
        def __init__(self, name, duration, frequency_per_week, week_days):
            self.name = name
            self.duration = duration
            self.frequency_per_week = frequency_per_week
            self.week_days = week_days
            self.position = 0
            self.total = duration * frequency_per_week

        def __str__(self):
            return " {self.name} ".format(self=self)

    class Day:
        def __init__(self, name):
            self.name = name

    m = Day("Monday")
    tu = Day("Tuesday")
    w = Day("Wednesday")
    th = Day("Thursday")
    f = Day("Friday")
    st = Day("Saturday")
    sn = Day("Sunday")

    days = (m, tu, w, th, f, st, sn)

    vacuum_the_carpet = Chore("vacuum the carpet", 20, 2, [1, 0, 1, 0, 0, 0, 0])
    walk_the_dog = Chore("walk the dog", 40, 7, [1, 1, 1, 1, 1, 1, 1])
    dust_the_furniture = Chore("dust the furniture", 15, 3, [1, 0, 1, 0, 1, 0, 0, 0])
    do_the_ironing = Chore("do the ironing", 60, 2, [0, 1, 0, 1, 0, 0, 0])
    wash_the_dishes = Chore("wash the dishes", 15, 7, [1, 1, 1, 1, 1, 1, 1, 1])
    take_out_the_rubbish = Chore(
        "take out the rubbish", 15, 7, [1, 1, 1, 1, 1, 1, 1, 1]
    )
    water_the_flowers = Chore("water the flowers", 15, 3, [1, 0, 1, 0, 1, 0, 0])
    do_the_laundry = Chore("do the laundry", 20, 2, [1, 0, 1, 0, 0, 0, 0, 0])
    first = Chore("", 0, 0, [0, 0, 0, 0, 0, 0, 0])

    chores_2 = [first]
    chores = [
        vacuum_the_carpet,
        walk_the_dog,
        dust_the_furniture,
        do_the_ironing,
        wash_the_dishes,
        take_out_the_rubbish,
        water_the_flowers,
        do_the_laundry,
    ]

    def draw():
        win.fill(BLUISH)
        frame = pygame.draw.rect(
            win,
            IND,
            pygame.Rect(
                margin,
                margin,
                int(WIDTH - line_width - margin * 2),
                int(HEIGHT - line_width - margin * 2),
            ),
            line_width,
        )

        text = TITLE_FONT.render("HOME GAME", 1, IND)
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 12))

    def draw_first_page():
        global shuffle
        shuffle = pygame.draw.rect(
            win,
            IND,
            pygame.Rect(WIDTH - 1000, HEIGHT - 180, 600, margin * 4),
            line_width,
        )

        text = TITLE_FONT.render("SHUFFLE", 1, IND)
        win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT - 166))

        for chore in chores:
            chore.x = (
                startx
                + margin
                + line_width
                + (rectangle_chore + gap_chore) * ((chores.index(chore)) % 4)
            )
            chore.y = starty + (((chores.index(chore)) // 4) * (rectangle_chore / 2))
            if chore in chores_2:
                chore.position = pygame.draw.rect(
                    win,
                    WHITE,
                    pygame.Rect(
                        chore.x, chore.y, int(rectangle_chore), rectangle_height
                    ),
                )
            else:
                chore.position = pygame.draw.rect(
                    win,
                    IND,
                    pygame.Rect(
                        chore.x, chore.y, int(rectangle_chore), rectangle_height
                    ),
                )
            if chore in chores_2:
                text = LETTER_FONT.render(chore.name, 1, IND)
            else:
                text = LETTER_FONT.render(chore.name, 1, WHITE)
            win.blit(
                text,
                (
                    chore.x + (rectangle_chore - text.get_width()) / 2,
                    chore.y + (rectangle_height - text.get_height()) / 2,
                ),
            )

        pygame.display.update()

    def draw_schedule():
        for day in days:
            day.x = (
                startx1
                + rectangle_chore_1
                + gap_day
                + ((rectangle_day + gap_day) * days.index(day))
            )
            day.y = starty2
            frame = pygame.draw.rect(
                win, IND, pygame.Rect(day.x, day.y, rectangle_day, rectangle_height)
            )
            frame_2 = pygame.draw.rect(
                win, IND, pygame.Rect(day.x, day.y, rectangle_day, rectangle_height)
            )
            text = LETTER_FONT.render(day.name, 1, APRICOT)
            win.blit(
                text,
                (
                    day.x + (rectangle_day - (text.get_width())) / 2,
                    day.y + (rectangle_height - (text.get_height())) / 2,
                ),
            )

        for chore in chores_2:
            day.x = startx1
            day.y = starty2 + (rectangle_height + gap_day) * ((chores_2.index(chore)))
            frame = pygame.draw.rect(
                win, IND, pygame.Rect(day.x, day.y, rectangle_chore_1, rectangle_height)
            )
            text = CHORES_FONT.render(chore.name, 1, APRICOT)
            win.blit(
                text,
                (
                    day.x + gap_day + text.get_width() / len(chores_2) / 2,
                    day.y + text.get_height() / 2,
                ),
            )

            day.x = (
                startx1
                + (rectangle_chore_1)
                + gap_day
                + ((rectangle_day + gap_day) * (days.index(day)))
            )
            day.y = starty2
            frame = pygame.draw.rect(
                win, IND, pygame.Rect(day.x, day.y, rectangle_day, rectangle_height)
            )
            text = LETTER_FONT.render(day.name, 1, APRICOT)
            win.blit(
                text,
                (
                    day.x + (rectangle_day - (text.get_width())) / 2,
                    day.y + (rectangle_height - (text.get_height())) / 2,
                ),
            )
            if chore in chores:
                z = 0
                for column in range(7):
                    schedule_x = (
                        startx1
                        + rectangle_chore_1
                        + (rectangle_day + gap_day) * column
                        + gap_day
                    )
                    schedule_y = starty2 + (
                        rectangle_height + gap_day
                    ) * chores_2.index(chore)
                    chores_schedule = pygame.draw.rect(
                        win,
                        WHITE,
                        pygame.Rect(
                            schedule_x, schedule_y, rectangle_day, rectangle_height
                        ),
                    )
                    if chore.week_days[z] == 1:
                        text111 = CHORES_FONT.render(
                            str(random.choice(inhabitants)), 1, BLACK
                        )
                        win.blit(
                            text111,
                            (
                                schedule_x +(rectangle_day- text111.get_width()) / 2,
                                schedule_y + (rectangle_height- text111.get_height()) / 2,
                            ),
                        )
                    z += 1


    def draw_text_box():
        text_step1 = CHORES_FONT.render(
            "1. Please enter all the names, separated with comma and submit with ENTER",
            1,
            IND,
        )
        win.blit(text_step1, (input_box.x + 5, input_box.y + 5))
        text_surface = LETTER_FONT.render(text1, True, IND)
        width = max(WIDTH - startx * 3, text_surface.get_width() - startx * 2)
        input_box.w = width
        win.blit(text_surface, (input_box.x + margin * 3, input_box.y + margin * 2))
        pygame.draw.rect(win, color, input_box, 2)
        text_step2 = CHORES_FONT.render(
            "2. Please click on the chores you want to choose", 1, IND
        )
        win.blit(text_step2, (input_box.x + 2, input_box.y + margin * 5))

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if shuffle.collidepoint(pos):
                    draw()
                    draw_schedule()
                    one = False

                for chore in chores:
                    if chore.position.collidepoint(pos):
                        if chore not in chores_2:
                            chores_2.append(chore)


            if one:
                draw()
                draw_first_page()
                draw_text_box()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if input_box.collidepoint(pos):
                        active = not active
                    else:
                        active = False
                    color = BLACK if active else IND
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(text1)
                            text1 = ""
                        elif event.key == pygame.K_BACKSPACE:
                            text1 = text1[:-1]
                        else:
                            text1 += event.unicode
                        inhabitants = list(text1.split(","))

        pygame.display.update()
    pygame.quit()


