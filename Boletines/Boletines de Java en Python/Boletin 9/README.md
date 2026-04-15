# Ejercicios genéricos de programación 9

Este boletín de ejercicios está orientado a practicar con:
- diccionarios / hash maps

1. Crear un programa o una función que reciba un diccionario con los datos de los clientes de una tienda y su edad y los muestre por consola ordenados por nombre de pila. El diccionario, ya creado en el código de tu programa, tendrá esta forma:

   ```python
   clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto, Francisco": 44, "Cotón, Carmelo": 56 }
   ```

   Y la salida por consola así:
   ```
   Carmelo Cotón (56)
   Francisco Rupto (44)
   José Chuletón (35)
   Rubén Tosidad (27)
   ```

2. Añade una función que sirva para añadir nombres al diccionario. La llamada a la función sería así:

   ```python
   nuevoCliente(clientes, "Felipe", "Lotas", 76)
   ```

   Tu función debería de añadir el nuevo cliente al diccionario con el formato correcto. Si este cliente ya existe debería de mostrar en consola un mensaje advirtiéndolo y preguntando si se quiere sobreescribir la edad o no.

3. Por último, crea ahora una función que sume un año a la edad de un cliente. La llamada sería así:

   ```python
   cumpleCliente(clientes, "José", "Chuletón")
   ```

   Si el cliente existe debería de sumar un año a su edad. Si no existe debería de informar de ello por consola y no hacer nada.

4. **EJERCICIO CON FORMATO DE EXAMEN**

   Escribir un programa que reciba un texto y devuelva un diccionario o una estructura similar donde las palabras del texto serán las claves y el número de veces que aparece cada una de ellas su valor. Considera que la frase que introducimos no tiene signos de puntuación, que el único separador entre palabras son los espacios y no tengas en cuenta las tildes ni mayúsculas. Es decir: "qué" se considera una palabra diferente de "que" y "Como" es distinta de "como".

   El texto debe de introducirse desde el teclado.

   Ejemplo de ejecución:
   ```
   Introduce tu texto: Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera
   Diccionario: {'Como': 1, 'quieres': 1, 'que': 4, 'te': 1, 'quiera': 3, 'si': 1, 'el': 1, 'quiero': 2, 'me': 3, 'no': 1, 'quiere': 1, 'como': 1}
   ```

5. Escribir un programa en Python que guarde en un diccionario los precios de las frutas de la siguiente tabla:

   | Fruta      | Precio (€/Kg) |
   |------------|---------------|
   | Aguacate   | 4.35          |
   | Mandarina  | 2.60          |
   | Kiwi       | 3.75          |
   | Naranja    | 1.80          |

   > **Nota:** El diccionario debes de crearlo en el código del programa con los datos listados en la tabla.

   Tu programa debe de preguntar al usuario por una fruta y un número de kilos y mostrar por pantalla el precio de ese número de kilos de fruta con dos decimales. El número de kilos debe de admitir decimales. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. Captura las posibles excepciones.

   El programa finalizará cuando se escriba la palabra `fin` (de forma insensible a mayúsculas y/o minúsculas).

   Ejemplo de ejecución:
   ```
   ¿Qué fruta quieres comprar? Sandía
   Lo siento mucho pero no vendemos esa fruta
   ¿Qué fruta quieres comprar? Kiwi
   ¿Cuantos kilos quieres? ff
   No has introducido bien la cantidad que quieres
   ¿Qué fruta quieres comprar? Mandarina
   ¿Cuantos kilos quieres? 4.75
   4.75 de Mandarina cuestan 12.35 €
   ¿Qué fruta quieres comprar? fin
   ```

---
