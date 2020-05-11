

import random
import curses

#initialize the screen
screen = curses.initscr()
#Hide cursor
curses.curs_set(0)

#Screen width and hight (x and y coordinates)
screen_hight, screen_width = screen.getmaxyx()

#window coordinates
widow = curses.newwin(screen_hight, screen_width, 0, 0)
#initialize using keypad
window.keypad(1)
#the screen refresh every 100 milli-sec
window.timeout(100)
#setting the snake position in the middle of the window at the begining of the game
snake_in_x = screen_width//4
snake_in_y = screen_hight//2
#setting the snake body
snake = [
    [snake_in_y, snake_in_x],
    [snake_in_y, snake_in_x-1],
    [snake_in_y, snake_in_x-2]
]

#setting the food position
food = [sh//2, sw//2]
window.addch(food[0], food[1], curses.ACS_PI)

#defines the direction of movement of the snake at the begining of the game
key = curses.KEY_RIGHT


while True:

#detecting the new direction of the snake movment according to which key you click on
    new_key = window.getch()
#check if there is a change in the direction of the snake
#if true store the new direction (new_key) in the old one (key)
#if false donot change anything and key remains the same
    key = key if new_key == -1 else new_key

#if the snake toches the screen borders or if it touches itself so you lost the game and quit
    if snake[0][0] in [0, screen_hight] or snake[0][1] in [0, screen_width] or snake[0] in snake[1: ]:
        curses.endwin()
        quit()


    new_direction = [snake[0][0], snake[0][1]]
#change the direction of movment of the snake according to the new key
    if key == curses.KEY_DOWN:
        new_direction[0] += 1
    if key == curses.KEY_UP:
        new_direction[0] -= 1
    if key == curses.KEY_RIGHT:
        new_direction[1] += 1
    if key == curses.KEY_LEFT:
        new_direction[1] -= 1

    snake.insert(0, new_direction)

#check if the snake eat the food to increase its size
# if the snake's head coordinates is the same as the coordinates of the food
    if snake[0] == food:
        food = None
        while food is None:
#setting the position of the new food after the food is eaten
            new_food = [
                random.randint(1, screen_hight-1),
                random.randint(1, screen_width-1)
            ]
#checking if the food is not located as the same as the snake's body position
#if true so place the new food and if false so it's refused
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:

#if the snake didnt eat anything so, prevent the snake's body from growing
        tail_grow = snake.pop()
        window.addch(tail_grow[0], tail_grow[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
