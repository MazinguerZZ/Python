# Manual básico de Ursina (Framework avanzado de Python)

## 1. Introducción

Ursina es un framework de Python orientado al desarrollo de videojuegos en 2D y 3D. Permite crear entornos interactivos de forma sencilla, utilizando una sintaxis clara y accesible.

### ¿Para qué sirve Ursina?

Ursina se utiliza principalmente para:

* Crear videojuegos en 3D.
* Desarrollar aplicaciones interactivas.
* Aprender programación gráfica de forma sencilla.

### ¿Por qué elegir Ursina?

He elegido Ursina porque permite ver resultados visuales rápidamente y facilita el desarrollo de videojuegos sin necesidad de motores complejos. Además, su integración con Python lo hace ideal para estudiantes.

---

## 2. Instalación de Ursina

### Paso 1: Comprobar Python

```bash

python --version

```

---

### Paso 2: Crear entorno virtual

```bash

python -m venv entorno\_ursina

```

Activación en Linux:

```bash

source entorno\_ursina/bin/activate

```

---

### Paso 3: Instalar Ursina

```bash

pip install ursina

```

---

## 3. Ejecución en Visual Studio Code o PyCharm

1. Crear un archivo llamado `main.py`.
2. Asegurarse de seleccionar el intérprete del entorno virtual.
3. Ejecutar con:

```bash

python main.py

```

## 4. Explicación del código

### Inicialización

* `Ursina()` inicia el motor gráfico.

### Clase CuboMagico

* Hereda de `Button`, lo que permite interacción con el ratón.
* `model='cube'` define su forma.
* `color` y `highlight\_color` controlan su apariencia.

### Interacción

* `self.hovered` detecta si el ratón está sobre el objeto.
* Al hacer clic (`left mouse down`), el cubo cambia a un color aleatorio.

### Suelo

* Se crea con `Entity`.
* `collider='box'` evita que el jugador lo atraviese.

### Jugador

* `FirstPersonController()` permite movimiento con:

* W, A, S, D
* Ratón para mirar

### Función update()

* Se ejecuta continuamente.
* Hace que el cubo rote lentamente.

---

## 5. Funcionamiento del programa

Al ejecutar el programa:

* Aparece un entorno 3D.
* El jugador puede moverse libremente.
* Hay un cubo delante.
* Al hacer clic sobre él:

* Cambia de color.
* El cubo rota constantemente.

---

## 6. Conclusión

Ursina es un framework muy potente y fácil de usar para crear aplicaciones interactivas en 3D. En este ejemplo se demuestra cómo combinar movimiento, interacción y gráficos básicos en pocas líneas de código.

Esto lo convierte en una herramienta ideal para aprender desarrollo de videojuegos de forma práctica.

