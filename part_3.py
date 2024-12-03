import roboticstoolbox as rtb
import swift
import numpy as np
import spatialmath as sm
import spatialgeometry as sg
import math
import matplotlib
from matplotlib import pyplot as plt
from commande import *

# The rotation angle, to modify as requested
theta = np.pi;

# The rotation axis, to modify as requested
u = np.array([1, 0.3, 1])
u = np.array([1, -0.3, 1])
#u = np.array([1, 0.3, -1])
#u = np.array([1, -0.3, -1])
#u = np.array([1, -0.3, 1])
#u = np.array([-1, 0.3, -1])


# Normalisation of the rotation axis (do not modify)
u = u / np.linalg.norm(u)


# A generic rotation matrix about a unitary axis u and a theta angle (do not modify)
R = np.array([[u[0]**2*(1-np.cos(theta))+np.cos(theta), u[0]*u[1]*(1-np.cos(theta))-u[2]*np.sin(theta), u[0]*u[2]*(1-np.cos(theta))+u[1]*np.sin(theta)] ,\
			  [u[0]*u[1]*(1-np.cos(theta))+u[2]*np.sin(theta), u[1]**2*(1-np.cos(theta))+np.cos(theta), u[1]*u[2]*(1-np.cos(theta))-u[0]*np.sin(theta)] ,\
			  [u[0]*u[2]*(1-np.cos(theta))-u[1]*np.sin(theta), u[1]*u[2]*(1-np.cos(theta))+u[0]*np.sin(theta), u[2]**2*(1-np.cos(theta))+np.cos(theta)  ]])


u_est = determine_signs(R)
print('u=',u)
print('u_est =',u_est)



