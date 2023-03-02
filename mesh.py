import json
import math
import collections
import sys
lev = sys.argv
mesh_list_1=[]
mesh_list_2=[]
def mesh_count_1(a):
    lg_result=str(math.floor(a[0]-100))
    la_aspect=str(math.floor(a[1])*(1.5)+(a[1]-math.floor(a[1]))*(0.9))
    la_result=la_aspect.split('.')[0]
    mesh_list_1.append(la_result+lg_result)
def mesh_count_2(a):
    lg_result_1=math.floor(a[0]-100)
    lg_result_2=int((a[0]-math.floor(a[0]))//0.125)
    la_result_1=int((a[1])*(60)//40)
    la_result_2=int(int((a[1])*(60)%40)//5)
    mesh_list_1.append((la_result_1*10000+lg_result_1*100+la_result_2*10+lg_result_2))
    mesh_list_2.append((la_result_1*10000+lg_result_1*100+la_result_2*10))
json_file=lev[2]
json_open = open(json_file,'r')
json_load = json.load(json_open)
features_list=json_load['features']
if lev[1] == "level1":
    polygon_dic=features_list[0]
    coordinates_dic=polygon_dic['geometry']
    for i in range(len(coordinates_dic)): 
        coordinates_list=coordinates_dic['coordinates'][i][0]
        for j in range(len(coordinates_list)):
            mesh_count_1(coordinates_list[j])
    c = collections.Counter(mesh_list_1)
    for key in sorted(c.keys()):
        print(key)
if lev[1] == "level2":
    polygon_dic=features_list[0]
    coordinates_dic=polygon_dic['geometry']
    for i in range(len(coordinates_dic)): 
        coordinates_list=coordinates_dic['coordinates'][i][0]
        for j in range(len(coordinates_list)):
            mesh_count_2(coordinates_list[j])
    c = collections.Counter(mesh_list_1)
    d = collections.Counter(mesh_list_2)
    for key in sorted(c.keys()):
        print(key)
    for key in sorted(d.keys()):
        print(key)
    