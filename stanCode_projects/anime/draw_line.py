"""
File: 
Name: Kuan
-------------------------
 First click, appear a round.
 Second click, draw a line and the first round disappear.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
window = GWindow()
click = 1
circle_x = 0
circle_y = 0
circle = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global circle_x
    global circle_y
    global circle
    global click
    if click % 2 == 1:
        circle = GOval(10, 10)
        window.add(circle, mouse.x - circle.width/2, mouse.y - circle.height/2)
        circle_x = mouse.x - circle.width/2
        circle_y = mouse.y - circle.height/2
        click += 1
    else:
        line = GLine(circle_x, circle_y, mouse.x, mouse.y)
        window.add(line)
        window.remove(circle)
        click += 1



if __name__ == "__main__":
    main()
