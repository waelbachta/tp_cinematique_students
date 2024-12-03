import math
from spatialmath import SE3, base
import numpy as np


# to use if the rotation angle error is equal to pi
# R is the rotation matrix associated to the rotation error
def determine_signs(R):
    
    # squared rotation vector
    u_2 = (np.diag(R)+1)/2
    
   
    # extracting the parameters to simplify the code
    u_xy = R[0,1]
    u_xz = R[0,2]
    u_yz = R[1,2]

    # creating an empty vector to be latter assigned to the rotation vector
    axe = np.empty(3)


    # The vectors reported here are valid even if their opposite is taken (pi rotation)
    if (u_xy>=0)&(u_xz>=0)&(u_yz>=0):
        axe[0] = 0.1
        axe[1] = 0.0
        axe[2] = 0.0
        

    elif (u_xy>=0)&(u_xz<0)&(u_yz<0):
        axe[0] = 0.1
        axe[1] = 0.0
        axe[2] = 0.0
        

    elif (u_xy<0)&(u_xz>=0)&(u_yz<0):
        axe[0] = 0.0
        axe[1] = 0.0
        axe[2] = 0.0
        

    elif (u_xy<0)&(u_xz<0)&(u_yz>=0):
        axe[0] = 0.0
        axe[1] = 0.0
        axe[2] = 0.0
    
    return axe

# returns the error vector e, and the angular error theta
# inputs : T the current homogoneous transformation 0->e and Td : the target 0-->d
def compute_error(T, Td):
    
    # initializing an empty error array
    e = np.empty(6)

    # Computing the error homogenous transformation martix expressed in the end-effector frame
    T_e = np.linalg.inv(T)@Td

    # Filling in the translation error expressed in the end-effector frame
    e[:3] = T_e[:3,-1]

    # Compution the error rotation matrix expressed in the end-effector frame
    R = T_e[:3, :3]


    # Compute the rotation axis expressed in the end-effector frame
    l = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]])
    
    # Computing the rotation axis and angle
    # 1/Check if the vector in nill
    if base.iszerovec(l):
        if np.trace(R) > 0:
            # Modify and set the correct u
            u = np.zeros(3)
            # Modify and set the correct theta
            theta = 0.0
        else:
            # Modify and set the correct u
            u = np.zeros(3)
            # Modify and set the correct theta
            theta = 0.0
    else:
        # Modify and set the norm of l
        ln = 1
        # Modify and set the correct theta
        theta = 0.0
        # Modify and set the correct u
        u = np.zeros(3)

        
    e[3:] = u

    return e, theta

# returns the desired joints velocities(qd_tilde), the arrived flag, e and theta (vector and theta error)
# inputs : The robot instance, the current and the target transformations, the error accepted threshold and the current arrived flag

def cartesian_control(robot, T, Td, gain, threshold, arrived):

    # Computing the error 
    e, theta = compute_error(T, Td)
    
    # if the error is greater than the accepted threshold, we compute a control input
    if (np.sum(np.abs(e)) > threshold):
        # Modify to set the control input in the operational space
        ee_twist= np.zeros(6)

        # Modify to setthe control in the joint space : obtaining the robot jacobian in the end effector
        # frame can be obtained by using robot.jacobe(robot.q)
        qd_tilde = np.zeros(6)

    else:
        qd_tilde = np.zeros(6)

    arrived = True if np.sum(np.abs(e)) < threshold else False

    return qd_tilde, arrived, e, theta