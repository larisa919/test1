import wrap,time
wrap.add_sprite_dir("sprites")
wrap.world.create_world(400,600)

mario=wrap.sprite.add("mario-1-big",350,200,"stand")
dragon=wrap.sprite.add("mario-enemies",50,200,"dragon_stand1")
wrap.sprite.set_reverse_x(mario,True)
wrap.sprite.set_reverse_x(dragon,True)
korzina=None
a=3
z=-2
speed_dragon=a
speed_mario=z
start=time.time()
x = time.time()
text=wrap.sprite.add_text("0",200,30,text_color=(255,255,255))
while True:
    wrap.sprite.move(dragon,0,speed_dragon)
    if wrap.sprite.get_bottom(dragon)>=600:
        speed_dragon=-a
    if wrap.sprite.get_top(dragon)<=0:
        speed_dragon=a

    wrap.sprite.move(mario, 0, speed_mario)
    if wrap.sprite.get_bottom(mario) >= 600:
        speed_mario = z
    if wrap.sprite.get_top(mario) <= 0:
        speed_mario = -z

    e=(time.time()-start)
    c=int(e)
    d=str(c)
    wrap.sprite_text.set_text(text,d)
    y_dragon=wrap.sprite.get_y(dragon)
    shot_time = (time.time() - x)
    k = (350 - 50) / 10
    if shot_time >= 5:
        korzina=wrap.sprite.add("1",80,y_dragon,"korzina2",visible=False)
        wrap.sprite.set_size(korzina,20,20)
        wrap.sprite.show(korzina)
        y_mario = wrap.sprite.get_y(mario)
        x=time.time()
    if korzina!=None:
        y_korzina=(y_mario-y_dragon)/k
        wrap.sprite.move(korzina,10,y_korzina,)
        wrap.sprite.set_angle(korzina,wrap.sprite.get_angle(korzina)+10)
        if wrap.sprite.is_collide_sprite(korzina,mario):
            break
while True:
    wrap.sprite.move(mario,0,10)
    wrap.sprite.set_angle(mario,wrap.sprite.get_angle(mario)+20)
