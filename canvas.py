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
    wt_a.text = s.value

    for i in range(14):
        atom[i].visible = False

    for j in range(0, 14):
        atom[j].pos.x = (2 - 2 * s.value) + 4 * j

    for i in range(s.value):
        atom[i].visible = True


sl_a = vp.slider(min=1, max=14, value=1, step=1, bind=add_atom)
wt_a = vp.wtext(text=sl_a.value)
scene_main.append_to_caption(" atoms\n\n")


def spring(s):
    wt_k.text = s.value


sl_k = vp.slider(min=0, max=10, value=0, step=0.1, bind=spring)
wt_k = vp.wtext(text=sl_k.value)
scene_main.append_to_caption("k N/m\n\n")

"""
------------------------------------------------------------------------------------
                                        animation
------------------------------------------------------------------------------------
"""

# Mouse stuff

x = np.pi/2
while True:
    vp.rate(50)
    for i in range(14):
        atom[i].pos.x = atom[i].pos.x + 0.01 * np.sin(x + i)

    x = x + 0.01
    if x == 2:
        x = 0
