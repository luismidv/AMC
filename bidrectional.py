import pandas as pd
from fontTools.merge.util import first
import math




def calculate_distance(first_city,second_city):
    #FUNCION QUE UTILIZAREMOS PARA EL CALCULO DE LAS DISTANCIAS ENTRE CIUDADES
    distance = (second_city[0] - first_city[0])**2 + (second_city[1] - first_city[1])**2
    return math.sqrt(distance)


def dataframe_builder(nodes,visited_dataframe):
    #RECIBE UN DICCIONARIO PYTHON CON LAS CIUDADES Y SUS COORDENADAS
    #CREA UN DATAFRAME PANDAS CON CADA UNA DE LAS CIUDADES Y LA DISTANCIA A LA QUE SE ENCUENTRA DEL RESTO DE CIUDADES
    #MANDA ESTOS DATOS A UN FICHERO distances.CSV EN LA CARPETA DATA
    for city in nodes.keys():
        city_list = []
        for city2 in nodes.keys():
            distancia = calculate_distance(list(nodes[city]), list(nodes[city2]))
            city_list.append(distancia)

        dataframe_distances[city] = city_list
        visited_dataframe[city] = (False,False)

    dataframe_distances.to_csv('data/distances.csv')

class Bidirectional_algorithm():
    def __init__(self,dataframe_distances, visited_dataframe ):
        self.dataframe_distances = dataframe_distances
        self.visited_dataframe = visited_dataframe
        self.current_city_first = ""
        self.current_city_second = ""

    def city_runner(self):
        #PREGUNTA POR LA CIUDAD A LA QUE QUEREMOS IR PRIMERO
        #FILTRAMOS EL DATAFRAME QUITANDO LA PROPIA CIUDAD EN LA QUE ESTAMOS
        #EN ESA CIUDAD CALCULA LA CIUDAD MÁS CERCANA
        #VAMOS FILTRANDO EL DATAFRAME PARA QUE ELIMINE LA CIUDAD QUE ACABAMOS DE RECORRER
        #DE MANERA QUE IREMOS ORDENANDO LA LISTA DE MENOR A MAYOR DISTANCIA, COGIENDO LA DE MENOR DISTANCIA
        #ESTO OCURRIRÁ MIENTRAS QUE EL NUMERO DE CIUDADES A LAS QUE HEMOS ACCEDIDO SEA MENOR QUE EL TOTAL DE CIUDADES
        self.number_visited = 0
        self.city_traveled_first = []
        self.city_traveled_second = []

        #PEDIMOS UNA CIUDAD POR LA QUE EMPEZAR
        self.current_city_first = input("Enter a city to start")
        self.visited_dataframe.loc['Runner 1', self.current_city_first] = True

        print(f"Primero en visitar {self.current_city_first} \n {self.visited_dataframe}")
        self.number_visited +=1

        #FILTERED DATAFRAME ELIMINATING SELF CITY
        self.all_cities = self.dataframe_distances.columns
        number_cities = len(self.all_cities)
        column = dataframe_distances[self.current_city_first]
        column = column[column != 0]

        first_iteration = True
        while self.number_visited < number_cities:
            #ELIMINAMOS LA PRIMERA CIUDAD PARA QUE NO LA TENGA EN CUENTA AL SELECCIONAR LA MÁS CERCANA

            column = column[column.index != self.current_city_first]
            column = column.sort_values()
            print(f"Buscamos la ciudad más cercana\n -----------------------------------------------\n{column}")

            #ESTE CODIGO SOLO SE EJECUTARA PARA LA PRIMERA ITERACCIÓN, LA DE LA CIUDAD INICIAL
            if first_iteration == True:
                first_iteration = False
                min_distance_value = column.iloc[0]

                #SELECCIONAMOS LA MÁS CERCANA AL CORREDOR 1
                self.current_city_first = column.index[0]
                self.visited_dataframe_process(self.current_city_first, "Runner 1")

                #SELECCIONAMOS LA SEGUNDA MÁS CERCANA AL CORREDOR 2
                self.current_city_second = column.index[1]
                self.visited_dataframe_process(self.current_city_second, "Runner 2")

                print(f"Ciudades {column}")

            else:
                #SE EJECUTARA PARA EL RESTO DE ITERACCIONES
                self.runner_advance("Runner 1")
                self.runner_advance("Runner 2")



    def visited_dataframe_process(self, runner_city, runner):
        print(f"El corredor uno ha llegado a las ciudades \n {self.city_traveled_first}")
        print(f"El corredor dos ha llegado a las ciudades \n {self.city_traveled_second}")

        if self.visited_dataframe[runner_city][runner] == False:
            self.visited_dataframe.loc[runner,runner_city] = True

            if runner == "Runner 1":
                self.current_city_first = runner_city
                self.city_traveled_first.append(runner_city)

            elif runner == "Runner 2":
                self.current_city_second = runner_city
                self.city_traveled_second.append(runner_city)
            self.number_visited += 1

        else:
            print("Intentando guardar entrara a una ciudad ya accedida")


    def runner_advance(self, runner):
        #DEFINE LAS CIUDADES POR LA QUE IRÁ PASANDO CADA UNO DE LOS CORREDORES

        #PRIMERO VERIFICAREMOS PARA QUE CORREDOR PERTENECE ESTA EJECUCIÓN
        if runner == "Runner 1":
            runner_city = self.current_city_first
        elif runner == "Runner 2":
            runner_city = self.current_city_second

        #FILTRAMOS LOS VALORES DEL DATAFRAME PARA LA CIUDAD EN LA QUE SE ENCUENTRA ACTUALMETE EL CORREDOR DE LA EJECUCIÓN
        column = dataframe_distances[runner_city]
        column = column[column != 0]

        #VOLVEMOS A FILTAR PARA ELIMINAR LAS CIUDADES QUE YA HAN SIDO RECORRIDAS
        for city in (self.city_traveled_first + self.city_traveled_second):
            column = column[column.index != city]
        column = column.sort_values()

        #SI LA EJECUCION ES DEL CORREDOR UNO ASIGNAMOS LA CIUDAD MÁS CERCANA AL CORREDOR 1
        if runner == "Runner 1":
            self.current_city_first = column.index[0]
            self.visited_dataframe_process(self.current_city_first, "Runner 1")

        #SI LA EJECUCION ES DEL CORREDOR DOS ASIGNAMOS LA CIUDAD MÁS CERCANA AL CORREDOR 2
        elif runner == "Runner 2":
            self.current_city_second = column.index[0]
            self.visited_dataframe_process(self.current_city_second, "Runner 2")

nodes = {
    'huelva' : (20,50),
    'sevilla' : (10,20),
    'valencia': (20,30),
    'mursia' : (30,70),
    'cordoba': (40,80),
    'osuna' : (20,40),
    'badajoz' : (30,50)
}

distances = {
    'huelva' : [],
    'sevilla' : [],
    'valencia': [],
    'mursia' : []
}
dataframe_distances = pd.DataFrame(index = nodes.keys(), columns=nodes.keys())
visited_dataframe = pd.DataFrame(index = ("Runner 1", "Runner 2"), columns = nodes.keys())

dataframe_builder(nodes,visited_dataframe)
print(f"{dataframe_distances} \n --------------------------------------------------------" )
print(visited_dataframe)
bidir_algorithm = Bidirectional_algorithm(dataframe_distances,visited_dataframe)
bidir_algorithm.city_runner()
print(f"Recorrido del primer runner {bidir_algorithm.city_traveled_first}")
print(f"Recorrido del segundo runner {bidir_algorithm.city_traveled_second}")