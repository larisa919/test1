import random
import time
import wrap
import math

width = 400
height = 600
wrap.world.create_world(width, height)

duck_x=300
duck_y=500
duck=wrap.sprite.add("mario-enemies",duck_x,duck_y,"duck_blue_go")

mario_x=100
mario_y=100
mario=wrap.sprite.add("mario-1-big",mario_x,mario_y,"stand")

wrap.sprite.add("mario-items",mario_x,mario_y,"coin")

way=math.sqrt((duck_x-mario_x)**2+(duck_y-mario_y)**2)
time.sleep(1)
wrap.actions.move_at_angle_point(mario,duck_x,duck_y,way/4)

mario_x_1=wrap.sprite.get_x(mario)
mario_y_1=wrap.sprite.get_y(mario)
wrap.sprite.add("mario-items",mario_x_1,mario_y_1,"coin")

time.sleep(1)
wrap.actions.move_at_angle_point(mario,duck_x,duck_y,way/4)
mario_x_2=wrap.sprite.get_x(mario)
mario_y_2=wrap.sprite.get_y(mario)
wrap.sprite.add("mario-items",mario_x_2,mario_y_2,"coin")

time.sleep(1)
wrap.actions.move_at_angle_point(mario,duck_x,duck_y,way/4)
mario_x_3=wrap.sprite.get_x(mario)
mario_y_3=wrap.sprite.get_y(mario)
wrap.sprite.add("mario-items",mario_x_3,mario_y_3,"coin")

time.sleep(1)
wrap.actions.move_at_angle_point(mario,duck_x,duck_y,way/4)
mario_x_4=wrap.sprite.get_x(mario)
mario_y_4=wrap.sprite.get_y(mario)
wrap.sprite.add("mario-items",mario_x_4,mario_y_4,"coin")
wrap.sprite.remove(duck)
