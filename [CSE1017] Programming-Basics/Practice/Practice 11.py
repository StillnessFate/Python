from tkinter import *
import math

def distance(x1, y1, x2, y2) : # 두점간의 거리를 구하는 function
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def intersect(A, B, C, D) : # 직선 교차 체크
    def ccw(A, B, C) :
        return ((C[1] - A[1]) * (B[0] - A[0])) > ((B[1] - A[1]) * (C[0] - A[0]))
    return (ccw(A, C, D) != ccw(B, C, D)) and (ccw(A, B, C) != ccw(A, B, D))

class Box :
    def __init__(self, size) :
        self.size = size
        
    def in_horizontal_contact(self, x) :
        return (x <= 0) or (x >= self.size)
        
    def in_vertical_contact(self, y) :
        return (y <= 0) or (y >= self.size)
        
class BlueBox:
    def __init__(self, x, y, size) :
        self.size = size
        self.x = x
        self.y = y
        
    def in_contact(self, x, y):
        return (self.x <= x <= self.x + self.size) and (self.y <= y <= self.y + self.size)
        
class MovingBall:
    def __init__(self, x, y, xv, yv, color, size, box, blue_box) :
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.color = color
        self.size = size
        self.box = box
        self.blue_box = blue_box
        
    def move(self, time_unit) :
        previous_x, previous_y = self.x, self.y
        self.x = self.x + (self.xv * time_unit)
        if self.box.in_horizontal_contact(self.x) :
            self.xv = -self.xv
        self.y = self.y + (self.yv * time_unit)
        if self.box.in_vertical_contact(self.y) :
            self.yv = -self.yv     

        if self.blue_box.in_contact(self.x, self.y) :
            self.set_bounce_velocity(previous_x, previous_y)

    def set_bounce_velocity(self, previous_x, previous_y) :
        if intersect((previous_x, previous_y), (self.x, self.y), (self.blue_box.x, self.blue_box.y), (self.blue_box.x, self.blue_box.y + self.blue_box.size)) or \
            intersect((previous_x, previous_y), (self.x, self.y), (self.blue_box.x, self.blue_box.y), (self.blue_box.x, self.blue_box.y + self.blue_box.size)) :
            self.xv = -self.xv

        if intersect((previous_x, previous_y), (self.x, self.y), (self.blue_box.x, self.blue_box.y), (self.blue_box.x + self.blue_box.size, self.blue_box.y + self.blue_box.size)) or \
            intersect((previous_x, previous_y), (self.x, self.y), (self.blue_box.x, self.blue_box.y + self.blue_box.size), (self.blue_box.x + self.blue_box.size, self.blue_box.y + self.blue_box.size)) :
            self.yv = -self.yv
            
class AnimationWriter:
    def __init__(self, root, balls, box, blue_box):
        size = box.size
        self.canvas = Canvas(root, width=size, height=size)
        self.canvas.grid()
        self.balls = balls
        self.box = box
        self.blue_box = blue_box
            
    def animate(self) :
        self.canvas.delete(ALL)
        for ball in self.balls :
            ball.move(1)
            self.check_ball_collision(ball)
            x = ball.x
            y = ball.y
            d = ball.size
            c = ball.color
            self.canvas.create_oval(x - d, y - d, x + d, y + d, outline=c, fill=c)
        
        self.canvas.create_rectangle(self.blue_box.x, self.blue_box.y, self.blue_box.x + self.blue_box.size, self.blue_box.y + self.blue_box.size, outline='blue', fill='blue')
        self.canvas.after(5, self.animate)


    def check_ball_collision(self, ball) :
        for x in self.balls :
            if x != ball :
                if distance(ball.x, ball.y, x.x, x.y) < ball.size :
                    ball.xv = -ball.xv
                    ball.yv = -ball.yv
                    break

class BounceController:
    def __init__(self) :
        box_size = 400
        ball_size = 10
        root = Tk()
        root.title("Bouncing Ball")
        root.geometry(str(box_size + 10) + 'x' + str(box_size + 10))

        box = Box(box_size)
        blue_box = BlueBox(((box_size+10) // 2) - (ball_size * 2), ((box_size+10) // 2) - (ball_size * 2), ball_size * 4)
        
        x_velocity, y_velocity = 5, 2
        ball_color = 'red'
        ball1 = MovingBall(box_size//3, box_size//5, x_velocity, y_velocity, ball_color, ball_size, box, blue_box)
        ball_color = 'green'
        x_velocity, y_velocity = 1, 4
        ball2 = MovingBall(box_size//4, box_size//5, x_velocity, y_velocity, ball_color, ball_size, box, blue_box)

        balls = [ball1, ball2]
        AnimationWriter(root, balls, box, blue_box).animate()
        root.mainloop()
    
BounceController()


