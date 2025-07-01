import random
import wrap
width=600
height=600
wrap.world.create_world(width,height)
x=random.randint(0,width)
y=random.randint(0,height)
dot=wrap.sprite.add("pacman",x,y,"dot")
pacman=wrap.sprite.add("pacman",width/2,height/2,"player2")
a=random.randint(20,200)
wrap.sprite.set_size(pacman,a,a)
wrap.actions.set_angle_to_point(pacman,x,y)
wrap.actions.move_to(pacman,x,y)
enemy=wrap.sprite.add("pacman",x,y,"enemy_blue_down1")
z=wrap.sprite.get_top(pacman)
wrap.sprite.move_bottom_to(enemy,z)
b=wrap.sprite.get_top(enemy)
wrap.sprite.add_text("Ага,попался!",x,b-20,text_color=(100,100,100))
wrap.actions.set_angle_to_point(pacman,x,height)
wrap.sprite.remove(dot)
wrap.actions.move_at_angle(pacman,180,height,)