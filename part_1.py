import roboticstoolbox as rtb
import swift
import numpy as np
import spatialmath as sm
import spatialgeometry as sg
import math
import matplotlib
from matplotlib import pyplot as plt


# The rotation angle, to modify as requested
theta = np.pi/8;

# The rotation axis, to modify as requested
u = np.array([0, 0, 1])

# Normalisation of the rotation axis (do not modify)
u = u / np.linalg.norm(u)


# A generic rotation matrix about a unitary axis u and a theta angle (do not modify)
R = np.array([[u[0]**2*(1-np.cos(theta))+np.cos(theta), u[0]*u[1]*(1-np.cos(theta))-u[2]*np.sin(theta), u[0]*u[2]*(1-np.cos(theta))+u[1]*np.sin(theta)] ,\
			  [u[0]*u[1]*(1-np.cos(theta))+u[2]*np.sin(theta), u[1]**2*(1-np.cos(theta))+np.cos(theta), u[1]*u[2]*(1-np.cos(theta))-u[0]*np.sin(theta)] ,\
			  [u[0]*u[2]*(1-np.cos(theta))-u[1]*np.sin(theta), u[1]*u[2]*(1-np.cos(theta))+u[0]*np.sin(theta), u[2]**2*(1-np.cos(theta))+np.cos(theta)  ]])



# The l vector extracted from the rotation matrix (define using numpy)
#l = ...

# Check if l is a vector composed by zeros
if sm.base.iszerovec(l): 
	print('l is a zero vector')
else:
	print('l is NOT a zero vector')


print('l =',l)
print('norm(l) =',np.linalg.norm(l))
print('2 sin(theta) = ',2*np.sin(theta))
print('1/(2 sin(theta))=', 1/(2*np.sin(theta)))
print('R =',R)
print('trace de R =',np.trace(R))

