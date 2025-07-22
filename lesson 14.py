import random
import time
import wrap
import math
c=math.sqrt(int("62"+str(int("1")+2**2)))+25
print(c)
width = 400
height = 600
wrap.world.create_world(width, height)

klad_x = random.randint(0, width)
klad_y = random.randint(300, height)

star=wrap.sprite.add("mario-items", klad_x, klad_y, "star",False)

mario_x=100
mario_y=100
mario=wrap.sprite.add("mario-1-big",mario_x,mario_y,"stand")
wrap.sprite.add("pacman",mario_x,mario_y,"dot")
way=math.sqrt((klad_x - mario_x) ** 2 + (klad_y - mario_y) ** 2)
a=str(int(way))
wrap.sprite.add_text("до клада "+a+" px",mario_x,mario_y-20,text_color=[255,255,255])
wrap.actions.set_angle_to_point(mario,klad_x,klad_y)
mario_x2=int(input("введите x клада"))
mario_y2=int(input("введите y клада"))
wrap.actions.move_to(mario,mario_x2,mario_y2)

# klad_x = random.randint(0, width)
# klad_y = random.randint(0, height)
# wrap.sprite.add("mario-items", klad_x, klad_y, "star",False)

wrap.sprite.add("pacman",mario_x2,mario_y2,"dot")
way=math.sqrt((klad_x - mario_x2) ** 2 + (klad_y - mario_y2) ** 2)
a=str(int(way))
wrap.sprite.add_text("до клада "+a+" px",mario_x2,mario_y2-20,text_color=[255,255,255])
wrap.actions.set_angle_to_point(mario,klad_x,klad_y)
mario_x3=int(input("введите x клада"))
mario_y3=int(input("введите y клада"))
wrap.actions.move_to(mario,mario_x3,mario_y3)

# klad_x = random.randint(0, width)
# klad_y = random.randint(0, height)
# star=wrap.sprite.add("mario-items", klad_x, klad_y, "star",False)

wrap.sprite.add("pacman",mario_x2,mario_y2,"dot")
way=math.sqrt((klad_x - mario_x3) ** 2 + (klad_y - mario_y3) ** 2)
a=str(int(way))
wrap.sprite.add_text("до клада "+a+" px",mario_x3,mario_y3-20,text_color=[255,255,255])
wrap.actions.set_angle_to_point(mario,klad_x,klad_y)
mario_x4=int(input("введите x клада"))
mario_y4=int(input("введите y клада"))
wrap.actions.move_to(mario,mario_x4,mario_y4)
wrap.sprite.show(star)
