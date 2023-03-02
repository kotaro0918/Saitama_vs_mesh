import numpy as np
a=[11,10,22,20,33,30]
b=[10,20,30]
mesh_list=[]
for i in b:
    c=[j for j in a if 0<=(j-i)<=9]
    mesh_list[len(mesh_list):len(mesh_list)]=(np.array(range(min(c),max(c)+1,1)))
print(mesh_list)