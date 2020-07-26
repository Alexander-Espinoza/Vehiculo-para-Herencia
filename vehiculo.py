class Vehiculo():

    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enMarcha=True
    
    def acelerar(self):
        self.acelera=True   

    def frenar(self):
        self.frena=True
    
    def estado(self):
        print ("""Marca: {} 
                \nModelo: {}
                \nEn marcha: {}
                \nAcelerando: {}
                \nFrenando: {}
                """.format(self.marca,self.modelo,self.enMarcha,self.acelera,self.frena))

class VElectrico():
    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True

class Furgoneta(Vehiculo):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            print("La furgoneta está cargada")
        else: 
            print("La furgoneta no está cargada")

class Moto(Vehiculo):
    hacerCaballito=""
    def caballito(self):
        self.hacerCaballito="Voy haciendo el caballito"

    def estado(self):
        print ("""Marca: {} 
                \nModelo: {}
                \nEn marcha: {}
                \nAcelerando: {}
                \nFrenando: {}
                \n{}
                """.format(self.marca,self.modelo,self.enMarcha,self.acelera,self.frena,self.hacerCaballito))

class BicicletaElectrica(Vehiculo,VElectrico):
    pass

miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

print("----------------------------------")
miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.carga(True)
print("----------------------------------")

miBici=BicicletaElectrica("Bach","LR1")
miBici.estado()

