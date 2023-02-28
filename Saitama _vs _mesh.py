import json
import collections
def mesh_count(a):
    lg_list=str(a[0]).split('.')
    lg_result=str(int(lg_list[0])-100)
    la_list=str(a[1]).split('.')
    la_aspect=str(float(la_list[0])*(1.5)+(float(a[1])-float(la_list[0]))*(0.9))
    la_result=la_aspect.split('.')[0]
    return(la_result+lg_result)
json_open = open('Saitama.json','r')
json_load = json.load(json_open)
key_list = list(json_load.keys())
features_list=json_load['features']
mesh_list=[]
for i in range(2): 
    polygon_dic=features_list[0]
    coordinates_dic=polygon_dic['geometry']
    coordinates_list=coordinates_dic['coordinates'][i][0]
    for j in range(len(coordinates_list)):
        mesh_list.append(mesh_count(coordinates_list[j]))
c = collections.Counter(mesh_list)
for key in sorted(c.keys()):
    print("11:{mesh}".format(mesh=key))
