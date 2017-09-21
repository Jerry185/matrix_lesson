from numpy import *
#--------------------------------
#余弦夹角

a=array([1,2,3])
b=array([4,5,6])
c=a+b
la=a.dot(a)
lb=b.dot(b)
print(la,lb)
print(c)
print(c.dot(c))
cosab=a.dot(b)/(la*lb)
print(cosab)
print()
