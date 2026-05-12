from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# 1. Inicializar la aplicación
app = Ursina()

# 2. Contador de clics (variable global)
click = 0

# 3. Texto en pantalla para mostrar el contador
texto_clics = Text(
    text = "Número de clicks: 0",
    position = (-0.85, 0.45),  # Esquina superior izquierda
    scale = 2,
    color = color.white
)

# 4. Definir una clase para nuestro objeto interactivo
class CuboMagico(Button):
    def __init__(self, position=(0, 1, 5)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",           # Forma 3D
            origin_y = 0.5,
            texture = "white_cube",   # Textura por defecto de Ursina
            color = color.orange,     # Color inicial
            highlight_color = color.lime # Color al pasar el ratón
        )

    # Función que se ejecuta al hacer clic en el cubo
    def input(self, key):
        global click  # Accedemos a la variable global
        if self.hovered:
            if key == "left mouse down":
                self.color = color.random_color()
                click += 1                              # Incrementar contador
                texto_clics.text = f"Número de clicks: {click}"   # Actualizar texto en pantalla
                print(f"¡Color cambiado! | Clics totales: {click}")

# 5. Crear el suelo (una entidad simple)
suelo = Entity(
    model = "plane",
    scale = (30, 1, 30),
    color = color.gray,
    texture = "white_cube",
    texture_scale = (30, 30),
    collider = "box" # Permite que el jugador no lo atraviese
)

# 6. Instanciar nuestro cubo y el controlador de jugador
cubo_ejemplo = CuboMagico()
jugador = FirstPersonController() # Añade controles W, A, S, D y ratón

# 7. Función de actualización por frame (opcional)
def update():
    # El cubo rotará lentamente de forma constante
    cubo_ejemplo.rotation_y += time.dt * 30

# 8. Función global de input para gestionar el ratón con Escape
def input(key):
    if key == "escape":
        mouse.locked = not mouse.locked      # Alterna si el ratón está capturado
        mouse.visible = not mouse.locked     # Muestra el cursor cuando está libre
        jugador.enabled = mouse.locked       # Pausa los controles FPS si el ratón está suelto

# Ejecutar el motor
app.run()