def mesh_count(a):
    lg_list=a[0].split('.')
    lg_result=str(int(lg_list[0])-100)
    la_list=a[1].split('.')
    la_aspect=str(float(la_list[0])*(1.5)+(float(a[1])-float(la_list[0]))*(0.9))
    la_result=la_aspect.split('.')[0]
    return(la_result+lg_result)
a=['139.08301630405936', '36.21773002681944']
print(mesh_count(a))