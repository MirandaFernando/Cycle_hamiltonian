import itertools
import json


def ReadJson():
    with open('Graph_districts.json', 'r', encoding='utf8') as f:
        return json.load(f)


def HamCycle(graph):
    routes = itertools.permutations(graph)
    hamilt_route = []
    quant_vert = graph.__len__()
    
    for route in routes:
        last = -1
        path = []
        for district in route:
            
            if(last == -1):
                last = district
                path.append(district)
                continue

            for key_district in range(quant_vert):

                if(graph[district][key_district] == 1 and graph[key_district] == graph[last]):
                    print("entrou")
                    last = district
                    path.append(district)
                    break 

            if(len(path) == quant_vert):
                if(graph[last][path[0]] == 1):
                    path.append(path[0])
                    hamilt_route.append(path)
    return hamilt_route


if __name__ == '__main__':
   graph = ReadJson()
   district_routes = HamCycle(graph)
   for district in district_routes:
       print(district)