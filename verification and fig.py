# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BLYpRUqqXA4wCvzVAZI6-tsfV8TssNMu
"""

# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BLYpRUqqXA4wCvzVAZI6-tsfV8TssNMu
"""

import matplotlib.pyplot as plt 
import numpy as np 
import subprocess
import shlex
plt.axis([0,6,-6,6])

plt.axis('on')

#finding the point P equidistant from A, B, C
A = np.array([[0,8],[4, 0]])
B = np.array([-8,12]) 
P = np.linalg.solve(A,B)
print(P)


A = np.array([5,3])
C = np.array([1,-5])
B = np.array([5,-5])


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

x_AP = line_gen(A,P)
x_CP = line_gen(C,P)
x_BP = line_gen(B,P)



def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

def dir_vec(A,B):
  return B-A

def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.vstack((n1,n2))
  O=np.linalg.inv(N)@p
  r = np.linalg.norm(A -O)
  return O,r

[O,R] = ccircle(A,B,C)
x_circ= circ_gen(O,R)

plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_BP[0,:],x_BP[1,:],label='$BP$')
plt.plot(x_CP[0,:],x_CP[1,:],label='$CP$')

plt.plot(x_circ[0,:],x_circ[1,:],label='$circumcircle$')


plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')

plt.text (5,3,'A(5,3)')
plt.text(5,-5,'B(5,-5)')
plt.text(1,-5,'C(1,-5)')
plt.text(3,-1,'P(3,-1)')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.savefig('equidistant point.png')
plt.show()

"""# New section"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

plt.axis([-6,5,-1,6])

plt.axis('on')
plt.grid(True)

A = np.array([[4,-1],
[2, -3]])
B = np.array([8,-6]) 
P = np.linalg.solve(A, B) 

C = np.array([[4,-1],
[0, 1]])
D = np.array([8,0]) 
Q = np.linalg.solve(C, D) 
print(Q)
E = np.array([[2,-3],
[0, 1]])
F = np.array([-6,0]) 
R = np.linalg.solve(E, F) 

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

  #Generating all lines
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RS$')

tri_coords = np.vstack((P,Q,R)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','R']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.savefig('line.pdf')
plt.show()