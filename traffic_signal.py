import turtle
import random
import time

screen = turtle.Screen()
screen.title("Traffic Signal Simulation")
screen.bgcolor("lightgreen")
screen.setup(width=800, height=600)
screen.tracer(0)

def draw_road():

    road = turtle.Turtle()
    road.speed(0)
    road.hideturtle()
    road.penup()

    road.goto(-400, -100)
    road.pendown()

    road.color("black")
    road.begin_fill()

    for i in range(2):
        road.forward(800)
        road.left(90)
        road.forward(200)
        road.left(90)

    road.end_fill()

    road.color("white")
    road.penup()
    road.goto(-400, 0)
    road.pendown()

    for i in range(16):
        road.forward(30)
        road.penup()
        road.forward(20)
        road.pendown()

class TrafficSignal:

    def __init__(self):

        self.color = "red"

        self.signal_box = turtle.Turtle()
        self.signal_box.shape("square")
        self.signal_box.color("black")
        self.signal_box.shapesize(
            stretch_wid=4,
            stretch_len=2
        )
        self.signal_box.penup()
        self.signal_box.goto(200, 170)

        self.signal = turtle.Turtle()
        self.signal.shape("circle")
        self.signal.penup()
        self.signal.goto(200, 170)
        self.signal.shapesize(2)

        self.update_signal()

    def update_signal(self):
        self.signal.color(self.color)
    def change(self):
        if self.color == "red":
            self.color = "green"
        elif self.color == "green":
            self.color = "yellow"
        else:
            self.color = "red"
        self.update_signal()

class Car:
    total_cars = 0
    def __init__(self, x, y):
        Car.total_cars += 1
        self.car = turtle.Turtle()
        self.car.shape("square")
        self.car.color(
            random.choice(
                ["blue", "red", "white", "orange"]
            )
        )
        self.car.shapesize(
            stretch_wid=1,
            stretch_len=2
        )
        self.car.penup()
        self.car.goto(x, y)
        self.speed = random.randint(2, 5)

    def move(self, signal_color):
        if signal_color == "green":
            self.car.forward(self.speed)
        elif signal_color == "yellow":
            self.car.forward(1)
        else:
            pass
        if self.car.xcor() > 400:
            self.car.goto(
                -400,
                self.car.ycor()
            )
draw_road()
signal = TrafficSignal()
cars = []
for i in range(5):
    x = random.randint(-400, -100)
    y = random.randint(-70, 50)
    car = Car(x, y)
    cars.append(car)
count = 0
while True:
    for car in cars:
        car.move(signal.color)
    screen.update()
    time.sleep(0.03)
    count += 1
    if count == 100:
        signal.change()
    elif count == 200:
        signal.change()
    elif count == 300:
        signal.change()
        count = 0