import random
import wrap

width = 600
height = 600
wrap.world.create_world(width, height)

x = random.randint(0, width)
y = random.randint(0, height)
enemy = wrap.sprite.add("pacman", x, y, "enemy_blue_down1")

a= random.randint(0, width)
b= random.randint(0, height)
dot = wrap.sprite.add("pacman", a, b, "dot")

if x>a:
    wrap.sprite.set_costume(enemy,"enemy_blue_left1")
else:
    wrap.sprite.set_costume(enemy, "enemy_blue_right1")
wrap.actions.move_to(enemy,a,y)

if y>b:
    wrap.sprite.set_costume(enemy, "enemy_blue_up1")
else:
    wrap.sprite.set_costume(enemy, "enemy_blue_down1")
wrap.actions.move_to(enemy,a,b)
