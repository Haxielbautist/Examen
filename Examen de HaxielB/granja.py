import conejo
import elefante
import perro

def ConstruirConejo(CantidadReproduccion,CantidadAnimales):
    c = Conejo.conejo(CantidadReproduccion,CantidadAnimales)
    return c

def ConstruirElefante(CantidadReproduccion,CantidadAnimales):
    e = elefante.elefante(CantidadReproduccion,CantidadAnimales)
    return e

def ContruirPerro(CantidadReproduccion,CantidadAnimales):
    p = perro.perro(CantidadReproduccion,CantidadAnimales)
    return p

def ImprimirMenu():
    print("1 Agregar Nuevo Animal\n2 Animales pregnados\n3 Alimentar Animales\n4Dar de beber")
    print("5 Salir")
    accion= int(input("Ingrese el numero de la accion que desea hacer "))
    return accion

def ImprimirAnimales():
    print("1 Conejos\n2 Elefante\n3 Perro")
    accion = int(input("Ingrese el numero de la accion que desea hacer "))
    return accion

conejoconstruido=False
elefanteconstruido=False
perroconstruido=False
salir=False

while not salir:
    accion = ImprimirMenu()
    if(accion==1):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            cantidadanimales=int(input("Ingrese la cantidad de conejos que tiene"))
            cantidadreproduccion=int(input("Ingrese la cantidad de animales por parto que puede tener un conejo"))
            conejoconstruido=ConstruirConejos(cantidadreproduccion,cantidadanimales)
        elif(tipoanimal==2):
            cantidadanimales=int(input("Ingrese la cantidad de elefantes que tiene"))
            cantidadreproduccion=int(input("Ingrese la cantidad de animales por parto que puede tener un elefante"))
            elefanteconstruido=ConstruirElefante(cantidadreproduccion,cantidadanimales)
        elif(tipoanimal==3):
            cantidadanimales=int(input("ingrese la cantidad de perros que tiene"))
            cantidadreproduccion=int(input("Ingrese la cantidad de animales por parto que puede tener un perro"))
            perrocontruido=ContruirPerro(cantidadreproduccion,cantidadanimales)
        else:
            print("El comando ingresado no se reconoce")
    elif(accion==2):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                cantidadanimalespreniados = int(input("Ingrese la cantidad de animales pregnados"))
                conejoconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print("No tiene conejos en su granja")
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                cantidadanimalespreniados = int(input("Ingrese la cantidad de animales pregnados"))
                elefanteconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print("No tiene elefantes en su granja")
        elif(tipoanimal==3):
            if(perroconstruido!=False):
                cantidadanimalespreniados = int(input("Ingrese la cantidad de animales pregnados"))
                perrosconstruido.Reproduccion(cantidadanimalespreniados)
            else:
                print("No tiene perros en su granja")
    elif(accion==3):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                tipoalimento=input("Ingrese el tipo de alimento que da a los conejos")
                cantidadalimento=int(input("Ingrese el tipo de alimento que da a los conejos"))
                conejoconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print("No tiene conejos en la granja")
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                tipoalimento=input("Ingrese el tipo de alimento que da a los elefantes")
                cantidadalimentos=int(input("Ingrese la cantidad de alimento"))
                elefanteconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print("No tiene elefante en su granja")
        elif(tipoanimal==3):
            if(perroconstruido!=False):
                tipoalimento=input("Ingrese el tipo de alimento que da a los perros")
                cantidadalimentos=int(input("Ingrese la cantidad de alimento"))
                perroconstruido.Alimentar(tipoalimento,cantidadalimento)
            else:
                print("No se recomoce el comando ingresado")
    elif(accion==4):
        tipoanimal=ImprimirAnimales()
        if(tipoanimal==1):
            if(conejoconstruido!=False):
                print("No puede dar de beber a los conejos")
            else:
                print("No tiene conejos en su granja")
        elif(tipoanimal==2):
            if(elefanteconstruido!=False):
                cantidadagua=int(input("Ingrese la cantidad de agua para los elefantes"))
                elefanteconstruido.Tomaragua(cantidadagua)
            else:
                print("No tiene elefantes en su granja")
        elif(tipoanimal==3):
            if(perrocontruido!=False):
                cantidadagua=int(input("ingrese la cantida de agua para los perros"))
                perrocontruido.Tomaragua(cantidadagua)
            else:
                print("No tiene perros en su granja")
        else:
            print("Comando ingresado desconocido")
    elif(accion==5):
        salir=True
    else:
        print("El comando ingresado no se reconoce")
