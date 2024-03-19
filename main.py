import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint as r

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# initiate player
player = Player()

# initiate scoreboard
level = 1
scoreboard = Scoreboard()
scoreboard.mark_score(level)

# initiate cars
cars = []
cars.append(CarManager())
car_timer = 0
next_car = 0
car_increment = 15

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    for car in cars:
        car.move()
        if car.xcor() < -320:
            car.hideturtle()
            cars.remove(car)
        if car.distance(player) < 30 and player.ycor() < car.ycor() + 15 and player.ycor() > car.ycor() - 25:
            game_is_on = False
            game_over = Scoreboard()
            game_over.game_over()
            break

    if next_car == car_timer:
        cars.append(CarManager())
        car_timer = 0
        next_car = r(1, car_increment)
    if player.check_score():
        level += 1
        scoreboard.mark_score(level)
        cars[0].new_level()
        if car_increment > 3:
            car_increment -= 3
        elif car_increment > 1:
            car_increment -= 2
    time.sleep(0.1)
    screen.update()
    car_timer += 1

screen.exitonclick()
