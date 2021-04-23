"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts
# graphics = BreakoutGraphics()


def main():
    graphics = BreakoutGraphics()
    graphics.start_play()
    live = NUM_LIVES
    while True:
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        # new_dx = random.randint(1, MAX_X_SPEED)
        # if random.random() > 0.5:
        #     new_dx = -new_dx
        # graphics.change_dx(new_dx)
        graphics.ball_hit_things()
        # graphics.ball_hit_things1()
        # graphics.ball_hit_things2()
        # graphics.ball_hit_things3()
        # graphics.ball_hit_things4()
        # if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
        #     new_dx = graphics.get_dx()
        #     new_dx = -new_dx
        #     graphics.change_dx(new_dx)
        graphics.ball_hit_wall()
        graphics.ball_hit_bottom2()
        if graphics.live1 == 0:
            break
        # if graphics.ball_hit_bottom():
        #     live -= 1
        #     graphics.live.text = f'live: {live}'
        #     graphics.ball.x = graphics.ball_original_position_x
        #     graphics.ball.y = graphics.ball_original_position_y
        #     graphics.reset_ball_velocity()
        #     graphics.can_click = True
        #     graphics.start_play()
        #     if live == 0:
        #         break
        pause(FRAME_RATE)



# Add animation loop here!
# def move_controlled(event):
#     if event.x > graphics.window.width:
#         graphics.peddle.x = graphics.window.width
#     else:
#         graphics.peddle.x = event.x

if __name__ == '__main__':
    main()
