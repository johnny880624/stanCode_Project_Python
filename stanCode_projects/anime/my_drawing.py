"""
File: 
Name: Kuan
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Facebook logo! xd~
    """
    window = GWindow()
    big_rect = GRect(300, 300)
    big_rect.color = 'dark blue'
    big_rect.filled = True
    big_rect.fill_color = 'navy'
    window.add(big_rect, 100, 100)
    label = GLabel('F', 180, 449)
    label.font = '-250'
    label.color = 'snow'
    window.add(label)
    label2 = GLabel('facebook', 335, 395)
    label2.color = 'ivory'
    window.add(label2)


if __name__ == '__main__':
    main()
