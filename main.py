from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(icon="./assets/gta-vi-logo.ico", title="GTV VI")
window.size = (1280, 720)
window.fullscreen = True
window.borderless = False
mouse.locked = True
window.editor_ui.enabled = False
window.fps_counter.enabled = True

loading_time = 40  
loading_timer = 0
game_started = False

loading_screen_video = "./assets/gta-vi-loading-screen.mp4"
loading_screen = Entity(
    model="quad", texture=loading_screen_video, scale=(16, 9), collider="box"
)


def update():
    global loading_timer, game_started

    loading_timer += time.dt

    if not game_started and loading_timer >= loading_time:
        start_game()


def start_game():
    global game_started
    game_started = True

    loading_screen.disable()
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
        origin_y=-0.8,
    )
    camera.position = (0, 1, -7)
    camera.rotation = (5, 0, 0)
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
