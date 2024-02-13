# coding: utf-8
# Codigo que implementa la encriptacion sha3 256

from hashlib import sha3_256 # libreria usada para encriptar informacion
from datetime import datetime # Contiene fecha y hora para registrar transacciones
import numpy as np # 
import pandas as pd # Facilita el almacenamiento de datos
from random import randint, sample # Usado para simulaciones

def encriptar(frase):
    encriptado = sha3_256(frase.encode('utf-8')).hexdigest().upper()
    return ' '.join([encriptado[i:i + 4] for i in range(0,64,4)])
    
print(encriptar('Consejo Monetario Centroamericano'))
