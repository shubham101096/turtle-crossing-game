from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.add_car()
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_car(self):
        car = Turtle(shape="square")
        car.color(random.choice(COLORS))
        car.shapesize(1, 2)
        car.penup()
        car.goto(280, random.randint(-250, 250))
        car.setheading(180)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)
            else:
                car.forward(self.move_distance)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT

