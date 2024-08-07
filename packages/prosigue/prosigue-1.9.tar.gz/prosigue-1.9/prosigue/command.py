
""" Modulo de libreria Prosigue """


"==================================================="

from multiprocessing import Process, Queue, Value
from prosigue.another_bookstores.do_hasta_time import Hasta_time
import os


class De_traspaso:
    
    def __init__(self):
        
        self.trasp_1= 0
        self.trasp_2= 2
            
"==================================================="

# Clases que realizan el proceso Prosigue

class Prosigue:
    
    def __init__(self, el_code, salida_externa= False):

        self.sentencia= el_code
        self.metaversion= True

        if salida_externa == True:
            self.metaversion= False

        if salida_externa == False:
            self.iterador= Queue()

        self.acces= True
        self.answer= None
        self.time_2= None
        
        self.dato= De_traspaso()
        self.balum= Hasta_time()
        
    def entry(self, dato= None):
        self.previo_mega= dato

    def tiempo(self, time):
        self.time_2= time

    def accion(self):
        
        if self.metaversion == False:
            self.sentencia.empieza(self.previo_mega)
        else:
            self.sentencia.empieza(self.previo_mega, self.iterador)
                    
    "......................................"
    
    def primero(self, puente):

        my_id= os.getpid()
        puente.trasp_1.value= my_id
        
        self.accion()
        self.procesando(puente)
    
    def procesando(self, puen):
                
        if self.acces is True: # Se esta confirmando...
            puen.trasp_2.value= 1

    "......................................"

    def cloud_rain(self):
        
        self.iterador= Queue()
        
        return self.iterador

    def close(self, finish= False):
        
        self.finish= finish # se termina cuando el script finaliza
        
        self.dato.trasp_1= Value("i", 0)
        self.dato.trasp_2= Value("i", 0)

        proceso_1= Process(target= self.primero, args= (self.dato,))
        proceso_1.start()

        confir_time= False
        while confir_time == False:
            
            if self.dato.trasp_2.value == 1: # puede ser inocuo
                if self.finish == True:
                    break   # porque ya se cerro se sale

            ya_esta= self.balum.acaso(self.time_2)
            
            if ya_esta == True:
                
                os.system("taskkill /PID {} /F".format(self.dato.trasp_1.value))
                self.acces= False
                confir_time= True
        
        "......................................"

        self.answer= self.dato.trasp_2.value
        
        my_data= None
        my_data= self.iterador.get()
        return my_data
    
    "......................................"

    def imagen_reset(self, proceso):
        
        proceso.termina(False)

