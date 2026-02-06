COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random as r


class CarManager():

    def __init__(self):
        self.cars = []



    def create_car(self):
        if r.randint(1,6) ==1:

            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(r.choice(COLORS))
            car.penup()
            car.goto(300, r.randint(-250, 250))

            self.cars.append(car)


    def delete_car(self):
        for car in self.cars:
            if car.xcor() <-320:
                self.cars.remove(car)


    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def detect_collision(self,player):
        for car in self.cars:
            if car.distance(player) < 15:
                return False
        return True
