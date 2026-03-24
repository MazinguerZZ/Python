from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# 1. Inicializar la aplicación
app = Ursina()

# 2. Definir una clase para nuestro objeto interactivo
class CuboMagico(Button):
    def __init__(self, position=(0, 1, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',           # Forma 3D
            origin_y=0.5,
            texture='white_cube',   # Textura por defecto de Ursina
            color=color.orange,     # Color inicial
            highlight_color=color.lime # Color al pasar el ratón
        )

    # Función que se ejecuta al hacer clic en el cubo
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                self.color = color.random_color()
                print("¡Color cambiado!")

# 3. Crear el suelo (una entidad simple)
suelo = Entity(
    model='plane',
    scale=(30, 1, 30),
    color=color.gray,
    texture='white_cube',
    texture_scale=(30, 30),
    collider='box' # Permite que el jugador no lo atraviese
)

# 4. Instanciar nuestro cubo y el controlador de jugador
cubo_ejemplo = CuboMagico()
jugador = FirstPersonController() # Añade controles W, A, S, D y ratón

# 5. Función de actualización por frame (opcional)
def update():
    # El cubo rotará lentamente de forma constante
    cubo_ejemplo.rotation_y += time.dt * 30

# Ejecutar el motor
app.run()