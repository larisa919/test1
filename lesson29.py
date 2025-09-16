import wrap
import random

wrap.world.create_world(600, 600)
tank = wrap.sprite.add("battle_city_tanks", 300, 300, "tank_enemy_size1_green1")
pacman = wrap.sprite.add("pacman", 200, 200, "player2", False)
wrap.sprite.set_size_percent(pacman, 50, 50)
wrap.sprite.set_angle(pacman, 0)


@wrap.always(40000)
def move_tank():
    x = random.randint(0, 600)
    y = random.randint(0, 600)
    wrap.sprite.move_to(tank, x, y)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def a(pos_x, pos_y):
    popali_pricelom=wrap.sprite.is_collide_sprite(pacman, tank) and wrap.sprite.is_visible(pacman)
    popali_mishyu=wrap.sprite.is_collide_point(tank, pos_x, pos_y)
    if popali_mishyu or popali_pricelom:
        wrap.sprite.set_costume_next(tank)


@wrap.on_key_down(wrap.K_UP)
def up():
    if wrap.sprite.get_height_percent(pacman) == 50 and wrap.sprite.is_visible(pacman) == False:
        wrap.sprite.show(pacman)
    elif wrap.sprite.get_height_percent(pacman) == 50 and wrap.sprite.is_visible(pacman) == True:
        wrap.sprite.set_size_percent(pacman, 100, 100)
    elif wrap.sprite.get_height_percent(pacman) == 100:
        wrap.sprite.set_size_percent(pacman, 200, 200)
    elif wrap.sprite.get_height_percent(pacman) == 200:
        wrap.sprite.set_size_percent(pacman, 50, 50)
        wrap.sprite.hide(pacman)


@wrap.on_mouse_move()
def move(pos_x, pos_y):
    wrap.sprite.move_to(pacman, pos_x, pos_y)
