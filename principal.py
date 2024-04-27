from impresora import Cola
if __name__=='__main__':
    un_trabajo=Cola()
    tiempoSim=int(input("Ingrese el tiempo de la simulación en minutos < 5 minutos "))
    #maximo=int(input("Ingrese el máximo de la cola"))
    un_trabajo.Crear(tiempoSim)