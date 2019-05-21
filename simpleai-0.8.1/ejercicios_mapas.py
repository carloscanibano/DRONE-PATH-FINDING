'''
    Busqueda no informada
    
    Para cualquier problema hay que implementar los siguientes metodos:
      actions: LISTA de acciones posibles en cierto estado: (accion1,accion2,...)
      result: LISTA (estado,accion)
      is_goal: TRUE si es un estado final
      cost: Coste de ir de un estado a otro mediante cierta accion
      heuristic: Valor de h(estado)

    Con WebViewer(), hay que conectarse al servidor para visualizar la ejecucion:
      http://localhost:8000/#

    Problema 3.1.1:
      Estado inicial: A
      Acciones: mover a un estado conectado
      Objetivo: H
      Heuristic: no
      Algorithm: breadth-first

    Problema 3.1.2:
      Estado inicial: A
      Acciones: mover a un estado conectado
      Objetivo: E
      Heuristic: no
      Algorithm: breadth-first

    Problema 3.1.3:
      Estado inicial: B
      Acciones: mover a un estado conectado
      Objetivo: H
      Heuristic: no
      Algorithm: breadth-first

    Problema 3.2: ATENCION, ESTA IMPLEMENTACION CAMBIA EL ORDEN
      Estado inicial: A
      Acciones: mover a un estado conectado
      Objetivo: H
      Heuristic: no
      Algorithm: depth-first

'''
from simpleai.search import SearchProblem, astar
from simpleai.search import breadth_first,depth_first
from simpleai.search.viewers import BaseViewer,ConsoleViewer,WebViewer

#
# DECLARACION DE LA CLASE MapProblem
# Se etiqueta con class y se pone la clase de la que deriva entre parentesis
#
# Los metodos son funciones declaradas dentro
# No es necesario, pero puede crearse un constructor __init__ (consultar)
# Se llama a los metodos y miembros de la clase usando explicitamente el objeto self
#
class MapProblem(SearchProblem):
    # En esta seccion inicializamos si queremos los atributos del objeto
    MAPA=None
    GOAL=None

    # Este prefijo solo sirve para mostar un nombre para la accion
    PREFIJO_ACCION='mover-'

    # --------------- Metodos Comunes a todo problema SearchProblem -----------------
    # Los implementamos de la siguiente manera
    # Cargamos una variable self.MAPA con las transiciones entre estados
    # Las acciones posibles son mover a los posibles estados directamente conectados
    #
    def actions(self, state):
        # ESTE METODO DEBE DEVOLVER UNA LISTA DE ACCIONES POSIBLES
        #
        # Vamos a dar a las acciones el nombre mover+el indice de cada destion
        # Asi, si hay dos destinos, tendermos mover1,mover2
        # Los indices son indiferentes, solo los anyadimos porque las acciones son distintas
    
        # La funcion range genera un vector entre el primer indice y el elemento anterior al ultimo
        vectorIndices=range(1,len(self.MAPA[state])+1)
        
        # Usamos la sintaxis de generadores para construir la lista
        # Usamos list() para que el resultado sea tipo lista
        # Usamos el operador de concatenar '+' para unir dos strings
        # Usamos la funcion str para convertir entero en string
        # Usamos la estructura mas tipica del bucle for
        acciones=list(self.PREFIJO_ACCION+str(i) for i in vectorIndices)

        # Devolvemos el resultado
        return acciones
    

    def result(self, state, action):
        # ESTE METODO DEBE DEVOLVER UN ESTADO
        # Contamos en que posicion del string empieza el numero
        inicio=len(self.PREFIJO_ACCION)
        # Slice de un string. Si el final no se especifica, llega hasta el final
        numeroAccion=action[inicio:]
        # Acceso a un elemento de una lista por su numero de orden. Conversion a entero
        return self.MAPA[state][int(numeroAccion)-1]

    def is_goal(self, state):
        # ESTE METODO DEBE DEVOLVER UN BOOLEANO (True: estado final)
        return state == self.GOAL

    def cost(self, state, action, state2):
        '''Returns the cost of applying `action` from `state` to `state2`.
           The returned value is a number (integer or floating point).
           By default this function returns `1`.
        '''
        return 1

    def heuristic(self, state):
        # ESTE METODO DEBE DEVOLVER UN VALOR NUMERICO H(estado)
        return 0

    # --------------- Metodos Especificos de los problemas MapProblem -----------------
    # El parametro inicial solo se introduce si es distinto de None

    def setParameters(self,mapa,final,inicial=None):
        # Como inicial es un parametro de la clase padre, hay que llamar a su constructor
        # Aqui comprobabos si un parametro existe de forma correcta en Python
        if inicial is not None:
            super(MapProblem,self).__init__(inicial)
        self.MAPA=mapa
        self.GOAL=final

# --------------- Metodos FUERA DE LA CLASE MapProblem -----------------

# El parametro algorithm es un metodo de busqueda, que se invocara internamente
# El parametro use_viewer determina si se usa o no el visor web
def ejercicioMapa(problem,algorithm,use_viewer=None):
    # ESTE METODO ES GENERICO PARA CUALQUIER MAPA
    # Previamente habremos llamado a setParameters para decir que mapa y que estado final
    
    
    # La primera linea es util para depurar con prints. En el interfaz web
    # esas salidas no se muestran.
    # Breadth-first es como el nuestro, pero solo comprueba al cerrar los nodos
    result = algorithm(problem,graph_search=True,viewer=use_viewer)
    
    # La llamada devuelve el estado en que termina la busqueda
    print("Estado final:" + result.state)
    
    # La llamada devuelve el camino hasta dicho estado.
    # Usamos format para presentar
    print("Camino: {0}".format(result.path()))
    
    # Ejemplo de creacion de una lista de pares {name,value}
    # No es necesario poner if not my_viewer == None
    if use_viewer:
        stats = [{'name': stat.replace('_', ' '), 'value': value}
                         for stat, value in list(use_viewer.stats.items())]
        
        # Ejemplo de bucle sobre elementos de una lista
        # Y comparacion de la presentacion con format y con un string concatenado
        for s in stats:
#            print (s['name']+': ' + str(s['value']))
            print ('{0}: {1}'.format(s['name'],s['value']))

    return result
# FIN de ejercicioMapa

# ------------  Aqui empieza el codigo que se ejecuta al cargar el script -------------

#
# REPRESENTACION DE LOS ESTADOS
#
# Los estados solo contienen la informacion de su nombre.
# Por lo tando no hace falta tener estructura, basta un string para identificarlos
#
# Como a cada vertice de un grafo le corresponde una lista de vertices conectados,
# la estructura adecuada es un diccionario.
# La lista de destinos aparece ordenada segun el criterio del problema
#
ejercicio3_1_mapa =  {'A': # vertice
                          ('B','C'), # lista de posibles destinos
                     'B': ('D','E'),
                     'C': ('E'),
                     'D': ('F','G'),
                     'E': ('G','H'),
                     'F': (), # Podemos crear una lista vaciaa
                     'G': ('H') } # Cerramos la variable

ejercicio3_1_inicial='A'
ejercicio3_1_final='H'

#
# REPRESENTACION DE LAS ACCIONES
#
# Implicita 'mover-i': ver el metodo actions

# -------------------------  RESOLUCION DE LOS PROBLEMAS ----------------------

# RESOLUCION DEL PROBLEMA 3.1.1
# Para crear un problema basta crear un objeto de esa clase y luego
# llamar a .setParameters con los parametros
problem = MapProblem()
problem.setParameters(mapa=ejercicio3_1_mapa,inicial=ejercicio3_1_inicial,final=ejercicio3_1_final)

# NOTA: ejercicioMapa es una funcion de este modulo, no un metodo
# Aqui es donde podemos seleccionar WebViewer,ConsoleViewer o BaseViewer
#   BaseViewer() simplemente ejecuta y muestra las trazas y estadisticas
#   ConsoleViewer() permite ejecutar paso a paso por pantalla
#      NOTA: Para usar esto, mejor hacemos un parche a este viewer, 
#            Si no, hay que poner la opcion entre comillas
#   WebViewer() usa el interfaz web
#
# ejercicioMapa(problem,algorithm=breadth_first,use_viewer=WebViewer())
ejercicioMapa(problem,algorithm=breadth_first,use_viewer=BaseViewer())


# RESOLUCION DEL PROBLEMA 3.1.2
problem.setParameters(mapa=ejercicio3_1_mapa,inicial=ejercicio3_1_inicial,final='E')
ejercicioMapa(problem,algorithm=breadth_first,use_viewer=BaseViewer())

# RESOLUCION DEL PROBLEMA 3.1.3
problem.setParameters(mapa=ejercicio3_1_mapa,inicial='B',final=ejercicio3_1_final)
ejercicioMapa(problem,algorithm=breadth_first,use_viewer=BaseViewer())

# RESOLUCION DEL PROBLEMA 3.2
ejercicio3_2_mapa =  {'A': # vertice
                          ('C','B'), # lista de posibles destinos
                     'B': ('E','D'),
                     'C': ('E'),
                     'D': ('G','F'),
                     'E': ('H','G'),
                     'F': (), # Podemos crear una lista vacia
                     'G': ('H') } # Cerramos la variable
ejercicio3_2_inicial='A'
ejercicio3_2_final='H'


problem.setParameters(mapa=ejercicio3_2_mapa,inicial=ejercicio3_2_inicial,final=ejercicio3_2_final)
ejercicioMapa(problem,algorithm=depth_first,use_viewer=BaseViewer())
    
