import turtle as tt
import time

tt.bgcolor('black')
tt.pensize(2)
tt.speed(15)
for i in range(6):

    for color in ('red', 'magenta', 'blue',
                  'cyan', 'green', 'white',
                  'yellow'):
        tt.color(color)

        tt.circle(100)

        tt.left(10)

    tt.hideturtle()

time.sleep(2)