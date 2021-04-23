"""
File: 
Name: Kuan
-------------------------
Make the ball fell by gravity and repeat three times, controlled by mouse.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
can_click = True
click_time = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball)
    onmouseclicked(click)


def click(mouse):
    global can_click
    global click_time
    if can_click is True:
        can_click = False
        vx = VX
        vy = 0
        while True:
            ball.move(vx, vy)
            vy += GRAVITY
            if ball.y + ball.height >= window.height:
                vy = -vy*REDUCE
            if ball.x + ball.width >= window.width:
                ball.x = START_X
                ball.y = START_Y
                can_click = True
                click_time += 1
                if click_time == 3:
                    can_click = False
                break
            pause(DELAY)


if __name__ == "__main__":
    main()
