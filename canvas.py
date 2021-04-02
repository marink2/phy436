import vpython as vp

scene_main = vp.canvas(width=600, height=600, userzoom=False, userspan=False, userspin=False, autoscale=False)
atom = vp.sphere(radius=0.2, color=vp.color.red)
vp.box(height=0.1, width=None, length=100)
