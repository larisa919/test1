import wrap
width=500
height=500
x1=100
x2=450
y=200
wrap.world.create_world(width,height)
wrap.sprite.add("mario-items",30,y,"moving_platform1")
wrap.sprite.add("mario-items",width-30,y,"moving_platform1")
wrap.sprite.add("mario-items",x1,y,"moving_platform1")
wrap.sprite.add("mario-items",x2,y,"moving_platform1")
mario=wrap.sprite.add("mario-1-big",30,y-40,"stand")
wrap.actions.move(mario,x1/2-15,-x1/2+15)
wrap.actions.move(mario,x1/2-15,x1/2-15)
wrap.actions.move(mario,(x2-x1)/2,-(x2-x1)/2)
wrap.actions.move(mario,(x2-x1)/2,(x2-x1)/2)
wrap.actions.move(mario,(width-30-x2)/2,-(width-30-x2)/2)
wrap.actions.move(mario,(width-30-x2)/2,(width-30-x2)/2)