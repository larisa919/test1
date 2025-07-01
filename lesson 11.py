import random
import wrap

width = 600
height = 600
wrap.world.create_world(width, height)

x = random.randint(0, width)
y = random.randint(0, height)
dot = wrap.sprite.add("pacman", x, y, "dot")

pacman = wrap.sprite.add("pacman", width / 2, height / 2, "player2")
size = random.randint(20, 200)
wrap.sprite.set_size(pacman, size, size)
wrap.actions.set_angle_to_point(pacman, x, y)
wrap.actions.move_to(pacman, x, y)
wrap.sprite.remove(dot)

d = random.randint(x - 50, x + 50)
enemy = wrap.sprite.add("pacman", d, y, "enemy_blue_down1")
z = wrap.sprite.get_top(pacman)
wrap.sprite.move_bottom_to(enemy, z)

b = wrap.sprite.get_top(enemy)
wrap.sprite.add_text("Ага,попался!", d, b - 20, text_color=(100, 100, 100))

enemy_y=wrap.sprite.get_centery(enemy)
wrap.actions.set_angle_to_point(pacman,d,enemy_y)
angle=wrap.sprite.get_angle(pacman)
wrap.actions.set_angle(pacman,angle+180)
wrap.actions.move_at_angle_dir(pacman,300)
