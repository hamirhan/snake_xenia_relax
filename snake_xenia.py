import threading
import tkinter
import time
import random


def mover():
    global fruit_cords
    global fruit
    global length
    while True:
        flag = False
        if fruit_cords[0] <= (head_cords[0] + head_cords[2]) / 2 <= fruit_cords[2] and \
           fruit_cords[1] <= (head_cords[1] + head_cords[3]) / 2 <= fruit_cords[3]:
            canv.delete(fruit)
            x = random.randint(20, width - 20)
            y = random.randint(20, height - 20)
            fruit_cords = [x - 7, y - 7, x + 7, y + 7]
            fruit = canv.create_rectangle(fruit_cords[0] - 7, fruit_cords[1] - 7, fruit_cords[0] + 7,
                                          fruit_cords[1] + 7, fill=fruit_color)
            length += 1
            flag = True
        if direction == 'right':
            head_cords[0] += 10
            head_cords[2] += 10
        elif direction == 'left':
            head_cords[0] -= 10
            head_cords[2] -= 10
        elif direction == 'up':
            head_cords[1] -= 10
            head_cords[3] -= 10
        elif direction == 'down':
            head_cords[1] += 10
            head_cords[3] += 10
        if not flag:
            canv.delete(snake[len(snake) - length])
        snake.append(canv.create_rectangle(head_cords[0], head_cords[1],
                                           head_cords[2], head_cords[3], fill=snake_color))
        time.sleep(speed)


def up(event):
    global direction
    if direction != 'down':
        direction = 'up'


def down(event):
    global direction
    if direction != 'up':
        direction = 'down'


def left(event):
    global direction
    if direction != 'right':
        direction = 'left'


def right(event):
    global direction
    if direction != 'left':
        direction = 'right'


direction = 'down'
snake_color = 'coral'
fruit_color = 'white smoke'
ground_color = 'CadetBlue1'
length = 1
speed = 0.1
snake = []
root = tkinter.Tk()
height = 500
width = 500
f_x = random.randint(20, width - 20)
f_y = random.randint(20, height - 20)
fruit_cords = [f_x - 7, f_y - 7, f_x + 7, f_y + 7]
canv = tkinter.Canvas(height=height, width=width, bg=ground_color)
canv.pack()
fruit = canv.create_rectangle(fruit_cords[0] - 7, fruit_cords[1] - 7, fruit_cords[0] + 7,
                              fruit_cords[1] + 7, fill=fruit_color)
root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<Right>', right)
root.bind('<Left>', left)
head_cords = [width // 2 - 6, height // 2 - 6, width // 2 + 6, width // 2 + 6]
tale_cords = [width // 2 - 6, height // 2 - 6, width // 2 + 6, width // 2 + 6]
snake.append(canv.create_rectangle(width // 2 - 6, height // 2 - 6, width // 2 + 6, width // 2 + 6, fill=snake_color))

threading.Thread(target=mover).start()

root.mainloop()
