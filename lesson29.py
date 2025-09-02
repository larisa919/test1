import wrap
import random

wrap.world.create_world(600,600)
tank=wrap.sprite.add("battle_city_tanks",300,300,"tank_enemy_size1_green1")
@wrap.always(2000)
def move_tank ():
    x = random.randint(0, 600)
    y = random.randint(0, 600)
    wrap.sprite.move_to(tank,x,y)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def a (pos_x,pos_y):
    if wrap.sprite.is_collide_point(tank,pos_x,pos_y):
        wrap.sprite.set_costume_next(tank)