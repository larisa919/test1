import time
from wrap import world, sprite, sprite_text, actions
world.create_world(600,600)

def appear(personaz):
    star=sprite.add("battle_city_items",sprite.get_x(personaz),sprite.get_y(personaz),"effect_appearance_player1")
    time.sleep(0.2)
    sprite.set_costume(star,"effect_appearance_player2")
    time.sleep(0.2)
    sprite.set_costume(star,"effect_appearance_player1")
    time.sleep(0.2)
    sprite.set_costume(star, "effect_appearance_player2")
    time.sleep(0.2)
    sprite.set_costume(star, "effect_appearance_player1")
    sprite.remove(star)
    sprite.show(personaz)

def move_left(personaz,x_left):
    sprite.set_angle(personaz,-90)
    if sprite.get_x(personaz)>x_left:
        actions.move(personaz,-x_left,0)
    else:actions.move(personaz,-sprite.get_x(personaz),0)

def move_down(personaz,y_down):
    sprite.set_angle(personaz,-180)
    if 600-sprite.get_y(personaz)>y_down:
        actions.move(personaz,0,y_down)
    else:actions.move(personaz,0,600-sprite.get_y(personaz))

def move_right(personaz,x_right):
    sprite.set_angle(personaz,90)
    if 600-sprite.get_x(personaz)>x_right:
        actions.move(personaz,x_right,0)
    else:actions.move(personaz,600-sprite.get_x(personaz),0)


def move_up(personaz, y_up):
    sprite.set_angle(personaz, 0)
    if sprite.get_y(personaz)>y_up:
        actions.move(personaz, 0, -y_up)
    else:actions.move(personaz,0,-sprite.get_y(personaz))

def polet_puli(personaz1,personaz2):
    bullet = sprite.add("battle_city_items", sprite.get_centerx(personaz1), sprite.get_centery(personaz1), "bullet")
    sprite.set_angle(bullet,sprite.get_angle(personaz1))
    while True:
        sprite.move_at_angle(bullet,sprite.get_angle(personaz1),10)
        if sprite.is_collide_sprite(bullet,personaz2):
            star = sprite.add("battle_city_items", sprite.get_x(personaz2), sprite.get_y(personaz2),"effect_appearance_player1",False)
            sprite.remove(personaz2)
            sprite.remove(bullet)
            sprite.show(star)
            time.sleep(0.2)
            sprite.set_costume(star, "effect_appearance_player2")
            time.sleep(0.2)
            sprite.set_costume(star, "effect_appearance_player1")
            time.sleep(0.2)
            sprite.set_costume(star, "effect_appearance_player2")
            time.sleep(0.2)
            sprite.set_costume(star, "effect_appearance_player1")
            sprite.remove(star)




tank1 = sprite.add("battle_city_tanks", 100, 100, "tank_player_size1_green1", False)
tank2 = sprite.add("battle_city_tanks", 200, 300, "tank_player_size1_yellow1", False)


appear(tank1)
appear(tank2)
#
move_left(tank1, 70)
move_left(tank2, 170)
move_down(tank1, 100)
polet_puli(tank1,tank2)
move_right(tank2, 50)
polet_puli(tank2,tank1)
move_up(tank2, 50)
polet_puli(tank2,tank1)