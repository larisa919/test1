import time, random
from wrap import world, sprite,sprite_text

world.create_world(400,600)
world.set_back_color(100,200,200)

x_star=random.randint(10,390)
y_star=random.randint(10,590)
start=time.time()
text_time=sprite.add_text("Time 0",30,30,text_color=(0,0,0))
text_count=sprite.add_text("Count 0",30,60,text_color=(0,0,0))

armadillo=sprite.add("mario-enemies",200,300,"armadillo_egg")
star=sprite.add("battle_city_items",x_star,y_star,"block_gift_star")
count=0
while True:
    sprite_text.set_text(text_time, "Time "+str(int(time.time() - start)))
    star_x=sprite.get_x(star)
    star_y = sprite.get_y(star)
    sprite.move_at_angle_point(armadillo,star_x,star_y,10)
    sprite.set_angle(armadillo,sprite.get_angle(armadillo)+10)
    if sprite.is_collide_sprite(armadillo,star):
        count+=1
        sprite_text.set_text(text_count, "Count "+str(count))
        sprite.remove(star)
        sprite.set_size_percent(armadillo,sprite.get_height_percent(armadillo)+10,sprite.get_width_percent(armadillo)+10)
        x_star = random.randint(10, 390)
        y_star = random.randint(10, 590)
        star = sprite.add("battle_city_items", x_star, y_star, "block_gift_star")
