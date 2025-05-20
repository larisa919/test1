import time

import wrap
wrap.world.create_world(500,600)
wrap.sprite.add("pacman",200,300,"enemy_blue_left1")
wrap.actions.move_to(0,250,500)
wrap.sprite.add("mario-3-big",100,100)
time.sleep(1.5)
wrap.world.set_back_color(51,108,163)
wrap.sprite.add_text("привет,привидение",200,100,text_color=(255,255,255))
wrap.actions.move_to(0,400,200)
wrap.sprite.add_text("привет,марио",200,200)
time.sleep(1.5)
wrap.sprite.add_text ("хочешь яблоко?",200,300,text_color=(255,0,0))
