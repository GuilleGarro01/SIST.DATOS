class Cola:
    def __init__(self):
        self.max= 0 #cantidad maxima de elementos
        self.trabajos=[0] #arreglo de trabajos
        self.pr=None #primer elemento
        self.ul=None #ultimo elemento
        self.t_max=5    #tiempo maximo de procesamiento
        self.t_llegada=5
        self.cant=None
        
        
    def Crear(self, t_simula):
        self.max=(t_simula//self.t_llegada)
        print(f"La cantidad de elementos que se podrán almacenar es de {self.max} ")
        self.trabajos=[0]*self.max
        self.agrega(self.generaElemento)
        
    
    def vacia(self):
        return(self.cant==0)
    
    def generaElemento(self):
        import random
        elementos=random.randint(1,50)
        return(elementos)
    
    
    
    def agrega(self,elemento):
        while(self.vacia()!=0):
            if self.pr==None and self.ul==None:
                self.pr+=1
                self.ul+=1
                self.trabajos[self.pr]=elemento
            elif self.pr<=self.ul:
                self.ul+=1
                self.trabajos[self.ul]=elemento
            elif self.__primero>self.__ultimo:
                self.__primero=-1
                self.__ultimo=-1
            self.insertar(elemento)
        #print("La cola esta llena ")
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
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""def inserta(self,elemento):
        print("ingresa al inserta")
        print(f"Valor de cant {self.cant} ")
        if self.max > 0:
            if (self.cant)== 0: #(self.max):
                self.ul = (self.ul + 1) % self.max
                print("Entra al if inserta") 
                self.trabajos[self.ul]=elemento
                self.ul=(self.ul+1)%self.max 
                self.cant=+1
            else:
                print("Sale de inserta por else")
        return 


    
    def vacia(self):
        return(self.cant==0)  #nos devuelve si está vacío
    
    def suprime(self):
        self.pr=(self.pr+1)%self.max
        #Actualiza el índice del primer elemento (pr) de la cola para que apunte al siguiente elemento en la cola circular. Se utiliza el operador módulo % para asegurar que el índice permanezca dentro de los límites del tamaño máximo de la cola 
        self.cant-=1
        return
    
    def reingrese(self,i):
        pendiente=self.trabajos[i]-5
        self.trabajos[self.ul]=pendiente
        self.ul=(self.ul+1)%self.max
        self.cant=+1
        self.suprime()
        return
        
            
    def imprime(self):  #al momento de la impresión, debe suprimir elementos de la lista y reprogramar aquellos que son >5
        if (self.vacia()!=0): #si la cola está vacia
            print("n\ No quedan elementos por imprimir")

        else:   #si la cola NO está vacia
            for i in self.trabajos:
                if self.trabajos[i]<5 or self.trabajos[i]==5:
                    print(f"Elemento suprimido: {self.trabajos[i]} ")
                    self.suprime()
                elif self.trabajos[i]>5:
                    self.reingrese(i)
    
    
        
                
                    
                
            
        
def vacia(self):
        return(self.cant==0)
    

        
    def suprimir(self):
        elemento=0
        if(self.vacia()):
            print("n/Pila vacia")
            return(0)
        else:
            self.elemento=self.item[self.pr]
            self.pr=(self.pr+1)%max
            self.cant-1
            return(self.elemento)
    def recorrer(self):
        i=0
        j=0
        if (vacia())
        i=self.pr
            j=0
            for(i;j<cant;i=(i+1)%max,j+1):"""