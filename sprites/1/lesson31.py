import wrap

from wrap import world, sprite, sprite_text, actions

wrap.world.create_world(600,600)
pacman=sprite.add("pacman", 100, 100, "enemy_blue_left2")
mario=sprite.add("mario-1-big", 200, 200, "stand")
dragon=sprite.add("mario-enemies", 300, 300, "dragon_stand1")

@wrap.on_key_down(wrap.K_UP,wrap.K_DOWN)
def a(pos_x, pos_y, key):

    if wrap.sprite.is_collide_point(pacman, pos_x, pos_y):
        personaz=pacman
    elif wrap.sprite.is_collide_point(mario, pos_x, pos_y):
        personaz = mario
    elif wrap.sprite.is_collide_point(dragon, pos_x, pos_y):
        personaz = dragon
    else:
        personaz = None
    if personaz==None:
        return

    if wrap.K_UP==key:
        wrap.sprite.set_costume_next(personaz)
    elif wrap.K_DOWN==key:
        wrap.sprite.set_costume_prev(personaz)


@wrap.on_key_down(wrap.K_LEFT, wrap.K_RIGHT)
def a(pos_x, pos_y, key):
    if wrap.sprite.is_collide_point(pacman, pos_x, pos_y):
        personaz = pacman
    elif wrap.sprite.is_collide_point(mario, pos_x, pos_y):
        personaz = mario
    elif wrap.sprite.is_collide_point(dragon, pos_x, pos_y):
        personaz = dragon
    else:
        personaz = None
    if personaz == None:
        return

    if wrap.K_LEFT == key:
        wrap.sprite.set_angle(personaz,wrap.sprite.get_angle(personaz)-10)
    elif wrap.K_RIGHT == key:
        wrap.sprite.set_angle(personaz,wrap.sprite.get_angle(personaz)+10)


