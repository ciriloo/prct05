#!usr/bin/python
pi=0
n=int(raw_input('Valor de n:'))
for i in range(1,n+1):
  x=(i-.5)/float(n)
 #print x
  fx=4/(1+(x*x))
 # print fx
  pi=pi+(fx)/n 
  print 'subintervalo: [%3.2f,%3.2f] x: %f fx: %6.5f '    %  ((i-1)/float(n), i/float(n), x, fx)
print 'El valor aproximado de PI es:  %f' %pi
print 'El valor de PI co 35 decimales :  3.1415926535897931159979634685441852'