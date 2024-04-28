class Cola:
    def __init__(self):
        self.max= 0 #cantidad maxima de elementos
        self.trabajos=[0] #arreglo de trabajos
        self.pr=0 #primer elemento
        self.ul=0 #ultimo elemento
        self.t_max=5    #tiempo maximo de procesamiento
        self.t_llegada=5
        self.cant=0
        
        
    def Crear(self, t_simula):
        self.max=(t_simula//self.t_llegada)
        print(f"La cantidad de elementos que se podrán almacenar es de {self.max} ")
        self.trabajos=[0]*self.max
        self.agrega()
        
    
    def llena(self):
        return(self.cant==self.max)

    
    
    
    def agrega(self):
        import random
        if(self.llena()==False): #SI, LA COLA ESTA llena, NO AGREGA ELEMENTOS
            if(self.cant<self.max):
                elemento=random.randint(1,10)
                if (self.cant==0): #Aun no se agregaron elementos
                    self.trabajos[self.pr]=elemento
                    self.trabajos[self.ul + 1]
                    self.cant+=1
                                                   
        elif self.cant==self.max:   #Estamos al tope de la cola
            print("Se salio del if ")
        self.mostrar_cola()
        
    
    def mostrar_cola(self):
        for i in self.trabajos:
            print(f"[{i}]")
        
    
            
        
            
            
        

        





















"""
    
    def Nodo(self,valor,esperando):
        self.__valor=valor
        self.__esperand=esperando
        self.__siguiente=None
    
    def getValor(self):
        return self.__valor
    
    def setValor(self,valor):
        self.__valor = valor

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,sig):
        self.__siguiente = sig

    def getEspernado(self):
        return self.__esperando
    
    def setEsperando(self,esperando):
        self.__esperando = esperando
        
        
                
    def genera_elemento(self,maximo):      #genera tiempo de impresión para la cola
        import random
        tiempo= random.randint(1,10)
        self.max=maximo
        print(f"el tiempo es {tiempo}")
        self.inserta(tiempo)
        return
    
    def inserta(self, elemento):
        
        while self.m>0: #vamos a insertar el primer elemento
            self.trabajos[self.ul]=elemento
            #print(f"elemento en la cola {self.trabajos[self.ul]}")
            if self.max==self.max:
                print("La cola esta llena ")
        print("La cola está vacía ")
        
        return
    
    def mostrar(self):
        for i in self.trabajos:
            print(f" elemento {i}, {self.trabajos}")
            
"""            
        
