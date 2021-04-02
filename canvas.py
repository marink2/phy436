import vpython as vp

"""
------------------------------------------------------------------------------------
                                        setup
------------------------------------------------------------------------------------
"""

scene_main = vp.canvas(center=vp.vector(12, 0, 0), width=1350, height=640, userzoom=False, userspan=False,
                       fov=0.001, userspin=False, autoscale=False, background=vp.color.gray(0.95))

container = vp.box(pos=vp.vector(0, 0, -2), length=20, width=1, height=20, color=vp.color.black, emissive=True)
divider_1 = vp.box(pos=vp.vector(0, 3.5, -1), length=20, width=0.1, height=0.1, color=vp.color.gray(0.95), emissive=True)
divider_2 = vp.box(pos=vp.vector(0, -3.5, -1), length=20, width=0.1, height=0.1, color=vp.color.gray(0.95), emissive=True)

atom = vp.sphere(pos=vp.vector(0, 7, 0), radius=0.2, color=vp.color.cyan, emissive=True)
lattice = vp.box(pos=vp.vector(0, 7, 0), length=20, width=None, height=0.1)

"""
------------------------------------------------------------------------------------
                                        controls
------------------------------------------------------------------------------------
"""


"""
------------------------------------------------------------------------------------
                                        animation
------------------------------------------------------------------------------------
"""


