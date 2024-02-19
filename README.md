# Blockchain con python inicial

Proyecto de implementacion de blockchain con Python nivel inicial

El blockchain es una tecnologia disruptiva que esta definiendo nuevas maneras de trabajar con la tecnologia de la información, es muy importante tener conocimientos básicos de esta para poder aplicarla en los proyectos que querieran este tipo de trabajo de par a par para mejorar y facilitar la adiminstración.

Primeramente se crea la función encargada de codificar una cadena de caracteres en hash

El codigo HASH es un algoritmo matemático que se encarga de convertir un objeto de datos en una cadena de caracteres de longitud fija, independientemente de la longitud de la información de entrada.

~~~python
def encriptar(frase):
    encriptado = sha3_256(frase.encode('utf-8')).hexdigest().upper()
    return ' '.join([encriptado[i:i + 4] for i in range(0,64,4)])
~~~


# REFERENCIAS

Romero Aguilar, R. (2019). Entendiendo el blockchain. Disponible en
https://www.secmca.org/wp-content/uploads/2019/12/Blockchain.pdf
