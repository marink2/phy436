import numpy as np
import vpython as vp

"""
------------------------------------------------------------------------------------
                                        setup
------------------------------------------------------------------------------------
"""

scene_main = vp.canvas(width=600, height=200, userzoom=False, userspan=False,
                       fov=0.001, userspin=False, autoscale=False, background=vp.color.black)

scene_main.append_to_caption("\n")

atom = [vp.sphere(radius=0.4, color=vp.color.cyan, emissive=True)]
for i in range(1, 14):
    atom.append(vp.sphere(pos=vp.vector(4 * i, 0, 0), radius=0.4, color=vp.color.cyan, emissive=True, visible=False))

lattice_1 = vp.box(pos=vp.vector(0, 5, 0), length=60, width=None, height=0.2)
lattice_2 = vp.box(length=60, width=None, height=0.2)
lattice_3 = vp.box(pos=vp.vector(0, -5, 0), length=60, width=None, height=0.2)

"""
------------------------------------------------------------------------------------
                                        controls
------------------------------------------------------------------------------------
"""


def add_atom(s):
    wt.text = s.value

    for i in range(14):
        atom[i].visible = False

    atom[0].pos.x = 2 - 2 * s.value
    for j in range(1, 14):
        atom[j].pos.x = atom[0].pos.x + 4 * j

    for i in range(s.value):
        atom[i].visible = True


sl = vp.slider(min=1, max=14, value=1, step=1, bind=add_atom)
wt = vp.wtext(text=sl.value)
scene_main.append_to_caption(" atoms")

"""
------------------------------------------------------------------------------------
                                        animation
------------------------------------------------------------------------------------
"""
x = 0
while True:
    vp.rate(50)
    for i in range(14):
        atom[i].pos.y = 2 * np.sin(i + 2 * x * np.pi)

    x = x + 0.01
    if x == 2:
        x = 0
