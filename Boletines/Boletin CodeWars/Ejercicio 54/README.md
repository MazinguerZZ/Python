# Kata: La Ola Mexicana
**Dificultad:** 3/8

---

## 📝 Enunciado

La ola (conocida como "ola mexicana") es ese efecto en los estadios donde grupos sucesivos de espectadores se levantan, gritan y alzan los brazos brevemente, creando una ola que recorre el graderío.

Tu tarea es crear una función que convierta una cadena de texto en una ola mexicana. Recibirás una cadena y deberás devolver un array de cadenas donde una letra en mayúscula representa a una persona levantándose.

### Reglas

1. La cadena de entrada siempre tendrá letras minúsculas y espacios, pero puede estar vacía, en cuyo caso debes devolver un array vacío.
2. Si el carácter es un espacio, ignóralo como si fuera un asiento vacío.

### Ejemplos

```
"hello"       =>  ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
" s p a c e s " =>  [" S p a c e s ", " s P a c e s ", " s p A c e s ", ...]
```