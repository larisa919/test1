import time, random
from wrap import world, sprite

world.create_world(400,600)
world.set_back_color(100,200,200)

x_star=random.randint(10,390)
y_star=random.randint(10,590)

armadillo=sprite.add("mario-enemies",200,300,"armadillo_egg")
star=sprite.add("battle_city_items",x_star,y_star,"block_gift_star")

while True:
    star_x=sprite.get_x(star)
    star_y = sprite.get_y(star)
    sprite.move_at_angle_point(armadillo,star_x,star_y,5)
    sprite.set_angle(armadillo,sprite.get_angle(armadillo)+10)
    if sprite.is_collide_sprite(armadillo,star):
        sprite.remove(star)
        x_star = random.randint(10, 390)
        y_star = random.randint(10, 590)
        star = sprite.add("battle_city_items", x_star, y_star, "block_gift_star")
