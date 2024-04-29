import random
class Cola:
    def __init__(self):
        self.__max= 0 #cantidad maxima de elementos
        self.__trabajos=[0] #arreglo de trabajos
        self.__pr=0 #primer elemento
        self.__ul=0 #ultimo elemento
        self.__t_max=5    #tiempo maximo de procesamiento
        self.__t_llegada=5
        self.__cant=0
        
        
    def Crear(self, t_simula):
        self.__max=(t_simula//self.__t_llegada)
        print(f"La cantidad de elementos que se podrán almacenar es de {self.__max} ")
        self.trabajos=[0]*self.__max
        self.agrega()
        
    
 

    
    
    
    def agrega(self):
        print(f"valor de max {self.__max}, valor de cant {self.__cant}")
        if(self.__cant<=self.__max):
            print("Entra al if ")
            elemento=random.randint(1,10)
            self.__trabajos[self.__ul]=elemento
            self.__ul=(self.__ul+1)
            self.__cant+=1 
        else:
            if self.__cant==self.__max:   #Estamos al tope de la cola
                print("La cola se encuentra llena ")
        return (self.agrega())
        
        
        
    
    def mostrar_cola(self):
        for i in self.__trabajos:
            print(f"[{i}]")
