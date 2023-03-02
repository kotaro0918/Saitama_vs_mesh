import numpy as np
a=[11,10,22,20,33,33]
b=[10,20,30]
for i in b:
    c=[j for j in a if 0<=(j-i)<=9]
    print(np.array(range(min(c),max(c),1)))