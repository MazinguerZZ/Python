# Ejercicios genéricos de programación 8

Este boletín de ejercicios está orientado a practicar con:
- arrays, cadenas y sentencias de control

1. Una matriz transpuesta es aquella en la que se intercambian filas por columnas. A continuación tienes dos ejemplos de una matriz y su transpuesta:

   | Matriz | Transpuesta |
   |--------|-------------|
   | \| 1 2 \| | \| 1 3 \| |
   | \| 3 4 \| | \| 2 4 \| |

   Realiza un programa que dada una matriz almacenada en un array te calcule su transpuesta y la almacene en otro diferente. Tu programa debería, además, dibujar en consola las matrices de la siguiente forma:

   ```
   | 1 2 |
   | 3 4 |

   | 1 3 |
   | 2 4 |
   ```

2. Escribe un programa que pida al usuario una contraseña y compruebe que cumple las siguientes condiciones:

   a. Debe tener al menos 8 caracteres y no más de 20.  
   b. Debe tener al menos una letra mayúscula y una minúscula.  
   c. Debe de tener al menos un número.  
   d. Debe tener un símbolo de entre los siguientes: `_`, `-`, `!`, `?`, `*`

   Si la contraseña no es válida, se pide de nuevo, y así sucesivamente hasta que sea correcta. Una vez que es correcta se pide al usuario que la introduzca de nuevo, si coincide se informa al usuario y se termina el proceso. Si no coincide se vuelve a empezar el proceso.

3. Vamos a realizar un programa de cifrado que haga lo siguiente: mezcle los caracteres alternando entre las del principio y las del final del mensaje empezando siempre por el final. Por ejemplo, si nuestro mensaje secreto fuera el siguiente:

   `12345`

   El mensaje cifrado sería así:

   `51432`

   Un ejemplo con un mensaje de texto real:

   ```
   Atacamos mañana
   ```

   Se codificaría así:

   ```
   aAntaañcaamm os
   ```

4. Modifica el programa anterior para que sea más difícil el descifrado haciendo que, de forma aleatoria, algunas letras cambien de mayúsculas a minúsculas en el cifrado. El mensaje anterior quedaría entonces así, por ejemplo (tu resultado podría ser diferente ya que la conversión de mayúsculas es aleatoria):

   `aanTAañCaaMm OS`

5. Realiza ahora el programa que haga el descifrado del mensaje. Como es imposible saber qué letras eran mayúsculas y cuáles minúsculas en el mensaje original, tu mensaje descifrado debería de aparecer con todas las letras en mayúsculas.

6. **EJERCICIO CON FORMATO DE EXAMEN**

   Realiza un programa que lea una frase y nos diga si es un palíndromo o no. Un palíndromo es una palabra o frase que se lee igual hacia adelante que hacia atrás sin tener en cuenta los espacios en blanco ni que los caracteres tengan tilde o estén en mayúsculas.

   Ejemplos de palíndromos:
   - La ruta nos aportó otro paso natural
   - Átale demoníaco Caín o me delata

   Para facilitar la codificación se deberán introducir las frases sin tildes, pero sí hay que tener en cuenta las mayúsculas y los espacios. Tampoco tendrán signos de puntuación.

   Ejemplo de funcionamiento:
   ```
   Introduce un texto: Dabale arroz a la zorra el abad
   El texto introducido es un palíndromo
   ```

   No hace falta comprobaciones sobre la entrada (que siempre será una cadena de texto), pero sí es preciso vigilar que a veces puede que haya más de un espacio entre las palabras o incluso al principio y al final de la frase.

7. **EJERCICIO CON FORMATO DE EXAMEN**

   Un número es Armstrong cuando la suma de cada uno de los números que lo componen elevado al número de dígitos de dicho número da como resultado el propio número.

   Realiza un programa que, dado un número introducido por teclado, averigüe si es un número Armstrong o Narcisista.

   Ejemplo de un número de 3 dígitos: 153 ya que 1³ + 5³ + 3³ = 1 + 125 + 27 = 153.

   Todos los números de una cifra son narcisistas. De tres cifras tienes, además del anterior, el 370, el 371 y el 407 y de más de tres cifras puedes probar con el 1634. No existen números narcisistas de dos cifras.

   Ejemplo de funcionamiento:
   ```
   Introduce un número: 371
   El número 371 es narcisista
   ```

   No hace falta comprobaciones acerca de la entrada que siempre será un número entero.

---
