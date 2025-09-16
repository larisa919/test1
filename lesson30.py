import wrap
wrap.add_sprite_dir("sprites")
wrap.world.create_world(600,600)
wrap.world.set_back_color(100,200,200)

def personaz(x,y,costume,width_percent,height_percent):
    vorota = wrap.sprite.add("1",x,y, costume,False)
    wrap.sprite.set_size_percent(vorota, width_percent,height_percent)
    wrap.sprite.show(vorota)
    return vorota

vorota=personaz(300,0,"vorota",10,10)
vorota_2=personaz(300,600,"vorota",10,10)
ball=personaz(500,400,"ball",8,8)
player_1=personaz(100,100,"Fotoram.io",13,13)
player_2=personaz(400,400,"Fotoram.io",13,13)

wrap.sprite.set_reverse_x(player_2,True)
x=wrap.sprite.get_x(ball)
y=wrap.sprite.get_top(ball)
def pas(player,player2):
    wrap.actions.move_to(player, x, y, 2000)
    if wrap.sprite.is_collide_sprite(player,ball):
        wrap.actions.move_to(ball,wrap.sprite.get_left(player2),wrap.sprite.get_bottom(player2),2000)

def goal(vorota):
    wrap.actions.move_to(ball, wrap.sprite.get_centerx(vorota), wrap.sprite.get_centery(vorota), 2000)
    if wrap.sprite.is_collide_sprite(ball,vorota):
        wrap.sprite.add_text("ГООООЛ!!!!",300,500)

def out(player,player2):
    wrap.actions.move_to(player,x, y, 2000)
    if wrap.sprite.is_collide_sprite(player,ball):
        wrap.actions.move_at_angle_point(ball,wrap.sprite.get_x(player2)-50,wrap.sprite.get_top(player2)-50,600,2000)
        wrap.sprite.add_text("АУТ", 300, 500)
out(player_2,player_1)

