
import random
import curses
screen = curses.initscr()
curses.curs_set(0)

screen_hight, screen_width = screen.getmaxyx()


widow = curses.newwin(screen_hight, screen_width, 0, 0)

window.keypad(1)

window.timeout(100)
snake_in_x = screen_width//4
snake_in_y = screen_hight//2

snake = [
    [snake_in_y, snake_in_x],
    [snake_in_y, snake_in_x-1],
    [snake_in_y, snake_in_x-2]
]


food = [sh//2, sw//2]
window.addch(food[0], food[1], curses.ACS_PI)


key = curses.KEY_RIGHT


while True:
    new_key = window.getch()
    key = key if new_key == -1 else new_key

    if snake[0][0] in [0, screen_hight] or snake[0][1] in [0, screen_width] or snake[0] in snake[1: ]:
        curses.endwin()
        quit()


    new_direction = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_direction[0] += 1
    if key == curses.KEY_UP:
        new_direction[0] -= 1
    if key == curses.KEY_RIGHT:
        new_direction[1] += 1
    if key == curses.KEY_LEFT:
        new_direction[1] -= 1

    snake.insert(0, new_direction)
    if snake[0] == food:
        food = None
        while food is None:

            new_food = [
                random.randint(1, screen_hight-1),
                random.randint(1, screen_width-1)
            ]

            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail_grow = snake.pop()
        window.addch(tail_grow[0], tail_grow[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
