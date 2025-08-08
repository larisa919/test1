import wrap,time
wrap.world.create_world(400,600)
mario=wrap.sprite.add("mario-1-big",350,200,"stand")
dragon=wrap.sprite.add("mario-enemies",50,200,"dragon_stand1")
wrap.sprite.set_reverse_x(mario,True)
wrap.sprite.set_reverse_x(dragon,True)
a=3
speed_y=a
while True:
    wrap.sprite.move(dragon,0,speed_y)
    print(wrap.sprite.get_bottom(dragon))
    if wrap.sprite.get_bottom(dragon)>=600:
        speed_y=-a
    if wrap.sprite.get_top(dragon)<=0:
        speed_y=a
