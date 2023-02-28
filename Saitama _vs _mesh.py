import json
import math
import collections
def mesh_count(a):
    lg_result=str(math.floor(a[0]-100))
    la_aspect=str(math.floor(a[1])*(1.5)+(a[1]-math.floor(a[1]))*(0.9))
    la_result=la_aspect.split('.')[0]
    return(la_result+lg_result)
json_open = open('Saitama.geojson','r')
json_load = json.load(json_open)
features_list=json_load['features']
mesh_list=[]
polygon_dic=features_list[0]
coordinates_dic=polygon_dic['geometry']
for i in range(len(coordinates_dic)): 
    coordinates_list=coordinates_dic['coordinates'][i][0]
    for j in range(len(coordinates_list)):
        mesh_list.append(mesh_count(coordinates_list[j]))
c = collections.Counter(mesh_list)
print(c)
for key in sorted(c.keys()):
    print("11:{mesh}".format(mesh=key))
