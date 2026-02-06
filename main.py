import time
from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()





screen.listen()


screen.onkeypress(player.move,"Up")


# game_is_on = True
while car_manager.detect_collision(player) :

    car_manager.create_car()
    car_manager.move_cars()
    car_manager.delete_car()
    time.sleep(0.1)
    print(len(car_manager.cars))

    screen.update()



