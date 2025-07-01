import wrap
width=400
height=600
x1=100
y1=200
x2=300
y2=400
x3=200
y3=134
wrap.world.create_world(width,height)
wrap.world.set_back_color(80,80,80)
wrap.sprite.add("pacman",18,18,"enemy_yellow_down1")
wrap.sprite.add("pacman",width-18,18,"enemy_blue_down1")
wrap.sprite.add("pacman",18,height-18,"enemy_pink_down1")
wrap.sprite.add("pacman",width-18,height-18,"enemy_red_down1")
a=wrap.sprite.add("pacman",x3,(y2+y1)/2,"player1")
wrap.sprite.add("pacman",x1,y1,"dot")
wrap.sprite.add("pacman",x2,y2,"dot")
wrap.sprite.add("pacman",x3,y3,"dot")
wrap.sprite.add_text("point 1",x1,y1-20,text_color=(0,0,0))
wrap.sprite.add_text("point 2",x2,y2-20,text_color=(0,0,0))
wrap.sprite.add_text("point 3",x3,y3-20,text_color=(0,0,0))
wrap.actions.move_to(a,x1,y1)
wrap.actions.move_to(a,x2,y2)
wrap.actions.move_to(a,x3,y3)