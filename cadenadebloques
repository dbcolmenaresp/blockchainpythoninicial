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

# Clase para la creacion de los bloques
# Esta clase contiene todos los atributos y metodos propios de una cadena
# dentro de una blockchain

class Bloque:
    def __init__(self, indice, saldos, codigo_previo):
        self.indice = indice
        self.saldos = saldos
        self.codigo_previo = codigo_previo
        self.codigo = None
        self.transacciones = pd.DataFrame(columns=['Fecha', 'De', 'Para', 'Cantidad'])
        self.fecha_hora = datetime.now()
        
    def encriptar_bloque(self):
        datos = ['indice', 'saldos', 'codigo_previo', 'transacciones', 'fecha_hora']
        contenido = ''.join(str(getattr(self,campo)) for campo in datos)
        self.codigo = encriptar(contenido)
        
    def actualizar_transacciones(self, de, para, cantidad):
        T = self.transacciones.shape[0]
        self.transacciones.loc[T] = [datetime.now(), de, para, cantidad]
        
# Clase que define los bloques que conforman las cadenas

class BlockChain(list):
    def __init__(self):
        saldo_original = pd.Series({0}, index=['Banco Central'])
        bloque_original = Bloque(0, saldo_original, None)
        self.append(bloque_original)
        
    @property
    def bloque_actual(self):
        return self[-1]
        
    @property
    def saldos(self):
        return self.bloque_actual.saldos
    
    @property
    def transacciones(self):
        return pd.concat([bloque.transacciones for bloque in self], keys=[f'Bloque{k}' for k in range(len(self))])
    
    def emitir_Cocoins(self, cantidad):
        if cantidad < -self.bloque_actual.saldos['Banco Central']:
            print("No pueden destruirse más Cocoins que los que posee el Banco Central")
        else:
            self.bloque_actual.saldos['Banco Central'] += cantidad
            self.bloque_actual.actualizar_transacciones("Imprimiendo nuevos Cocoins", 'Banco Central', cantidad)
            
    def pagar(self, cuenta_origen, cuenta_destino, cantidad):
        cb = self.bloque_actual
        
        if cantidad < 0:
            print("El monto del pago no puede ser negativo.")
        elif cb.saldos[cuenta_origen] < cantidad:
            print(f"La cuenta {cuenta_origen} no tiene fondos suficientes!")
        else:
            if cuenta_destino not in cb.saldos.keys():
                cb.saldos[cuenta_destino] = 0
                
            cb.saldos[cuenta_origen] -= cantidad
            cb.saldos[cuenta_destino] += cantidad
            
            cb.actualizar_transacciones(cuenta_origen, cuenta_destino, cantidad)
            msg = '%12s le pagó %6.2f Cocoins a %s.'
            print(msg % (cuenta_origen, cantidad, cuenta_destino))
            
    def crear_siguiente_bloque(self):
        cb = self.bloque_actual
        cb.encriptar_bloque()
        self.append(Bloque(cb.indice + 1, db.saldos.copy(), cb.codigo))
        
    def verificar_integridad(self):
        anterior = self.bloque_actual.codigo_previo
        for bloque in self[-2::-1]:
            print(f'\nVerificando bloque{bloque.indice}', anterior, sep='\n')
            bloque.encriptar_bloque()
            print(bloque.codigo)
            
            if bloque.codigo != anterior:
                print('ADVERTENCIA: LA CADENA DE BLOQUES FUE ADULTERADA EN EL BLOQUE %d!!!' % bloque.indice)
                return
            else:
                anterior = bloque.codigo_previo
                
        print('LA CADENA DE BLOQUES ESTA BIEN!')
        
