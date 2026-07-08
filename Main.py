from ursina import *
app = Ursina()

shapes_index = 0
Speed = 4

CUBE = Entity(
    model='cube',
    position=(0, 0, 0),
    color=color.red,
    texture="white_cube",
)

def update():
    movements()
    Shapes()

def input(key):
    Shape_Switch(key)

def movements():
    if held_keys["w"]:
        CUBE.rotation_x += Speed
    if held_keys["s"]:
        CUBE.rotation_x -= Speed
    if held_keys["a"]:
        CUBE.rotation_z -= Speed
    if held_keys["d"]:
        CUBE.rotation_z += Speed

def Shape_Switch(key):
    global shapes_index
    if key == 'r':
        if shapes_index != 4:
            shapes_index += 1
        else:
            shapes_index = 0

def Shapes():
    if shapes_index == 0:
        CUBE.model = 'cube'
    elif shapes_index == 1:
        CUBE.model = 'sphere'
    elif shapes_index == 2:
        CUBE.model = 'cylinder'
    elif shapes_index == 3:
        CUBE.model = 'cone'
    elif shapes_index == 4:
        CUBE.model = 'plane'

app.run()
