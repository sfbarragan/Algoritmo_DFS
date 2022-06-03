#importamos la libreria Queue
from queue import Queue

class Grafo:
    """
    Clase Grafo, esta clase representara a un grafo junto a sus atributos y funcionalidades,

     Atributos
    ----------
        m_numero_nodos : int
            Cantidad de nodos que tendra el grafo.
        m_nodos : int
            Rango de nodos sobre los que trabajara el grafo.
        m_dirigido : boolean
            Tipo de nodo dirigido o no dirigido.
        m_lista_adyacencia : diccionario
            Diccionario que almacena el valor de los nodos


     Métodos
    ----------

    __init__(self, num_de_nodos, dirigido=True)
        Este metodo funcionara como el constuctor de la clase `Grafo()`, recibe el Numero de nodos (m_num_nodos),
        crea el rango de nodos (numero_nodos), determina el tipo de grafo si es dirigido o no dirigido (m_dirigido) y
        creara el diccionario de la lista de adyacencia.

    agregar_borde(self, nodo1, nodo2, peso=1)
        Genera los bordes de la lista de adyacencia agregando el nodo 2 a la lista de adyacencia del nodo 1.

    Imprimir_lista_adyacencia(self)
        Imprime el grafo generado en base a la lista de adyacencia.

    dfs(self, inicio, objetivo, ruta = [], visitado = set())
        Método que imprime el recorrido BFS de un vértice fuente dado.
    """

    def __init__(self, numero_nodos, dirigido=True):
        """
        Este metodo funcionara como el constuctor de la clase Grafo(), recibe el Numero de nodos (m_num_nodos),
        crea el rango de nodos (numero_nodos), determina el tipo de grafo si es dirigido o no dirigido (m_dirigido) y
        creara el diccionario de la lista de adyacencia.


        Parametros
        ----------
        m_numero_nodos : int
            Cantidad de nodos que tendra el grafo.
        m_nodos : int
            Rango de nodos sobre los que trabajara el grafo.
        m_dirigido : boolean
            Tipo de nodo dirigido o no dirigido.
        m_lista_adyacencia : diccionario
            Diccionario que almacena el valor de los nodos
        """
        # Se asigna el valor del numero de nodos a través del parametro recibido
        self.m_numero_nodos = numero_nodos
        # Se genera el rango de nodos en base a m_numero_nodos
        self.m_nodos = range(self.m_numero_nodos)
        # se define el tipo de grafo
        self.m_dirigido = dirigido
        # Se crea el diccionario de la lista de adyacencia
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}

   
    def agregar_borde(self, nodo1, nodo2, peso=1):
        """
        Este método define el borde de la lista de adyacencia.
        Recibe como parametros el nodo1, el nodo2 y el peso cuyo valor por defecto es de 1.
        Posteriormente se agregan a la lista de adyacencia del nodo al que corresponde.

        Parametros
        ----------
        nodo1 : int
        nodo2 : int
        peso: int

        Retorno
        -------
        Nada 
        """
        # Agrega el nodo 2 a la lista de adyacencia del nodo 1.
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        if not self.m_dirigido:
            # Agrega el nodo 1 a la lista de adyacencia del nodo 2.
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))


    def Imprimir_lista_adyacencia(self):
        """
        Este método imprime el grafo generado a través de la lista de adyacencia.

        Parametros
        ----------
        Nada

        Retorno
        -------
        Nada 
        """
        # recorre la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            # imprime el cada nodo almacenado en la lista de adyacencia.
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])


    def dfs(self, inicio, objetivo, ruta = [], visitado = set()):
        """
        Este método imprime el recorrido dfs generado a través de un nodo inicial y un nodo objetivo.
        Genera una lista de los nodos visitados y muestra el recorrido realizado hasta llegar al objetivo. 

        Parametros
        ----------
        ruta : lista
        visitado : diccionario

        Retorno
        -------
        ruta / resultado / None 
        """

        ruta.append(inicio) #se agrega a la ruta el nodo inicial
        visitado.add(inicio) #se agrega a la la lista de nodos visitados el nodo inicial

        if inicio == objetivo:  #Si inicio es igual a objetivo
            return ruta #Retorna la ruta
            
        for(vecino, peso) in self.m_lista_adyacencia[inicio]: #Bucle que recorrera la lista de adyacencia
            if vecino not in visitado:  #Si el vecino no se encuentra en el diccionario de nodos visitados
                resultado = self.dfs(vecino, objetivo, ruta, visitado) #se asigna a la variable resultado el nodo vecino, el objetivo, la ruta y la lista de nodos visitados
                
                if resultado is not None: #Si la lista resultado no esta vacio
                    return resultado #Retorna resultado
                    
        
        ruta.pop() # elimina y retorna el elemento de la ruta
        return None 


if __name__ == "__main__":
    """
    Dentro de la clase main se instancia a la clase Grafo para acceder a sus metodos.
    Se crearan en este caso 5 casos de prueba para comprobar el funcionamiento del programa.
    """
    
    
    print("Caso de Prueba 1")
    grafo1 = Grafo(5, dirigido=False)#Se instancia la clase Grafo

 
    grafo1.agregar_borde(0, 1) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo1.agregar_borde(0, 2) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo1.agregar_borde(1, 3) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo1.agregar_borde(2, 3) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo1.agregar_borde(3, 4) # Se agrega los bordes del grafo con valor peso = 1 por defecto

    grafo1.Imprimir_lista_adyacencia() #Imprime la lista de adyacencia

    ruta_transversal1 = [] # Se inicializa la variable ruta_transversal
    ruta_transversal1 = grafo1.dfs(0, 3) # Se almacena el recorrido dfs en la variable ruta_transversal
    print(f"La ruta transversal desde el nodo 0 al nodo 3 es {ruta_transversal1}") #Imprime el recorriodo dfs

    """
    
    print("Caso de Prueba 2")
    grafo2 = Grafo(5, dirigido=False)#Se instancia la clase Grafo

 
    grafo2.agregar_borde(0, 4) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo2.agregar_borde(0, 3) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo2.agregar_borde(1, 2) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo2.agregar_borde(2, 0) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo2.agregar_borde(3, 4) # Se agrega los bordes del grafo con valor peso = 1 por defecto

    grafo2.Imprimir_lista_adyacencia() #Imprime la lista de adyacencia

    ruta_transversal2 = [] # Se inicializa la variable ruta_transversal
    ruta_transversal2 = grafo2.dfs(0, 4) # Se almacena el recorrido dfs en la variable ruta_transversal
    print(f" La ruta transversal desde el nodo 0 al nodo 4 es {ruta_transversal2}") #Imprime el recorriodo dfs

    """
    
    """
    print("Caso de Prueba 3")
    grafo3 = Grafo(6, dirigido=False)#Se instancia la clase Grafo

 
    grafo3.agregar_borde(1, 2) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo3.agregar_borde(1, 0) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo3.agregar_borde(0, 2) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo3.agregar_borde(5, 3) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo3.agregar_borde(2, 3) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo3.agregar_borde(1, 4) # Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo3.agregar_borde(2, 5) # Se agrega los bordes del grafo con valor peso = 1 por defecto

    grafo3.Imprimir_lista_adyacencia() #Imprime la lista de adyacencia

    ruta_transversal3 = [] # Se inicializa la variable ruta_transversal
    ruta_transversal3 = grafo3.dfs(1, 5) # Se almacena el recorrido dfs en la variable ruta_transversal
    print(f" La ruta transversal desde el nodo 1 al nodo 5 es {ruta_transversal3}") #Imprime el recorriodo dfs

   """
