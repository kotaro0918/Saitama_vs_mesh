import math
def mesh_count(a):
    lg_result=str(math.floor(a[0]-100))
    la_aspect=str(math.floor(a[1])*(1.5)+(a[1]-math.floor(a[1]))*(0.9))
    la_result=la_aspect.split('.')[0]
    return(la_result+lg_result)
a=[139.08301630405936, 36.21773002681944]
print(mesh_count(a))