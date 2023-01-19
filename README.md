# Convocatoria_ordinaria (2022-2023)
- Enlace link: https://github.com/luciacantos/Convocatoria_ordinaria-2022-2023-/blob/main/README.md

## EJERCICIO 1
Para este ejercicio, creará un solucionador de Nonogramas. 
Si no sabe qué son los nonogramas, puede consultar algunas instrucciones y también probar
algunos nonogramas aquí.
Para resolver un Nonograma, primero debemos entender cómo funcionan. Un Nonograma es 
un rompecabezas que consta de una matriz de celdas en blanco y negro. Las pistas se 
proporcionan en los bordes de la matriz en forma de números que indican cuántas celdas 
negras hay en cada fila o columna consecutiva.
Por ejemplo, si las pistas para una fila son [2, 1], significa que hay dos grupos de celdas negras 
consecutivas en esa fila, el primero con dos celdas y el segundo con una sola celda. La 
solución para esta fila sería "BB_X_B" (donde "B" representa una celda negra y "X" representa 
una celda en blanco).
Para resolver un Nonograma completo, debemos usar las pistas y nuestro conocimiento de 
cómo funcionan los Nonogramas para ir rellenando la matriz poco a poco hasta obtener la 
solución final.
solo tendrás que resolver Nonogramas 5x5

## EJERCICIO 2
Cuando asistíamos a la escuela secundaria, se nos pidió que simplificáramos expresiones 
matemáticas como "3x-yx+2xy-x" (o generalmente más grande), y eso fue muy fácil 
("2x+xy"). ¡Pero díselo a tu pc y ya veremos!
Existen varias formas de simplificar una expresión matemática, pero una posible solución a su 
problema sería utilizar la regla de la suma y del producto de los exponentes para combinar 
términos similares en la expresión.
Por ejemplo, la expresión "3x-zx+2xy-x" se podría simplificar de la siguiente manera:
1. Identificar los términos que tienen la misma base (por ejemplo, "x") y agruparlos juntos: 
"3x - x + 2xy - zx"
2. Aplicar la regla de la suma y del producto de los exponentes para cada grupo de 
términos:
- Para el grupo "3x - x", el exponente de la base "x" es 1 en ambos términos, por lo que 
se pueden combinar utilizando la regla de la suma de exponentes: 3x - x = 2x
- Para el grupo "2xy - zx", el exponente de la base "x" es 1 en ambos términos, por lo 
que se pueden combinar utilizando la regla de la suma de exponentes: 2xy - zx = (2-
z)xy
3. Reemplazar cada grupo de términos simplificados en la expresión original: "3x - x + 2xy 
- zx" se convierte en "2x + (2-z)xy"

## EJERCICIO 3
Si escribimos los dígitos de "60" como palabras en inglés, obtenemos "sixzero"; el número de 
letras en "sixzero" es siete. El número de letras en "siete" es cinco. El número de letras en 
"cinco" es cuatro. El número de letras en "cuatro" es cuatro: hemos alcanzado un equilibrio 
estable.
Esto es correcto. Cuando escribimos "60" como palabras en inglés, obtenemos "sixzero", que 
tiene siete letras. El número de letras en "siete" es cinco, y el número de letras en "cinco" es 
cuatro. Por lo tanto, al escribir el número "60" como palabras en inglés y contando el número de 
letras de cada palabra resultante, eventualmente llegamos a un equilibrio en el que el número 
de letras es igual a cuatro.
Nota: para números enteros mayores de 9, escriba los nombres de cada dígito en una sola 
palabra (en lugar del nombre propio del número en inglés). Por ejemplo, escribe 12 como 
"unodos" (en lugar de doce) y 999 como "nineninenine" (en lugar de novecientos noventa y 
nueve).
Para cualquier número entero entre 0 y 999, devuelva una matriz que muestre la ruta desde 
ese número entero hasta un equilibrio estable.

## EJERCICIO 4
Su tarea es escribir una función llamada do_math que reciba un solo argumento. Este 
argumento es una cadena que contiene varios números delimitados por espacios en 
blanco. Cada número tiene una sola letra del alfabeto en algún lugar dentro de él.
Ejemplo: "24z6 1x23 y369 89a 900b"
Como se muestra arriba, esta letra del alfabeto puede aparecer en cualquier lugar dentro del 
número. Tienes que extraer las letras y ordenar los números según sus letras 
correspondientes.
Ejemplo: "24z6 1x23 y369 89a 900b" se convertirá 89 900 123 369 246 (ordenados según la 
letra del alfabeto)
Aquí viene la parte difícil, ahora tienes que hacer una serie de cálculos sobre los números que 
has extraído.
- La secuencia de cálculos es + - * /. Las reglas matemáticas básicas NO se aplican, 
debe hacer cada cálculo exactamente en este orden.
- Esto tiene que funcionar para cualquier tamaño de números enviados (después de la 
división, volver a la suma, etc.).
- En el caso de letras del alfabeto duplicadas, debe organizarlas de acuerdo con el 
número que apareció primero en la cadena de entrada.
- Recuerde también redondear la respuesta final al entero más cercano.

## EJERCICIO 5
Su tarea es escribir una función llamada do_math que reciba un solo argumento. Este 
argumento es una cadena que contiene varios números delimitados por espacios en 
blanco. Cada número tiene una sola letra del alfabeto en algún lugar dentro de él.
Ejemplo: "24z6 1x23 y369 89a 900b"
Como se muestra arriba, esta letra del alfabeto puede aparecer en cualquier lugar dentro del 
número. Tienes que extraer las letras y ordenar los números según sus letras 
correspondientes.
Ejemplo: "24z6 1x23 y369 89a 900b" se convertirá 89 900 123 369 246 (ordenados según la 
letra del alfabeto)
Aquí viene la parte difícil, ahora tienes que hacer una serie de cálculos sobre los números que 
has extraído.
- La secuencia de cálculos es + - * /. Las reglas matemáticas básicas NO se aplican, 
debe hacer cada cálculo exactamente en este orden.
- Esto tiene que funcionar para cualquier tamaño de números enviados (después de la 
división, volver a la suma, etc.).
- En el caso de letras del alfabeto duplicadas, debe organizarlas de acuerdo con el 
número que apareció primero en la cadena de entrada.
- Recuerde también redondear la respuesta final al entero más cercano.

## EJERCICIO 6
El Rey y la Reina de FarFarAway van a visitar a Shrek y Fiona en su pantano. Sin embargo, 
Shrek tiene miedo de que Burro vuelva a hacer travesuras, por lo que decide atarlo para que no 
moleste en la cena real. Shrek cultiva un parche circular de hierba deliciosa y decide atar a 
Burro a un poste de la cerca en su borde. Sin embargo, teme que cuando Burro tenga hambre, 
se coma toda la hierba, y Shrek necesita la hierba para preparar un plato de sabrosa ensalada 
de hierba de ogro para la cena. La cuerda debe ser corta para que el burro no pueda comer (o, 
peor aún, fertilizar) demasiada hierba.
Shrek puede resolver este problema de varias maneras. Una opción sería colocar una cuerda 
larga y suficientemente resistente en el poste y enlazarla a un collar o una correa que se 
coloque alrededor del cuello de Burro. De esta manera, Shrek podrá controlar la distancia que 
Burro puede recorrer y asegurarse de que no se acerque demasiado a la hierba deliciosa.
Otra opción sería colocar una cerca alrededor del parche circular de hierba y asegurarse de 
que Burro no pueda acceder a él. De esta manera, Shrek podrá proteger su preciada hierba y 
asegurarse de que esté disponible para la cena.
En cualquier caso, es importante que Shrek sea cuidadoso y no permita que Burro se acerque 
demasiado a la hierba, ya que de lo contrario podría terminar comiéndola o causando daños en 
el parche. Además, es crucial que Shrek mantenga una buena comunicación con Burro y le 
haga entender que su comportamiento no es aceptable, para evitar que vuelva a suceder en el 
futuro.
Dado el diámetro del parche circular de pasto (medido en pasos de ogro), calcule la longitud 
máxima de la cuerda para que Burro no pueda comer más del porcentaje de pasto dado (dado 
como proporción en el rango 0 <= percentage <= 1, es decir, 0.5significa 50%). Como Shrek es 
solo un ogro y no está muy familiarizado con las fracciones, la longitud debe devolverse como 
pasos de ogro enteros.

## EJERCICIO 7
Dadas dos posiciones diferentes en un tablero de ajedrez, encuentre el menor número de 
movimientos que le tomaría a un caballo pasar de una a la otra. Las posiciones se pasarán 
como dos argumentos en notación algebraica.
Por ejemplo, knight("a3", "b5")debería devolver 1.
El caballo no puede moverse fuera del tablero. El tablero es de 8x8.
Para resolver este problema, podemos seguir los siguientes pasos:
1. Convertimos las posiciones de notación algebraica a coordenadas (fila, columna) en un 
tablero de 8x8. Por ejemplo, la posición "a3" se convertiría a (3, 1) donde 3 es la fila y 1 
es la columna.
2. Creamos una matriz de 8x8 que represente el tablero de ajedrez, y marcamos las 
posiciones inicial y final con un valor especial (por ejemplo, 0 y 1).
3. Utilizamos un algoritmo de búsqueda como BFS (Breadth-First Search) para encontrar 
el camino más corto entre la posición inicial y final. La búsqueda se realiza desde la 
posición inicial y se expande en todas las posibles posiciones a las que el caballo 
puede moverse. Cada vez que se encuentra una posición válida (es decir, que está 
dentro del tablero y no ha sido visitada antes), se agrega a la cola de búsqueda, para 
nuestro caso una lista. La búsqueda termina cuando se encuentra la posición final o se 
agota la cola de búsqueda(lista) sin encontrarla.
4. El número de movimientos requeridos se calcula como la longitud del camino 
encontrado menos 1 (ya que la posición inicial se cuenta como un movimiento).

## EJERCICIO 8
Estás de camino al mercado cuando escuchas una hermosa música de un artista callejero 
cercano. Las notas se juntan como si no lo creerías mientras el músico junta patrones de 
melodías. Mientras te preguntas qué tipo de algoritmo podrías usar para cambiar las octavas 
en 8 tonos o algo así de tonto, te das cuenta de que has estado observando al músico durante 
unos 10 minutos impares. Usted pregunta, "¿cuánto suele dar propina la gente por algo como 
esto?" El artista mira hacia arriba. "Siempre va a tratarse de Tree Fiddy".
¡Fue entonces cuando te das cuenta de que el músico era una bestia de 400 pies de altura de 
la era paleolítica! ¡El Monstruo del Lago Ness casi te engaña!
Solo hay 2 formas garantizadas de saber si estás hablando con el Monstruo del Lago Ness: A) 
es una bestia de 400 pies de altura de la era paleolítica; B) te pedirá árbol fiddy.
Dado que Nessie es una maestra del disfraz, la única forma de saberlo con precisión es buscar 
la frase "tree fiddy". Como estás cansado de que este monstruo te engañe, ha llegado el 
momento de codificar una solución para encontrar al Monstruo del Lago Ness. Tenga en cuenta 
que la frase también se puede escribir como "3.50"o "three fifty".

## EJERCICIO 9

Cree un método para encontrar el número de lunes dado el cumpleaños de una persona y la 
fecha actual. Para este ejercicio simple, no te preocupes por los días festivos/vacaciones, 
licencia por enfermedad, etc. Supongamos que una persona tiene un trabajo y va a trabajar 
durante todo el año si está en edad de trabajar. Para simplificar las cosas, suponga que alguien 
comienza a trabajar cuando tiene 22 años y se jubila cuando tiene 78.

Para resolver este problema, se puede seguir los siguientes pasos:
1. Calcular la edad de la persona en la fecha actual. Para ello, se puede calcular la 
diferencia en años entre la fecha actual y la fecha de cumpleaños de la persona.
2. Verificar si la persona está en edad de trabajar. Para ello, se puede comprobar si su 
edad está entre 22 y 78 años.
3. Calcular el número de lunes que hay entre la fecha de cumpleaños y la fecha actual. 
Para ello, se puede calcular el número de días que hay entre ambas fechas y dividirlo 
por 7, ya que una semana tiene 7 días.
4. Si la persona está en edad de trabajar, devolver el número de lunes calculado en el 
paso 3. En caso contrario, devolver 0.

## EJERCICIO 10

Bueno, es posible que ya lo haya adivinado, pero para que quede claro: debe crear una función 
de Fibonacci que, dada una matriz/lista de firmas, devuelva los primeros n elementos, 
incluida la firma de la secuencia así sembrada.
La firma siempre contendrá 3 números; n siempre será un número no negativo; if n == 0, luego 
devuelve una matriz vacía (excepto en C devuelve NULL) y prepárate para cualquier otra cosa 
que no esté claramente especificada;)
Entendiendo que la firma siempre contiene 3 números, y que la secuencia de Tribonacci se 
genera sumando los últimos 3 números de la secuencia…
Bueno, es hora de expandir un poco más la familia: piense en un Quadribonacci que comienza 
con una firma de 4 elementos y cada elemento siguiente es la suma de los 4 anteriores, un 
Pentabonacci (bueno , Cinquebonacci probablemente sonaría un poco más italiano, pero sería 
también suena realmente horrible) con una firma de 5 elementos y cada elemento siguiente es 
la suma de los 5 anteriores, y así sucesivamente.
¿Bien adivina que? Debe crear una función Xbonacci que tome una firma de X elementos, y 
recuerde que cada elemento siguiente es la suma de los últimos X elementos, y devuelva los 
primeros n elementos de la secuencia así sembrada.
xbonacci {1,1,1,1} 10 = {1,1,1,1,4,7,13,25,49,94}
xbonacci {0,0,0,0,1} 10 = {0,0,0,0,1,1,2,4,8,16}
xbonacci {1,0,0,0,0,0,1} 10 = {1,0,0,0,0,0,1,2,3,6}




