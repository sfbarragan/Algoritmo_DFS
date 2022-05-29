#importamos la librerioa Queue
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