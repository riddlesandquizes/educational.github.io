import pygame
import random
import csv
import math

# Initialize pygame
pygame.init()

# Window
screen_width = 800
screen_height = 600
main_window = pygame.display.set_mode((screen_width, screen_height))

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray1 = (246, 247, 251)
gray2 = (217, 221, 232)

# Define font
font1 = pygame.font.Font("freesansbold.ttf", 24)
font2 = pygame.font.Font("freesansbold.ttf", 38)
font3 = pygame.font.Font("freesansbold.ttf", 64)
font4 = pygame.font.Font("freesansbold.ttf", 18)

# Text
text1 = font1.render("  Flashcards", True, black)
text2 = font1.render(" Test", True, black)
text3 = font1.render(" Game", True, black)
text4 = font1.render("←", True, black)
text5 = font1.render("→", True, black)
text6 = font1.render("Submit", True, black)
text7 = font1.render("Add Term:", True, black)
text8 = font1.render("Add Definition:", True, black)

# images
flashcards_img = pygame.image.load("images/flashcards.png")
learn_img = pygame.image.load("images/learn.png")
test_img = pygame.image.load("images/test.png")
left_img = pygame.image.load("images/left.png")
right_img = pygame.image.load("images/right.png")
random_img = pygame.image.load("images/random.png")


def icon(icon_img, x, y):
    main_window.blit(icon_img, (x, y))


# box with text and shadow
def box1(x1, y1, x2, y2, text, window):
    # Rectangle positions for box, side, and shadow
    box_rect = pygame.Rect(x1, y1, x2, y2)
    side_rect = pygame.Rect(x1 - 1, y1 - 1, x2 + 2, y2 + 2)
    shadow_rect = pygame.Rect(x1, y1, x2 + 4, y2 + 4)
    # Detects if mouse is over
    if box_rect.collidepoint(pygame.mouse.get_pos()):
        # Draws a shadow
        pygame.draw.rect(window, gray2, shadow_rect)
    # Draws box and side
    pygame.draw.rect(window, gray2, side_rect)
    pygame.draw.rect(window, white, box_rect)
    # Gets the center position of the box
    text_rect = text.get_rect(center=box_rect.center)
    # Draws the text in the middle of the box
    window.blit(text, text_rect)


# box with only shadow
def box2(x1, y1, x2, y2, window):
    # Rectangle positions for box, side, and shadow
    box_rect = pygame.Rect(x1, y1, x2, y2)
    side_rect = pygame.Rect(x1 - 1, y1 - 1, x2 + 2, y2 + 2)
    shadow_rect = pygame.Rect(x1, y1, x2 + 4, y2 + 4)
    # Detects if mouse is over
    if box_rect.collidepoint(pygame.mouse.get_pos()):
        # Draws a shadow
        pygame.draw.rect(window, gray2, shadow_rect)
    # Draws box and side
    pygame.draw.rect(window, gray2, side_rect)
    pygame.draw.rect(window, white, box_rect)


# box with only text
def box3(x1, y1, x2, y2, text, window):
    # Rectangle positions for box, side
    box_rect = pygame.Rect(x1, y1, x2, y2)
    side_rect = pygame.Rect(x1 - 1, y1 - 1, x2 + 2, y2 + 2)
    # Draws box and side
    pygame.draw.rect(window, gray2, side_rect)
    pygame.draw.rect(window, white, box_rect)
    # Gets the center position of the box
    text_rect = text.get_rect(center=box_rect.center)
    # Draws the text in the middle of the box
    window.blit(text, text_rect)


# box
def box4(x1, y1, x2, y2, window):
    box_rect = pygame.Rect(x1, y1, x2, y2)
    side_rect = pygame.Rect(x1 - 1, y1 - 1, x2 + 2, y2 + 2)
    pygame.draw.rect(window, gray2, side_rect)
    pygame.draw.rect(window, white, box_rect)


# Words
def insert_term_csv(your_set):
    with open("csv/term.csv", 'r') as file1:
        csv_reader = csv.reader(file1)
        for item in csv_reader:
            your_set.extend(item)


def insert_definition_csv(your_set):
    with open("csv/definition.csv", 'r') as file1:
        csv_reader = csv.reader(file1)
        for item in csv_reader:
            your_set.extend(item)


term_set = []
definition_set = []
insert_term_csv(term_set)
insert_definition_csv(definition_set)

# term_set = ["one", "two", "three", "four", "five", "six"]
# definition_set = ["A", "B", "C", "D", "E", "F"]
num = 0
flip = False
is_shuffled = False
error_message = False
# Inputs
term_input = ""
definition_input = ""
term_box_color = pygame.Color("gray1")
definition_box_color = pygame.Color("gray1")
term_active = False
definition_active = False
clock = pygame.time.Clock()


# CSV file
def append_term_csv(new_term):
    with open("csv/term.csv", 'a') as file2:
        appender = csv.writer(file2)
        appender.writerow([new_term])


def append_definition_csv(new_definition):
    with open("csv/definition.csv", 'a') as file2:
        appender = csv.writer(file2)
        appender.writerow([new_definition])


# def rewrite_term_csv(new_term):
#     with open("csv/term.csv", 'w') as file3:
#         writer = csv.writer(file3)
#         writer.writerow(new_term)
#
#
# def rewrite_definition_csv(new_definition):
#     with open("csv/definition.csv", 'w') as file3:
#         writer = csv.writer(file3)
#         writer.writerow(new_definition)


# Define variables
running = True
page1 = True
page2 = False
page3 = False

# Initialize variables
high_score_value = 0

original_set = []
count = -1
for i in range(len(term_set)):
    count += 1
    row = [term_set[count], definition_set[count]]
    original_set.append(row)
shuffled_set = list(original_set)
while running:

    if page1:
        # Set caption
        pygame.display.set_caption("Flashcards")
        # Fill main window in white
        main_window.fill(gray1)

        # Menu box
        # Position of menu box
        box1_rect = pygame.Rect(50, 20, 200, 50)
        box2_rect = pygame.Rect(300, 20, 200, 50)
        box3_rect = pygame.Rect(550, 20, 200, 50)
        # Drawing menu box
        box1(50, 20, 200, 50, text1, main_window)
        box1(300, 20, 200, 50, text2, main_window)
        box1(550, 20, 200, 50, text3, main_window)
        # Drawing icons
        icon(flashcards_img, 53, 23)
        icon(learn_img, 303, 20)
        icon(test_img, 558, 23)

        # Drawing line
        line_rect = pygame.Rect(10, 90, 780, 2)
        pygame.draw.rect(main_window, black, line_rect)

        # Flashcard
        # Position of flashcard
        flashcard_rect = pygame.Rect(25, 190, 750, 210)
        # Drawing flashcard
        box4(25, 100, 750, 300, main_window)
        # Flashcard function
        if num + 1 > len(term_set):
            num = 0
        if num == -1:
            num = len(term_set) - 1
        if flip is False:
            word = font3.render(shuffled_set[num][0], True, black)
        else:
            word = font4.render(shuffled_set[num][1], True, black)
        word_rect = word.get_rect(centerx=flashcard_rect.centerx, centery=flashcard_rect.centery - 40)
        main_window.blit(word, word_rect)
        # n / n
        order = font2.render(str(num + 1) + "/" + str(len(term_set)), True, black)
        main_window.blit(order, order.get_rect(centerx=flashcard_rect.centerx, y=120))
        # Left arrow
        # Position of left arrow
        left_rect = pygame.Rect(25, 410, 750 / 2 - 5, 70)
        # Drawing left arrow
        box2(25, 410, 750 / 2 - 5, 70, main_window)
        icon(left_img, 750 / 4, 423)
        # Right arrow
        # Position of right arrow
        right_rect = pygame.Rect(35 + (750 / 2 - 5), 410, 750 / 2 - 5, 70)
        # Drawing right arrow
        box2(35 + (750 / 2 - 5), 410, 750 / 2 - 5, 70, main_window)
        icon(right_img, (750 / 4) * 3, 423)
        # Randomize
        r_shadow_rect = pygame.draw.circle(main_window, gray2, (70, 145), 38)
        random_rect = pygame.draw.circle(main_window, white, (70, 145), 35)
        if is_shuffled:
            pygame.draw.circle(main_window, gray2, (70, 145), 35)
        icon(random_img, 45, 120)

        # Inputs
        box3(20, 490, 200, 45, text7, main_window)
        box3(20, 545, 200, 45, text8, main_window)
        text_box1 = pygame.Rect(230, 487.5, 440, 50)
        text_box2 = pygame.Rect(230, 545, 440, 50)
        if term_active:
            term_box_color = pygame.Color("blue")
        else:
            term_box_color = pygame.Color("gray1")
        if definition_active:
            definition_box_color = pygame.Color("blue")
        else:
            definition_box_color = pygame.Color("gray1")
        pygame.draw.rect(main_window, term_box_color, text_box1, 3)
        pygame.draw.rect(main_window, definition_box_color, text_box2, 3)
        surf1 = font1.render(term_input, True, "black")
        surf2 = font1.render(definition_input, True, "black")
        main_window.blit(surf1, (text_box1.x + 5, text_box1.y + 12))
        main_window.blit(surf2, (text_box2.x + 5, text_box2.y + 12))
        # Submit button
        submit_rect = pygame.Rect(680, 520, 100, 40)
        box1(680, 520, 100, 40, text6, main_window)

        if error_message:
            message_rect = pygame.Rect(150, 200, 600, 50)
            message = font1.render("Please insert word for both term and definition", True, red)
            main_window.blit(message, message_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            pygame.display.update()
            error_message = False

        pygame.display.update()
        clock.tick(60)

        for events in pygame.event.get():

            if events.type == pygame.QUIT:
                running = False
            if events.type == pygame.KEYDOWN:
                if term_active:
                    if events.type == pygame.KEYDOWN:
                        if term_active:
                            if events.key == pygame.K_BACKSPACE:
                                term_input = term_input[:-1]
                            else:
                                term_input += events.unicode

                if definition_active:
                    if events.type == pygame.KEYDOWN:
                        if definition_active:
                            if events.key == pygame.K_BACKSPACE:
                                definition_input = definition_input[:-1]
                            else:
                                definition_input += events.unicode

                if events.key == pygame.K_SPACE:
                    if flip is True:
                        flip = False
                    else:
                        flip = True
                if events.key == pygame.K_LEFT:
                    flip = False
                    num -= 1
                if events.key == pygame.K_RIGHT:
                    flip = False
                    num += 1

            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                if random_rect.collidepoint(pygame.mouse.get_pos()):
                    if not is_shuffled:
                        random.shuffle(shuffled_set)
                        is_shuffled = True
                    else:
                        shuffled_set = list(original_set)
                        is_shuffled = False
                if flashcard_rect.collidepoint(pygame.mouse.get_pos()):
                    if flip is True:
                        flip = False
                    else:
                        flip = True
                if text_box1.collidepoint(events.pos):
                    term_active = True
                else:
                    term_active = False
                if text_box2.collidepoint(events.pos):
                    definition_active = True
                else:
                    definition_active = False
                if submit_rect.collidepoint(events.pos):
                    if term_input == "" or definition_input == "":
                        error_message = True
                    else:
                        error_message = False
                        term_set.append(term_input)
                        new_t = term_input
                        append_term_csv(new_t)

                        term_input = ""
                        definition_set.append(definition_input)
                        new_d = definition_input
                        append_definition_csv(new_d)
                        definition_input = ""

                        row = [term_set[-1], definition_set[-1]]
                        original_set.append(row)
                        shuffled_set = list(original_set)
                if left_rect.collidepoint(pygame.mouse.get_pos()):
                    num -= 1
                if right_rect.collidepoint(pygame.mouse.get_pos()):
                    num += 1
                if box1_rect.collidepoint(events.pos):
                    page1 = True
                    page2 = False
                    page3 = False
                if box2_rect.collidepoint(events.pos):
                    page1 = False
                    page2 = True
                    page3 = False
                if box3_rect.collidepoint(events.pos):
                    page1 = False
                    page2 = False
                    page3 = True

    elif page2:
        hinting = False
        answer_input = ""
        answering = False
        correct_message = False
        question_num = 0

        term_question = term_set
        definition_question = definition_set
        question_set = []
        count = -1
        for i in range(len(term_question)):
            count += 1
            row = [term_question[count], definition_question[count]]
            question_set.append(row)
        random.shuffle(question_set)
        correct_num = 0
        incorrect_num = 0
        while page2:
            # Set caption
            pygame.display.set_caption("Test")
            # Fill sub window in red
            main_window.fill(gray1)

            # Menu box
            # Position of menu box
            box1_rect = pygame.Rect(50, 20, 200, 50)
            box2_rect = pygame.Rect(300, 20, 200, 50)
            box3_rect = pygame.Rect(550, 20, 200, 50)
            # Drawing menu box
            box1(50, 20, 200, 50, text1, main_window)
            box1(300, 20, 200, 50, text2, main_window)
            box1(550, 20, 200, 50, text3, main_window)
            # Drawing icons
            icon(flashcards_img, 53, 23)
            icon(learn_img, 303, 20)
            icon(test_img, 558, 23)

            # Drawing line
            line_rect = pygame.Rect(10, 90, 780, 2)
            pygame.draw.rect(main_window, black, line_rect)

            # Testing frame
            # Position of testing
            testing_rect = pygame.Rect(25, 100, 750, 300)
            # Drawing testing
            box4(25, 100, 750, 300, main_window)
            question_h_rect = pygame.Rect(30, 135, 740, 50)
            question_t_rect = pygame.Rect(50, 175, 740, 50)
            question_head = font1.render("Definition:", True, black)
            if question_num + 1 > len(term_question):
                score = round(correct_num / question_num * 100, 2)
                percent = "Your score: " + str(score) + "%"
                result_text = font2.render(percent, True, "black")
                box3(25, 100, 750, 300, result_text, main_window)
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.display.update()
                correct_num = 0
                question_num = 0
                correct_message = False
                random.shuffle(question_set)
            question_text = font4.render(question_set[question_num][1], True, black)
            main_window.blit(question_head, question_h_rect)
            main_window.blit(question_text, question_t_rect)
            your_rect = pygame.Rect(30, 265, 745, 50)
            your_a = font1.render("Your Answer:", True, black)
            main_window.blit(your_a, your_rect)
            # n / n
            order = font2.render(str(question_num + 1) + "/" + str(len(term_set)), True, black)
            main_window.blit(order, order.get_rect(centerx=testing_rect.centerx, y=120))
            # Inputs
            answer_box = pygame.Rect(30, 295, 740, 50)
            if answering:
                answer_color = pygame.Color("blue")
            else:
                answer_color = pygame.Color("gray1")
            pygame.draw.rect(main_window, answer_color, answer_box, 3)
            surf3 = font1.render(answer_input, True, "black")
            main_window.blit(surf3, (answer_box.x + 5, answer_box.y + 12))
            # Submit button
            answer_rect = pygame.Rect(650, 350, 100, 40)
            # Drawing menu box
            if answer_input != "":
                answer_button = text6
            else:
                answer_button = font1.render("Skip?", True, "blue")
            box1(650, 350, 100, 40, answer_button, main_window)

            if correct_message:
                reminder = font1.render("The correct answer was", True, black)
                correct_answer = font1.render(str(question_set[question_num - 1][0]), True, red)
                reminder_rect = (20, 415, 755, 50)
                correcter_rect = (20 + 290, 415, 755, 50)
                main_window.blit(reminder, reminder_rect)
                main_window.blit(correct_answer, correcter_rect)

            # Hint button
            hint_rect = pygame.Rect(540, 350, 100, 40)
            hint_button = font1.render("Hint", True, "black")
            box1(540, 350, 100, 40, hint_button, main_window)

            if hinting:
                hinter = font1.render("The first letter of the term is", True, black)
                the_letter = str(question_set[question_num][0])
                first_letter = font1.render(the_letter[0], True, red)
                hinter_rect = (20, 415 + 55, 755, 50)
                first_rect = (20 + 340, 415 + 55, 755, 50)
                main_window.blit(hinter, hinter_rect)
                main_window.blit(first_letter, first_rect)

            pygame.display.update()

            for sub_event in pygame.event.get():
                if sub_event.type == pygame.QUIT:
                    running = False
                elif sub_event.type == pygame.KEYDOWN and sub_event.key == pygame.K_ESCAPE:
                    page1 = True
                    page2 = False
                    page3 = False
                if sub_event.type == pygame.KEYDOWN:
                    if answering:
                        if sub_event.type == pygame.KEYDOWN:
                            if answering:
                                if sub_event.key == pygame.K_BACKSPACE:
                                    answer_input = answer_input[:-1]
                                elif sub_event.key == pygame.K_RETURN:
                                    if answer_input == question_set[question_num][0]:
                                        correct_num += 1
                                        correct_message = False
                                    else:
                                        correct_message = True
                                    question_num += 1
                                    answer_input = ""
                                else:
                                    answer_input += sub_event.unicode
                if sub_event.type == pygame.MOUSEBUTTONDOWN and sub_event.button == 1:
                    if hint_rect.collidepoint(sub_event.pos):
                        if hinting:
                            hinting = False
                        else:
                            hinting = True
                    if answer_box.collidepoint(sub_event.pos):
                        answering = True
                    else:
                        answering = False
                    if answer_rect.collidepoint(sub_event.pos):
                        if answer_input == question_set[question_num][0]:
                            correct_num += 1
                            correct_message = False
                        else:
                            correct_message = True
                        question_num += 1
                        answer_input = ""
                    if box1_rect.collidepoint(sub_event.pos):
                        page1 = True
                        page2 = False
                        page3 = False
                    if box2_rect.collidepoint(sub_event.pos):
                        page1 = False
                        page2 = True
                        page3 = False
                    if box3_rect.collidepoint(sub_event.pos):
                        page1 = False
                        page2 = False
                        page3 = True

    elif page3:
        background = pygame.image.load("images/background.jpeg")
        # Player
        player_img = pygame.image.load("images/player.png")
        player_x = 370
        player_y = 480
        player_x_change = 0


        def player(x, y):
            main_window.blit(player_img, (x, y))


        # Enemy
        enemy_img = []
        enemy_x = []
        enemy_y = []
        enemy_x_change = []
        enemy_y_change = []
        enemy_term = []

        new_term_set = []
        new_definition_set = []
        if len(term_set) > 5:
            li = range(1, len(term_set))
            number_set = random.sample(li, 5)

            for i in number_set:
                new_term_set.append(term_set[i])
                new_definition_set.append(definition_set[i])
        else:
            new_term_set = term_set
            new_definition_set = definition_set

        for i in new_term_set:
            enemy_img.append(font1.render(i, True, white))
            enemy_x.append(random.randint(0, 750))
            enemy_y.append(random.randint(105, 150))
            enemy_x_change.append(3)
            enemy_y_change.append(40)
            enemy_term.append(i)


        def enemy(x, y, z):
            main_window.blit(enemy_img[z], (x, y))


        # Explosion
        explode_img = pygame.image.load("images/explode.png")
        explode_x = -100
        explode_y = -100
        explosion_timer = 0
        clock = pygame.time.Clock()


        def explosion(x, y):
            main_window.blit(explode_img, (x, y))


        # Bullet
        # Ready - You cannot see the bullet on the screen
        # Fire - The bullet is currently moving
        bullet_img = pygame.image.load("images/bullet.png")
        bullet_x = 0
        bullet_y = 480
        bullet_x_change = 0
        bullet_y_change = 10
        bullet_state = "ready"


        def fire_bullet(x, y):
            global bullet_state
            bullet_state = "fire"
            main_window.blit(bullet_img, (x + 8, y + 10))


        def is_collision(x1, y1, x2, y2):
            distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
            if distance < 54:
                return True
            else:
                return False


        # Score
        score_value = 0
        font = pygame.font.Font("freesansbold.ttf", 36)
        text_x = 10
        text_y = 120


        def show_score(x, y):
            point = font.render("Score: " + str(score_value), True, green)
            main_window.blit(point, (x, y))


        def show_high_score(x, y):
            point = font.render("High Score: " + str(high_score_value), True, green)
            main_window.blit(point, (x, y))


        # Game Over text
        cont = True
        choice = False
        over_font = pygame.font.Font("freesansbold.ttf", 64)


        def game_over_text():
            over_text = over_font.render("GAME OVER", True, (255, 255, 255))
            main_window.blit(over_text, (200, 250))


        # Current Bullet
        random_num = random.randint(0, len(new_term_set) - 1)
        current_bullet = new_definition_set[random_num]

        game_over = False

        while page3:
            # Set caption
            pygame.display.set_caption("Game")
            # Fill sub window in red
            main_window.fill(gray1)

            # Menu box
            # Position of menu box
            box1_rect = pygame.Rect(50, 20, 200, 50)
            box2_rect = pygame.Rect(300, 20, 200, 50)
            box3_rect = pygame.Rect(550, 20, 200, 50)
            # Drawing menu box
            box1(50, 20, 200, 50, text1, main_window)
            box1(300, 20, 200, 50, text2, main_window)
            box1(550, 20, 200, 50, text3, main_window)
            # Drawing icons
            icon(flashcards_img, 53, 23)
            icon(learn_img, 303, 20)
            icon(test_img, 558, 23)

            # Drawing line
            line_rect = pygame.Rect(10, 90, 780, 2)
            pygame.draw.rect(main_window, black, line_rect)

            delta_time = clock.tick(60) / 1000.0

            # Background Image
            main_window.blit(background, (0, 105))
            line_rect = pygame.Rect(10, 440, 780, 4)
            pygame.draw.rect(main_window, red, line_rect)

            # Bullet message
            current_message = font4.render("Hit: " + current_bullet, True, black)
            box3(20, 550, 760, 40, current_message, main_window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    page3 = False
                    running = False
                # if keystroke is pressed check whether its right or left
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player_x_change = -5
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player_x_change = 5
                    if event.key == pygame.K_SPACE:
                        if bullet_state == "ready":
                            # Get the current x coordinate of the spaceship
                            bullet_x = player_x
                            fire_bullet(bullet_x, bullet_y)
                if event.type == pygame.KEYUP:
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) \
                            or (event.key == pygame.K_a or event.key == pygame.K_d):
                        player_x_change = 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    page1 = True
                    page2 = False
                    page3 = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if box1_rect.collidepoint(event.pos):
                        page1 = True
                        page2 = False
                        page3 = False
                    if box2_rect.collidepoint(event.pos):
                        page1 = False
                        page2 = True
                        page3 = False
                    if box3_rect.collidepoint(event.pos):
                        page1 = False
                        page2 = False
                        page3 = True

            # Checking for boundaries of spaceship, so it does not go off the screen
            player_x += player_x_change

            if player_x <= 0:
                player_x = 0
            elif player_x >= 750:
                player_x = 750

            # Enemy movement
            for i in range(len(new_term_set)):
                enemy_x[i] += enemy_x_change[i]

                # Game Over
                if enemy_y[i] > 440:
                    for j in range(len(new_term_set)):
                        enemy_y[j] = 2000
                    game_over = True
                    break

                if enemy_x[i] <= 0:
                    enemy_x_change[i] = 3
                    enemy_y[i] += enemy_y_change[i]
                elif enemy_x[i] >= 750:
                    enemy_x_change[i] = -3
                    enemy_y[i] += enemy_y_change[i]

                # Collision
                collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
                if collision is True:
                    if new_term_set.index(enemy_term[i]) == new_definition_set.index(current_bullet):
                        explosion_timer = 1.0
                        explode_x = enemy_x[i]
                        explode_y = enemy_y[i]
                        bullet_y = 480
                        bullet_state = "ready"
                        score_value += 1
                        enemy_x[i] = random.randint(0, 750)
                        enemy_y[i] = random.randint(105, 150)
                        random_num = random.randint(0, len(new_term_set) - 1)
                        current_bullet = new_definition_set[random_num]

                if explosion_timer > 0:
                    explosion(explode_x, explode_y)
                    explosion_timer -= delta_time
                    if explosion_timer <= 0:
                        explode_x = -100
                        explode_y = -100
                        explosion_timer = 0

                explosion(explode_x, explode_y)
                enemy(enemy_x[i], enemy_y[i], i)

            # Bullet Movement
            if bullet_y <= -50:
                bullet_y = 480
                bullet_state = "ready"
            if bullet_state == "fire":
                fire_bullet(bullet_x, bullet_y)
                bullet_y -= bullet_y_change

            player(player_x, player_y)
            show_score(text_x, text_y)
            show_high_score(text_x, text_y+35)
            explosion(-100, -100)

            if game_over:
                game_over_text()
                pygame.display.update()
                pygame.time.delay(2000)

                if score_value > high_score_value:
                    high_score_value = score_value
                score_value = 0
                player_x = 370
                player_y = 480
                bullet_state = "ready"
                enemy_img = []
                enemy_x = []
                enemy_y = []
                enemy_x_change = []
                enemy_y_change = []
                enemy_term = []

                new_term_set = []
                new_definition_set = []
                if len(term_set) > 5:
                    li = range(1, len(term_set))
                    number_set = random.sample(li, 5)

                    for i in number_set:
                        new_term_set.append(term_set[i])
                        new_definition_set.append(definition_set[i])
                else:
                    new_term_set = term_set
                    new_definition_set = definition_set

                for i in new_term_set:
                    enemy_img.append(font1.render(i, True, white))
                    enemy_x.append(random.randint(0, 750))
                    enemy_y.append(random.randint(105, 150))
                    enemy_x_change.append(3)
                    enemy_y_change.append(40)
                    enemy_term.append(i)

                random_num = random.randint(0, len(new_term_set) - 1)
                current_bullet = new_definition_set[random_num]
                print(new_term_set)
                print(new_definition_set)

                game_over = False

            pygame.display.update()
