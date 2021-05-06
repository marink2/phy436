import vpython as vp
import numpy as np

"""
------------------------------------------------------------------------------------
                                        Parameter Values
------------------------------------------------------------------------------------
"""

K_initial = 4
K = 0.1
A_initial = 2
A = 0.1
a = 4
N = 1                       # is half the number of atoms in the chain
k_initial = np.pi / a
k = 0
k_int_val = 0
M_initial = 2
M = 0.1
m_initial = 2
R_initial = 0.4
R = 0.4
r_initial = 0.4
r = 0.4
m = 0.1
t = 0

"""
------------------------------------------------------------------------------------
                                        Setup
------------------------------------------------------------------------------------
"""

scene_main = vp.canvas(width=600, height=200, userzoom=True, userspan=False,
                       fov=0.001, userspin=False, autoscale=False, background=vp.color.black)

scene_main.append_to_caption("\n")

atom = [vp.sphere(pos=vp.vector(0, 3, 0), radius=R, color=vp.color.cyan, emissive=True)]
pos_x_initial = [0]
phase = [vp.sphere(pos=vp.vector(0, -3, 0), radius=0.4, color=vp.color.white, emissive=True)]
for i in range(1, 14):
    if i == 1:
        atom.append(vp.sphere(pos=vp.vector(a * i, 3, 0), radius=R, color=vp.color.cyan, emissive=True, visible=True))
        phase.append(vp.sphere(pos=vp.vector(a * i, -3, 0), radius=0.4, color=vp.color.white, emissive=True, visible=True))

    else:
        atom.append(vp.sphere(pos=vp.vector(a * i, 3, 0), radius=R, color=vp.color.cyan, emissive=True, visible=False))
        phase.append(vp.sphere(pos=vp.vector(a * i, -3, 0), radius=0.4, color=vp.color.white, emissive=True, visible=False))

    pos_x_initial.append(a * i)


atom2 = [vp.sphere(pos=vp.vector(0.5 * a, 3, 0), radius=r, color=vp.color.red, emissive=True, visible=False)]
pos2_x_initial = [0.5 * a]
phase2 = [vp.sphere(pos=vp.vector(0.5 * a, -3, 0), radius=0.4, color=vp.color.white, emissive=True, visible=False)]
for i in range(1, 14):
    atom2.append(vp.sphere(pos=vp.vector((a * i) + (0.5 * a), 3, 0), radius=r, color=vp.color.red, emissive=True, visible=False))
    phase2.append(vp.sphere(pos=vp.vector((a * i) + (0.5 * a), -3, 0), radius=0.4, color=vp.color.white, emissive=True, visible=False))
    pos2_x_initial.append((a * i) + (0.5 * a))

lattice_1 = vp.box(pos=vp.vector(0, 3, 0), length=6000, width=None, height=0.2)
lattice_2 = vp.box(pos=vp.vector(0, -3, 0), length=6000, width=None, height=0.2)

"""
------------------------------------------------------------------------------------
                                        controls
------------------------------------------------------------------------------------
"""

switch = True


def toggle(b):
    global switch
    if switch:
        b.text = '<b>Two Atom Type<b>'
        b.background = vp.color.green
        switch = False

        for i in range(sl_atom.value):
            atom2[i].visible = True
            phase2[i].visible = True

    else:
        b.text = '<b>One Atom Type<b>'
        b.background = vp.color.cyan
        switch = True
        for i in range(14):
            atom2[i].visible = False
            phase2[i].visible = False


s_button = vp.button(text='<b>One Atom Type<b>', background=vp.color.cyan, pos=scene_main.title_anchor, bind=toggle)


def add_atom(s):
    global k_initial, k, N, t
    t = 0
    wt_atom.text = s.value
    N = s.value / 2
    k = 0

    for h in range(15):
        k_buttons[h].disabled = True
        if h == 7:
            k_buttons[h].background = vp.color.orange

        else:
            k_buttons[h].background = vp.color.white

    for h in range(s.value + 1):
        k_buttons[h + (int(0.5 * (14 - s.value)))].disabled = False

    for i in range(14):
        atom[i].visible = False
        atom2[i].visible = False
        phase[i].visible = False
        phase2[i].visible = False

    for j in range(14):
        atom[j].pos.x = ((0.5 * a) - (0.5 * a) * s.value) + a * j
        atom2[j].pos.x = ((0.5 * a) - (0.5 * a) * s.value) + (a * j + (0.5 * a))

        phase[j].pos.x = ((0.5 * a) - (0.5 * a) * s.value) + a * j
        phase[j].pos.y = -3

        phase2[j].pos.x = ((0.5 * a) - (0.5 * a) * s.value) + (a * j + (0.5 * a))

    for j in range(14):
        pos_x_initial[j] = atom[j].pos.x
        pos2_x_initial[j] = atom2[j].pos.x

    for i in range(s.value):
        atom[i].visible = True
        phase[i].visible = True

        if not switch:
            atom2[i].visible = True
            phase2[i].visible = True


sl_atom = vp.slider(min=2, max=14, value=2, step=2, bind=add_atom)
wt_atom = vp.wtext(text=sl_atom.value)
scene_main.append_to_caption(" atoms\n\n")


def lattice_spacing(s):
    global a, k_initial, k, t
    t = 0
    k = 0

    for i in range(14):
        phase[i].pos.y = -3

    wt_a.text = s.value
    a = s.value
    k_initial = np.pi / a
    add_atom(sl_atom)


sl_a = vp.slider(min=4, max=10, value=4, step=1, bind=lattice_spacing)
wt_a = vp.wtext(text=sl_a.value)
scene_main.append_to_caption("a (lattice)\n\n")


def wave(b):
    global k_initial, k_int_val, k, k_buttons, N, t

    for i in range(14):
        phase[i].pos.y = -3

    for h in range(15):
        k_buttons[h].background = vp.color.white

    b.background = vp.color.orange
    t = 0
    k_int_val = int(b.text)
    k = k_int_val * k_initial / N


k_buttons = []
for i in range(-7, 8):
    if i == 0 or i == -1 or i == 1:
        if i == 0:
            k_buttons.append(vp.button(text=str(i), background=vp.color.orange, bind=wave, disabled=False))

        else:
            k_buttons.append(vp.button(text=str(i), background=vp.color.white, bind=wave, disabled=False))

    else:
        k_buttons.append(vp.button(text=str(i), background=vp.color.white, bind=wave, disabled=True))

scene_main.append_to_caption(" 2π/Na (k)\n\n\n\n")


def spring(s):
    global K_initial, K
    wt_K.text = s.value
    K = K_initial * s.value


sl_K = vp.slider(min=0.1, max=6, value=0.1, step=0.1, bind=spring)
wt_K = vp.wtext(text=sl_K.value)
scene_main.append_to_caption("K N/m (Spring Force)\n\n")


def constant_A(s):
    global A_initial, A, t
    t = 0
    wt_A.text = s.value
    A = A_initial * s.value


sl_A = vp.slider(min=0.1, max=1, value=0.1, step=0.1, bind=constant_A)
wt_A = vp.wtext(text=sl_A.value)
scene_main.append_to_caption("A (Constant)\n\n\n\n")


def mass_M(s):
    global M_initial, M, m_initial, m, R_initial, R, r_initial, r, t
    t = 0
    wt_M.text = s.value
    M = m_initial * s.value
    m = M_initial / s.value

    for i in range(14):
        atom[i].radius = r_initial * s.value
        atom2[i].radius = R_initial / s.value


sl_M = vp.slider(min=1, max=2, value=1, step=0.1, bind=mass_M)
wt_M = vp.wtext(text=sl_M.value)
scene_main.append_to_caption("M/m \n\n")

# Mouse clicking controls

# drag = False
# atom_select = None
#
#
# def down():
#     global drag, atom_select
#     for i in range(14):
#         if (atom[i].pos.x - 0.4 <= scene_main.mouse.pos.x <= atom[i].pos.x + 0.4) and (
#                 atom[i].pos.y - 0.4 <= scene_main.mouse.pos.y <= atom[i].pos.y + 0.4):
#             drag = True
#             atom_select = i
#
#
# def move():
#     global drag, atom_select
#     if drag:
#         atom[atom_select].pos.x = scene_main.mouse.pos.x
#
#
# def up():
#     global drag, atom_select
#     drag = False
#     atom_select = None
#
#
# scene_main.bind("mousedown", down)
#
# scene_main.bind("mousemove", move)
#
# scene_main.bind("mouseup", up)

"""
------------------------------------------------------------------------------------
                                        animation
------------------------------------------------------------------------------------
"""

while True:
    vp.rate(100)

    w = np.sqrt((4 * K * (np.sin(0.5 * k * a)) ** 2) / M)
    w2 = np.sqrt(((K * (M + m)) / (M * m)) - K * np.sqrt((((M + m) / (M * m)) ** 2) - ((4 / (M * m)) * (np.sin(0.5 * k * a)) ** 2)))

    alpha = ((2 * K) - ((w2 ** 2) * M)) / (2 * K * np.cos(0.5 * k * a))

    for i in range(14):
        if switch:
            atom[i].pos.x = A * np.cos((k * pos_x_initial[i]) - w * t) + pos_x_initial[i]

        else:
            atom[i].pos.x = A * np.cos((0.5 * k * pos_x_initial[i]) - w2 * t) + pos_x_initial[i]
            atom2[i].pos.x = alpha * A * np.cos((0.5 * k * pos2_x_initial[i]) - w2 * t) + pos2_x_initial[i]

    t = t + 0.01

    direction = A * np.cos((k * pos_x_initial[0]) - w * t) - A * np.cos((k * pos_x_initial[0]) - w * (t - 0.01))

    index = int(k_int_val + N)

    if k_int_val > 0:
        index = index - 1

    if direction > 0:
        phase[index].pos.y = -1

    if direction < 0:
        phase[index].pos.y = -5
