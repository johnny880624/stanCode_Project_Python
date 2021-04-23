"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from simpleimage import SimpleImage
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    # Constructor
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, window_width/2-self.paddle.width/2, window_height-paddle_offset)

        # Live label
        self.live1 = 3
        self.live = GLabel('live: 3')
        self.live.font = '-30'
        self.window.add(self.live, x=0, y=window_height-self.live.height+30)
        # self.live2 = SimpleImage('love.png')
        # self.window.add(self.live2, x=0, y=window_height - self.live2.height + 30)

        # Score label
        self.score = 0
        self.score1 = GLabel(f'Score: {self.score}')
        self.score1.font = '-30'
        self.window.add(self.score1, x=window_width-self.score1.width-25, y=window_height-self.score1.height+30)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, (self.window.width-self.ball.width)/2, (self.window.height-self.ball.height)/2)
        self.ball_radius = ball_radius

        # Draw bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(brick_width, brick_height)
                self.brick.x = self.brick.x + self.brick.width*j + BRICK_SPACING*j
                self.brick.y = self.brick.y + self.brick.height*i + BRICK_SPACING*i
                self.brick.filled = True
                self.brick.color = 'white'
                if i == 0 or i == 1:
                    self.brick.fill_color = 'red'
                if i == 2 or i == 3:
                    self.brick.fill_color = 'orange'
                if i == 4 or i == 5:
                    self.brick.fill_color = 'yellow'
                if i == 6 or i == 7:
                    self.brick.fill_color = 'green'
                if i == 8 or i == 9:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, self.brick.x, self.brick.y)

        # Default initial position for the ball
        self.ball_original_position_x = (self.window.width - self.ball.width)/2
        self.ball_original_position_y = (self.window.height - self.ball.height)/2

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        #  Control switch
        self.can_click = True

        # Control paddle's movement
        onmousemoved(self.move_controlled)

        # change ball velocity when hit the wall or brick

    # click to start the ball
    def start_play(self):
        onmouseclicked(self.click_controlled)

    # click to turn off the switch, make sure user can only click one time.
    def click_controlled(self, event):
        if self.can_click is True:
            self.__dy = INITIAL_Y_SPEED
            self.can_click = False
            # self.set_ball_x_velocity()

    # Change ball x velocity, avoiding ball only go the same way or up and down.
    def set_ball_x_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    #   When ball hit hit the ground, reset ball velocity to zero.
    def reset_ball_velocity(self):
        self.__dx = 0
        self.__dy = 0

    # control the paddle
    def move_controlled(self, event):
        if event.x > self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        elif event.x - self.paddle.width/2 < 0:
            self.paddle.x = 0
        else:
            self.paddle.x = event.x - self.paddle.width/2

    # Detect ball's corners, whether there is a object over there.
    # If there is object there, return the position of the object.
    def ball_corner(self):
        ball_upper_left_corner = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_upper_right_corner = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
        ball_lower_left_corner = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
        ball_lower_right_corner = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y + self.ball_radius * 2)
        if ball_upper_left_corner is not None:
            return ball_upper_left_corner
        elif ball_upper_right_corner is not None:
            return ball_upper_right_corner
        elif ball_lower_left_corner is not None:
            return ball_lower_left_corner
        elif ball_lower_right_corner is not None:
            return ball_lower_right_corner

    # Distinguish the object between paddle and bricks.
    # When ball hits paddle, rebounds it and changes the x velocity.
    # When ball hits bricks, rebounds it and removes it.
    def ball_hit_things(self):
        if self.ball_corner() is self.paddle:
            self.__dy = -self.__dy
            self.set_ball_x_velocity()
        elif self.ball_corner() is self.live:
            self.__dy = self.__dy
        elif self.ball_corner() is self.score1:
            self.__dy = self.__dy
        elif self.ball_corner() is not None:
            self.window.remove(self.ball_corner())
            self.__dy = -self.__dy
            self.score +=1
            self.score1.text = f'Score: {self.score }'

    # When ball hits the wall, rebounds it.
    def ball_hit_wall(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -1*self.__dy

    # When ball hits the bottom, returns something gets hit.
    def ball_hit_bottom(self):
        hit_thing = False
        if self.ball.y + self.ball.height >= self.window.height:
            hit_thing = True
            return hit_thing

    # When ball hits the bottom, returns something gets hit.
    def ball_hit_bottom2(self):
        if self.ball.y + self.ball.height >= self.window.height:
            self.live1 -= 1
            self.live.text = f'live: {self.live1}'
            self.ball.x = self.ball_original_position_x
            self.ball.y = self.ball_original_position_y
            self.reset_ball_velocity()
            self.can_click = True
            self.start_play()

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def change_dx(self, new_speed):
        self.__dx = new_speed
    # def ball_corner1(self):
    #     ball_upper_left_corner = self.window.get_object_at(self.ball.x, self.ball.y)
    #     if ball_upper_left_corner is not None:
    #         return ball_upper_left_corner
    #
    # def ball_corner2(self):
    #     ball_upper_right_corner = self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y)
    #     if ball_upper_right_corner is not None:
    #         return ball_upper_right_corner
    #
    # def ball_corner3(self):
    #     ball_lower_left_corner = self.window.get_object_at(self.ball.x, self.ball.y+self.ball_radius*2)
    #     if ball_lower_left_corner is not None:
    #         return ball_lower_left_corner
    #
    # def ball_corner4(self):
    #     ball_lower_right_corner = self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y+self.ball_radius*2)
    #     if ball_lower_right_corner is not None:
    #         return ball_lower_right_corner

    # def ball_hit_things1(self):
    #     if self.ball_corner1() is self.paddle:
    #         self.__dy = -self.__dy
    #     elif self.ball_corner1() is self.live:
    #         self.__dy = self.__dy
    #     elif self.ball_corner1() is self.score1:
    #         self.__dy = self.__dy
    #     elif self.ball_corner1() is not None:
    #         self.window.remove(self.ball_corner1())
    #         self.__dy = -self.__dy
    #
    # def ball_hit_things2(self):
    #     if self.ball_corner2() is self.paddle:
    #         self.__dy = -self.__dy
    #     elif self.ball_corner1() is self.live:
    #         self.__dy = self.__dy
    #     elif self.ball_corner1() is self.score1:
    #         self.__dy = self.__dy
    #     elif self.ball_corner2() is not None:
    #         self.window.remove(self.ball_corner2())
    #         self.__dy = -self.__dy
    #
    # def ball_hit_things3(self):
    #     if self.ball_corner3() is self.paddle:
    #         self.__dy = -self.__dy
    #     elif self.ball_corner1() is self.live:
    #         self.__dy = self.__dy
    #     elif self.ball_corner1() is self.score1:
    #         self.__dy = self.__dy
    #     elif self.ball_corner3() is not None:
    #         self.window.remove(self.ball_corner3())
    #         self.__dy = -self.__dy
    #
    # def ball_hit_things4(self):
    #     if self.ball_corner4() is self.paddle:
    #         self.__dy = -self.__dy
    #     elif self.ball_corner1() is self.live:
    #         self.__dy = self.__dy
    #     elif self.ball_corner1() is self.score1:
    #         self.__dy = self.__dy
    #     elif self.ball_corner4() is not None:
    #         self.window.remove(self.ball_corner4())
    #         self.__dy = -self.__dy


