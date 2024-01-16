from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(icon="./assets/gta-vi-logo.ico", title="GTV VI")

window.entity_counter.enabled = False
window.collider_counter.enabled = False
window.fps_counter.enabled = True
window.size = (1280, 720)
window.fullscreen = True
window.borderless = False
window.vsync = False
window.exit_button = "f11"
sky = Sky()
sky.color = color.rgb(131, 225, 227)

try:
    map = Entity(
        model="/assets/map.obj",
        collider="box",
        ignore=True,
        position=(0, 0, 0),
        parent=scene,
        origin_y=0.5,
    )
except Exception as e:
    print(f"Error loading map: {e}")

player = FirstPersonController(
    model="cube",
    collider="box",
    color=color.red,
    position=(0, 3, 0),
    origin_y=-0.7,
)
camera.position = (0, 1, -7)
camera.rotation = (-3, 0, 0)
player.cursor.enabled = False

crosshair = Entity(
    model="quad", scale=0.005, color=color.white, rotation_z=45, parent=camera.ui
)
lamborghini_model = load_model("/models/lamborgini/lamborghini.obj")

lamborghini = Entity(
    model=lamborghini_model,
    collider="mesh",
    texture="/models/lamborgini/lamborghini.jpeg",
    scale=0.08,
)

lamborghini.position = (3.5, 0, 0)


def input(key):
    if key == "escape":
        application.quit()


app.run()
