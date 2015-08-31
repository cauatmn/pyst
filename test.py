__author__ = 'cm'
#! usr/bin/python
import math
L = [['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']]
print L[0][0]
print L[1][1]
print L[2][2]

def quadratic(a,b,c):
    if a == 0:
        return False
    x1 =(((-b)+math.sqrt(b*b-4*a*c))/(2*a))
    x2 = (((-b)-math.sqrt(b*b-4*a*c))/(2*a))
    print x1,x2
    return x1,x2

def power(x=3,n=2):
        s = 1
        while (n>0):
            n = n - 1
            s = s*x
        return s

if __name__ =='__main__':
    # quadratic(2,3,1)
   # quadratic(1,3,-4)
   #  print power(5,2)
   #  print power(6)
    #print power(n=3)
    L = list(range(100))
    print L
    print L[:10]
    print L[-10:]
    print L[10:20]
    print L[:10:2]
    print L[::5]