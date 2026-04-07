from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# 1. Inicializar la aplicación
app = Ursina(title="Cubo colorido", icon="cubo.ico")

class CuboMagico(Button):
    def __init__(self, position=(0, 1, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='foto',
            color=color.white,
            highlight_color=color.lime
        )

    def input(self, key):
        # Usamos 'mouse combined' o simplemente 'left mouse down' si heredamos de Button
        if self.hovered and key == 'left mouse down':
            self.color = color.random_color()
            print("¡Color cambiado!")

# 3. Suelo
suelo = Entity(
    model='plane',
    scale=(30, 1, 30),
    color=color.gray,
    texture='white_cube',
    texture_scale=(30, 30),
    collider='box'
)

cubo_ejemplo = CuboMagico()
jugador = FirstPersonController()

def update():
    cubo_ejemplo.rotation_y += time.dt * 30

app.run()
