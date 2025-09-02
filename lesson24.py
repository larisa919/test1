import time

from wrap import world, sprite, sprite_text, actions
def skazi(nazvanie,personaz,):
    text = sprite.add_text(nazvanie, sprite.get_x(personaz), sprite.get_top(personaz) - 20)
    time.sleep(0.5)
    sprite.remove(text)
def pogonya():
    #погоня
    skazi("Погоня!",hunter)
    actions.move_at_angle_point(hunter, sprite.get_x(victim), sprite.get_y(victim), 70, 500)

def pobeg(angle):
    #побег
    skazi("Бежим",victim)
    actions.set_size_percent(victim, 30, 30, 500)
    actions.set_angle(victim, angle, 500)
    actions.move_at_angle_dir(victim, 100, 600)
    actions.set_size_percent(victim, 100, 100, 500)

world.create_world(400, 600, 900, 50)
world.set_back_color(100, 200, 200)

victim = sprite.add("pacman", 300, 100, "player2")
hunter = sprite.add("pacman", 100, 100, "enemy_blue_right1")

pobeg(180)

pogonya()

pobeg(135)

pogonya()