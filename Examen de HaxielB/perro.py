import Animales

class perro(Animales.Animal):
    def TomarAgua(self,cantidadagua):
        self.cantidadagua+=cantidadagua
        print("El perro tiene {0} litros de agua".format(self.cantidadagua))

    def Alimentar(self,tipoalimento,cantidadalimento):
        if(tipoalimento.lower()=="dogui"):
            self.cantidadalimento+=cantidadalimento
        else:
            print("Solo me alimento de dogui")
