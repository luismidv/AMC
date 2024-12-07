#FIRST IMPLEMENTATION EXHAUSTIVE VORAZ
#PRIMERA ITERACCIÓN VER
from os import close

import pandas as pd
import math

from fontTools.merge.util import first


class Algorithm:
    def __init__(self,cities):
        self.nodes_coordinates = cities
        self.current_city = ""
        self.current_city_bidirectional= ""
        self.first_city = ""
        self.first_city_bidirectional = ""


    def __getcities__(self):
        print(self.nodes_coordinates)

    def calculate_distance(self,coord1,coord2):
        distancex = coord2[0] - coord1[0]
        distancey = coord2[1] - coord1[1]
        distance = distancex**2 + distancey**2
        result = math.sqrt(distance)
        #print(result)
        return result

    def cities_exhaustive2(self):
        counter = 0
        for city2 in self.nodes_coordinates.keys():
            for city3 in self.nodes_coordinates.keys():
                if city3 != city2:
                    counter+=1
                    distance = self.calculate_distance(nodes[city2],nodes[city3])
                    distances[city2].append((city3,distance))

    def city_calculator(self,distances,current_city):
        print(f"Tenemos el diccionario {distances} \n"
              f"Distancia para la ciudad {current_city}")
        if current_city == "":
            current_city = input("Choose a city to start: ")
        min_distance_city = min(distances[current_city], key=lambda x: x[1])
        return min_distance_city
    #EXHAUSTIVE
    def city_runner_exhaustive(self, distances):
        my_cities = list(distances.keys())
        self.current_city = input("Choose a city to start: ")
        self.first_city = self.current_city
        while(len(list(distances.keys())) > 1):
            print(distances)
            print(f"Iteraccion numero {len(list(distances.keys()))}")
            closest_city = self.city_calculator(distances,self.current_city)
            print(f"Closes city to {self.current_city} | {closest_city}")
            del distances[self.current_city]
            distances = self.dictionar_iterator(distances,self.current_city)
            self.current_city = closest_city[0]
            print(f"Current city: {self.current_city}")
            print(f"Cities left {distances}")

        current_city = self.first_city
        print(F"Volvemos a {self.first_city}")

    def dictionar_iterator(self,distances,city):
        print(f"Procedemos a borrar {city}")
        my_dict = {
            k: [tupla for tupla in v if city not in tupla]
            for k, v in distances.items()
        }
        return my_dict

    def bidirectional_forward(self,distances,visited):
        self.current_city_bidirectional = input("Choose a city to start: ")
        self.first_city_bidirectional = self.current_city_bidirectional

        sorted_distances = {
            city : sorted(distances, key=lambda x: x[1])for city,distances in distances.items()
        }

        closest_city = self.city_calculator(sorted_distances, self.first_city_bidirectional)
        second_closest_city = self.city_calculator(sorted_distances, self.first_city_bidirectional)

        closest_city_name = closest_city[0]
        first_visited = visited[closest_city_name]
        first_visited = first_visited[0]
        second_visited = False
        if first_visited == False:
            print(f"{closest_city[0]} es visitable")
        else:
            print(visited[closest_city[0]])

            print(f"{closest_city[0]} es not visitable")

        if second_visited == False:
            print(f"{second_closest_city[0]} es visitable")
        else:
            print(f"{second_closest_city[0]} es not visitable")




nodes = {
    'huelva' : (20,50),
    'sevilla' : (10,20),
    'valencia': (20,30),
    'mursia' : (30,70)
}

distances = {
    'huelva' : [],
    'sevilla' : [],
    'valencia': [],
    'mursia' : []
}

visited = {
    'huelva' : (False,False),
    'sevilla': (False, False),
    'valencia': (False, False),
    'mursia': (False, False)
}




myalgo = Algorithm(nodes)
myalgo.cities_exhaustive2()
#myalgo.city_calculator(distances)
#myalgo.city_runner(distances)
#myalgo.city_runner_exhaustive(distances)
myalgo.bidirectional_forward(distances,visited)
