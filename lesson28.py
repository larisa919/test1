import wrap

wrap.world.create_world(600, 600)
pacman = wrap.sprite.add("pacman", 300, 300, "player2")
prividenie=wrap.sprite.add("pacman",100,100,"enemy_ill_blue2",False)

@wrap.on_key_always(wrap.K_UP,delay=10)
def left():
    wrap.sprite.move_at_angle_dir(pacman,3)


@wrap.on_key_down(wrap.K_RIGHT,wrap.K_LEFT)
def right(key):
    print(key)
    angle = wrap.sprite.get_angle(pacman)
    if key==wrap.K_RIGHT:
        wrap.sprite.set_angle(pacman,angle+15)
    else:wrap.sprite.set_angle(pacman,angle-15)

@wrap.on_mouse_move
def move(pos_x,pos_y):
    # print(pos_x,pos_y)
    wrap.sprite.move_to(prividenie,pos_x,pos_y)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def show():
    wrap.sprite.show(prividenie)

@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def up():
    wrap.sprite.hide(prividenie)

@wrap.always(30)
def a ():
    if wrap.sprite.is_visible(prividenie):
        wrap.sprite.set_angle_to_point(pacman,wrap.sprite.get_x(prividenie),wrap.sprite.get_y(prividenie))
        wrap.sprite.move_at_angle_point(pacman,wrap.sprite.get_x(prividenie),wrap.sprite.get_y(prividenie),7)
        print(wrap.sprite.get_x(pacman),wrap.sprite.get_y(pacman))


