from pylab import *
from math import *
print'n,x,jn(x)'
x=[0.1,0.2,0.3,0.4,0.5]
for n in range(1,6):
    for i in x:
        i/=2.0
        term=[]
        term.append(i**n/factorial(n))
        for p in range(1,10):
            term.append(-term[p-1]*i*i/(p*(p+n)))
            print ('j%d(%4.2f)=%5.3f%(n,2*i,sum(term))')