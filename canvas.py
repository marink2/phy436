import numpy as np
import vpython as vp

"""
------------------------------------------------------------------------------------
                                        setup
------------------------------------------------------------------------------------
"""

scene_main = vp.canvas(width=400, height=200, userzoom=False, userspan=False,
                       fov=0.001, userspin=False, autoscale=False, background=vp.color.black)

scene_main.append_to_caption("\n")

atom = vp.sphere(radius=0.4, color=vp.color.cyan, emissive=True)
lattice = vp.box(length=40, width=None, height=0.2)

"""
------------------------------------------------------------------------------------
                                        controls
------------------------------------------------------------------------------------
"""


def add_atom(s):
    wt.text = s.value


sl = vp.slider(min=1, max=12, value=1, step=1, bind=add_atom)

wt = vp.wtext(text=sl.value)

"""
------------------------------------------------------------------------------------
                                        animation
------------------------------------------------------------------------------------
"""

while True:
    vp.rate(100)
