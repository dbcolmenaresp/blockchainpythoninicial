# Blockchain con python inicial
Proyecto de implementacion de blockchain con Python nivel inicial

El blockchain es una tecnologia disruptiva que esta definiendo nuevas maneras de trabajar con la tecnologia

Primeramente se crea la función encargada de codificar una cadena de caracteres en hash

def encriptar(frase):
    encriptado = sha3_256(frase.encode('utf-8')).hexdigest().upper()
    return ' '.join([encriptado[i:i + 4] for i in range(0,64,4)])


REFERENCIAS
Romero Aguilar, R. (2019). Entendiendo el blockchain. Disponible en
https://www.secmca.org/wp-content/uploads/2019/12/Blockchain.pdf
