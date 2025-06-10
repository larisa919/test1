import wrap
width=500
height=500
wrap.world.create_world(width,height)
wrap.sprite.add("pacman",0,0,"enemy_red_down1")
wrap.sprite.add("pacman",width,0,"enemy_blue_down1")
wrap.sprite.add("pacman",0,height,"enemy_pink_down1")
wrap.sprite.add("pacman",width,height,"enemy_red_down1")
wrap.sprite.add("pacman",width/2,height/2,"enemy_red_down1")

