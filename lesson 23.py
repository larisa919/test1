import wrap,time
wrap.add_sprite_dir("sprites")
wrap.world.create_world(400,600)
mario=wrap.sprite.add("mario-1-big",350,200,"stand")
dragon=wrap.sprite.add("mario-enemies",50,200,"dragon_stand1")
wrap.sprite.set_reverse_x(mario,True)
wrap.sprite.set_reverse_x(dragon,True)
a=3
speed_y=a
start=time.time()
text=wrap.sprite.add_text("0",200,30,text_color=(255,255,255))
while True:
    wrap.sprite.move(dragon,0,speed_y)

    if wrap.sprite.get_bottom(dragon)>=600:
        speed_y=-a
    if wrap.sprite.get_top(dragon)<=0:
        speed_y=a

    d=str(int(time.time()-start))
    wrap.sprite_text.set_text(text,d)
    y_dragon=wrap.sprite.get_y(dragon)

    korzina=wrap.sprite.add("1",50,y_dragon,"korzina2",visible=False)
    wrap.sprite.set_size(korzina,20,20)
    wrap.sprite.show(korzina)