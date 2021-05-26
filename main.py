import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, key="Up")

game_is_on = True
counter = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    counter += 1
    if counter == 6:
        car_manager.add_car()
        counter = 0

    car_manager.move()

    if player.ycor() >= FINISH_LINE_Y:
        player.start()
        score.update()
        car_manager.speed_up()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()