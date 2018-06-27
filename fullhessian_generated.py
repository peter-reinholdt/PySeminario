import numpy as np
from math import sqrt

def radius_first_derivative(X1,Y1,Z1,X2,Y2,Z2,d1):
    output = 0.0
    if d1.upper() == "X1":
        output = radius_dX1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y1":
        output = radius_dY1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z1":
        output = radius_dZ1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X2":
        output = radius_dX2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y2":
        output = radius_dY2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z2":
        output = radius_dZ2(X1,Y1,Z1,X2,Y2,Z2)
    else:
        print("radius_first_derivative not understood")
    return output

def theta_first_derivative(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,d1):
    output = 0.0
    if d1.upper() == "X1":
        output = theta_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y1":
        output = theta_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z1":
        output = theta_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X2":
        output = theta_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y2":
        output = theta_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z2":
        output = theta_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X3":
        output = theta_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y3":
        output = theta_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z3":
        output = theta_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    else:
        print("theta_first_derivative not understood")
    return output

def phi_first_derivative(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4,d1):
    output = 0.0
    if d1.upper() == "X1":
        output = phi_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1":
        output = phi_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1":
        output = phi_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2":
        output = phi_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2":
        output = phi_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2":
        output = phi_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3":
        output = phi_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3":
        output = phi_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3":
        output = phi_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4":
        output = phi_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4":
        output = phi_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4":
        output = phi_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    else:
        print("phi_first_derivative not understood")
    return output

def radius_second_derivative(X1,Y1,Z1,X2,Y2,Z2,d1,d2):
    output = 0.0
    if d1 .upper()== "X1" and d2.upper() == "X1":
        output = radius_dX1_dX1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X1" and d2.upper() == "Y1":
        output = radius_dX1_dY1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X1" and d2.upper() == "Z1":
        output = radius_dX1_dZ1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X1" and d2.upper() == "X2":
        output = radius_dX1_dX2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X1" and d2.upper() == "Y2":
        output = radius_dX1_dY2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X1" and d2.upper() == "Z2":
        output = radius_dX1_dZ2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y1" and d2.upper() == "X1":
        output = radius_dY1_dX1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y1" and d2.upper() == "Y1":
        output = radius_dY1_dY1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y1" and d2.upper() == "Z1":
        output = radius_dY1_dZ1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y1" and d2.upper() == "X2":
        output = radius_dY1_dX2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y1" and d2.upper() == "Y2":
        output = radius_dY1_dY2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y1" and d2.upper() == "Z2":
        output = radius_dY1_dZ2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z1" and d2.upper() == "X1":
        output = radius_dZ1_dX1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z1" and d2.upper() == "Y1":
        output = radius_dZ1_dY1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z1" and d2.upper() == "Z1":
        output = radius_dZ1_dZ1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z1" and d2.upper() == "X2":
        output = radius_dZ1_dX2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z1" and d2.upper() == "Y2":
        output = radius_dZ1_dY2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z1" and d2.upper() == "Z2":
        output = radius_dZ1_dZ2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X2" and d2.upper() == "X1":
        output = radius_dX2_dX1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X2" and d2.upper() == "Y1":
        output = radius_dX2_dY1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X2" and d2.upper() == "Z1":
        output = radius_dX2_dZ1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X2" and d2.upper() == "X2":
        output = radius_dX2_dX2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X2" and d2.upper() == "Y2":
        output = radius_dX2_dY2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "X2" and d2.upper() == "Z2":
        output = radius_dX2_dZ2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y2" and d2.upper() == "X1":
        output = radius_dY2_dX1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y2" and d2.upper() == "Y1":
        output = radius_dY2_dY1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y2" and d2.upper() == "Z1":
        output = radius_dY2_dZ1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y2" and d2.upper() == "X2":
        output = radius_dY2_dX2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y2" and d2.upper() == "Y2":
        output = radius_dY2_dY2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Y2" and d2.upper() == "Z2":
        output = radius_dY2_dZ2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z2" and d2.upper() == "X1":
        output = radius_dZ2_dX1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z2" and d2.upper() == "Y1":
        output = radius_dZ2_dY1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z2" and d2.upper() == "Z1":
        output = radius_dZ2_dZ1(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z2" and d2.upper() == "X2":
        output = radius_dZ2_dX2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z2" and d2.upper() == "Y2":
        output = radius_dZ2_dY2(X1,Y1,Z1,X2,Y2,Z2)
    elif d1.upper() == "Z2" and d2.upper() == "Z2":
        output = radius_dZ2_dZ2(X1,Y1,Z1,X2,Y2,Z2)
    else:
        print("radius_second_derivative not understood")
    return output

def theta_second_derivative(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,d1,d2):
    output = 0.0
    if d1.upper() == "X1" and d2.upper() == "X1":
        output = theta_dX1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X1" and d2.upper() == "Y1":
        output = theta_dX1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X1" and d2.upper() == "Z1":
        output = theta_dX1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X1" and d2.upper() == "X2":
        output = theta_dX1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X1" and d2.upper() == "Y2":
        output = theta_dX1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X1" and d2.upper() == "Z2":
        output = theta_dX1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X1" and d2.upper() == "X3":
        output = theta_dX1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X1" and d2.upper() == "Y3":
        output = theta_dX1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X1" and d2.upper() == "Z3":
        output = theta_dX1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y1" and d2.upper() == "X1":
        output = theta_dY1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y1" and d2.upper() == "Y1":
        output = theta_dY1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y1" and d2.upper() == "Z1":
        output = theta_dY1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y1" and d2.upper() == "X2":
        output = theta_dY1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y1" and d2.upper() == "Y2":
        output = theta_dY1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y1" and d2.upper() == "Z2":
        output = theta_dY1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y1" and d2.upper() == "X3":
        output = theta_dY1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y1" and d2.upper() == "Y3":
        output = theta_dY1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y1" and d2.upper() == "Z3":
        output = theta_dY1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z1" and d2.upper() == "X1":
        output = theta_dZ1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z1" and d2.upper() == "Y1":
        output = theta_dZ1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z1" and d2.upper() == "Z1":
        output = theta_dZ1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z1" and d2.upper() == "X2":
        output = theta_dZ1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z1" and d2.upper() == "Y2":
        output = theta_dZ1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z1" and d2.upper() == "Z2":
        output = theta_dZ1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z1" and d2.upper() == "X3":
        output = theta_dZ1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z1" and d2.upper() == "Y3":
        output = theta_dZ1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z1" and d2.upper() == "Z3":
        output = theta_dZ1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X2" and d2.upper() == "X1":
        output = theta_dX2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X2" and d2.upper() == "Y1":
        output = theta_dX2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X2" and d2.upper() == "Z1":
        output = theta_dX2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X2" and d2.upper() == "X2":
        output = theta_dX2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X2" and d2.upper() == "Y2":
        output = theta_dX2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X2" and d2.upper() == "Z2":
        output = theta_dX2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X2" and d2.upper() == "X3":
        output = theta_dX2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X2" and d2.upper() == "Y3":
        output = theta_dX2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X2" and d2.upper() == "Z3":
        output = theta_dX2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y2" and d2.upper() == "X1":
        output = theta_dY2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y2" and d2.upper() == "Y1":
        output = theta_dY2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y2" and d2.upper() == "Z1":
        output = theta_dY2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y2" and d2.upper() == "X2":
        output = theta_dY2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y2" and d2.upper() == "Y2":
        output = theta_dY2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y2" and d2.upper() == "Z2":
        output = theta_dY2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y2" and d2.upper() == "X3":
        output = theta_dY2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y2" and d2.upper() == "Y3":
        output = theta_dY2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y2" and d2.upper() == "Z3":
        output = theta_dY2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z2" and d2.upper() == "X1":
        output = theta_dZ2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z2" and d2.upper() == "Y1":
        output = theta_dZ2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z2" and d2.upper() == "Z1":
        output = theta_dZ2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z2" and d2.upper() == "X2":
        output = theta_dZ2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z2" and d2.upper() == "Y2":
        output = theta_dZ2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z2" and d2.upper() == "Z2":
        output = theta_dZ2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z2" and d2.upper() == "X3":
        output = theta_dZ2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z2" and d2.upper() == "Y3":
        output = theta_dZ2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z2" and d2.upper() == "Z3":
        output = theta_dZ2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X3" and d2.upper() == "X1":
        output = theta_dX3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X3" and d2.upper() == "Y1":
        output = theta_dX3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X3" and d2.upper() == "Z1":
        output = theta_dX3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X3" and d2.upper() == "X2":
        output = theta_dX3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X3" and d2.upper() == "Y2":
        output = theta_dX3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X3" and d2.upper() == "Z2":
        output = theta_dX3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X3" and d2.upper() == "X3":
        output = theta_dX3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X3" and d2.upper() == "Y3":
        output = theta_dX3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "X3" and d2.upper() == "Z3":
        output = theta_dX3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y3" and d2.upper() == "X1":
        output = theta_dY3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y3" and d2.upper() == "Y1":
        output = theta_dY3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y3" and d2.upper() == "Z1":
        output = theta_dY3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y3" and d2.upper() == "X2":
        output = theta_dY3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y3" and d2.upper() == "Y2":
        output = theta_dY3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y3" and d2.upper() == "Z2":
        output = theta_dY3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y3" and d2.upper() == "X3":
        output = theta_dY3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y3" and d2.upper() == "Y3":
        output = theta_dY3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Y3" and d2.upper() == "Z3":
        output = theta_dY3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z3" and d2.upper() == "X1":
        output = theta_dZ3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z3" and d2.upper() == "Y1":
        output = theta_dZ3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z3" and d2.upper() == "Z1":
        output = theta_dZ3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z3" and d2.upper() == "X2":
        output = theta_dZ3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z3" and d2.upper() == "Y2":
        output = theta_dZ3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z3" and d2.upper() == "Z2":
        output = theta_dZ3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z3" and d2.upper() == "X3":
        output = theta_dZ3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z3" and d2.upper() == "Y3":
        output = theta_dZ3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    elif d1.upper() == "Z3" and d2.upper() == "Z3":
        output = theta_dZ3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)
    else:
        print("theta_second_derivative not understood")
    return output

def theta_second_derivative(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4,d1,d2):
    output = 0.0
    if d1.upper() == "X1" and d2.upper() == "X1":
        output = phi_dX1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X1" and d2.upper() == "Y1":
        output = phi_dX1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X1" and d2.upper() == "Z1":
        output = phi_dX1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X1" and d2.upper() == "X2":
        output = phi_dX1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X1" and d2.upper() == "Y2":
        output = phi_dX1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X1" and d2.upper() == "Z2":
        output = phi_dX1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X1" and d2.upper() == "X3":
        output = phi_dX1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X1" and d2.upper() == "Y3":
        output = phi_dX1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X1" and d2.upper() == "Z3":
        output = phi_dX1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X1" and d2.upper() == "X4":
        output = phi_dX1_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X1" and d2.upper() == "Y4":
        output = phi_dX1_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X1" and d2.upper() == "Z4":
        output = phi_dX1_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "X1":
        output = phi_dY1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "Y1":
        output = phi_dY1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "Z1":
        output = phi_dY1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "X2":
        output = phi_dY1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "Y2":
        output = phi_dY1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "Z2":
        output = phi_dY1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "X3":
        output = phi_dY1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "Y3":
        output = phi_dY1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "Z3":
        output = phi_dY1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "X4":
        output = phi_dY1_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "Y4":
        output = phi_dY1_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y1" and d2.upper() == "Z4":
        output = phi_dY1_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "X1":
        output = phi_dZ1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "Y1":
        output = phi_dZ1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "Z1":
        output = phi_dZ1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "X2":
        output = phi_dZ1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "Y2":
        output = phi_dZ1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "Z2":
        output = phi_dZ1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "X3":
        output = phi_dZ1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "Y3":
        output = phi_dZ1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "Z3":
        output = phi_dZ1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "X4":
        output = phi_dZ1_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "Y4":
        output = phi_dZ1_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z1" and d2.upper() == "Z4":
        output = phi_dZ1_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "X1":
        output = phi_dX2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "Y1":
        output = phi_dX2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "Z1":
        output = phi_dX2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "X2":
        output = phi_dX2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "Y2":
        output = phi_dX2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "Z2":
        output = phi_dX2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "X3":
        output = phi_dX2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "Y3":
        output = phi_dX2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "Z3":
        output = phi_dX2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "X4":
        output = phi_dX2_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "Y4":
        output = phi_dX2_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X2" and d2.upper() == "Z4":
        output = phi_dX2_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "X1":
        output = phi_dY2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "Y1":
        output = phi_dY2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "Z1":
        output = phi_dY2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "X2":
        output = phi_dY2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "Y2":
        output = phi_dY2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "Z2":
        output = phi_dY2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "X3":
        output = phi_dY2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "Y3":
        output = phi_dY2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "Z3":
        output = phi_dY2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "X4":
        output = phi_dY2_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "Y4":
        output = phi_dY2_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y2" and d2.upper() == "Z4":
        output = phi_dY2_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "X1":
        output = phi_dZ2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "Y1":
        output = phi_dZ2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "Z1":
        output = phi_dZ2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "X2":
        output = phi_dZ2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "Y2":
        output = phi_dZ2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "Z2":
        output = phi_dZ2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "X3":
        output = phi_dZ2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "Y3":
        output = phi_dZ2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "Z3":
        output = phi_dZ2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "X4":
        output = phi_dZ2_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "Y4":
        output = phi_dZ2_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z2" and d2.upper() == "Z4":
        output = phi_dZ2_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "X1":
        output = phi_dX3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "Y1":
        output = phi_dX3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "Z1":
        output = phi_dX3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "X2":
        output = phi_dX3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "Y2":
        output = phi_dX3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "Z2":
        output = phi_dX3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "X3":
        output = phi_dX3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "Y3":
        output = phi_dX3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "Z3":
        output = phi_dX3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "X4":
        output = phi_dX3_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "Y4":
        output = phi_dX3_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X3" and d2.upper() == "Z4":
        output = phi_dX3_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "X1":
        output = phi_dY3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "Y1":
        output = phi_dY3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "Z1":
        output = phi_dY3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "X2":
        output = phi_dY3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "Y2":
        output = phi_dY3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "Z2":
        output = phi_dY3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "X3":
        output = phi_dY3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "Y3":
        output = phi_dY3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "Z3":
        output = phi_dY3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "X4":
        output = phi_dY3_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "Y4":
        output = phi_dY3_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y3" and d2.upper() == "Z4":
        output = phi_dY3_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "X1":
        output = phi_dZ3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "Y1":
        output = phi_dZ3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "Z1":
        output = phi_dZ3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "X2":
        output = phi_dZ3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "Y2":
        output = phi_dZ3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "Z2":
        output = phi_dZ3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "X3":
        output = phi_dZ3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "Y3":
        output = phi_dZ3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "Z3":
        output = phi_dZ3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "X4":
        output = phi_dZ3_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "Y4":
        output = phi_dZ3_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z3" and d2.upper() == "Z4":
        output = phi_dZ3_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "X1":
        output = phi_dX4_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "Y1":
        output = phi_dX4_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "Z1":
        output = phi_dX4_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "X2":
        output = phi_dX4_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "Y2":
        output = phi_dX4_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "Z2":
        output = phi_dX4_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "X3":
        output = phi_dX4_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "Y3":
        output = phi_dX4_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "Z3":
        output = phi_dX4_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "X4":
        output = phi_dX4_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "Y4":
        output = phi_dX4_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "X4" and d2.upper() == "Z4":
        output = phi_dX4_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "X1":
        output = phi_dY4_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "Y1":
        output = phi_dY4_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "Z1":
        output = phi_dY4_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "X2":
        output = phi_dY4_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "Y2":
        output = phi_dY4_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "Z2":
        output = phi_dY4_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "X3":
        output = phi_dY4_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "Y3":
        output = phi_dY4_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "Z3":
        output = phi_dY4_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "X4":
        output = phi_dY4_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "Y4":
        output = phi_dY4_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Y4" and d2.upper() == "Z4":
        output = phi_dY4_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "X1":
        output = phi_dZ4_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "Y1":
        output = phi_dZ4_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "Z1":
        output = phi_dZ4_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "X2":
        output = phi_dZ4_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "Y2":
        output = phi_dZ4_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "Z2":
        output = phi_dZ4_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "X3":
        output = phi_dZ4_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "Y3":
        output = phi_dZ4_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "Z3":
        output = phi_dZ4_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "X4":
        output = phi_dZ4_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "Y4":
        output = phi_dZ4_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    elif d1.upper() == "Z4" and d2.upper() == "Z4":
        output = phi_dZ4_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)
    else:
        print("phi_second_derivative not understood")
    return output

def radius_dX1(X1,Y1,Z1,X2,Y2,Z2):
    return (1.0*X1 - 1.0*X2)*((X1 - X2)**2 + (Y1 - Y2)**2 + (Z1 - Z2)**2)**(-0.5)

def radius_dY1(X1,Y1,Z1,X2,Y2,Z2):
    return (1.0*Y1 - 1.0*Y2)*((X1 - X2)**2 + (Y1 - Y2)**2 + (Z1 - Z2)**2)**(-0.5)

def radius_dZ1(X1,Y1,Z1,X2,Y2,Z2):
    return (1.0*Z1 - 1.0*Z2)*((X1 - X2)**2 + (Y1 - Y2)**2 + (Z1 - Z2)**2)**(-0.5)

def radius_dX2(X1,Y1,Z1,X2,Y2,Z2):
    return (-1.0*X1 + 1.0*X2)*((X1 - X2)**2 + (Y1 - Y2)**2 + (Z1 - Z2)**2)**(-0.5)

def radius_dY2(X1,Y1,Z1,X2,Y2,Z2):
    return (-1.0*Y1 + 1.0*Y2)*((X1 - X2)**2 + (Y1 - Y2)**2 + (Z1 - Z2)**2)**(-0.5)

def radius_dZ2(X1,Y1,Z1,X2,Y2,Z2):
    return (-1.0*Z1 + 1.0*Z2)*((X1 - X2)**2 + (Y1 - Y2)**2 + (Z1 - Z2)**2)**(-0.5)

def theta_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x0*x4 + x1*x5 + x2*x6
    x9 = x7**(-0.5)
    return -(-x3**(-1.5)*x8*x9*(-1.0*X1 + 1.0*X2) - x3**(-0.5)*x4*x9)/sqrt(-x3**(-1.0)*x7**(-1.0)*x8**2 + 1)

def theta_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x0*x4 + x1*x5 + x2*x6
    x9 = x7**(-0.5)
    return -(-x3**(-1.5)*x8*x9*(-1.0*Y1 + 1.0*Y2) - x3**(-0.5)*x5*x9)/sqrt(-x3**(-1.0)*x7**(-1.0)*x8**2 + 1)

def theta_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x0*x4 + x1*x5 + x2*x6
    x9 = x7**(-0.5)
    return -(-x3**(-1.5)*x8*x9*(-1.0*Z1 + 1.0*Z2) - x3**(-0.5)*x6*x9)/sqrt(-x3**(-1.0)*x7**(-1.0)*x8**2 + 1)

def theta_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x0*x4 + x1*x5 + x2*x6
    x9 = x3**(-0.5)
    x10 = x7**(-0.5)
    x11 = -1.0*X2
    return -(-x10*x3**(-1.5)*x8*(1.0*X1 + x11) - x10*x9*(X1 - 2*X2 + X3) - x7**(-1.5)*x8*x9*(1.0*X3 + x11))/sqrt(-x3**(-1.0)*x7**(-1.0)*x8**2 + 1)

def theta_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x0*x4 + x1*x5 + x2*x6
    x9 = x3**(-0.5)
    x10 = x7**(-0.5)
    x11 = -1.0*Y2
    return -(-x10*x3**(-1.5)*x8*(1.0*Y1 + x11) - x10*x9*(Y1 - 2*Y2 + Y3) - x7**(-1.5)*x8*x9*(1.0*Y3 + x11))/sqrt(-x3**(-1.0)*x7**(-1.0)*x8**2 + 1)

def theta_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x0*x4 + x1*x5 + x2*x6
    x9 = x3**(-0.5)
    x10 = x7**(-0.5)
    x11 = -1.0*Z2
    return -(-x10*x3**(-1.5)*x8*(1.0*Z1 + x11) - x10*x9*(Z1 - 2*Z2 + Z3) - x7**(-1.5)*x8*x9*(1.0*Z3 + x11))/sqrt(-x3**(-1.0)*x7**(-1.0)*x8**2 + 1)

def theta_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x0*x4 + x1*x5 + x2*x6
    x9 = x3**(-0.5)
    return -(-x7**(-1.5)*x8*x9*(1.0*X2 - 1.0*X3) - x7**(-0.5)*x9*(-X1 + X2))/sqrt(-x3**(-1.0)*x7**(-1.0)*x8**2 + 1)

def theta_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x0*x4 + x1*x5 + x2*x6
    x9 = x3**(-0.5)
    return -(-x7**(-1.5)*x8*x9*(1.0*Y2 - 1.0*Y3) - x7**(-0.5)*x9*(-Y1 + Y2))/sqrt(-x3**(-1.0)*x7**(-1.0)*x8**2 + 1)

def theta_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x0*x4 + x1*x5 + x2*x6
    x9 = x3**(-0.5)
    return -(-x7**(-1.5)*x8*x9*(1.0*Z2 - 1.0*Z3) - x7**(-0.5)*x9*(-Z1 + Z2))/sqrt(-x3**(-1.0)*x7**(-1.0)*x8**2 + 1)

def phi_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = Y2 - Y3
    x1 = x0**2
    x2 = Z3 - Z4
    x3 = Y3 - Y4
    x4 = Z2 - Z3
    x5 = x0*x2 - x3*x4
    x6 = x4**2
    x7 = X2 - X3
    x8 = X3 - X4
    x9 = x2*x7 - x4*x8
    x10 = -x0*x8 + x3*x7
    x11 = X1 - X2
    x12 = Y1 - Y2
    x13 = x0*x11 - x12*x7
    x14 = Z1 - Z2
    x15 = x11*x4 - x14*x7
    x16 = -x0*x14 + x12*x4
    x17 = x10*x13 + x15*x9 + x16*x5
    x18 = x1 + x6 + x7**2
    x19 = x0*(-x10*x16 + x13*x5) + x4*(x15*x5 - x16*x9) + x7*(-x10*x15 + x13*x9)
    x20 = 1/(sqrt(x18)*(x17**2 + x19**2/x18))
    return -x17*x20*(x1*x5 + x5*x6 + x7*(x0*x9 - x10*x4)) + x19*x20*(x0*x10 + x4*x9)

def phi_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = Z2 - Z3
    x1 = x0**2
    x2 = X2 - X3
    x3 = Z3 - Z4
    x4 = X3 - X4
    x5 = -x0*x4 + x2*x3
    x6 = -X2
    x7 = X3 + x6
    x8 = Y2 - Y3
    x9 = Y3 - Y4
    x10 = -x0*x9 + x3*x8
    x11 = x2*x9 - x4*x8
    x12 = X1 + x6
    x13 = Y1 - Y2
    x14 = x12*x8 - x13*x2
    x15 = Z1 - Z2
    x16 = x0*x12 - x15*x2
    x17 = x0*x13 - x15*x8
    x18 = x10*x17 + x11*x14 + x16*x5
    x19 = x1 + x2**2 + x8**2
    x20 = x0*(x10*x16 - x17*x5) + x2*(-x11*x16 + x14*x5) + x8*(x10*x14 - x11*x17)
    x21 = 1/(sqrt(x19)*(x18**2 + x20**2/x19))
    return -x18*x21*(-x1*x5 + x2*x5*x7 + x8*(-x0*x11 + x10*x7)) + x20*x21*(x0*x10 + x11*x7)

def phi_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X2
    x1 = X3 + x0
    x2 = X2 - X3
    x3 = Y3 - Y4
    x4 = X3 - X4
    x5 = Y2 - Y3
    x6 = x2*x3 - x4*x5
    x7 = -Y2
    x8 = Y3 + x7
    x9 = Z2 - Z3
    x10 = Z3 - Z4
    x11 = x10*x5 - x3*x9
    x12 = x10*x2 - x4*x9
    x13 = X1 + x0
    x14 = Y1 + x7
    x15 = x13*x5 - x14*x2
    x16 = Z1 - Z2
    x17 = x13*x9 - x16*x2
    x18 = x14*x9 - x16*x5
    x19 = x11*x18 + x12*x17 + x15*x6
    x20 = x2**2 + x5**2 + x9**2
    x21 = x2*(x12*x15 - x17*x6) + x5*(x11*x15 - x18*x6) + x9*(x11*x17 - x12*x18)
    x22 = 1/(sqrt(x20)*(x19**2 + x21**2/x20))
    return -x19*x22*(-x1*x2*x6 - x5*x6*x8 + x9*(x1*x11 - x12*x8)) + x21*x22*(x1*x12 + x11*x8)

def phi_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = Z2 - Z3
    x3 = x0**2 + x1**2 + x2**2
    x4 = 1/sqrt(x3)
    x5 = -Y1 + Y3
    x6 = Y3 - Y4
    x7 = X3 - X4
    x8 = x0*x6 - x1*x7
    x9 = -X2
    x10 = X1 + x9
    x11 = Y1 - Y2
    x12 = -x0*x11 + x1*x10
    x13 = -Z1 + Z3
    x14 = Z3 - Z4
    x15 = x0*x14 - x2*x7
    x16 = Z1 - Z2
    x17 = -x0*x16 + x10*x2
    x18 = x12*x15 - x17*x8
    x19 = x1*x14 - x2*x6
    x20 = -x1*x16 + x11*x2
    x21 = x0*x18 + x1*(x12*x19 - x20*x8) + x2*(-x15*x20 + x17*x19)
    x22 = x12*x8 + x15*x17 + x19*x20
    x23 = 1/(x21**2/x3 + x22**2)
    return x21*x23*x4*(x12*x6 + x13*x15 + x14*x17 + x5*x8) + x22*x23*(-x21*(X3 + x9)/x3**(3/2) - x4*(x0*(x12*x14 - x13*x8 + x15*x5 - x17*x6) + x1*(x19*x5 - x20*x6) + x18 + x2*(x13*x19 - x14*x20)))

def phi_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x1**2 + x2**2 + x3**2
    x5 = 1/sqrt(x4)
    x6 = X1 + x0
    x7 = Y3 - Y4
    x8 = X3 - X4
    x9 = x1*x7 - x2*x8
    x10 = X4 + x0
    x11 = X1 - X2
    x12 = -Y2
    x13 = Y1 + x12
    x14 = -x1*x13 + x11*x2
    x15 = -Z1 + Z3
    x16 = Z3 - Z4
    x17 = x16*x2 - x3*x7
    x18 = Z1 - Z2
    x19 = x13*x3 - x18*x2
    x20 = x1*x16 - x3*x8
    x21 = -x1*x18 + x11*x3
    x22 = x14*x17 - x19*x9
    x23 = x1*(x14*x20 - x21*x9) + x2*x22 + x3*(x17*x21 - x19*x20)
    x24 = x14*x9 + x17*x19 + x20*x21
    x25 = 1/(x23**2/x4 + x24**2)
    return x23*x25*x5*(x10*x14 + x15*x17 + x16*x19 + x6*x9) + x24*x25*(-x23*(Y3 + x12)/x4**(3/2) - x5*(x1*(-x10*x21 + x20*x6) + x2*(-x10*x19 + x14*x16 - x15*x9 + x17*x6) + x22 + x3*(-x15*x20 + x16*x21)))

def phi_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = Z2 - Z3
    x5 = x1**2 + x3**2 + x4**2
    x6 = 1/sqrt(x5)
    x7 = X1 + x0
    x8 = Z3 - Z4
    x9 = X3 - X4
    x10 = x1*x8 - x4*x9
    x11 = X4 + x0
    x12 = X1 - X2
    x13 = -Z2
    x14 = Z1 + x13
    x15 = -x1*x14 + x12*x4
    x16 = Y1 + x2
    x17 = Y3 - Y4
    x18 = -x17*x4 + x3*x8
    x19 = Y4 + x2
    x20 = Y1 - Y2
    x21 = -x14*x3 + x20*x4
    x22 = -x1*x20 + x12*x3
    x23 = x1*x17 - x3*x9
    x24 = -x10*x21 + x15*x18
    x25 = x1*(x10*x22 - x15*x23) + x24*x4 + x3*(x18*x22 - x21*x23)
    x26 = x10*x15 + x18*x21 + x22*x23
    x27 = 1/(x25**2/x5 + x26**2)
    return x25*x27*x6*(x10*x7 + x11*x15 + x16*x18 + x19*x21) + x26*x27*(-x25*(Z3 + x13)/x5**(3/2) - x6*(x1*(x11*x22 - x23*x7) + x24 + x3*(-x16*x23 + x19*x22) + x4*(-x10*x16 - x11*x21 + x15*x19 + x18*x7)))

def phi_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = Z2 - Z3
    x3 = x0**2 + x1**2 + x2**2
    x4 = 1/sqrt(x3)
    x5 = -Y2
    x6 = Y1 + x5
    x7 = Y3 - Y4
    x8 = X3 - X4
    x9 = x0*x7 - x1*x8
    x10 = Y4 + x5
    x11 = X1 - X2
    x12 = -x0*x6 + x1*x11
    x13 = -Z2
    x14 = Z1 + x13
    x15 = Z3 - Z4
    x16 = x0*x15 - x2*x8
    x17 = Z4 + x13
    x18 = -x0*x14 + x11*x2
    x19 = x12*x16
    x20 = x18*x9
    x21 = x1*x15 - x2*x7
    x22 = -x1*x14 + x2*x6
    x23 = x0*(x19 - x20) + x1*(x12*x21 - x22*x9) + x2*(-x16*x22 + x18*x21)
    x24 = x12*x9 + x16*x18 + x21*x22
    x25 = 1/(x23**2/x3 + x24**2)
    return x23*x25*x4*(x10*x12 + x14*x16 + x17*x18 + x6*x9) + x24*x25*(-x0*x23/x3**(3/2) - x4*(x0*(-x10*x18 + x12*x17 - x14*x9 + x16*x6) + x1*(-x10*x22 + x21*x6) - x19 + x2*(x14*x21 - x17*x22) + x20))

def phi_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = Z2 - Z3
    x3 = x0**2 + x1**2 + x2**2
    x4 = 1/sqrt(x3)
    x5 = -X1 + X2
    x6 = Y3 - Y4
    x7 = -X4
    x8 = X3 + x7
    x9 = x0*x6 - x1*x8
    x10 = X2 + x7
    x11 = X1 - X2
    x12 = Y1 - Y2
    x13 = -x0*x12 + x1*x11
    x14 = -Z2
    x15 = Z1 + x14
    x16 = Z3 - Z4
    x17 = x1*x16 - x2*x6
    x18 = Z4 + x14
    x19 = -x1*x15 + x12*x2
    x20 = x0*x16 - x2*x8
    x21 = -x0*x15 + x11*x2
    x22 = x13*x17
    x23 = x19*x9
    x24 = x0*(x13*x20 - x21*x9) + x1*(x22 - x23) + x2*(x17*x21 - x19*x20)
    x25 = x13*x9 + x17*x19 + x20*x21
    x26 = 1/(x24**2/x3 + x25**2)
    return x24*x26*x4*(x10*x13 + x15*x17 + x18*x19 + x5*x9) + x25*x26*(-x1*x24/x3**(3/2) - x4*(x0*(-x10*x21 + x20*x5) + x1*(-x10*x19 + x13*x18 - x15*x9 + x17*x5) + x2*(-x15*x20 + x18*x21) - x22 + x23))

def phi_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = Z2 - Z3
    x3 = x0**2 + x1**2 + x2**2
    x4 = 1/sqrt(x3)
    x5 = -X1 + X2
    x6 = Z3 - Z4
    x7 = -X4
    x8 = X3 + x7
    x9 = x0*x6 - x2*x8
    x10 = X2 + x7
    x11 = X1 - X2
    x12 = Z1 - Z2
    x13 = -x0*x12 + x11*x2
    x14 = -Y1 + Y2
    x15 = -Y4
    x16 = Y3 + x15
    x17 = x1*x6 - x16*x2
    x18 = Y2 + x15
    x19 = Y1 - Y2
    x20 = -x1*x12 + x19*x2
    x21 = -x0*x19 + x1*x11
    x22 = x0*x16 - x1*x8
    x23 = x13*x17
    x24 = x20*x9
    x25 = x0*(-x13*x22 + x21*x9) + x1*(x17*x21 - x20*x22) + x2*(x23 - x24)
    x26 = x13*x9 + x17*x20 + x21*x22
    x27 = 1/(x25**2/x3 + x26**2)
    return x25*x27*x4*(x10*x13 + x14*x17 + x18*x20 + x5*x9) + x26*x27*(-x2*x25/x3**(3/2) - x4*(x0*(x10*x21 - x22*x5) + x1*(-x14*x22 + x18*x21) + x2*(-x10*x20 + x13*x18 - x14*x9 + x17*x5) - x23 + x24))

def phi_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = Y2 - Y3
    x1 = x0**2
    x2 = Y1 - Y2
    x3 = Z2 - Z3
    x4 = Z1 - Z2
    x5 = -x0*x4 + x2*x3
    x6 = x3**2
    x7 = X2 - X3
    x8 = X1 - X2
    x9 = x0*x8 - x2*x7
    x10 = x3*x8 - x4*x7
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = -x0*x12 + x11*x7
    x14 = Z3 - Z4
    x15 = -x12*x3 + x14*x7
    x16 = x0*x14 - x11*x3
    x17 = x10*x15 + x13*x9 + x16*x5
    x18 = x1 + x6 + x7**2
    x19 = x0*(-x13*x5 + x16*x9) + x3*(x10*x16 - x15*x5) + x7*(-x10*x13 + x15*x9)
    x20 = 1/(sqrt(x18)*(x17**2 + x19**2/x18))
    return -x17*x20*(-x1*x5 - x5*x6 + x7*(-x0*x10 + x3*x9)) + x19*x20*(x0*x9 + x10*x3)

def phi_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = Z2 - Z3
    x1 = x0**2
    x2 = -X2
    x3 = X1 + x2
    x4 = X2 - X3
    x5 = Z1 - Z2
    x6 = x0*x3 - x4*x5
    x7 = X3 + x2
    x8 = Y2 - Y3
    x9 = Y1 - Y2
    x10 = x3*x8 - x4*x9
    x11 = x0*x9 - x5*x8
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x12*x4 - x13*x8
    x15 = Z3 - Z4
    x16 = -x0*x13 + x15*x4
    x17 = -x0*x12 + x15*x8
    x18 = x10*x14 + x11*x17 + x16*x6
    x19 = x1 + x4**2 + x8**2
    x20 = x0*(-x11*x16 + x17*x6) + x4*(x10*x16 - x14*x6) + x8*(x10*x17 - x11*x14)
    x21 = 1/(sqrt(x19)*(x18**2 + x20**2/x19))
    return -x18*x21*(x1*x6 - x4*x6*x7 + x8*(x0*x10 - x11*x7)) + x20*x21*(x0*x11 + x10*x7)

def phi_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X2
    x1 = X3 + x0
    x2 = X2 - X3
    x3 = X1 + x0
    x4 = Y2 - Y3
    x5 = -Y2
    x6 = Y1 + x5
    x7 = -x2*x6 + x3*x4
    x8 = Y3 + x5
    x9 = Z2 - Z3
    x10 = Z1 - Z2
    x11 = -x10*x2 + x3*x9
    x12 = -x10*x4 + x6*x9
    x13 = Y3 - Y4
    x14 = X3 - X4
    x15 = x13*x2 - x14*x4
    x16 = Z3 - Z4
    x17 = -x14*x9 + x16*x2
    x18 = -x13*x9 + x16*x4
    x19 = x11*x17 + x12*x18 + x15*x7
    x20 = x2**2 + x4**2 + x9**2
    x21 = x2*(-x11*x15 + x17*x7) + x4*(-x12*x15 + x18*x7) + x9*(x11*x18 - x12*x17)
    x22 = 1/(sqrt(x20)*(x19**2 + x21**2/x20))
    return -x19*x22*(x1*x2*x7 + x4*x7*x8 + x9*(-x1*x12 + x11*x8)) + x21*x22*(x1*x11 + x12*x8)

def radius_dX1_dX1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (X1 - X2)**2
    x1 = x0 + (Y1 - Y2)**2 + (Z1 - Z2)**2
    return -1.0*x0*x1**(-1.5) + 1.0*x1**(-0.5)

def radius_dX1_dY1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Y1 - Y2
    return -1.0*x0*x1*(x0**2 + x1**2 + (Z1 - Z2)**2)**(-1.5)

def radius_dX1_dZ1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Z1 - Z2
    return -1.0*x0*x1*(x0**2 + x1**2 + (Y1 - Y2)**2)**(-1.5)

def radius_dX1_dX2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (X1 - X2)**2
    x1 = x0 + (Y1 - Y2)**2 + (Z1 - Z2)**2
    return 1.0*x0*x1**(-1.5) - 1.0*x1**(-0.5)

def radius_dX1_dY2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Y1 - Y2
    return 1.0*x0*x1*(x0**2 + x1**2 + (Z1 - Z2)**2)**(-1.5)

def radius_dX1_dZ2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Z1 - Z2
    return 1.0*x0*x1*(x0**2 + x1**2 + (Y1 - Y2)**2)**(-1.5)

def radius_dY1_dX1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Y1 - Y2
    return -1.0*x0*x1*(x0**2 + x1**2 + (Z1 - Z2)**2)**(-1.5)

def radius_dY1_dY1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (Y1 - Y2)**2
    x1 = x0 + (X1 - X2)**2 + (Z1 - Z2)**2
    return -1.0*x0*x1**(-1.5) + 1.0*x1**(-0.5)

def radius_dY1_dZ1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = Y1 - Y2
    x1 = Z1 - Z2
    return -1.0*x0*x1*(x0**2 + x1**2 + (X1 - X2)**2)**(-1.5)

def radius_dY1_dX2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Y1 - Y2
    return 1.0*x0*x1*(x0**2 + x1**2 + (Z1 - Z2)**2)**(-1.5)

def radius_dY1_dY2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (Y1 - Y2)**2
    x1 = x0 + (X1 - X2)**2 + (Z1 - Z2)**2
    return 1.0*x0*x1**(-1.5) - 1.0*x1**(-0.5)

def radius_dY1_dZ2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = Y1 - Y2
    x1 = Z1 - Z2
    return 1.0*x0*x1*(x0**2 + x1**2 + (X1 - X2)**2)**(-1.5)

def radius_dZ1_dX1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Z1 - Z2
    return -1.0*x0*x1*(x0**2 + x1**2 + (Y1 - Y2)**2)**(-1.5)

def radius_dZ1_dY1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = Y1 - Y2
    x1 = Z1 - Z2
    return -1.0*x0*x1*(x0**2 + x1**2 + (X1 - X2)**2)**(-1.5)

def radius_dZ1_dZ1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (Z1 - Z2)**2
    x1 = x0 + (X1 - X2)**2 + (Y1 - Y2)**2
    return -1.0*x0*x1**(-1.5) + 1.0*x1**(-0.5)

def radius_dZ1_dX2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Z1 - Z2
    return 1.0*x0*x1*(x0**2 + x1**2 + (Y1 - Y2)**2)**(-1.5)

def radius_dZ1_dY2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = Y1 - Y2
    x1 = Z1 - Z2
    return 1.0*x0*x1*(x0**2 + x1**2 + (X1 - X2)**2)**(-1.5)

def radius_dZ1_dZ2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (Z1 - Z2)**2
    x1 = x0 + (X1 - X2)**2 + (Y1 - Y2)**2
    return 1.0*x0*x1**(-1.5) - 1.0*x1**(-0.5)

def radius_dX2_dX1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (X1 - X2)**2
    x1 = x0 + (Y1 - Y2)**2 + (Z1 - Z2)**2
    return 1.0*x0*x1**(-1.5) - 1.0*x1**(-0.5)

def radius_dX2_dY1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Y1 - Y2
    return 1.0*x0*x1*(x0**2 + x1**2 + (Z1 - Z2)**2)**(-1.5)

def radius_dX2_dZ1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Z1 - Z2
    return 1.0*x0*x1*(x0**2 + x1**2 + (Y1 - Y2)**2)**(-1.5)

def radius_dX2_dX2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (X1 - X2)**2
    x1 = x0 + (Y1 - Y2)**2 + (Z1 - Z2)**2
    return -1.0*x0*x1**(-1.5) + 1.0*x1**(-0.5)

def radius_dX2_dY2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Y1 - Y2
    return -1.0*x0*x1*(x0**2 + x1**2 + (Z1 - Z2)**2)**(-1.5)

def radius_dX2_dZ2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Z1 - Z2
    return -1.0*x0*x1*(x0**2 + x1**2 + (Y1 - Y2)**2)**(-1.5)

def radius_dY2_dX1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Y1 - Y2
    return 1.0*x0*x1*(x0**2 + x1**2 + (Z1 - Z2)**2)**(-1.5)

def radius_dY2_dY1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (Y1 - Y2)**2
    x1 = x0 + (X1 - X2)**2 + (Z1 - Z2)**2
    return 1.0*x0*x1**(-1.5) - 1.0*x1**(-0.5)

def radius_dY2_dZ1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = Y1 - Y2
    x1 = Z1 - Z2
    return 1.0*x0*x1*(x0**2 + x1**2 + (X1 - X2)**2)**(-1.5)

def radius_dY2_dX2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Y1 - Y2
    return -1.0*x0*x1*(x0**2 + x1**2 + (Z1 - Z2)**2)**(-1.5)

def radius_dY2_dY2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (Y1 - Y2)**2
    x1 = x0 + (X1 - X2)**2 + (Z1 - Z2)**2
    return -1.0*x0*x1**(-1.5) + 1.0*x1**(-0.5)

def radius_dY2_dZ2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = Y1 - Y2
    x1 = Z1 - Z2
    return -1.0*x0*x1*(x0**2 + x1**2 + (X1 - X2)**2)**(-1.5)

def radius_dZ2_dX1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Z1 - Z2
    return 1.0*x0*x1*(x0**2 + x1**2 + (Y1 - Y2)**2)**(-1.5)

def radius_dZ2_dY1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = Y1 - Y2
    x1 = Z1 - Z2
    return 1.0*x0*x1*(x0**2 + x1**2 + (X1 - X2)**2)**(-1.5)

def radius_dZ2_dZ1(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (Z1 - Z2)**2
    x1 = x0 + (X1 - X2)**2 + (Y1 - Y2)**2
    return 1.0*x0*x1**(-1.5) - 1.0*x1**(-0.5)

def radius_dZ2_dX2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = X1 - X2
    x1 = Z1 - Z2
    return -1.0*x0*x1*(x0**2 + x1**2 + (Y1 - Y2)**2)**(-1.5)

def radius_dZ2_dY2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = Y1 - Y2
    x1 = Z1 - Z2
    return -1.0*x0*x1*(x0**2 + x1**2 + (X1 - X2)**2)**(-1.5)

def radius_dZ2_dZ2(X1,Y1,Z1,X2,Y2,Z2):
    x0 = (Z1 - Z2)**2
    x1 = x0 + (X1 - X2)**2 + (Y1 - Y2)**2
    return -1.0*x0*x1**(-1.5) + 1.0*x1**(-0.5)

def theta_dX1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = x0**2
    x2 = Y1 - Y2
    x3 = Z1 - Z2
    x4 = x1 + x2**2 + x3**2
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = Y2 - Y3
    x8 = Z2 - Z3
    x9 = x6**2 + x7**2 + x8**2
    x10 = x0*x6
    x11 = x10 + x2*x7 + x3*x8
    x12 = -x11**2*x5*x9**(-1.0) + 1
    x13 = x4**(-1.5)
    x14 = 1.0*x11*x13
    return (x11*x9**(-1.5)*(x0*x14 - x4**(-0.5)*x6)*(x0*x11*x4**(-2.0) - x5*x6)/x12 - x9**(-0.5)*(-3.0*x1*x11*x4**(-2.5) + 2.0*x10*x13 + x14))/sqrt(x12)

def theta_dX1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x0*x5 + x1*x6 + x2*x7
    x10 = -x4*x8**(-1.0)*x9**2 + 1
    x11 = x3**(-1.5)
    x12 = 1.0*x0*x11
    x13 = x1*x9
    return (-x8**(-0.5)*(-3.0*x0*x13*x3**(-2.5) + 1.0*x1*x11*x5 + x12*x6) + x8**(-1.5)*x9*(x12*x9 - x3**(-0.5)*x5)*(x13*x3**(-2.0) - x4*x6)/x10)/sqrt(x10)

def theta_dX1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x0*x5 + x1*x6 + x2*x7
    x10 = -x4*x8**(-1.0)*x9**2 + 1
    x11 = x3**(-1.5)
    x12 = 1.0*x0*x11
    x13 = x2*x9
    return (-x8**(-0.5)*(-3.0*x0*x13*x3**(-2.5) + 1.0*x11*x2*x5 + x12*x7) + x8**(-1.5)*x9*(x12*x9 - x3**(-0.5)*x5)*(x13*x3**(-2.0) - x4*x7)/x10)/sqrt(x10)

def theta_dX1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = x0*x1
    x3 = Y1 - Y2
    x4 = Y2 - Y3
    x5 = Z1 - Z2
    x6 = Z2 - Z3
    x7 = x2 + x3*x4 + x5*x6
    x8 = x0**2
    x9 = x3**2 + x5**2 + x8
    x10 = x9**(-1.0)
    x11 = x1**2
    x12 = x11 + x4**2 + x6**2
    x13 = x12**(-1.0)
    x14 = x10*x13
    x15 = -x14*x7**2 + 1
    x16 = x9**(-0.5)
    x17 = x12**(-0.5)
    x18 = 1.0*x12**(-1.5)
    x19 = x9**(-1.5)
    x20 = 1.0*x17*x19
    x21 = X1 - 2*X2 + X3
    x22 = x17*x7
    x23 = x0*x7
    return (x0*x1*x18*x19*x7 - x0*x20*x21 - x11*x16*x18 + x16*x17 + x2*x20 + x20*x7 - 3.0*x22*x8*x9**(-2.5) - x22*(-x1*x16 + 1.0*x19*x23)*(-1.0*x1*x10*x12**(-2.0)*x7 + x13*x23*x9**(-2.0) + x14*x21)/x15)/sqrt(x15)

def theta_dX1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x7**(-1.5)
    x14 = x9**(-0.5)
    x15 = 1.0*x13*x14
    x16 = x1*x7**(-0.5)
    x17 = 1.0*Y2 - 1.0*Y3
    x18 = x17*x9**(-1.5)
    x19 = Y1 - 2*Y2 + Y3
    x20 = x0*x13*x6
    return -(3.0*x0*x14*x2*x6*x7**(-2.5) + x0*x15*x19 - x1*x15*x2 + x16*x18 - x18*x20 + x14*x6*(-x16 + 1.0*x20)*(x10*x2*x6*x7**(-2.0) + x11*x19 - x17*x6*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dX1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x7**(-1.5)
    x14 = x9**(-0.5)
    x15 = 1.0*x13*x14
    x16 = x1*x7**(-0.5)
    x17 = 1.0*Z2 - 1.0*Z3
    x18 = x17*x9**(-1.5)
    x19 = Z1 - 2*Z2 + Z3
    x20 = x0*x13*x6
    return -(3.0*x0*x14*x4*x6*x7**(-2.5) + x0*x15*x19 - x1*x15*x4 + x16*x18 - x18*x20 + x14*x6*(-x16 + 1.0*x20)*(x10*x4*x6*x7**(-2.0) + x11*x19 - x17*x6*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dX1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = x0**2
    x2 = Y1 - Y2
    x3 = Z1 - Z2
    x4 = x1 + x2**2 + x3**2
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = x6**2
    x8 = Y2 - Y3
    x9 = Z2 - Z3
    x10 = x7 + x8**2 + x9**2
    x11 = x10**(-1.0)
    x12 = x0*x6 + x2*x8 + x3*x9
    x13 = -x11*x12**2*x5 + 1
    x14 = x4**(-0.5)
    x15 = x10**(-0.5)
    x16 = x4**(-1.5)
    x17 = x10**(-1.5)
    x18 = 1.0*x12*x16
    return (-x0*x17*x18*x6 + 1.0*x1*x15*x16 + x12*x15*x5*(x0*x11 - 1.0*x10**(-2.0)*x12*x6)*(x0*x18 - x14*x6)/x13 - x14*x15 + 1.0*x14*x17*x7)/sqrt(x13)

def theta_dX1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x8**(-0.5)
    x13 = 1.0*x0*x3**(-1.5)
    x14 = 1.0*Y2 - 1.0*Y3
    x15 = x3**(-0.5)
    x16 = x8**(-1.5)
    x17 = x10*x13
    return (x1*x12*x13 + x10*x12*x4*(x1*x9 - x10*x14*x8**(-2.0))*(-x15*x5 + x17)/x11 + x14*x15*x16*x5 - x16*x17*x6)/sqrt(x11)

def theta_dX1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x8**(-0.5)
    x13 = 1.0*x0*x3**(-1.5)
    x14 = 1.0*Z2 - 1.0*Z3
    x15 = x3**(-0.5)
    x16 = x8**(-1.5)
    x17 = x10*x13
    return (x10*x12*x4*(-x15*x5 + x17)*(-x10*x14*x8**(-2.0) + x2*x9)/x11 + x12*x13*x2 + x14*x15*x16*x5 - x16*x17*x7)/sqrt(x11)

def theta_dY1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x0*x5 + x1*x6 + x2*x7
    x10 = -x4*x8**(-1.0)*x9**2 + 1
    x11 = x3**(-1.5)
    x12 = 1.0*x1*x11
    x13 = x0*x9
    return (-x8**(-0.5)*(1.0*x0*x11*x6 - 3.0*x1*x13*x3**(-2.5) + x12*x5) + x8**(-1.5)*x9*(x12*x9 - x3**(-0.5)*x6)*(x13*x3**(-2.0) - x4*x5)/x10)/sqrt(x10)

def theta_dY1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = x1**2
    x3 = Z1 - Z2
    x4 = x0**2 + x2 + x3**2
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = Y2 - Y3
    x8 = Z2 - Z3
    x9 = x6**2 + x7**2 + x8**2
    x10 = x1*x7
    x11 = x0*x6 + x10 + x3*x8
    x12 = -x11**2*x5*x9**(-1.0) + 1
    x13 = x4**(-1.5)
    x14 = 1.0*x11*x13
    return (x11*x9**(-1.5)*(x1*x14 - x4**(-0.5)*x7)*(x1*x11*x4**(-2.0) - x5*x7)/x12 - x9**(-0.5)*(2.0*x10*x13 - 3.0*x11*x2*x4**(-2.5) + x14))/sqrt(x12)

def theta_dY1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x0*x5 + x1*x6 + x2*x7
    x10 = -x4*x8**(-1.0)*x9**2 + 1
    x11 = x3**(-1.5)
    x12 = 1.0*x1*x11
    x13 = x2*x9
    return (-x8**(-0.5)*(-3.0*x1*x13*x3**(-2.5) + 1.0*x11*x2*x6 + x12*x7) + x8**(-1.5)*x9*(x12*x9 - x3**(-0.5)*x6)*(x13*x3**(-2.0) - x4*x7)/x10)/sqrt(x10)

def theta_dY1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x7**(-1.5)
    x14 = x9**(-0.5)
    x15 = 1.0*x13*x14
    x16 = x3*x7**(-0.5)
    x17 = 1.0*X2 - 1.0*X3
    x18 = x17*x9**(-1.5)
    x19 = X1 - 2*X2 + X3
    x20 = x13*x2*x6
    return -(3.0*x0*x14*x2*x6*x7**(-2.5) - x0*x15*x3 + x15*x19*x2 + x16*x18 - x18*x20 + x14*x6*(-x16 + 1.0*x20)*(x0*x10*x6*x7**(-2.0) + x11*x19 - x17*x6*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dY1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = x2*x3
    x5 = Z1 - Z2
    x6 = Z2 - Z3
    x7 = x0*x1 + x4 + x5*x6
    x8 = x2**2
    x9 = x0**2 + x5**2 + x8
    x10 = x9**(-1.0)
    x11 = x3**2
    x12 = x1**2 + x11 + x6**2
    x13 = x12**(-1.0)
    x14 = x10*x13
    x15 = -x14*x7**2 + 1
    x16 = x9**(-0.5)
    x17 = x12**(-0.5)
    x18 = 1.0*x12**(-1.5)
    x19 = x9**(-1.5)
    x20 = 1.0*x17*x19
    x21 = Y1 - 2*Y2 + Y3
    x22 = x17*x7
    x23 = x2*x7
    return (-x11*x16*x18 + x16*x17 + x18*x19*x2*x3*x7 - x2*x20*x21 + x20*x4 + x20*x7 - 3.0*x22*x8*x9**(-2.5) - x22*(-x16*x3 + 1.0*x19*x23)*(-1.0*x10*x12**(-2.0)*x3*x7 + x13*x23*x9**(-2.0) + x14*x21)/x15)/sqrt(x15)

def theta_dY1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x7**(-1.5)
    x14 = x9**(-0.5)
    x15 = 1.0*x13*x14
    x16 = x3*x7**(-0.5)
    x17 = 1.0*Z2 - 1.0*Z3
    x18 = x17*x9**(-1.5)
    x19 = Z1 - 2*Z2 + Z3
    x20 = x13*x2*x6
    return -(3.0*x14*x2*x4*x6*x7**(-2.5) + x15*x19*x2 - x15*x3*x4 + x16*x18 - x18*x20 + x14*x6*(-x16 + 1.0*x20)*(x10*x4*x6*x7**(-2.0) + x11*x19 - x17*x6*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dY1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x8**(-0.5)
    x13 = 1.0*x1*x3**(-1.5)
    x14 = 1.0*X2 - 1.0*X3
    x15 = x3**(-0.5)
    x16 = x8**(-1.5)
    x17 = x10*x13
    return (x0*x12*x13 + x10*x12*x4*(x0*x9 - x10*x14*x8**(-2.0))*(-x15*x6 + x17)/x11 + x14*x15*x16*x6 - x16*x17*x5)/sqrt(x11)

def theta_dY1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = x1**2
    x3 = Z1 - Z2
    x4 = x0**2 + x2 + x3**2
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = Y2 - Y3
    x8 = x7**2
    x9 = Z2 - Z3
    x10 = x6**2 + x8 + x9**2
    x11 = x10**(-1.0)
    x12 = x0*x6 + x1*x7 + x3*x9
    x13 = -x11*x12**2*x5 + 1
    x14 = x4**(-0.5)
    x15 = x10**(-0.5)
    x16 = x4**(-1.5)
    x17 = x10**(-1.5)
    x18 = 1.0*x12*x16
    return (-x1*x17*x18*x7 + x12*x15*x5*(x1*x11 - 1.0*x10**(-2.0)*x12*x7)*(x1*x18 - x14*x7)/x13 - x14*x15 + 1.0*x14*x17*x8 + 1.0*x15*x16*x2)/sqrt(x13)

def theta_dY1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x8**(-0.5)
    x13 = 1.0*x1*x3**(-1.5)
    x14 = 1.0*Z2 - 1.0*Z3
    x15 = x3**(-0.5)
    x16 = x8**(-1.5)
    x17 = x10*x13
    return (x10*x12*x4*(-x15*x6 + x17)*(-x10*x14*x8**(-2.0) + x2*x9)/x11 + x12*x13*x2 + x14*x15*x16*x6 - x16*x17*x7)/sqrt(x11)

def theta_dZ1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x0*x5 + x1*x6 + x2*x7
    x10 = -x4*x8**(-1.0)*x9**2 + 1
    x11 = x3**(-1.5)
    x12 = 1.0*x11*x2
    x13 = x0*x9
    return (-x8**(-0.5)*(1.0*x0*x11*x7 + x12*x5 - 3.0*x13*x2*x3**(-2.5)) + x8**(-1.5)*x9*(x12*x9 - x3**(-0.5)*x7)*(x13*x3**(-2.0) - x4*x5)/x10)/sqrt(x10)

def theta_dZ1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x0*x5 + x1*x6 + x2*x7
    x10 = -x4*x8**(-1.0)*x9**2 + 1
    x11 = x3**(-1.5)
    x12 = 1.0*x11*x2
    x13 = x1*x9
    return (-x8**(-0.5)*(1.0*x1*x11*x7 + x12*x6 - 3.0*x13*x2*x3**(-2.5)) + x8**(-1.5)*x9*(x12*x9 - x3**(-0.5)*x7)*(x13*x3**(-2.0) - x4*x6)/x10)/sqrt(x10)

def theta_dZ1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x2**2
    x4 = x0**2 + x1**2 + x3
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = Y2 - Y3
    x8 = Z2 - Z3
    x9 = x6**2 + x7**2 + x8**2
    x10 = x2*x8
    x11 = x0*x6 + x1*x7 + x10
    x12 = -x11**2*x5*x9**(-1.0) + 1
    x13 = x4**(-1.5)
    x14 = 1.0*x11*x13
    return (x11*x9**(-1.5)*(x14*x2 - x4**(-0.5)*x8)*(x11*x2*x4**(-2.0) - x5*x8)/x12 - x9**(-0.5)*(2.0*x10*x13 - 3.0*x11*x3*x4**(-2.5) + x14))/sqrt(x12)

def theta_dZ1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x7**(-1.5)
    x14 = x9**(-0.5)
    x15 = 1.0*x13*x14
    x16 = x5*x7**(-0.5)
    x17 = 1.0*X2 - 1.0*X3
    x18 = x17*x9**(-1.5)
    x19 = X1 - 2*X2 + X3
    x20 = x13*x4*x6
    return -(3.0*x0*x14*x4*x6*x7**(-2.5) - x0*x15*x5 + x15*x19*x4 + x16*x18 - x18*x20 + x14*x6*(-x16 + 1.0*x20)*(x0*x10*x6*x7**(-2.0) + x11*x19 - x17*x6*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dZ1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x7**(-1.5)
    x14 = x9**(-0.5)
    x15 = 1.0*x13*x14
    x16 = x5*x7**(-0.5)
    x17 = 1.0*Y2 - 1.0*Y3
    x18 = x17*x9**(-1.5)
    x19 = Y1 - 2*Y2 + Y3
    x20 = x13*x4*x6
    return -(3.0*x14*x2*x4*x6*x7**(-2.5) + x15*x19*x4 - x15*x2*x5 + x16*x18 - x18*x20 + x14*x6*(-x16 + 1.0*x20)*(x10*x2*x6*x7**(-2.0) + x11*x19 - x17*x6*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dZ1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x4*x5
    x7 = x0*x1 + x2*x3 + x6
    x8 = x4**2
    x9 = x0**2 + x2**2 + x8
    x10 = x9**(-1.0)
    x11 = x5**2
    x12 = x1**2 + x11 + x3**2
    x13 = x12**(-1.0)
    x14 = x10*x13
    x15 = -x14*x7**2 + 1
    x16 = x9**(-0.5)
    x17 = x12**(-0.5)
    x18 = 1.0*x12**(-1.5)
    x19 = x9**(-1.5)
    x20 = 1.0*x17*x19
    x21 = Z1 - 2*Z2 + Z3
    x22 = x17*x7
    x23 = x4*x7
    return (-x11*x16*x18 + x16*x17 + x18*x19*x4*x5*x7 - x20*x21*x4 + x20*x6 + x20*x7 - 3.0*x22*x8*x9**(-2.5) - x22*(-x16*x5 + 1.0*x19*x23)*(-1.0*x10*x12**(-2.0)*x5*x7 + x13*x23*x9**(-2.0) + x14*x21)/x15)/sqrt(x15)

def theta_dZ1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x8**(-0.5)
    x13 = 1.0*x2*x3**(-1.5)
    x14 = 1.0*X2 - 1.0*X3
    x15 = x3**(-0.5)
    x16 = x8**(-1.5)
    x17 = x10*x13
    return (x0*x12*x13 + x10*x12*x4*(x0*x9 - x10*x14*x8**(-2.0))*(-x15*x7 + x17)/x11 + x14*x15*x16*x7 - x16*x17*x5)/sqrt(x11)

def theta_dZ1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x8**(-0.5)
    x13 = 1.0*x2*x3**(-1.5)
    x14 = 1.0*Y2 - 1.0*Y3
    x15 = x3**(-0.5)
    x16 = x8**(-1.5)
    x17 = x10*x13
    return (x1*x12*x13 + x10*x12*x4*(x1*x9 - x10*x14*x8**(-2.0))*(-x15*x7 + x17)/x11 + x14*x15*x16*x7 - x16*x17*x6)/sqrt(x11)

def theta_dZ1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x2**2
    x4 = x0**2 + x1**2 + x3
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = Y2 - Y3
    x8 = Z2 - Z3
    x9 = x8**2
    x10 = x6**2 + x7**2 + x9
    x11 = x10**(-1.0)
    x12 = x0*x6 + x1*x7 + x2*x8
    x13 = -x11*x12**2*x5 + 1
    x14 = x4**(-0.5)
    x15 = x10**(-0.5)
    x16 = x4**(-1.5)
    x17 = x10**(-1.5)
    x18 = 1.0*x12*x16
    return (x12*x15*x5*(-x14*x8 + x18*x2)*(-1.0*x10**(-2.0)*x12*x8 + x11*x2)/x13 - x14*x15 + 1.0*x14*x17*x9 + 1.0*x15*x16*x3 - x17*x18*x2*x8)/sqrt(x13)

def theta_dX2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = x0**2
    x2 = Y1 - Y2
    x3 = Z1 - Z2
    x4 = x1 + x2**2 + x3**2
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = x6**2
    x8 = Y2 - Y3
    x9 = Z2 - Z3
    x10 = x7 + x8**2 + x9**2
    x11 = x10**(-1.0)
    x12 = x0*x6
    x13 = x12 + x2*x8 + x3*x9
    x14 = -x11*x13**2*x5 + 1
    x15 = x4**(-0.5)
    x16 = x10**(-0.5)
    x17 = x15*x16
    x18 = x10**(-1.5)
    x19 = 1.0*x15*x18
    x20 = x4**(-1.5)
    x21 = 1.0*x16*x20
    x22 = X1 - 2*X2 + X3
    x23 = 1.0*x0*x16*x20
    return (-3.0*x1*x13*x16*x4**(-2.5) - x11*x13*(x0*x13*x4**(-2.0) - x5*x6)*(-x13*x19*x6 + x13*x23 + x17*x22)/x14 + 1.0*x12*x13*x18*x20 + x12*x21 + x13*x21 + x17 - x19*x7 - x22*x23)/sqrt(x14)

def theta_dX2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*Y2 - 1.0*Y3
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x0*x13*x14
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x5
    x19 = 1.0*x1*x13
    x20 = x14*(X1 - 2*X2 + X3)
    x21 = x1*x10
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return -(3.0*x0*x14*x21*x3**(-2.5) - x10*x17*x19*x5 + x10*x9*(x21*x3**(-2.0) - x4*x6)*(x15*x22 + x16*x20 - x18*x22)/x11 - x12*x15 + x12*x18 + x19*x20)/sqrt(x11)

def theta_dX2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*Z2 - 1.0*Z3
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x0*x13*x14
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x5
    x19 = 1.0*x13*x2
    x20 = x14*(X1 - 2*X2 + X3)
    x21 = x10*x2
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return -(3.0*x0*x14*x21*x3**(-2.5) - x10*x17*x19*x5 + x10*x9*(x21*x3**(-2.0) - x4*x7)*(x15*x22 + x16*x20 - x18*x22)/x11 - x12*x15 + x12*x18 + x19*x20)/sqrt(x11)

def theta_dX2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = x0*x1
    x3 = Y1 - Y2
    x4 = Y2 - Y3
    x5 = Z1 - Z2
    x6 = Z2 - Z3
    x7 = x2 + x3*x4 + x5*x6
    x8 = x0**2
    x9 = x3**2 + x5**2 + x8
    x10 = x9**(-1.0)
    x11 = x1**2
    x12 = x11 + x4**2 + x6**2
    x13 = x12**(-1.0)
    x14 = x10*x13
    x15 = -x14*x7**2 + 1
    x16 = x9**(-0.5)
    x17 = x12**(-0.5)
    x18 = x16*x17
    x19 = 2.0*X1 - 4.0*X2 + 2.0*X3
    x20 = x9**(-1.5)
    x21 = x0*x17*x20
    x22 = x12**(-1.5)
    x23 = x1*x16*x22
    x24 = 1.0*x0*x1 + 1.0*x3*x4 + 1.0*x5*x6
    x25 = 3.0*x0*x1 + 3.0*x3*x4 + 3.0*x5*x6
    x26 = X1 - 2*X2 + X3
    return (x11*x12**(-2.5)*x16*x25 - x16*x22*x24 - x17*x20*x24 + x17*x25*x8*x9**(-2.5) - 2*x18 + x19*x21 - x19*x23 - 2.0*x2*x20*x22*x7 + x7*(x18*x26 + x21*x24 - x23*x24)*(x0*x13*x7*x9**(-2.0) - x1*x10*x12**(-2.0)*x24 + x14*x26)/x15)/sqrt(x15)

def theta_dX2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = 1.0*Y1 - 2.0*Y2 + 1.0*Y3
    x14 = x7**(-1.5)
    x15 = x9**(-0.5)
    x16 = x0*x14*x15
    x17 = x7**(-0.5)
    x18 = x9**(-1.5)
    x19 = x1*x17*x18
    x20 = X1 - 2*X2 + X3
    x21 = x15*x20
    x22 = 1.0*Y2 - 1.0*Y3
    x23 = x2*x6
    x24 = x18*x6
    x25 = 1.0*x0*x1 + 1.0*x2*x3 + 1.0*x4*x5
    return (-1.0*x0*x14*x24*x3 + 3.0*x0*x15*x23*x7**(-2.5) - 1.0*x1*x14*x2*x24 + 3.0*x1*x17*x3*x6*x9**(-2.5) + x13*x16 - x13*x19 + 1.0*x14*x2*x21 - x17*x18*x20*x22 + x6*(x16*x25 + x17*x21 - x19*x25)*(x10*x23*x7**(-2.0) + x11*(Y1 - 2*Y2 + Y3) - x22*x6*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dX2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = 1.0*Z1 - 2.0*Z2 + 1.0*Z3
    x14 = x7**(-1.5)
    x15 = x9**(-0.5)
    x16 = x0*x14*x15
    x17 = x7**(-0.5)
    x18 = x9**(-1.5)
    x19 = x1*x17*x18
    x20 = X1 - 2*X2 + X3
    x21 = x15*x20
    x22 = 1.0*Z2 - 1.0*Z3
    x23 = x4*x6
    x24 = x18*x6
    x25 = 1.0*x0*x1 + 1.0*x2*x3 + 1.0*x4*x5
    return (-1.0*x0*x14*x24*x5 + 3.0*x0*x15*x23*x7**(-2.5) - 1.0*x1*x14*x24*x4 + 3.0*x1*x17*x5*x6*x9**(-2.5) + x13*x16 - x13*x19 + 1.0*x14*x21*x4 - x17*x18*x20*x22 + x6*(x16*x25 + x17*x21 - x19*x25)*(x10*x23*x7**(-2.0) + x11*(Z1 - 2*Z2 + Z3) - x22*x6*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dX2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = x0**2
    x2 = Y1 - Y2
    x3 = Z1 - Z2
    x4 = x1 + x2**2 + x3**2
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = x6**2
    x8 = Y2 - Y3
    x9 = Z2 - Z3
    x10 = x7 + x8**2 + x9**2
    x11 = x10**(-1.0)
    x12 = x0*x6
    x13 = x12 + x2*x8 + x3*x9
    x14 = -x11*x13**2*x5 + 1
    x15 = x4**(-0.5)
    x16 = x10**(-0.5)
    x17 = x15*x16
    x18 = x4**(-1.5)
    x19 = 1.0*x16*x18
    x20 = x10**(-1.5)
    x21 = 1.0*x15*x20
    x22 = X1 - 2*X2 + X3
    x23 = 1.0*x15*x20*x6
    x24 = 1.0*x0*x6 + 1.0*x2*x8 + 1.0*x3*x9
    return (x0*x18*x20*x24*x6 - x1*x19 - 3.0*x10**(-2.5)*x13*x15*x7 + x12*x21 + x13*x21 - x13*x5*(x0*x11 - x10**(-2.0)*x24*x6)*(x0*x13*x19 - x13*x23 + x17*x22)/x14 + x17 + x22*x23)/sqrt(x14)

def theta_dX2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*Y1 - 1.0*Y2
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x0*x13*x14
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x5
    x19 = x16*(X1 - 2*X2 + X3)
    x20 = 1.0*Y2 - 1.0*Y3
    x21 = x17*x20
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return (x0*x10*x13*x21 - 3.0*x10*x16*x5*x6*x8**(-2.5) - x10*x4*(x1*x9 - x10*x20*x8**(-2.0))*(x14*x19 + x15*x22 - x18*x22)/x11 - x12*x15 + x12*x18 + x19*x21)/sqrt(x11)

def theta_dX2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*Z1 - 1.0*Z2
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x0*x13*x14
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x5
    x19 = x16*(X1 - 2*X2 + X3)
    x20 = 1.0*Z2 - 1.0*Z3
    x21 = x17*x20
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return (x0*x10*x13*x21 - 3.0*x10*x16*x5*x7*x8**(-2.5) - x10*x4*(-x10*x20*x8**(-2.0) + x2*x9)*(x14*x19 + x15*x22 - x18*x22)/x11 - x12*x15 + x12*x18 + x19*x21)/sqrt(x11)

def theta_dY2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*X2 - 1.0*X3
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x1*x13*x14
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x6
    x19 = 1.0*x0*x13
    x20 = x14*(Y1 - 2*Y2 + Y3)
    x21 = x0*x10
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return -(3.0*x1*x14*x21*x3**(-2.5) - x10*x17*x19*x6 + x10*x9*(x21*x3**(-2.0) - x4*x5)*(x15*x22 + x16*x20 - x18*x22)/x11 - x12*x15 + x12*x18 + x19*x20)/sqrt(x11)

def theta_dY2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = x1**2
    x3 = Z1 - Z2
    x4 = x0**2 + x2 + x3**2
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = Y2 - Y3
    x8 = x7**2
    x9 = Z2 - Z3
    x10 = x6**2 + x8 + x9**2
    x11 = x10**(-1.0)
    x12 = x1*x7
    x13 = x0*x6 + x12 + x3*x9
    x14 = -x11*x13**2*x5 + 1
    x15 = x4**(-0.5)
    x16 = x10**(-0.5)
    x17 = x15*x16
    x18 = x10**(-1.5)
    x19 = 1.0*x15*x18
    x20 = x4**(-1.5)
    x21 = 1.0*x16*x20
    x22 = Y1 - 2*Y2 + Y3
    x23 = 1.0*x1*x16*x20
    return (-x11*x13*(x1*x13*x4**(-2.0) - x5*x7)*(-x13*x19*x7 + x13*x23 + x17*x22)/x14 + 1.0*x12*x13*x18*x20 + x12*x21 - 3.0*x13*x16*x2*x4**(-2.5) + x13*x21 + x17 - x19*x8 - x22*x23)/sqrt(x14)

def theta_dY2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*Z2 - 1.0*Z3
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x1*x13*x14
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x6
    x19 = 1.0*x13*x2
    x20 = x14*(Y1 - 2*Y2 + Y3)
    x21 = x10*x2
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return -(3.0*x1*x14*x21*x3**(-2.5) - x10*x17*x19*x6 + x10*x9*(x21*x3**(-2.0) - x4*x7)*(x15*x22 + x16*x20 - x18*x22)/x11 - x12*x15 + x12*x18 + x19*x20)/sqrt(x11)

def theta_dY2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x7**(-1.5)
    x14 = 1.0*x0*x13
    x15 = Y1 - 2*Y2 + Y3
    x16 = x9**(-0.5)
    x17 = x15*x16
    x18 = x7**(-0.5)
    x19 = x9**(-1.5)
    x20 = X1 - 2*X2 + X3
    x21 = 1.0*x13*x16*x2
    x22 = 1.0*x18*x19*x3
    x23 = x0*x6
    x24 = x1*x6
    return (-1.0*x1*x15*x18*x19 - 1.0*x13*x19*x2*x24 + x14*x17 - x14*x19*x3*x6 + 3.0*x16*x2*x23*x7**(-2.5) + 3.0*x18*x24*x3*x9**(-2.5) + x20*x21 - x20*x22 + x6*(x17*x18 + x21*x6 - x22*x6)*(x10*x23*x7**(-2.0) + x11*x20 - 1.0*x24*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dY2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = x2*x3
    x5 = Z1 - Z2
    x6 = Z2 - Z3
    x7 = x0*x1 + x4 + x5*x6
    x8 = x2**2
    x9 = x0**2 + x5**2 + x8
    x10 = x9**(-1.0)
    x11 = x3**2
    x12 = x1**2 + x11 + x6**2
    x13 = x12**(-1.0)
    x14 = x10*x13
    x15 = -x14*x7**2 + 1
    x16 = x9**(-0.5)
    x17 = x12**(-0.5)
    x18 = x16*x17
    x19 = 2.0*Y1 - 4.0*Y2 + 2.0*Y3
    x20 = x9**(-1.5)
    x21 = x17*x2*x20
    x22 = x12**(-1.5)
    x23 = x16*x22*x3
    x24 = 1.0*x0*x1 + 1.0*x2*x3 + 1.0*x5*x6
    x25 = 3.0*x0*x1 + 3.0*x2*x3 + 3.0*x5*x6
    x26 = Y1 - 2*Y2 + Y3
    return (x11*x12**(-2.5)*x16*x25 - x16*x22*x24 - x17*x20*x24 + x17*x25*x8*x9**(-2.5) - 2*x18 + x19*x21 - x19*x23 - 2.0*x20*x22*x4*x7 + x7*(x18*x26 + x21*x24 - x23*x24)*(-x10*x12**(-2.0)*x24*x3 + x13*x2*x7*x9**(-2.0) + x14*x26)/x15)/sqrt(x15)

def theta_dY2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = 1.0*Z1 - 2.0*Z2 + 1.0*Z3
    x14 = x7**(-1.5)
    x15 = x9**(-0.5)
    x16 = x14*x15*x2
    x17 = x7**(-0.5)
    x18 = x9**(-1.5)
    x19 = x17*x18*x3
    x20 = Y1 - 2*Y2 + Y3
    x21 = x15*x20
    x22 = 1.0*Z2 - 1.0*Z3
    x23 = x4*x6
    x24 = x18*x6
    x25 = 1.0*x0*x1 + 1.0*x2*x3 + 1.0*x4*x5
    return (x13*x16 - x13*x19 - 1.0*x14*x2*x24*x5 + 1.0*x14*x21*x4 - 1.0*x14*x24*x3*x4 + 3.0*x15*x2*x23*x7**(-2.5) - x17*x18*x20*x22 + 3.0*x17*x3*x5*x6*x9**(-2.5) + x6*(x16*x25 + x17*x21 - x19*x25)*(x10*x23*x7**(-2.0) + x11*(Z1 - 2*Z2 + Z3) - x22*x6*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dY2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*X1 - 1.0*X2
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x1*x13*x14
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x6
    x19 = x16*(Y1 - 2*Y2 + Y3)
    x20 = 1.0*X2 - 1.0*X3
    x21 = x17*x20
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return (x1*x10*x13*x21 - 3.0*x10*x16*x5*x6*x8**(-2.5) - x10*x4*(x0*x9 - x10*x20*x8**(-2.0))*(x14*x19 + x15*x22 - x18*x22)/x11 - x12*x15 + x12*x18 + x19*x21)/sqrt(x11)

def theta_dY2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = x1**2
    x3 = Z1 - Z2
    x4 = x0**2 + x2 + x3**2
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = Y2 - Y3
    x8 = x7**2
    x9 = Z2 - Z3
    x10 = x6**2 + x8 + x9**2
    x11 = x10**(-1.0)
    x12 = x1*x7
    x13 = x0*x6 + x12 + x3*x9
    x14 = -x11*x13**2*x5 + 1
    x15 = x4**(-0.5)
    x16 = x10**(-0.5)
    x17 = x15*x16
    x18 = x4**(-1.5)
    x19 = 1.0*x16*x18
    x20 = x10**(-1.5)
    x21 = 1.0*x15*x20
    x22 = Y1 - 2*Y2 + Y3
    x23 = 1.0*x15*x20*x7
    x24 = 1.0*x0*x6 + 1.0*x1*x7 + 1.0*x3*x9
    return (x1*x18*x20*x24*x7 - 3.0*x10**(-2.5)*x13*x15*x8 + x12*x21 + x13*x21 - x13*x5*(x1*x11 - x10**(-2.0)*x24*x7)*(x1*x13*x19 - x13*x23 + x17*x22)/x14 + x17 - x19*x2 + x22*x23)/sqrt(x14)

def theta_dY2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*Z1 - 1.0*Z2
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x1*x13*x14
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x6
    x19 = x16*(Y1 - 2*Y2 + Y3)
    x20 = 1.0*Z2 - 1.0*Z3
    x21 = x17*x20
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return (x1*x10*x13*x21 - 3.0*x10*x16*x6*x7*x8**(-2.5) - x10*x4*(-x10*x20*x8**(-2.0) + x2*x9)*(x14*x19 + x15*x22 - x18*x22)/x11 - x12*x15 + x12*x18 + x19*x21)/sqrt(x11)

def theta_dZ2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*X2 - 1.0*X3
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x13*x14*x2
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x7
    x19 = 1.0*x0*x13
    x20 = x14*(Z1 - 2*Z2 + Z3)
    x21 = x0*x10
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return -(-x10*x17*x19*x7 + x10*x9*(x21*x3**(-2.0) - x4*x5)*(x15*x22 + x16*x20 - x18*x22)/x11 - x12*x15 + x12*x18 + 3.0*x14*x2*x21*x3**(-2.5) + x19*x20)/sqrt(x11)

def theta_dZ2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*Y2 - 1.0*Y3
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x13*x14*x2
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x7
    x19 = 1.0*x1*x13
    x20 = x14*(Z1 - 2*Z2 + Z3)
    x21 = x1*x10
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return -(-x10*x17*x19*x7 + x10*x9*(x21*x3**(-2.0) - x4*x6)*(x15*x22 + x16*x20 - x18*x22)/x11 - x12*x15 + x12*x18 + 3.0*x14*x2*x21*x3**(-2.5) + x19*x20)/sqrt(x11)

def theta_dZ2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x2**2
    x4 = x0**2 + x1**2 + x3
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = Y2 - Y3
    x8 = Z2 - Z3
    x9 = x8**2
    x10 = x6**2 + x7**2 + x9
    x11 = x10**(-1.0)
    x12 = x2*x8
    x13 = x0*x6 + x1*x7 + x12
    x14 = -x11*x13**2*x5 + 1
    x15 = x4**(-0.5)
    x16 = x10**(-0.5)
    x17 = x15*x16
    x18 = x10**(-1.5)
    x19 = 1.0*x15*x18
    x20 = x4**(-1.5)
    x21 = 1.0*x16*x20
    x22 = Z1 - 2*Z2 + Z3
    x23 = 1.0*x16*x2*x20
    return (-x11*x13*(x13*x2*x4**(-2.0) - x5*x8)*(-x13*x19*x8 + x13*x23 + x17*x22)/x14 + 1.0*x12*x13*x18*x20 + x12*x21 - 3.0*x13*x16*x3*x4**(-2.5) + x13*x21 + x17 - x19*x9 - x22*x23)/sqrt(x14)

def theta_dZ2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x7**(-1.5)
    x14 = 1.0*x0*x13
    x15 = Z1 - 2*Z2 + Z3
    x16 = x9**(-0.5)
    x17 = x15*x16
    x18 = x7**(-0.5)
    x19 = x9**(-1.5)
    x20 = X1 - 2*X2 + X3
    x21 = 1.0*x13*x16*x4
    x22 = 1.0*x18*x19*x5
    x23 = x0*x6
    x24 = x1*x6
    return (-1.0*x1*x15*x18*x19 - 1.0*x13*x19*x24*x4 + x14*x17 - x14*x19*x5*x6 + 3.0*x16*x23*x4*x7**(-2.5) + 3.0*x18*x24*x5*x9**(-2.5) + x20*x21 - x20*x22 + x6*(x17*x18 + x21*x6 - x22*x6)*(x10*x23*x7**(-2.0) + x11*x20 - 1.0*x24*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dZ2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x7**(-1.5)
    x14 = 1.0*x13*x2
    x15 = Z1 - 2*Z2 + Z3
    x16 = x9**(-0.5)
    x17 = x15*x16
    x18 = x7**(-0.5)
    x19 = x9**(-1.5)
    x20 = Y1 - 2*Y2 + Y3
    x21 = 1.0*x13*x16*x4
    x22 = 1.0*x18*x19*x5
    x23 = x2*x6
    x24 = x3*x6
    return (-1.0*x13*x19*x24*x4 + x14*x17 - x14*x19*x5*x6 - 1.0*x15*x18*x19*x3 + 3.0*x16*x23*x4*x7**(-2.5) + 3.0*x18*x24*x5*x9**(-2.5) + x20*x21 - x20*x22 + x6*(x17*x18 + x21*x6 - x22*x6)*(x10*x23*x7**(-2.0) + x11*x20 - 1.0*x24*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dZ2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x4*x5
    x7 = x0*x1 + x2*x3 + x6
    x8 = x4**2
    x9 = x0**2 + x2**2 + x8
    x10 = x9**(-1.0)
    x11 = x5**2
    x12 = x1**2 + x11 + x3**2
    x13 = x12**(-1.0)
    x14 = x10*x13
    x15 = -x14*x7**2 + 1
    x16 = x9**(-0.5)
    x17 = x12**(-0.5)
    x18 = x16*x17
    x19 = 2.0*Z1 - 4.0*Z2 + 2.0*Z3
    x20 = x9**(-1.5)
    x21 = x17*x20*x4
    x22 = x12**(-1.5)
    x23 = x16*x22*x5
    x24 = 1.0*x0*x1 + 1.0*x2*x3 + 1.0*x4*x5
    x25 = 3.0*x0*x1 + 3.0*x2*x3 + 3.0*x4*x5
    x26 = Z1 - 2*Z2 + Z3
    return (x11*x12**(-2.5)*x16*x25 - x16*x22*x24 - x17*x20*x24 + x17*x25*x8*x9**(-2.5) - 2*x18 + x19*x21 - x19*x23 - 2.0*x20*x22*x6*x7 + x7*(x18*x26 + x21*x24 - x23*x24)*(-x10*x12**(-2.0)*x24*x5 + x13*x4*x7*x9**(-2.0) + x14*x26)/x15)/sqrt(x15)

def theta_dZ2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*X1 - 1.0*X2
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x13*x14*x2
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x7
    x19 = x16*(Z1 - 2*Z2 + Z3)
    x20 = 1.0*X2 - 1.0*X3
    x21 = x17*x20
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return (x10*x13*x2*x21 - 3.0*x10*x16*x5*x7*x8**(-2.5) - x10*x4*(x0*x9 - x10*x20*x8**(-2.0))*(x14*x19 + x15*x22 - x18*x22)/x11 - x12*x15 + x12*x18 + x19*x21)/sqrt(x11)

def theta_dZ2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = 1.0*Y1 - 1.0*Y2
    x13 = x3**(-1.5)
    x14 = x8**(-0.5)
    x15 = x13*x14*x2
    x16 = x3**(-0.5)
    x17 = x8**(-1.5)
    x18 = x16*x17*x7
    x19 = x16*(Z1 - 2*Z2 + Z3)
    x20 = 1.0*Y2 - 1.0*Y3
    x21 = x17*x20
    x22 = 1.0*x0*x5 + 1.0*x1*x6 + 1.0*x2*x7
    return (x10*x13*x2*x21 - 3.0*x10*x16*x6*x7*x8**(-2.5) - x10*x4*(x1*x9 - x10*x20*x8**(-2.0))*(x14*x19 + x15*x22 - x18*x22)/x11 - x12*x15 + x12*x18 + x19*x21)/sqrt(x11)

def theta_dZ2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x2**2
    x4 = x0**2 + x1**2 + x3
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = Y2 - Y3
    x8 = Z2 - Z3
    x9 = x8**2
    x10 = x6**2 + x7**2 + x9
    x11 = x10**(-1.0)
    x12 = x2*x8
    x13 = x0*x6 + x1*x7 + x12
    x14 = -x11*x13**2*x5 + 1
    x15 = x4**(-0.5)
    x16 = x10**(-0.5)
    x17 = x15*x16
    x18 = x4**(-1.5)
    x19 = 1.0*x16*x18
    x20 = x10**(-1.5)
    x21 = 1.0*x15*x20
    x22 = Z1 - 2*Z2 + Z3
    x23 = 1.0*x15*x20*x8
    x24 = 1.0*x0*x6 + 1.0*x1*x7 + 1.0*x2*x8
    return (-3.0*x10**(-2.5)*x13*x15*x9 + x12*x21 + x13*x21 - x13*x5*(-x10**(-2.0)*x24*x8 + x11*x2)*(x13*x19*x2 - x13*x23 + x17*x22)/x14 + x17 + x18*x2*x20*x24*x8 - x19*x3 + x22*x23)/sqrt(x14)

def theta_dX3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = x0**2
    x2 = Y1 - Y2
    x3 = Z1 - Z2
    x4 = x1 + x2**2 + x3**2
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = x6**2
    x8 = Y2 - Y3
    x9 = Z2 - Z3
    x10 = x7 + x8**2 + x9**2
    x11 = x10**(-1.0)
    x12 = x0*x6 + x2*x8 + x3*x9
    x13 = -x11*x12**2*x5 + 1
    x14 = x4**(-0.5)
    x15 = x10**(-0.5)
    x16 = 1.0*x4**(-1.5)
    x17 = x10**(-1.5)
    x18 = 1.0*x17
    return (-x0*x12*x16*x17*x6 + x1*x15*x16 + x11*x12*x14*(x0*x15 - x12*x18*x6)*(x0*x12*x4**(-2.0) - x5*x6)/x13 - x14*x15 + x14*x18*x7)/sqrt(x13)

def theta_dX3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x0*x8**(-0.5)
    x13 = 1.0*x1*x3**(-1.5)
    x14 = x3**(-0.5)
    x15 = x8**(-1.5)
    x16 = 1.0*x15*x5
    return (-x10*x13*x15*x5 + x10*x14*x9*(-x10*x16 + x12)*(x1*x10*x3**(-2.0) - x4*x6)/x11 + x12*x13 + x14*x16*x6)/sqrt(x11)

def theta_dX3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x0*x8**(-0.5)
    x13 = 1.0*x2*x3**(-1.5)
    x14 = x3**(-0.5)
    x15 = x8**(-1.5)
    x16 = 1.0*x15*x5
    return (-x10*x13*x15*x5 + x10*x14*x9*(-x10*x16 + x12)*(x10*x2*x3**(-2.0) - x4*x7)/x11 + x12*x13 + x14*x16*x7)/sqrt(x11)

def theta_dX3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = x0*x1
    x3 = Y1 - Y2
    x4 = Y2 - Y3
    x5 = Z1 - Z2
    x6 = Z2 - Z3
    x7 = x2 + x3*x4 + x5*x6
    x8 = x0**2
    x9 = x3**2 + x5**2 + x8
    x10 = x9**(-1.0)
    x11 = x1**2
    x12 = x11 + x4**2 + x6**2
    x13 = x12**(-1.0)
    x14 = x10*x13
    x15 = -x14*x7**2 + 1
    x16 = x9**(-0.5)
    x17 = x12**(-0.5)
    x18 = 1.0*x9**(-1.5)
    x19 = x12**(-1.5)
    x20 = 1.0*x16*x19
    x21 = X1 - 2*X2 + X3
    x22 = x16*x7
    x23 = 1.0*x1*x7
    return (x0*x1*x18*x19*x7 + x1*x20*x21 - 3.0*x11*x12**(-2.5)*x22 + x16*x17 - x17*x18*x8 + x2*x20 + x20*x7 - x22*(x0*x17 - x19*x23)*(x0*x13*x7*x9**(-2.0) - x10*x12**(-2.0)*x23 + x14*x21)/x15)/sqrt(x15)

def theta_dX3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x0*x9**(-0.5)
    x14 = x7**(-1.5)
    x15 = x7**(-0.5)
    x16 = x9**(-1.5)
    x17 = 1.0*x15*x16
    x18 = Y1 - 2*Y2 + Y3
    x19 = x1*x16
    x20 = x15*x6
    x21 = 1.0*x0*x1 + 1.0*x2*x3 + 1.0*x4*x5
    return (x0*x17*x3 + x1*x17*x18 - 3.0*x1*x20*x3*x9**(-2.5) - 1.0*x13*x14*x2 + 1.0*x14*x19*x2*x6 - x20*(x13 - x19*x21)*(x10*x2*x6*x7**(-2.0) + x11*x18 - x21*x3*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dX3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x0*x9**(-0.5)
    x14 = x7**(-1.5)
    x15 = x7**(-0.5)
    x16 = x9**(-1.5)
    x17 = 1.0*x15*x16
    x18 = Z1 - 2*Z2 + Z3
    x19 = x1*x16
    x20 = x15*x6
    x21 = 1.0*x0*x1 + 1.0*x2*x3 + 1.0*x4*x5
    return (x0*x17*x5 + x1*x17*x18 - 3.0*x1*x20*x5*x9**(-2.5) - 1.0*x13*x14*x4 + 1.0*x14*x19*x4*x6 - x20*(x13 - x19*x21)*(x10*x4*x6*x7**(-2.0) + x11*x18 - x21*x5*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dX3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = x4**2
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x4
    x11 = x1*x6 + x10 + x2*x7
    x12 = -x11**2*x3**(-1.0)*x9 + 1
    x13 = x8**(-1.5)
    x14 = 1.0*x0*x4 + 1.0*x1*x6 + 1.0*x2*x7
    return (x11*x3**(-1.5)*(x0*x8**(-0.5) - x13*x14*x4)*(x0*x9 - x14*x4*x8**(-2.0))/x12 - x3**(-0.5)*(2.0*x10*x13 - 3.0*x11*x5*x8**(-2.5) + x13*x14))/sqrt(x12)

def theta_dX3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x7**(-1.0)
    x9 = x0*x4 + x1*x5 + x2*x6
    x10 = -x3**(-1.0)*x8*x9**2 + 1
    x11 = x7**(-1.5)
    x12 = 1.0*x11*x4
    x13 = x5*x9
    return (-x3**(-0.5)*(1.0*x0*x11*x5 + x1*x12 - 3.0*x13*x4*x7**(-2.5)) + x3**(-1.5)*x9*(x0*x7**(-0.5) - x12*x9)*(x1*x8 - 1.0*x13*x7**(-2.0))/x10)/sqrt(x10)

def theta_dX3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x7**(-1.0)
    x9 = x0*x4 + x1*x5 + x2*x6
    x10 = -x3**(-1.0)*x8*x9**2 + 1
    x11 = x7**(-1.5)
    x12 = 1.0*x11*x4
    x13 = x6*x9
    return (-x3**(-0.5)*(1.0*x0*x11*x6 + x12*x2 - 3.0*x13*x4*x7**(-2.5)) + x3**(-1.5)*x9*(x0*x7**(-0.5) - x12*x9)*(-1.0*x13*x7**(-2.0) + x2*x8)/x10)/sqrt(x10)

def theta_dY3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x1*x8**(-0.5)
    x13 = 1.0*x0*x3**(-1.5)
    x14 = x3**(-0.5)
    x15 = x8**(-1.5)
    x16 = 1.0*x15*x6
    return (-x10*x13*x15*x6 + x10*x14*x9*(-x10*x16 + x12)*(x0*x10*x3**(-2.0) - x4*x5)/x11 + x12*x13 + x14*x16*x5)/sqrt(x11)

def theta_dY3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = x1**2
    x3 = Z1 - Z2
    x4 = x0**2 + x2 + x3**2
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = Y2 - Y3
    x8 = x7**2
    x9 = Z2 - Z3
    x10 = x6**2 + x8 + x9**2
    x11 = x10**(-1.0)
    x12 = x0*x6 + x1*x7 + x3*x9
    x13 = -x11*x12**2*x5 + 1
    x14 = x4**(-0.5)
    x15 = x10**(-0.5)
    x16 = 1.0*x4**(-1.5)
    x17 = x10**(-1.5)
    x18 = 1.0*x17
    return (-x1*x12*x16*x17*x7 + x11*x12*x14*(x1*x15 - x12*x18*x7)*(x1*x12*x4**(-2.0) - x5*x7)/x13 - x14*x15 + x14*x18*x8 + x15*x16*x2)/sqrt(x13)

def theta_dY3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x1*x8**(-0.5)
    x13 = 1.0*x2*x3**(-1.5)
    x14 = x3**(-0.5)
    x15 = x8**(-1.5)
    x16 = 1.0*x15*x6
    return (-x10*x13*x15*x6 + x10*x14*x9*(-x10*x16 + x12)*(x10*x2*x3**(-2.0) - x4*x7)/x11 + x12*x13 + x14*x16*x7)/sqrt(x11)

def theta_dY3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x2*x9**(-0.5)
    x14 = x7**(-1.5)
    x15 = x7**(-0.5)
    x16 = x9**(-1.5)
    x17 = 1.0*x15*x16
    x18 = X1 - 2*X2 + X3
    x19 = x16*x3
    x20 = x15*x6
    x21 = 1.0*x0*x1 + 1.0*x2*x3 + 1.0*x4*x5
    return (-1.0*x0*x13*x14 + 1.0*x0*x14*x19*x6 + x1*x17*x2 - 3.0*x1*x20*x3*x9**(-2.5) + x17*x18*x3 - x20*(x13 - x19*x21)*(x0*x10*x6*x7**(-2.0) - x1*x21*x8*x9**(-2.0) + x11*x18)/x12)/sqrt(x12)

def theta_dY3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = x2*x3
    x5 = Z1 - Z2
    x6 = Z2 - Z3
    x7 = x0*x1 + x4 + x5*x6
    x8 = x2**2
    x9 = x0**2 + x5**2 + x8
    x10 = x9**(-1.0)
    x11 = x3**2
    x12 = x1**2 + x11 + x6**2
    x13 = x12**(-1.0)
    x14 = x10*x13
    x15 = -x14*x7**2 + 1
    x16 = x9**(-0.5)
    x17 = x12**(-0.5)
    x18 = 1.0*x9**(-1.5)
    x19 = x12**(-1.5)
    x20 = 1.0*x16*x19
    x21 = Y1 - 2*Y2 + Y3
    x22 = x16*x7
    x23 = 1.0*x3*x7
    return (-3.0*x11*x12**(-2.5)*x22 + x16*x17 - x17*x18*x8 + x18*x19*x2*x3*x7 + x20*x21*x3 + x20*x4 + x20*x7 - x22*(x17*x2 - x19*x23)*(-x10*x12**(-2.0)*x23 + x13*x2*x7*x9**(-2.0) + x14*x21)/x15)/sqrt(x15)

def theta_dY3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x2*x9**(-0.5)
    x14 = x7**(-1.5)
    x15 = x7**(-0.5)
    x16 = x9**(-1.5)
    x17 = 1.0*x15*x16
    x18 = Z1 - 2*Z2 + Z3
    x19 = x16*x3
    x20 = x15*x6
    x21 = 1.0*x0*x1 + 1.0*x2*x3 + 1.0*x4*x5
    return (-1.0*x13*x14*x4 + 1.0*x14*x19*x4*x6 + x17*x18*x3 + x17*x2*x5 - 3.0*x20*x3*x5*x9**(-2.5) - x20*(x13 - x19*x21)*(x10*x4*x6*x7**(-2.0) + x11*x18 - x21*x5*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dY3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x7**(-1.0)
    x9 = x0*x4 + x1*x5 + x2*x6
    x10 = -x3**(-1.0)*x8*x9**2 + 1
    x11 = x7**(-1.5)
    x12 = 1.0*x11*x5
    x13 = x4*x9
    return (-x3**(-0.5)*(x0*x12 + 1.0*x1*x11*x4 - 3.0*x13*x5*x7**(-2.5)) + x3**(-1.5)*x9*(x0*x8 - 1.0*x13*x7**(-2.0))*(x1*x7**(-0.5) - x12*x9)/x10)/sqrt(x10)

def theta_dY3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = x5**2
    x7 = Z2 - Z3
    x8 = x4**2 + x6 + x7**2
    x9 = x8**(-1.0)
    x10 = x1*x5
    x11 = x0*x4 + x10 + x2*x7
    x12 = -x11**2*x3**(-1.0)*x9 + 1
    x13 = x8**(-1.5)
    x14 = 1.0*x0*x4 + 1.0*x1*x5 + 1.0*x2*x7
    return (x11*x3**(-1.5)*(x1*x8**(-0.5) - x13*x14*x5)*(x1*x9 - x14*x5*x8**(-2.0))/x12 - x3**(-0.5)*(2.0*x10*x13 - 3.0*x11*x6*x8**(-2.5) + x13*x14))/sqrt(x12)

def theta_dY3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x7**(-1.0)
    x9 = x0*x4 + x1*x5 + x2*x6
    x10 = -x3**(-1.0)*x8*x9**2 + 1
    x11 = x7**(-1.5)
    x12 = 1.0*x11*x5
    x13 = x6*x9
    return (-x3**(-0.5)*(1.0*x1*x11*x6 + x12*x2 - 3.0*x13*x5*x7**(-2.5)) + x3**(-1.5)*x9*(x1*x7**(-0.5) - x12*x9)*(-1.0*x13*x7**(-2.0) + x2*x8)/x10)/sqrt(x10)

def theta_dZ3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x2*x8**(-0.5)
    x13 = 1.0*x0*x3**(-1.5)
    x14 = x3**(-0.5)
    x15 = x8**(-1.5)
    x16 = 1.0*x15*x7
    return (-x10*x13*x15*x7 + x10*x14*x9*(-x10*x16 + x12)*(x0*x10*x3**(-2.0) - x4*x5)/x11 + x12*x13 + x14*x16*x5)/sqrt(x11)

def theta_dZ3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = x3**(-1.0)
    x5 = X2 - X3
    x6 = Y2 - Y3
    x7 = Z2 - Z3
    x8 = x5**2 + x6**2 + x7**2
    x9 = x8**(-1.0)
    x10 = x0*x5 + x1*x6 + x2*x7
    x11 = -x10**2*x4*x9 + 1
    x12 = x2*x8**(-0.5)
    x13 = 1.0*x1*x3**(-1.5)
    x14 = x3**(-0.5)
    x15 = x8**(-1.5)
    x16 = 1.0*x15*x7
    return (-x10*x13*x15*x7 + x10*x14*x9*(-x10*x16 + x12)*(x1*x10*x3**(-2.0) - x4*x6)/x11 + x12*x13 + x14*x16*x6)/sqrt(x11)

def theta_dZ3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x2**2
    x4 = x0**2 + x1**2 + x3
    x5 = x4**(-1.0)
    x6 = X2 - X3
    x7 = Y2 - Y3
    x8 = Z2 - Z3
    x9 = x8**2
    x10 = x6**2 + x7**2 + x9
    x11 = x10**(-1.0)
    x12 = x0*x6 + x1*x7 + x2*x8
    x13 = -x11*x12**2*x5 + 1
    x14 = x4**(-0.5)
    x15 = x10**(-0.5)
    x16 = 1.0*x4**(-1.5)
    x17 = x10**(-1.5)
    x18 = 1.0*x17
    return (x11*x12*x14*(-x12*x18*x8 + x15*x2)*(x12*x2*x4**(-2.0) - x5*x8)/x13 - x12*x16*x17*x2*x8 - x14*x15 + x14*x18*x9 + x15*x16*x3)/sqrt(x13)

def theta_dZ3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x4*x9**(-0.5)
    x14 = x7**(-1.5)
    x15 = x7**(-0.5)
    x16 = x9**(-1.5)
    x17 = 1.0*x15*x16
    x18 = X1 - 2*X2 + X3
    x19 = x16*x5
    x20 = x15*x6
    x21 = 1.0*x0*x1 + 1.0*x2*x3 + 1.0*x4*x5
    return (-1.0*x0*x13*x14 + 1.0*x0*x14*x19*x6 + x1*x17*x4 - 3.0*x1*x20*x5*x9**(-2.5) + x17*x18*x5 - x20*(x13 - x19*x21)*(x0*x10*x6*x7**(-2.0) - x1*x21*x8*x9**(-2.0) + x11*x18)/x12)/sqrt(x12)

def theta_dZ3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x0*x1 + x2*x3 + x4*x5
    x7 = x0**2 + x2**2 + x4**2
    x8 = x7**(-1.0)
    x9 = x1**2 + x3**2 + x5**2
    x10 = x9**(-1.0)
    x11 = x10*x8
    x12 = -x11*x6**2 + 1
    x13 = x4*x9**(-0.5)
    x14 = x7**(-1.5)
    x15 = x7**(-0.5)
    x16 = x9**(-1.5)
    x17 = 1.0*x15*x16
    x18 = Y1 - 2*Y2 + Y3
    x19 = x16*x5
    x20 = x15*x6
    x21 = 1.0*x0*x1 + 1.0*x2*x3 + 1.0*x4*x5
    return (-1.0*x13*x14*x2 + 1.0*x14*x19*x2*x6 + x17*x18*x5 + x17*x3*x4 - 3.0*x20*x3*x5*x9**(-2.5) - x20*(x13 - x19*x21)*(x10*x2*x6*x7**(-2.0) + x11*x18 - x21*x3*x8*x9**(-2.0))/x12)/sqrt(x12)

def theta_dZ3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = X2 - X3
    x2 = Y1 - Y2
    x3 = Y2 - Y3
    x4 = Z1 - Z2
    x5 = Z2 - Z3
    x6 = x4*x5
    x7 = x0*x1 + x2*x3 + x6
    x8 = x4**2
    x9 = x0**2 + x2**2 + x8
    x10 = x9**(-1.0)
    x11 = x5**2
    x12 = x1**2 + x11 + x3**2
    x13 = x12**(-1.0)
    x14 = x10*x13
    x15 = -x14*x7**2 + 1
    x16 = x9**(-0.5)
    x17 = x12**(-0.5)
    x18 = 1.0*x9**(-1.5)
    x19 = x12**(-1.5)
    x20 = 1.0*x16*x19
    x21 = Z1 - 2*Z2 + Z3
    x22 = x16*x7
    x23 = 1.0*x5*x7
    return (-3.0*x11*x12**(-2.5)*x22 + x16*x17 - x17*x18*x8 + x18*x19*x4*x5*x7 + x20*x21*x5 + x20*x6 + x20*x7 - x22*(x17*x4 - x19*x23)*(-x10*x12**(-2.0)*x23 + x13*x4*x7*x9**(-2.0) + x14*x21)/x15)/sqrt(x15)

def theta_dZ3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x7**(-1.0)
    x9 = x0*x4 + x1*x5 + x2*x6
    x10 = -x3**(-1.0)*x8*x9**2 + 1
    x11 = x7**(-1.5)
    x12 = 1.0*x11*x6
    x13 = x4*x9
    return (-x3**(-0.5)*(x0*x12 + 1.0*x11*x2*x4 - 3.0*x13*x6*x7**(-2.5)) + x3**(-1.5)*x9*(x0*x8 - 1.0*x13*x7**(-2.0))*(-x12*x9 + x2*x7**(-0.5))/x10)/sqrt(x10)

def theta_dZ3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x4**2 + x5**2 + x6**2
    x8 = x7**(-1.0)
    x9 = x0*x4 + x1*x5 + x2*x6
    x10 = -x3**(-1.0)*x8*x9**2 + 1
    x11 = x7**(-1.5)
    x12 = 1.0*x11*x6
    x13 = x5*x9
    return (-x3**(-0.5)*(x1*x12 + 1.0*x11*x2*x5 - 3.0*x13*x6*x7**(-2.5)) + x3**(-1.5)*x9*(x1*x8 - 1.0*x13*x7**(-2.0))*(-x12*x9 + x2*x7**(-0.5))/x10)/sqrt(x10)

def theta_dZ3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):
    x0 = X1 - X2
    x1 = Y1 - Y2
    x2 = Z1 - Z2
    x3 = x0**2 + x1**2 + x2**2
    x4 = X2 - X3
    x5 = Y2 - Y3
    x6 = Z2 - Z3
    x7 = x6**2
    x8 = x4**2 + x5**2 + x7
    x9 = x8**(-1.0)
    x10 = x2*x6
    x11 = x0*x4 + x1*x5 + x10
    x12 = -x11**2*x3**(-1.0)*x9 + 1
    x13 = x8**(-1.5)
    x14 = 1.0*x0*x4 + 1.0*x1*x5 + 1.0*x2*x6
    return (x11*x3**(-1.5)*(-x13*x14*x6 + x2*x8**(-0.5))*(-x14*x6*x8**(-2.0) + x2*x9)/x12 - x3**(-0.5)*(2.0*x10*x13 - 3.0*x11*x7*x8**(-2.5) + x13*x14))/sqrt(x12)

def phi_dX1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x1*x6
    x9 = Y3 - Y4
    x10 = X3 - X4
    x11 = x0*x9 - x1*x10
    x12 = Z1 - Z2
    x13 = -x0*x12 + x3*x6
    x14 = Z3 - Z4
    x15 = x0*x14 - x10*x3
    x16 = -x1*x12 + x3*x7
    x17 = x1*x14 - x3*x9
    x18 = x11*x8 + x13*x15 + x16*x17
    x19 = 1/x5
    x20 = x0*(-x11*x13 + x15*x8) + x1*(-x11*x16 + x17*x8) + x3*(x13*x17 - x15*x16)
    x21 = x0*(x1*x15 - x11*x3) + x17*x2 + x17*x4
    x22 = x1*x11 + x15*x3
    return 2*(x18*x21 - x20*x22)*(x18*x22 + x19*x20*x21)/(sqrt(x5)*(x18**2 + x19*x20**2)**2)

def phi_dX1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x0*x10 - x11*x2
    x13 = Z1 - Z2
    x14 = -x0*x13 + x4*x7
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x4
    x17 = -x13*x2 + x4*x8
    x18 = -x10*x4 + x15*x2
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x14 + x16*x9) + x2*(-x12*x17 + x18*x9) + x4*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x12*x2 + x16*x4
    x24 = x12*x4
    x25 = x1*x16 + x16*x5 + x2*(x0*x18 + x24)
    x26 = x0*x12 - x18*x4
    x27 = x0*(x16*x2 - x24) + x18*x3 + x18*x5
    x28 = 2*x22*(x19*x26 + x20*x21*x25)
    return x22*(-x19*x27*x28 + x21*x23*x28 - x23*x25 + x26*x27)/sqrt(x6)

def phi_dX1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = -X2
    x8 = X1 + x7
    x9 = -Y2
    x10 = Y1 + x9
    x11 = -x0*x10 + x2*x8
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x0*x12 - x13*x2
    x15 = Z1 - Z2
    x16 = -x0*x15 + x4*x8
    x17 = Z3 - Z4
    x18 = x0*x17 - x13*x4
    x19 = x10*x4 - x15*x2
    x20 = -x12*x4 + x17*x2
    x21 = x11*x14 + x16*x18 + x19*x20
    x22 = 1/x6
    x23 = x0*(x11*x18 - x14*x16) + x2*(x11*x20 - x14*x19) + x4*(x16*x20 - x18*x19)
    x24 = 1/(x21**2 + x22*x23**2)
    x25 = x0*x18 + x2*x20
    x26 = x18*x2
    x27 = x0*(-x14*x4 + x26) + x20*x3 + x20*x5
    x28 = x14*x2
    x29 = x18*x4 + x28
    x30 = X3 + x7
    x31 = Y3 + x9
    x32 = 2*x24*(x21*x25 + x22*x23*(x0*x14*x30 + x28*x31 - x4*(-x18*x31 + x20*x30)))
    return x24*(-x21*x27*x32 + x23*x29*x32 + x25*x27 + x29*(x1*x14 + x14*x3 + x4*(-x0*x20 + x26)))/sqrt(x6)

def phi_dX1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = -Y3
    x2 = Y2 + x1
    x3 = x2**2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x0**2 + x3 + x6
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x0*x9 + x2*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x0*x11 - x12*x2
    x14 = Z1 - Z2
    x15 = -x0*x14 + x5*x8
    x16 = Z3 - Z4
    x17 = x0*x16 - x12*x5
    x18 = -x14*x2 + x5*x9
    x19 = -x11*x5 + x16*x2
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x7
    x22 = x10*x17
    x23 = x13*x15
    x24 = x0*(x22 - x23) + x2*(x10*x19 - x13*x18) + x5*(x15*x19 - x17*x18)
    x25 = x24**2
    x26 = 1/(x20**2 + x21*x25)
    x27 = -x13*x5 + x17*x2
    x28 = Y1 + x1
    x29 = Z1 + x4
    x30 = -x10*x11 + x13*x28 - x15*x16 + x17*x29
    x31 = x0*x27 + x19*x3 + x19*x6
    x32 = x0*x21
    x33 = x20*x31
    x34 = x13*x2 + x17*x5
    x35 = x24*x34
    x36 = x17*x28
    x37 = x11*x15
    x38 = x13*x29
    x39 = x10*x16
    x40 = x2*(x11*x18 + x19*x28) - x22 + x23 + x5*(x16*x18 + x19*x29)
    x41 = 2*x26*(x0*x25/x7**2 + x20*x30 + x21*x24*(-x0*(-x36 - x37 + x38 + x39) + x40))
    return x26*(-x20*(x0*x19 + x27) + x24*(x11*x2 + x16*x5) + x30*x31 + x32*x33 - x32*x35 - x33*x41 - x34*(x0*(x36 + x37 - x38 - x39) + x40) + x35*x41)/sqrt(x7)

def phi_dX1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x6**2
    x8 = x2 + x4 + x7
    x9 = X1 - X2
    x10 = Y1 - Y2
    x11 = -x1*x10 + x3*x9
    x12 = Y3 - Y4
    x13 = x1*x12
    x14 = X3 - X4
    x15 = x14*x3
    x16 = x13 - x15
    x17 = Z1 - Z2
    x18 = -x1*x17 + x6*x9
    x19 = Z3 - Z4
    x20 = x1*x19 - x14*x6
    x21 = x10*x6 - x17*x3
    x22 = -x12*x6 + x19*x3
    x23 = x11*x16 + x18*x20 + x21*x22
    x24 = 1/x8
    x25 = x11*x22 - x16*x21
    x26 = x1*(x11*x20 - x16*x18) + x25*x3 + x6*(x18*x22 - x20*x21)
    x27 = x26**2
    x28 = 1/(x23**2 + x24*x27)
    x29 = X1 + x0
    x30 = Z1 + x5
    x31 = -x11*x14 + x16*x29 + x19*x21 - x22*x30
    x32 = x1*(-x16*x6 + x20*x3) + x22*x4 + x22*x7
    x33 = x24*x3
    x34 = x23*x32
    x35 = x16*x3 + x20*x6
    x36 = x26*x35
    x37 = x1*(x14*x18 + x20*x29) + x25 + x3*(x11*x19 + x14*x21 + x16*x30 + x22*x29) + x6*(x18*x19 + x20*x30)
    x38 = 2*x28*(x23*x31 + x24*x26*x37 - x27*x3/x8**2)
    return x28*(-x23*(x19*x2 + x19*x4 + x19*x7 + 2*x22*x3) + x26*(x13 - 2*x15) - x31*x32 + x33*x34 - x33*x36 + x34*x38 + x35*x37 - x36*x38)/sqrt(x8)

def phi_dX1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = -Y3
    x4 = Y2 + x3
    x5 = x4**2
    x6 = Z2 - Z3
    x7 = x6**2
    x8 = x2 + x5 + x7
    x9 = X1 - X2
    x10 = Y1 - Y2
    x11 = -x1*x10 + x4*x9
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x1*x12 - x13*x4
    x15 = Z1 - Z2
    x16 = -x1*x15 + x6*x9
    x17 = Z3 - Z4
    x18 = x1*x17
    x19 = x13*x6
    x20 = x18 - x19
    x21 = x10*x6 - x15*x4
    x22 = -x12*x6 + x17*x4
    x23 = x11*x14 + x16*x20 + x21*x22
    x24 = 1/x8
    x25 = x16*x22
    x26 = x20*x21
    x27 = x1*(x11*x20 - x14*x16) + x4*(x11*x22 - x14*x21) + x6*(x25 - x26)
    x28 = x27**2
    x29 = 1/(x23**2 + x24*x28)
    x30 = X1 + x0
    x31 = Y1 + x3
    x32 = -x12*x21 - x13*x16 + x20*x30 + x22*x31
    x33 = x1*(-x14*x6 + x20*x4) + x22*x5 + x22*x7
    x34 = x24*x6
    x35 = x23*x33
    x36 = x14*x4 + x20*x6
    x37 = x27*x36
    x38 = x14*x30
    x39 = x14*x31
    x40 = -x25 + x26 - x6*(-x12*x16 + x13*x21 - x20*x31 + x22*x30)
    x41 = 2*x29*(x23*x32 - x24*x27*(x1*(-x11*(X4 + x0) + x38) + x4*(-x11*(Y4 + x3) + x39) + x40) - x28*x6/x8**2)
    return x29*(x23*(x12*x2 + x12*x5 + x12*x7 - 2*x22*x6) + x27*(x18 - 2*x19) - x32*x33 + x34*x35 - x34*x37 + x35*x41 - x36*(x1*(x11*x13 + x38) + x4*(x11*x12 + x39) + x40) - x37*x41)/sqrt(x8)

def phi_dX1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x1*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = X3 - X4
    x12 = x0*x10 - x1*x11
    x13 = Z1 - Z2
    x14 = -x0*x13 + x3*x6
    x15 = -Z4
    x16 = Z3 + x15
    x17 = x0*x16 - x11*x3
    x18 = -x1*x13 + x3*x7
    x19 = x1*x16 - x10*x3
    x20 = x12*x8 + x14*x17 + x18*x19
    x21 = 1/x5
    x22 = x17*x8
    x23 = x12*x14
    x24 = x0*(x22 - x23) + x1*(-x12*x18 + x19*x8) + x3*(x14*x19 - x17*x18)
    x25 = x24**2
    x26 = 1/(x20**2 + x21*x25)
    x27 = Z2 + x15
    x28 = Y2 + x9
    x29 = x1*x17 - x12*x3
    x30 = x12*x7 + x13*x17 - x14*x27 - x28*x8
    x31 = x0*x29 + x19*x2 + x19*x4
    x32 = x0*x21
    x33 = x20*x31
    x34 = x1*x12 + x17*x3
    x35 = x24*x34
    x36 = x0*(-x12*x13 + x14*x28 + x17*x7 - x27*x8) + x1*(x18*x28 + x19*x7) - x22 + x23 + x3*(x13*x19 + x18*x27)
    x37 = 2*x26*(x0*x25/x5**2 + x20*x30 + x21*x24*x36)
    return x26*(x20*(x0*(x1*x27 - x28*x3) + x29) - x24*(x1*x28 + x27*x3) - x30*x31 - x32*x33 + x32*x35 + x33*x37 + x34*x36 - x35*x37)/sqrt(x5)

def phi_dX1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x1*x6
    x9 = Y3 - Y4
    x10 = x0*x9
    x11 = -X4
    x12 = X3 + x11
    x13 = x1*x12
    x14 = x10 - x13
    x15 = -Z2
    x16 = Z1 + x15
    x17 = -x0*x16 + x3*x6
    x18 = -Z4
    x19 = Z3 + x18
    x20 = x0*x19 - x12*x3
    x21 = -x1*x16 + x3*x7
    x22 = x1*x19 - x3*x9
    x23 = x14*x8 + x17*x20 + x21*x22
    x24 = 1/x5
    x25 = x22*x8
    x26 = -x14*x21
    x27 = x0*(-x14*x17 + x20*x8) + x1*(x25 + x26) + x3*(x17*x22 - x20*x21)
    x28 = x27**2
    x29 = 1/(x23**2 + x24*x28)
    x30 = Z2 + x18
    x31 = X2 + x11
    x32 = x14*x6 - x16*x22 + x21*x30 - x31*x8
    x33 = x0*(x1*x20 - x14*x3) + x2*x22 + x22*x4
    x34 = x1*x24
    x35 = x23*x33
    x36 = x1*x14 + x20*x3
    x37 = x27*x36
    x38 = x16*x20
    x39 = x0*(x17*x31 + x20*x6) + x1*(x14*x16 + x21*x31 + x22*x6 + x30*x8) + x25 + x26
    x40 = 2*x29*(-x1*x28/x5**2 + x23*x32 + x24*x27*(x3*(-x17*(Z4 + x15) + x38) + x39))
    return x29*(x23*(x0*(x20 + x3*x31) + 2*x1*x22 + x2*x30 + x30*x4) + x27*(x1*x31 - x10 + x13) + x32*x33 - x34*x35 + x34*x37 - x35*x40 - x36*(x3*(x17*x30 + x38) + x39) + x37*x40)/sqrt(x5)

def phi_dX1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x1*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = -X4
    x12 = X3 + x11
    x13 = x0*x10 - x1*x12
    x14 = Z1 - Z2
    x15 = -x0*x14 + x3*x6
    x16 = Z3 - Z4
    x17 = x0*x16
    x18 = x12*x3
    x19 = x17 - x18
    x20 = -x1*x14 + x3*x7
    x21 = x1*x16 - x10*x3
    x22 = x13*x8 + x15*x19 + x20*x21
    x23 = 1/x5
    x24 = x15*x21
    x25 = x19*x20
    x26 = x24 - x25
    x27 = x0*(-x13*x15 + x19*x8) + x1*(-x13*x20 + x21*x8) + x26*x3
    x28 = x27**2
    x29 = 1/(x22**2 + x23*x28)
    x30 = Y2 + x9
    x31 = X2 + x11
    x32 = -x15*x31 + x19*x6 - x20*x30 + x21*x7
    x33 = x0*(x1*x19 - x13*x3) + x2*x21 + x21*x4
    x34 = x23*x3
    x35 = x22*x33
    x36 = x1*x13 + x19*x3
    x37 = x27*x36
    x38 = x31*x8
    x39 = x30*x8
    x40 = x21*x6
    x41 = x20*x31
    x42 = x19*x7
    x43 = x15*x30
    x44 = 2*x29*(x22*x32 + x23*x27*(x0*(x13*(-X1 + X2) - x38) + x1*(x13*(-Y1 + Y2) - x39) + x26 - x3*(-x40 - x41 + x42 + x43)) - x28*x3/x5**2)
    return x29*(-x22*(x0*(x1*x31 + x13) + x2*x30 - 2*x21*x3 + x30*x4) + x27*(-x17 + x18 + x3*x31) + x32*x33 - x34*x35 + x34*x37 - x35*x44 + x36*(x0*(x13*x6 + x38) + x1*(x13*x7 + x39) - x24 + x25 - x3*(x40 + x41 - x42 - x43)) + x37*x44)/sqrt(x5)

def phi_dX1_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x2 + x4
    x6 = x0**2 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x1*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x0*x10 - x1*x11
    x13 = Z1 - Z2
    x14 = -x0*x13 + x3*x7
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x3
    x17 = -x1*x13 + x3*x8
    x18 = x1*x15 - x10*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x14 + x16*x9) + x1*(-x12*x17 + x18*x9) + x3*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x1*x9 + x14*x3
    x24 = x0*(x1*x16 - x12*x3) + x18*x2 + x18*x4
    x25 = x1*x12 + x16*x3
    x26 = x0*(x1*x14 - x3*x9) + x17*x2 + x17*x4
    x27 = 2*x22*(x19*x23 - x20*x21*x26)
    return x22*(x19*x24*x27 - x21*x25*x27 + x21*x5 - x23*x24 - x25*x26)/sqrt(x6)

def phi_dX1_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X1 - X2
    x1 = Y2 - Y3
    x2 = X2 - X3
    x3 = Y1 - Y2
    x4 = x0*x1 - x2*x3
    x5 = Y3 - Y4
    x6 = X3 - X4
    x7 = -x1*x6 + x2*x5
    x8 = Z2 - Z3
    x9 = Z1 - Z2
    x10 = x0*x8 - x2*x9
    x11 = Z3 - Z4
    x12 = x11*x2 - x6*x8
    x13 = -x1*x9 + x3*x8
    x14 = x1*x11 - x5*x8
    x15 = x10*x12 + x13*x14 + x4*x7
    x16 = x2**2
    x17 = x1**2
    x18 = x8**2
    x19 = x16 + x17 + x18
    x20 = 1/x19
    x21 = x1*(-x13*x7 + x14*x4) + x2*(-x10*x7 + x12*x4) + x8*(x10*x14 - x12*x13)
    x22 = 1/(x15**2 + x20*x21**2)
    x23 = sqrt(x19)
    x24 = 1/x23
    x25 = x1*x7 + x12*x8
    x26 = x1*(x13*x2 + x4*x8) + x10*x16 + x10*x18
    x27 = -x13*x8 + x2*x4
    x28 = x14*x17 + x14*x18 + x2*(x1*x12 - x7*x8)
    x29 = 2*x22*(-x15*x27 + x20*x21*x26)
    return x22*(-x1*x2*x21*x24 - x15*x23*x8 + x15*x24*x28*x29 - x21*x24*x25*x29 + x24*x25*x26 + x24*x27*x28)

def phi_dX1_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X2
    x1 = X1 + x0
    x2 = Y2 - Y3
    x3 = X2 - X3
    x4 = -Y2
    x5 = Y1 + x4
    x6 = x1*x2 - x3*x5
    x7 = Y3 - Y4
    x8 = X3 - X4
    x9 = -x2*x8 + x3*x7
    x10 = Z2 - Z3
    x11 = Z1 - Z2
    x12 = x1*x10 - x11*x3
    x13 = Z3 - Z4
    x14 = -x10*x8 + x13*x3
    x15 = x10*x5 - x11*x2
    x16 = -x10*x7 + x13*x2
    x17 = x12*x14 + x15*x16 + x6*x9
    x18 = x3**2
    x19 = x2**2
    x20 = x10**2
    x21 = x18 + x19 + x20
    x22 = 1/x21
    x23 = x10*(x12*x16 - x14*x15) + x2*(-x15*x9 + x16*x6) + x3*(-x12*x9 + x14*x6)
    x24 = 1/(x17**2 + x22*x23**2)
    x25 = sqrt(x21)
    x26 = x12*x3 + x15*x2
    x27 = 1/x25
    x28 = x16*x19 + x16*x20 + x3*(-x10*x9 + x14*x2)
    x29 = x10*x14 + x2*x9
    x30 = x18*x6 + x19*x6
    x31 = 2*x24*(x17*x26 + x22*x23*(x10*(-x12*(Y3 + x4) + x15*(X3 + x0)) + x30))
    return x24*(-x10*x23*x27*x3 + x17*x2*x25 - x17*x27*x28*x31 + x23*x27*x29*x31 + x26*x27*x28 - x27*x29*(x10*(x12*x2 - x15*x3) + x30))

def phi_dY1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x0*x10 - x11*x2
    x13 = Z1 - Z2
    x14 = -x0*x13 + x4*x7
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x4
    x17 = -x13*x2 + x4*x8
    x18 = -x10*x4 + x15*x2
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x14 + x16*x9) + x2*(-x12*x17 + x18*x9) + x4*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x12*x2 + x16*x4
    x24 = x12*x4
    x25 = x1*x16 + x16*x5 + x2*(x0*x18 + x24)
    x26 = x0*x12 - x18*x4
    x27 = x0*(x16*x2 - x24) + x18*x3 + x18*x5
    x28 = 2*x22*(x19*x23 + x20*x21*x27)
    return x22*(-x19*x25*x28 + x21*x26*x28 + x23*x25 - x26*x27)/sqrt(x6)

def phi_dY1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x1 + x2**2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = Y3 - Y4
    x10 = X3 - X4
    x11 = x0*x9 - x10*x2
    x12 = Z1 - Z2
    x13 = -x0*x12 + x3*x6
    x14 = Z3 - Z4
    x15 = x0*x14 - x10*x3
    x16 = -x12*x2 + x3*x7
    x17 = x14*x2 - x3*x9
    x18 = x11*x8 + x13*x15 + x16*x17
    x19 = 1/x5
    x20 = x0*(-x11*x13 + x15*x8) + x2*(-x11*x16 + x17*x8) + x3*(x13*x17 - x15*x16)
    x21 = x1*x15 + x15*x4 + x2*(x0*x17 + x11*x3)
    x22 = x0*x11 - x17*x3
    return 2*(x18*x21 - x20*x22)*(x18*x22 + x19*x20*x21)/(sqrt(x5)*(x18**2 + x19*x20**2)**2)

def phi_dY1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = -X2
    x8 = X1 + x7
    x9 = -Y2
    x10 = Y1 + x9
    x11 = -x0*x10 + x2*x8
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x0*x12 - x13*x2
    x15 = Z1 - Z2
    x16 = -x0*x15 + x4*x8
    x17 = Z3 - Z4
    x18 = x0*x17 - x13*x4
    x19 = x10*x4 - x15*x2
    x20 = -x12*x4 + x17*x2
    x21 = x11*x14 + x16*x18 + x19*x20
    x22 = 1/x6
    x23 = x0*(x11*x18 - x14*x16) + x2*(x11*x20 - x14*x19) + x4*(x16*x20 - x18*x19)
    x24 = 1/(x21**2 + x22*x23**2)
    x25 = x0*x18 + x2*x20
    x26 = x0*x20
    x27 = x1*x18 + x18*x5 + x2*(x14*x4 + x26)
    x28 = x0*x14
    x29 = -x20*x4 + x28
    x30 = X3 + x7
    x31 = Y3 + x9
    x32 = 2*x24*(x21*x25 + x22*x23*(x14*x2*x31 + x28*x30 - x4*(-x18*x31 + x20*x30)))
    return x24*(x21*x27*x32 - x23*x29*x32 - x25*x27 - x29*(x1*x14 + x14*x3 + x4*(x18*x2 - x26)))/sqrt(x6)

def phi_dY1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = -Y3
    x3 = Y2 + x2
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x6**2
    x8 = x1 + x4 + x7
    x9 = X1 - X2
    x10 = Y1 - Y2
    x11 = -x0*x10 + x3*x9
    x12 = Y3 - Y4
    x13 = x0*x12
    x14 = X3 - X4
    x15 = -x14*x3
    x16 = x13 + x15
    x17 = Z1 - Z2
    x18 = -x0*x17 + x6*x9
    x19 = Z3 - Z4
    x20 = x0*x19 - x14*x6
    x21 = x10*x6 - x17*x3
    x22 = -x12*x6 + x19*x3
    x23 = x11*x16 + x18*x20 + x21*x22
    x24 = 1/x8
    x25 = x11*x20
    x26 = x16*x18
    x27 = x0*(x25 - x26) + x3*(x11*x22 - x16*x21) + x6*(x18*x22 - x20*x21)
    x28 = x27**2
    x29 = 1/(x23**2 + x24*x28)
    x30 = Y1 + x2
    x31 = Z1 + x5
    x32 = -x11*x12 + x16*x30 - x18*x19 + x20*x31
    x33 = x1*x20 + x20*x7 + x3*(x0*x22 + x16*x6)
    x34 = x0*x24
    x35 = x23*x33
    x36 = x0*x16 - x22*x6
    x37 = x27*x36
    x38 = x20*x30
    x39 = x12*x18
    x40 = x16*x31
    x41 = x11*x19
    x42 = -x25 + x26 + x3*(x12*x21 + x22*x30) + x6*(x19*x21 + x22*x31)
    x43 = 2*x29*(x0*x28/x8**2 + x23*x32 + x24*x27*(-x0*(-x38 - x39 + x40 + x41) + x42))
    return x29*(x23*(2*x0*x20 + x1*x19 + x19*x4 + x19*x7) - x27*(2*x13 + x15) - x32*x33 - x34*x35 + x34*x37 + x35*x43 + x36*(x0*(x38 + x39 - x40 - x41) + x42) - x37*x43)/sqrt(x8)

def phi_dY1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x2 + x3**2 + x6
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x1*x9 + x3*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x1*x11 - x12*x3
    x14 = Z1 - Z2
    x15 = -x1*x14 + x5*x8
    x16 = Z3 - Z4
    x17 = x1*x16 - x12*x5
    x18 = -x14*x3 + x5*x9
    x19 = -x11*x5 + x16*x3
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x7
    x22 = x10*x19 - x13*x18
    x23 = x1*(x10*x17 - x13*x15) + x22*x3 + x5*(x15*x19 - x17*x18)
    x24 = x23**2
    x25 = 1/(x20**2 + x21*x24)
    x26 = x1*x19 + x13*x5
    x27 = X1 + x0
    x28 = Z1 + x4
    x29 = -x10*x12 + x13*x27 + x16*x18 - x19*x28
    x30 = x17*x2 + x17*x6 + x26*x3
    x31 = x21*x3
    x32 = x20*x30
    x33 = x1*x13 - x19*x5
    x34 = x23*x33
    x35 = x1*(x12*x15 + x17*x27) + x22 + x3*(x10*x16 + x12*x18 + x13*x28 + x19*x27) + x5*(x15*x16 + x17*x28)
    x36 = 2*x25*(x20*x29 + x21*x23*x35 - x24*x3/x7**2)
    return x25*(x20*(x17*x3 + x26) + x23*(x1*x12 + x16*x5) + x29*x30 - x31*x32 + x31*x34 - x32*x36 - x33*x35 + x34*x36)/sqrt(x7)

def phi_dY1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = -Y3
    x4 = Y2 + x3
    x5 = x4**2
    x6 = Z2 - Z3
    x7 = x6**2
    x8 = x2 + x5 + x7
    x9 = X1 - X2
    x10 = Y1 - Y2
    x11 = -x1*x10 + x4*x9
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x1*x12 - x13*x4
    x15 = Z1 - Z2
    x16 = -x1*x15 + x6*x9
    x17 = Z3 - Z4
    x18 = x1*x17 - x13*x6
    x19 = x10*x6 - x15*x4
    x20 = x17*x4
    x21 = x12*x6
    x22 = x20 - x21
    x23 = x11*x14 + x16*x18 + x19*x22
    x24 = 1/x8
    x25 = x16*x22
    x26 = x18*x19
    x27 = x1*(x11*x18 - x14*x16) + x4*(x11*x22 - x14*x19) + x6*(x25 - x26)
    x28 = x27**2
    x29 = 1/(x23**2 + x24*x28)
    x30 = X1 + x0
    x31 = Y1 + x3
    x32 = -x12*x19 - x13*x16 + x18*x30 + x22*x31
    x33 = x18*x2 + x18*x7 + x4*(x1*x22 + x14*x6)
    x34 = x24*x6
    x35 = x23*x33
    x36 = x1*x14 - x22*x6
    x37 = x27*x36
    x38 = x14*x30
    x39 = x14*x31
    x40 = -x25 + x26 - x6*(-x12*x16 + x13*x19 - x18*x31 + x22*x30)
    x41 = 2*x29*(x23*x32 - x24*x27*(x1*(-x11*(X4 + x0) + x38) + x4*(-x11*(Y4 + x3) + x39) + x40) - x28*x6/x8**2)
    return x29*(-x23*(x13*x2 + x13*x5 + x13*x7 - 2*x18*x6) + x27*(x20 - 2*x21) + x32*x33 - x34*x35 + x34*x37 - x35*x41 + x36*(x1*(x11*x13 + x38) + x4*(x11*x12 + x39) + x40) + x37*x41)/sqrt(x8)

def phi_dY1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x1 + x2**2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = X3 - X4
    x12 = x0*x10 - x11*x2
    x13 = Z1 - Z2
    x14 = -x0*x13 + x3*x6
    x15 = -Z4
    x16 = Z3 + x15
    x17 = x0*x16 - x11*x3
    x18 = -x13*x2 + x3*x7
    x19 = -x10*x3 + x16*x2
    x20 = x12*x8 + x14*x17 + x18*x19
    x21 = 1/x5
    x22 = x17*x8
    x23 = x12*x14
    x24 = x0*(x22 - x23) + x2*(-x12*x18 + x19*x8) + x3*(x14*x19 - x17*x18)
    x25 = x24**2
    x26 = 1/(x20**2 + x21*x25)
    x27 = Z2 + x15
    x28 = Y2 + x9
    x29 = x12*x7 + x13*x17 - x14*x27 - x28*x8
    x30 = x1*x17 + x17*x4 + x2*(x0*x19 + x12*x3)
    x31 = x0*x21
    x32 = x20*x30
    x33 = x0*x12 - x19*x3
    x34 = x24*x33
    x35 = x0*(-x12*x13 + x14*x28 + x17*x7 - x27*x8) + x2*(x18*x28 + x19*x7) - x22 + x23 + x3*(x13*x19 + x18*x27)
    x36 = 2*x26*(x0*x25/x5**2 + x20*x29 + x21*x24*x35)
    return x26*(-x20*(2*x0*x17 + x1*x27 + x2*(x19 + x28*x3) + x27*x4) + x24*(x0*x28 + x12) + x29*x30 + x31*x32 - x31*x34 - x32*x36 - x33*x35 + x34*x36)/sqrt(x5)

def phi_dY1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x1 + x2**2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = Y3 - Y4
    x10 = -X4
    x11 = X3 + x10
    x12 = x0*x9 - x11*x2
    x13 = -Z2
    x14 = Z1 + x13
    x15 = -x0*x14 + x3*x6
    x16 = -Z4
    x17 = Z3 + x16
    x18 = x0*x17 - x11*x3
    x19 = -x14*x2 + x3*x7
    x20 = x17*x2 - x3*x9
    x21 = x12*x8 + x15*x18 + x19*x20
    x22 = 1/x5
    x23 = x20*x8
    x24 = -x12*x19
    x25 = x0*(-x12*x15 + x18*x8) + x2*(x23 + x24) + x3*(x15*x20 - x18*x19)
    x26 = x25**2
    x27 = 1/(x21**2 + x22*x26)
    x28 = Z2 + x16
    x29 = X2 + x10
    x30 = x0*x20 + x12*x3
    x31 = x12*x6 - x14*x20 + x19*x28 - x29*x8
    x32 = x1*x18 + x18*x4 + x2*x30
    x33 = x2*x22
    x34 = x21*x32
    x35 = x0*x12 - x20*x3
    x36 = x25*x35
    x37 = x14*x18
    x38 = x0*(x15*x29 + x18*x6) + x2*(x12*x14 + x19*x29 + x20*x6 + x28*x8) + x23 + x24
    x39 = 2*x27*(x2*x26/x5**2 - x21*x31 - x22*x25*(x3*(-x15*(Z4 + x13) + x37) + x38))
    return x27*(-x21*(x2*(x0*x28 - x29*x3) + x30) - x25*(x0*x29 + x28*x3) - x31*x32 + x33*x34 - x33*x36 - x34*x39 + x35*(x3*(x15*x28 + x37) + x38) + x36*x39)/sqrt(x5)

def phi_dY1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x1 + x2**2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = x0*x10
    x12 = -X4
    x13 = X3 + x12
    x14 = x13*x2
    x15 = x11 - x14
    x16 = Z1 - Z2
    x17 = -x0*x16 + x3*x6
    x18 = Z3 - Z4
    x19 = x0*x18 - x13*x3
    x20 = -x16*x2 + x3*x7
    x21 = x18*x2
    x22 = x10*x3
    x23 = x21 - x22
    x24 = x15*x8 + x17*x19 + x20*x23
    x25 = 1/x5
    x26 = x17*x23
    x27 = x19*x20
    x28 = x26 - x27
    x29 = x0*(-x15*x17 + x19*x8) + x2*(-x15*x20 + x23*x8) + x28*x3
    x30 = x29**2
    x31 = 1/(x24**2 + x25*x30)
    x32 = X2 + x12
    x33 = Y2 + x9
    x34 = -x17*x32 + x19*x6 - x20*x33 + x23*x7
    x35 = x1*x19 + x19*x4 + x2*(x0*x23 + x15*x3)
    x36 = x25*x3
    x37 = x24*x35
    x38 = x0*x15 - x23*x3
    x39 = x29*x38
    x40 = x32*x8
    x41 = x33*x8
    x42 = x23*x6
    x43 = x20*x32
    x44 = x19*x7
    x45 = x17*x33
    x46 = 2*x31*(x24*x34 + x25*x29*(x0*(x15*(-X1 + X2) - x40) + x2*(x15*(-Y1 + Y2) - x41) + x28 - x3*(-x42 - x43 + x44 + x45)) - x3*x30/x5**2)
    return x31*(x24*(x1*x32 - 2*x19*x3 + x2*(x0*x33 - x11 + x14) + x32*x4) + x29*(-x21 + x22 + x3*x33) - x34*x35 + x36*x37 - x36*x39 + x37*x46 - x38*(x0*(x15*x6 + x40) + x2*(x15*x7 + x41) - x26 + x27 - x3*(x42 + x43 - x44 - x45)) - x39*x46)/sqrt(x5)

def phi_dY1_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X1 - X2
    x1 = Y2 - Y3
    x2 = X2 - X3
    x3 = Y1 - Y2
    x4 = x0*x1 - x2*x3
    x5 = Y3 - Y4
    x6 = X3 - X4
    x7 = -x1*x6 + x2*x5
    x8 = Z2 - Z3
    x9 = Z1 - Z2
    x10 = x0*x8 - x2*x9
    x11 = Z3 - Z4
    x12 = x11*x2 - x6*x8
    x13 = -x1*x9 + x3*x8
    x14 = x1*x11 - x5*x8
    x15 = x10*x12 + x13*x14 + x4*x7
    x16 = x2**2
    x17 = x1**2
    x18 = x8**2
    x19 = x16 + x17 + x18
    x20 = 1/x19
    x21 = x1*(-x13*x7 + x14*x4) + x2*(-x10*x7 + x12*x4) + x8*(x10*x14 - x12*x13)
    x22 = 1/(x15**2 + x20*x21**2)
    x23 = sqrt(x19)
    x24 = x1*x4 + x10*x8
    x25 = 1/x23
    x26 = x1*(x14*x2 + x7*x8) + x12*x16 + x12*x18
    x27 = -x14*x8 + x2*x7
    x28 = x13*x17 + x13*x18 + x2*(x1*x10 - x4*x8)
    x29 = 2*x22*(x15*x24 - x20*x21*x28)
    return x22*(-x1*x2*x21*x25 + x15*x23*x8 - x15*x25*x26*x29 + x21*x25*x27*x29 + x24*x25*x26 + x25*x27*x28)

def phi_dY1_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = Y2 - Y3
    x1 = X2 - X3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x2 + x4
    x6 = x0**2 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = x0*x7 - x1*x8
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = -x0*x11 + x1*x10
    x13 = Z1 - Z2
    x14 = -x1*x13 + x3*x7
    x15 = Z3 - Z4
    x16 = x1*x15 - x11*x3
    x17 = -x0*x13 + x3*x8
    x18 = x0*x15 - x10*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x17 + x18*x9) + x1*(-x12*x14 + x16*x9) + x3*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x1*x9 - x17*x3
    x24 = x0*(x1*x18 + x12*x3) + x16*x2 + x16*x4
    x25 = x1*x12 - x18*x3
    x26 = x0*(x1*x17 + x3*x9) + x14*x2 + x14*x4
    x27 = 2*x22*(-x19*x23 + x20*x21*x26)
    return x22*(-x19*x24*x27 + x21*x25*x27 + x21*x5 - x23*x24 - x25*x26)/sqrt(x6)

def phi_dY1_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X2
    x1 = X1 + x0
    x2 = Y2 - Y3
    x3 = X2 - X3
    x4 = -Y2
    x5 = Y1 + x4
    x6 = x1*x2 - x3*x5
    x7 = Y3 - Y4
    x8 = X3 - X4
    x9 = -x2*x8 + x3*x7
    x10 = Z2 - Z3
    x11 = Z1 - Z2
    x12 = x1*x10 - x11*x3
    x13 = Z3 - Z4
    x14 = -x10*x8 + x13*x3
    x15 = x10*x5 - x11*x2
    x16 = -x10*x7 + x13*x2
    x17 = x12*x14 + x15*x16 + x6*x9
    x18 = x3**2
    x19 = x2**2
    x20 = x10**2
    x21 = x18 + x19 + x20
    x22 = 1/x21
    x23 = x10*(x12*x16 - x14*x15) + x2*(-x15*x9 + x16*x6) + x3*(-x12*x9 + x14*x6)
    x24 = 1/(x17**2 + x22*x23**2)
    x25 = sqrt(x21)
    x26 = x12*x3 + x15*x2
    x27 = 1/x25
    x28 = x14*x18 + x14*x20 + x2*(x10*x9 + x16*x3)
    x29 = -x10*x16 + x3*x9
    x30 = x18*x6 + x19*x6
    x31 = 2*x24*(x17*x26 + x22*x23*(x10*(-x12*(Y3 + x4) + x15*(X3 + x0)) + x30))
    return x24*(-x10*x2*x23*x27 - x17*x25*x3 + x17*x27*x28*x31 - x23*x27*x29*x31 - x26*x27*x28 + x27*x29*(x10*(x12*x2 - x15*x3) + x30))

def phi_dZ1_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x0*x10 - x11*x2
    x13 = Z1 - Z2
    x14 = -x0*x13 + x4*x7
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x4
    x17 = -x13*x2 + x4*x8
    x18 = -x10*x4 + x15*x2
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x14 + x16*x9) + x2*(-x12*x17 + x18*x9) + x4*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x0*x16 + x18*x2
    x24 = x16*x2
    x25 = x0*(-x12*x4 + x24) + x18*x3 + x18*x5
    x26 = x12*x2 + x16*x4
    x27 = x1*x12 + x12*x3 + x4*(-x0*x18 + x24)
    x28 = 2*x22*(x19*x26 + x20*x21*x25)
    return x22*(x19*x27*x28 + x21*x23*x28 - x23*x25 - x26*x27)/sqrt(x6)

def phi_dZ1_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x0*x10 - x11*x2
    x13 = Z1 - Z2
    x14 = -x0*x13 + x4*x7
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x4
    x17 = -x13*x2 + x4*x8
    x18 = -x10*x4 + x15*x2
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x14 + x16*x9) + x2*(-x12*x17 + x18*x9) + x4*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x0*x16 + x18*x2
    x24 = x0*x18
    x25 = x1*x16 + x16*x5 + x2*(x12*x4 + x24)
    x26 = x0*x12 - x18*x4
    x27 = x1*x12 + x12*x3 + x4*(x16*x2 - x24)
    x28 = 2*x22*(x19*x26 + x20*x21*x25)
    return x22*(-x19*x27*x28 - x21*x23*x28 + x23*x25 + x26*x27)/sqrt(x6)

def phi_dZ1_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x1 + x3 + x4**2
    x6 = -X2
    x7 = X1 + x6
    x8 = -Y2
    x9 = Y1 + x8
    x10 = -x0*x9 + x2*x7
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x0*x11 - x12*x2
    x14 = Z1 - Z2
    x15 = -x0*x14 + x4*x7
    x16 = Z3 - Z4
    x17 = x0*x16 - x12*x4
    x18 = -x14*x2 + x4*x9
    x19 = -x11*x4 + x16*x2
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x5
    x22 = x0*(x10*x17 - x13*x15) + x2*(x10*x19 - x13*x18) + x4*(x15*x19 - x17*x18)
    x23 = x0*x17 + x19*x2
    x24 = X3 + x6
    x25 = Y3 + x8
    return -2*(x20*x23 + x21*x22*(x0*x13*x24 + x13*x2*x25 - x4*(-x17*x25 + x19*x24)))*(x20*(x1*x13 + x13*x3 + x4*(-x0*x19 + x17*x2)) + x22*x23)/(sqrt(x5)*(x20**2 + x21*x22**2)**2)

def phi_dZ1_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = -Y3
    x3 = Y2 + x2
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x1 + x4 + x6**2
    x8 = X1 - X2
    x9 = -Y2
    x10 = Y1 + x9
    x11 = -x0*x10 + x3*x8
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x0*x12 - x13*x3
    x15 = Z1 - Z2
    x16 = -x0*x15 + x6*x8
    x17 = Z3 - Z4
    x18 = x0*x17
    x19 = -x13*x6
    x20 = x18 + x19
    x21 = x10*x6 - x15*x3
    x22 = -x12*x6 + x17*x3
    x23 = x11*x14 + x16*x20 + x21*x22
    x24 = 1/x7
    x25 = x11*x20
    x26 = x14*x16
    x27 = x0*(x25 - x26) + x3*(x11*x22 - x14*x21) + x6*(x16*x22 - x20*x21)
    x28 = x27**2
    x29 = 1/(x23**2 + x24*x28)
    x30 = Y1 + x2
    x31 = Z1 + x5
    x32 = -x11*x12 + x14*x30 - x16*x17 + x20*x31
    x33 = x1*x14 + x14*x4 + x6*(-x0*x22 + x20*x3)
    x34 = x0*x24
    x35 = x23*x33
    x36 = x0*x20 + x22*x3
    x37 = x27*x36
    x38 = x20*x30
    x39 = x12*x16
    x40 = x14*x31
    x41 = x11*x17
    x42 = -x25 + x26 + x3*(x12*x21 + x22*x30) + x6*(x17*x21 + x22*x31)
    x43 = 2*x29*(x0*x28/x7**2 + x23*x32 + x24*x27*(-x0*(-x38 - x39 + x40 + x41) + x42))
    return x29*(-x23*(2*x0*x14 + x1*x12 + x12*x4 - x6*(x17*(Y3 + x9) + x22)) - x27*(2*x18 + x19) + x32*x33 + x34*x35 + x34*x37 - x35*x43 + x36*(x0*(x38 + x39 - x40 - x41) + x42) - x37*x43)/sqrt(x7)

def phi_dZ1_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x6**2
    x8 = x2 + x4 + x7
    x9 = X1 - X2
    x10 = Y1 - Y2
    x11 = -x1*x10 + x3*x9
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x1*x12 - x13*x3
    x15 = Z1 - Z2
    x16 = -x1*x15 + x6*x9
    x17 = Z3 - Z4
    x18 = x1*x17 - x13*x6
    x19 = x10*x6 - x15*x3
    x20 = x17*x3
    x21 = -x12*x6
    x22 = x20 + x21
    x23 = x11*x14 + x16*x18 + x19*x22
    x24 = 1/x8
    x25 = x11*x22 - x14*x19
    x26 = x1*(x11*x18 - x14*x16) + x25*x3 + x6*(x16*x22 - x18*x19)
    x27 = x26**2
    x28 = 1/(x23**2 + x24*x27)
    x29 = X1 + x0
    x30 = Z1 + x5
    x31 = -x11*x13 + x14*x29 + x17*x19 - x22*x30
    x32 = x14*x2 + x14*x4 + x6*(-x1*x22 + x18*x3)
    x33 = x24*x3
    x34 = x23*x32
    x35 = x1*x18 + x22*x3
    x36 = x26*x35
    x37 = x1*(x13*x16 + x18*x29) + x25 + x3*(x11*x17 + x13*x19 + x14*x30 + x22*x29) + x6*(x16*x17 + x18*x30)
    x38 = 2*x28*(x23*x31 + x24*x26*x37 - x27*x3/x8**2)
    return x28*(x23*(x13*x2 + x13*x4 + x13*x7 - 2*x14*x3) - x26*(2*x20 + x21) - x31*x32 + x33*x34 + x33*x36 + x34*x38 - x35*x37 + x36*x38)/sqrt(x8)

def phi_dZ1_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = -Y3
    x4 = Y2 + x3
    x5 = x4**2
    x6 = Z2 - Z3
    x7 = x2 + x5 + x6**2
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x1*x9 + x4*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x1*x11 - x12*x4
    x14 = Z1 - Z2
    x15 = -x1*x14 + x6*x8
    x16 = Z3 - Z4
    x17 = x1*x16 - x12*x6
    x18 = -x14*x4 + x6*x9
    x19 = -x11*x6 + x16*x4
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x7
    x22 = x15*x19
    x23 = x17*x18
    x24 = x1*(x10*x17 - x13*x15) + x4*(x10*x19 - x13*x18) + x6*(x22 - x23)
    x25 = x24**2
    x26 = 1/(x20**2 + x21*x25)
    x27 = -x1*x19 + x17*x4
    x28 = X1 + x0
    x29 = Y1 + x3
    x30 = -x11*x18 - x12*x15 + x17*x28 + x19*x29
    x31 = x13*x2 + x13*x5 + x27*x6
    x32 = x21*x6
    x33 = x20*x31
    x34 = x1*x17 + x19*x4
    x35 = x24*x34
    x36 = x13*x28
    x37 = x13*x29
    x38 = -x22 + x23 - x6*(-x11*x15 + x12*x18 - x17*x29 + x19*x28)
    x39 = 2*x26*(x20*x30 - x21*x24*(x1*(-x10*(X4 + x0) + x36) + x38 + x4*(-x10*(Y4 + x3) + x37)) - x25*x6/x7**2)
    return x26*(-x20*(x13*x6 + x27) + x24*(x1*x12 + x11*x4) - x30*x31 + x32*x33 + x32*x35 + x33*x39 + x34*(x1*(x10*x12 + x36) + x38 + x4*(x10*x11 + x37)) + x35*x39)/sqrt(x7)

def phi_dZ1_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x1 + x3 + x4**2
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = X3 - X4
    x12 = x0*x10 - x11*x2
    x13 = Z1 - Z2
    x14 = -x0*x13 + x4*x6
    x15 = -Z4
    x16 = Z3 + x15
    x17 = x0*x16 - x11*x4
    x18 = -x13*x2 + x4*x7
    x19 = x16*x2
    x20 = x10*x4
    x21 = x19 - x20
    x22 = x12*x8 + x14*x17 + x18*x21
    x23 = 1/x5
    x24 = x17*x8
    x25 = x12*x14
    x26 = x0*(x24 - x25) + x2*(-x12*x18 + x21*x8) + x4*(x14*x21 - x17*x18)
    x27 = x26**2
    x28 = 1/(x22**2 + x23*x27)
    x29 = Y2 + x9
    x30 = Z2 + x15
    x31 = x12*x7 + x13*x17 - x14*x30 - x29*x8
    x32 = x1*x12 + x12*x3 + x4*(-x0*x21 + x17*x2)
    x33 = x0*x23
    x34 = x22*x32
    x35 = x0*x17 + x2*x21
    x36 = x26*x35
    x37 = x0*(-x12*x13 + x14*x29 + x17*x7 - x30*x8) + x2*(x18*x29 + x21*x7) - x24 + x25 + x4*(x13*x21 + x18*x30)
    x38 = 2*x28*(x0*x27/x5**2 + x22*x31 + x23*x26*x37)
    return x28*(x22*(2*x0*x12 + x1*x29 + x29*x3 + x4*(-x19 + x2*x30 + x20)) + x26*(x0*x30 + x17) - x31*x32 - x33*x34 - x33*x36 + x34*x38 - x35*x37 + x36*x38)/sqrt(x5)

def phi_dZ1_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x1 + x3 + x4**2
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = Y3 - Y4
    x10 = -X4
    x11 = X3 + x10
    x12 = x0*x9 - x11*x2
    x13 = -Z2
    x14 = Z1 + x13
    x15 = -x0*x14 + x4*x6
    x16 = -Z4
    x17 = Z3 + x16
    x18 = x0*x17
    x19 = x11*x4
    x20 = x18 - x19
    x21 = -x14*x2 + x4*x7
    x22 = x17*x2 - x4*x9
    x23 = x12*x8 + x15*x20 + x21*x22
    x24 = 1/x5
    x25 = x22*x8
    x26 = -x12*x21
    x27 = x0*(-x12*x15 + x20*x8) + x2*(x25 + x26) + x4*(x15*x22 - x20*x21)
    x28 = x27**2
    x29 = 1/(x23**2 + x24*x28)
    x30 = X2 + x10
    x31 = Z2 + x16
    x32 = x12*x6 - x14*x22 + x21*x31 - x30*x8
    x33 = x1*x12 + x12*x3 + x4*(-x0*x22 + x2*x20)
    x34 = x2*x24
    x35 = x23*x33
    x36 = x0*x20 + x2*x22
    x37 = x27*x36
    x38 = x14*x20
    x39 = x0*(x15*x30 + x20*x6) + x2*(x12*x14 + x21*x30 + x22*x6 + x31*x8) + x25 + x26
    x40 = 2*x29*(x2*x28/x5**2 - x23*x32 - x24*x27*(x39 + x4*(-x15*(Z4 + x13) + x38)))
    return x29*(-x23*(x1*x30 - 2*x12*x2 + x3*x30 + x4*(x0*x31 - x18 + x19)) + x27*(x2*x31 + x22) + x32*x33 - x34*x35 - x34*x37 + x35*x40 + x36*(x39 + x4*(x15*x31 + x38)) + x37*x40)/sqrt(x5)

def phi_dZ1_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x1 + x3 + x4**2
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = -X4
    x12 = X3 + x11
    x13 = x0*x10 - x12*x2
    x14 = Z1 - Z2
    x15 = -x0*x14 + x4*x6
    x16 = Z3 - Z4
    x17 = x0*x16 - x12*x4
    x18 = -x14*x2 + x4*x7
    x19 = -x10*x4 + x16*x2
    x20 = x13*x8 + x15*x17 + x18*x19
    x21 = 1/x5
    x22 = x15*x19 - x17*x18
    x23 = x0*(-x13*x15 + x17*x8) + x2*(-x13*x18 + x19*x8) + x22*x4
    x24 = x23**2
    x25 = 1/(x20**2 + x21*x24)
    x26 = Y2 + x9
    x27 = X2 + x11
    x28 = -x0*x19 + x17*x2
    x29 = -x15*x27 + x17*x6 - x18*x26 + x19*x7
    x30 = x1*x13 + x13*x3 + x28*x4
    x31 = x21*x4
    x32 = x20*x30
    x33 = x0*x17 + x19*x2
    x34 = x23*x33
    x35 = x27*x8
    x36 = x26*x8
    x37 = x19*x6
    x38 = x18*x27
    x39 = x17*x7
    x40 = x15*x26
    x41 = 2*x25*(-x20*x29 - x21*x23*(x0*(x13*(-X1 + X2) - x35) + x2*(x13*(-Y1 + Y2) - x36) + x22 - x4*(-x37 - x38 + x39 + x40)) + x24*x4/x5**2)
    return x25*(x20*(x28 + x4*(x0*x26 - x2*x27)) - x23*(x0*x27 + x2*x26) + x29*x30 - x31*x32 - x31*x34 + x32*x41 + x33*(-x0*(x13*x6 + x35) - x2*(x13*x7 + x36) + x22 + x4*(x37 + x38 - x39 - x40)) + x34*x41)/sqrt(x5)

def phi_dZ1_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X1 - X2
    x1 = Y2 - Y3
    x2 = X2 - X3
    x3 = Y1 - Y2
    x4 = x0*x1 - x2*x3
    x5 = Y3 - Y4
    x6 = X3 - X4
    x7 = -x1*x6 + x2*x5
    x8 = Z2 - Z3
    x9 = Z1 - Z2
    x10 = x0*x8 - x2*x9
    x11 = Z3 - Z4
    x12 = x11*x2 - x6*x8
    x13 = -x1*x9 + x3*x8
    x14 = x1*x11 - x5*x8
    x15 = x10*x12 + x13*x14 + x4*x7
    x16 = x2**2
    x17 = x1**2
    x18 = x8**2
    x19 = x16 + x17 + x18
    x20 = 1/x19
    x21 = x1*(-x13*x7 + x14*x4) + x2*(-x10*x7 + x12*x4) + x8*(x10*x14 - x12*x13)
    x22 = 1/(x15**2 + x20*x21**2)
    x23 = sqrt(x19)
    x24 = 1/x23
    x25 = x1*x14 + x12*x2
    x26 = x13*x17 + x13*x18 + x2*(x1*x10 - x4*x8)
    x27 = x1*x4 + x10*x8
    x28 = x16*x7 + x17*x7 - x8*(-x1*x12 + x14*x2)
    x29 = 2*x22*(x15*x27 - x20*x21*x26)
    return x22*(-x1*x15*x23 + x15*x24*x28*x29 - x2*x21*x24*x8 + x21*x24*x25*x29 + x24*x25*x26 - x24*x27*x28)

def phi_dZ1_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X1 - X2
    x1 = Y2 - Y3
    x2 = X2 - X3
    x3 = Y1 - Y2
    x4 = x0*x1 - x2*x3
    x5 = Y3 - Y4
    x6 = X3 - X4
    x7 = -x1*x6 + x2*x5
    x8 = Z2 - Z3
    x9 = Z1 - Z2
    x10 = x0*x8 - x2*x9
    x11 = Z3 - Z4
    x12 = x11*x2 - x6*x8
    x13 = -x1*x9 + x3*x8
    x14 = x1*x11 - x5*x8
    x15 = x10*x12 + x13*x14 + x4*x7
    x16 = x2**2
    x17 = x1**2
    x18 = x8**2
    x19 = x16 + x17 + x18
    x20 = 1/x19
    x21 = x1*(-x13*x7 + x14*x4) + x2*(-x10*x7 + x12*x4) + x8*(x10*x14 - x12*x13)
    x22 = 1/(x15**2 + x20*x21**2)
    x23 = sqrt(x19)
    x24 = 1/x23
    x25 = x1*x14 + x12*x2
    x26 = x1*(x13*x2 + x4*x8) + x10*x16 + x10*x18
    x27 = -x13*x8 + x2*x4
    x28 = x16*x7 + x17*x7 + x8*(x1*x12 - x14*x2)
    x29 = 2*x22*(-x15*x27 + x20*x21*x26)
    return x22*(-x1*x21*x24*x8 + x15*x2*x23 + x15*x24*x28*x29 + x21*x24*x25*x29 - x24*x25*x26 + x24*x27*x28)

def phi_dZ1_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = Z2 - Z3
    x1 = X2 - X3
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = x3**2
    x5 = x2 + x4
    x6 = x0**2 + x5
    x7 = -X2
    x8 = X1 + x7
    x9 = -Y2
    x10 = Y1 + x9
    x11 = -x1*x10 + x3*x8
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x1*x12 - x13*x3
    x15 = Z1 - Z2
    x16 = x0*x8 - x1*x15
    x17 = Z3 - Z4
    x18 = -x0*x13 + x1*x17
    x19 = x0*x10 - x15*x3
    x20 = -x0*x12 + x17*x3
    x21 = x11*x14 + x16*x18 + x19*x20
    x22 = 1/x6
    x23 = x0*(x16*x20 - x18*x19) + x1*(x11*x18 - x14*x16) + x3*(x11*x20 - x14*x19)
    x24 = 1/(x21**2 + x22*x23**2)
    x25 = x1*x16 + x19*x3
    x26 = x0*(-x1*x20 + x18*x3) + x14*x2 + x14*x4
    x27 = x1*x18 + x20*x3
    x28 = x11*x2 + x11*x4
    x29 = 2*x24*(x21*x25 + x22*x23*(x0*(-x16*(Y3 + x9) + x19*(X3 + x7)) + x28))
    return x24*(-x21*x26*x29 - x23*x27*x29 + x23*x5 + x25*x26 + x27*(x0*(-x1*x19 + x16*x3) + x28))/sqrt(x6)

def phi_dX2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = -Y3
    x2 = Y2 + x1
    x3 = x2**2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x0**2 + x3 + x6
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x0*x9 + x2*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x0*x11 - x12*x2
    x14 = Z1 - Z2
    x15 = -x0*x14 + x5*x8
    x16 = Z3 - Z4
    x17 = x0*x16 - x12*x5
    x18 = -x14*x2 + x5*x9
    x19 = -x11*x5 + x16*x2
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x7
    x22 = x10*x17
    x23 = x13*x15
    x24 = x0*(x22 - x23) + x2*(x10*x19 - x13*x18) + x5*(x15*x19 - x17*x18)
    x25 = 1/(x20**2 + x21*x24**2)
    x26 = Y1 + x1
    x27 = Z1 + x4
    x28 = -x10*x11 + x13*x26 - x15*x16 + x17*x27
    x29 = x17*x2
    x30 = x13*x5
    x31 = x0*(x29 - x30) + x19*x3 + x19*x6
    x32 = x0*x21
    x33 = x13*x2 + x17*x5
    x34 = -x0*(x10*x16 - x11*x15 + x13*x27 - x17*x26) + x2*(x11*x18 + x19*x26) - x22 + x23 + x24*x32 + x5*(x16*x18 + x19*x27)
    x35 = 2*x25*(x20*x33 + x21*x24*x31)
    return x25*(-x20*x34*x35 + x20*(-x0*x19 - x29 + x30 + x31*x32) + x24*x28*x35 + x24*(x11*x2 + x16*x5) - x28*x31 + x33*x34)/sqrt(x7)

def phi_dX2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = -Y3
    x3 = Y2 + x2
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x6**2
    x8 = x1 + x4 + x7
    x9 = X1 - X2
    x10 = Y1 - Y2
    x11 = -x0*x10 + x3*x9
    x12 = Y3 - Y4
    x13 = x0*x12
    x14 = X3 - X4
    x15 = -x14*x3
    x16 = x13 + x15
    x17 = Z1 - Z2
    x18 = -x0*x17 + x6*x9
    x19 = Z3 - Z4
    x20 = x0*x19
    x21 = -x14*x6
    x22 = x20 + x21
    x23 = x10*x6 - x17*x3
    x24 = -x12*x6 + x19*x3
    x25 = x11*x16 + x18*x22 + x23*x24
    x26 = 1/x8
    x27 = x11*x22
    x28 = x16*x18
    x29 = x0*(x27 - x28) + x3*(x11*x24 - x16*x23) + x6*(x18*x24 - x22*x23)
    x30 = 1/(x25**2 + x26*x29**2)
    x31 = Y1 + x2
    x32 = Z1 + x5
    x33 = -x11*x12 + x16*x31 - x18*x19 + x22*x32
    x34 = x1*x22 + x22*x7 + x3*(x0*x24 + x16*x6)
    x35 = x0*x26
    x36 = x0*x16 - x24*x6
    x37 = -x0*(x11*x19 - x12*x18 + x16*x32 - x22*x31) - x27 + x28 + x29*x35 + x3*(x12*x23 + x24*x31) + x6*(x19*x23 + x24*x32)
    x38 = 2*x30*(x25*x36 + x26*x29*x34)
    return x30*(x25*x37*x38 - x25*(-x0*x22 - x0*(2*x20 + x21) - x19*x4 - x19*x7 + x34*x35) - x29*x33*x38 - x29*(2*x13 + x15) + x33*x34 - x36*x37)/sqrt(x8)

def phi_dX2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = -Y3
    x3 = Y2 + x2
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x1 + x4 + x6**2
    x8 = -X2
    x9 = X1 + x8
    x10 = -Y2
    x11 = Y1 + x10
    x12 = -x0*x11 + x3*x9
    x13 = Y3 - Y4
    x14 = x0*x13
    x15 = X3 - X4
    x16 = x15*x3
    x17 = x14 - x16
    x18 = Z1 - Z2
    x19 = -x0*x18 + x6*x9
    x20 = Z3 - Z4
    x21 = x0*x20
    x22 = -x15*x6
    x23 = x21 + x22
    x24 = x11*x6 - x18*x3
    x25 = -x13*x6 + x20*x3
    x26 = x12*x17 + x19*x23 + x24*x25
    x27 = 1/x7
    x28 = x12*x23
    x29 = x17*x19
    x30 = x0*(x28 - x29) + x3*(x12*x25 - x17*x24) + x6*(x19*x25 - x23*x24)
    x31 = 1/(x26**2 + x27*x30**2)
    x32 = Y1 + x2
    x33 = Z1 + x5
    x34 = -x12*x13 + x17*x32 - x19*x20 + x23*x33
    x35 = x1*x17 + x17*x4
    x36 = x0*x25
    x37 = x23*x3
    x38 = x0*x27
    x39 = x35 + x6*(-x36 + x37)
    x40 = x0*x23 + x25*x3
    x41 = -x0*(x12*x20 - x13*x19 + x17*x33 - x23*x32) - x28 + x29 + x3*(x13*x24 + x25*x32) + x30*x38 + x6*(x20*x24 + x25*x33)
    x42 = 2*x31*(x26*x40 - x27*x30*x39)
    return x31*(x26*x41*x42 + x26*(-x0*x17 + x0*(x13*(X3 + x8) - x14 + x16) - x13*x4 + x38*x39 + x6*(x20*(Y3 + x10) + x25)) - x30*x34*x42 - x30*(2*x21 + x22) - x34*(x35 - x6*(x36 - x37)) - x40*x41)/sqrt(x7)

def phi_dX2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = -Y3
    x3 = Y2 + x2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1 + x3**2 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x3*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x0*x10 - x11*x3
    x13 = Z1 - Z2
    x14 = -x0*x13 + x5*x7
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x5
    x17 = -x13*x3 + x5*x8
    x18 = -x10*x5 + x15*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x16*x9
    x22 = x12*x14
    x23 = x21 - x22
    x24 = -x12*x17 + x18*x9
    x25 = x14*x18 - x16*x17
    x26 = x0*x23 + x24*x3 + x25*x5
    x27 = x26**2
    x28 = 1/(x19**2 + x20*x27)
    x29 = Y1 + x2
    x30 = Z1 + x4
    x31 = 2*x0*x23 + 2*x24*x3 + 2*x25*x5
    x32 = -x10*x9 + x12*x29 - x14*x15 + x16*x30
    x33 = x20*x26
    x34 = x0*x33
    x35 = x16*x29
    x36 = x10*x14
    x37 = x12*x30
    x38 = x15*x9
    x39 = -x21 + x22 + x3*(x10*x17 + x18*x29) + x5*(x15*x17 + x18*x30)
    x40 = -x0*(-x35 - x36 + x37 + x38) + x39
    x41 = x34 + x40
    x42 = 2*X2 - 2*X3
    x43 = x6**(-2)
    x44 = x28*(x0*x27*x43 + x19*x32 + x33*x40)
    return x28*(2*x19*x41*x44 - x19*(3*x1*x26*x43 + x20*x40*x42 - x33 - 2*x35 - 2*x36 + 2*x37 + 2*x38 - x42*(-x10*x30 + x15*x29)) - x31*x32*x44 - x31*(x10*x29 + x15*x30) + x32*x34 - x32*x41 + x32*(x0*(x35 + x36 - x37 - x38) + x39))/sqrt(x6)

def phi_dX2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1**2 + x3**2 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x3*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x1*x10 - x11*x3
    x13 = Z1 - Z2
    x14 = -x1*x13 + x5*x7
    x15 = Z3 - Z4
    x16 = x1*x15 - x11*x5
    x17 = -x13*x3 + x5*x8
    x18 = -x10*x5 + x15*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x16*x9
    x22 = x12*x14
    x23 = -x12*x17 + x18*x9
    x24 = x1*(x21 - x22) + x23*x3 + x5*(x14*x18 - x16*x17)
    x25 = x24**2
    x26 = 1/(x19**2 + x20*x25)
    x27 = X1 + x0
    x28 = Y1 + x2
    x29 = x20*x3
    x30 = Z1 + x4
    x31 = x16*x30
    x32 = x14*x15
    x33 = -x10*x9 + x12*x28 + x31 - x32
    x34 = x24*x33
    x35 = x11*x14 + x16*x27
    x36 = x12*x30 + x15*x9
    x37 = x1*x35 + x23 + x3*(x11*x17 + x18*x27 + x36) + x5*(x31 + x32)
    x38 = x15*x17
    x39 = x18*x30
    x40 = -x11*x9 + x12*x27 + x38 - x39
    x41 = x18*x28
    x42 = x10*x17
    x43 = -x1*(-x10*x14 - x16*x28 + x36) - x21 + x22 + x3*(x41 + x42) + x5*(x38 + x39)
    x44 = x1*x20*x24 + x43
    x45 = x3/x6**2
    x46 = x20*x37
    x47 = 2*x26*(x19*x40 + x24*x46 - x25*x45)
    return x26*(-x19*x44*x47 - x19*(3*x1*x24*x45 - x1*x46 + x1*(-x11*x30 + x15*x27) + x29*x43 - x3*(-x10*x30 + x15*x28) + x35 - x41 - x42) + x24*(x10*x27 + x11*x28) + x29*x34 - x33*x37 + x34*x47 + x40*x44)/sqrt(x6)

def phi_dX2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1**2 + x3**2 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x3*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x1*x10 - x11*x3
    x13 = Z1 - Z2
    x14 = -x1*x13 + x5*x7
    x15 = Z3 - Z4
    x16 = x1*x15 - x11*x5
    x17 = -x13*x3 + x5*x8
    x18 = -x10*x5 + x15*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x16*x9
    x22 = x12*x14
    x23 = x21 - x22
    x24 = x14*x18
    x25 = x16*x17
    x26 = x24 - x25
    x27 = x1*x23 + x26*x5 + x3*(-x12*x17 + x18*x9)
    x28 = x27**2
    x29 = 1/(x19**2 + x20*x28)
    x30 = X1 + x0
    x31 = Z1 + x4
    x32 = x20*x5
    x33 = Y1 + x2
    x34 = x12*x33
    x35 = x10*x9
    x36 = -x14*x15 + x16*x31 + x34 - x35
    x37 = x27*x36
    x38 = x12*x30
    x39 = x11*x9
    x40 = -x10*x14 - x16*x33
    x41 = x5*(x11*x17 + x18*x30 + x40)
    x42 = -x24 + x25 - x41
    x43 = x18*x33
    x44 = x10*x17
    x45 = -x11*x14 + x16*x30 + x43 - x44
    x46 = x3*(x43 + x44)
    x47 = x15*x17 + x18*x31
    x48 = x47*x5
    x49 = x1*(x12*x31 + x15*x9 + x40)
    x50 = x1*x20*x27 - x21 + x22 + x46 + x48 - x49
    x51 = X4 + x0
    x52 = Y4 + x2
    x53 = x5/x6**2
    x54 = x1*(x38 - x51*x9)
    x55 = x3*(x34 - x52*x9)
    x56 = 2*x29*(x19*x45 - x20*x27*(x42 + x54 + x55) - x28*x53)
    return x29*(-x19*x50*x56 + x19*(x1*x20*(x26 + x41 - x54 - x55) - 3*x1*x27*x53 + x1*(x10*x30 - x51*(-Y1 + Y3)) + x32*(x23 - x46 - x48 + x49) + x38 + x39 + x47 + x5*(x15*x33 - x52*(-Z1 + Z3))) + x27*(x11*x31 + x15*x30) + x32*x37 + x36*(x1*(x38 + x39) + x3*(x34 + x35) + x42) + x37*x56 + x45*x50)/sqrt(x6)

def phi_dX2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = -Y3
    x3 = Y2 + x2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1 + x3**2 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x3*x7
    x10 = -Y4
    x11 = Y3 + x10
    x12 = X3 - X4
    x13 = x0*x11 - x12*x3
    x14 = Z1 - Z2
    x15 = -x0*x14 + x5*x7
    x16 = -Z4
    x17 = Z3 + x16
    x18 = x0*x17 - x12*x5
    x19 = -x14*x3 + x5*x8
    x20 = -x11*x5 + x17*x3
    x21 = x13*x9 + x15*x18 + x19*x20
    x22 = 1/x6
    x23 = x18*x9
    x24 = x13*x15
    x25 = x0*(x23 - x24) + x3*(-x13*x19 + x20*x9) + x5*(x15*x20 - x18*x19)
    x26 = x25**2
    x27 = 1/(x21**2 + x22*x26)
    x28 = Y1 + x2
    x29 = Y2 + x10
    x30 = Z1 + x4
    x31 = Z2 + x16
    x32 = -x11*x9 + x13*x28 - x15*x17 + x18*x30
    x33 = x22*x25
    x34 = x0*x33
    x35 = -x23 + x24
    x36 = x18*x8
    x37 = x15*x29
    x38 = x13*x14
    x39 = x31*x9
    x40 = x0*(x36 + x37 - x38 - x39) + x3*(x19*x29 + x20*x8) + x35 + x5*(x14*x20 + x19*x31)
    x41 = x13*x8 + x14*x18 - x15*x31 - x29*x9
    x42 = -x11*x15 + x13*x30 + x17*x9 - x18*x28
    x43 = -x0*x42 + x3*(x11*x19 + x20*x28) + x35 + x5*(x17*x19 + x20*x30)
    x44 = x34 + x43
    x45 = x6**(-2)
    x46 = x0*x22
    x47 = 2*x27*(x0*x26*x45 + x21*x41 + x33*x40)
    return x27*(-x21*x44*x47 + x21*(-x0*(-x11*x14 + x17*x8 + x28*x31 - x29*x30) + 3*x1*x25*x45 - x33 - x36 - x37 + x38 + x39 + x40*x46 + x42 + x43*x46) + x25*x32*x47 + x25*(x11*x8 + x14*x17 + x28*x29 + x30*x31) - x32*x34 - x32*x40 + x41*x44)/sqrt(x6)

def phi_dX2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = -Y3
    x2 = Y2 + x1
    x3 = -Z3
    x4 = Z2 + x3
    x5 = x0**2 + x2**2 + x4**2
    x6 = X1 - X2
    x7 = x2*x6
    x8 = Y1 - Y2
    x9 = x0*x8
    x10 = x7 - x9
    x11 = Y3 - Y4
    x12 = x0*x11
    x13 = -X4
    x14 = X3 + x13
    x15 = x14*x2
    x16 = x12 - x15
    x17 = -Z2
    x18 = Z1 + x17
    x19 = -x0*x18 + x4*x6
    x20 = -Z4
    x21 = Z3 + x20
    x22 = x0*x21
    x23 = x14*x4
    x24 = x22 - x23
    x25 = -x18*x2 + x4*x8
    x26 = x2*x21
    x27 = x11*x4
    x28 = x26 - x27
    x29 = x10*x16 + x19*x24 + x25*x28
    x30 = 1/x5
    x31 = x10*x24
    x32 = x16*x19
    x33 = x10*x28
    x34 = -x16*x25
    x35 = x0*(x31 - x32) + x2*(x33 + x34) + x4*(x19*x28 - x24*x25)
    x36 = x35**2
    x37 = 1/(x29**2 + x30*x36)
    x38 = X2 + x13
    x39 = Y1 + x1
    x40 = x2*x30
    x41 = Z1 + x3
    x42 = -x10*x11 + x16*x39 - x19*x21 + x24*x41
    x43 = x35*x42
    x44 = x18*x24
    x45 = Z2 + x20
    x46 = x19*x38 + x24*x6
    x47 = x0*x46 + x2*(x10*x45 + x16*x18 + x25*x38 + x28*x6) + x33 + x34
    x48 = -x10*x38 + x16*x6 - x18*x28 + x25*x45
    x49 = x28*x39
    x50 = x11*x25
    x51 = -x0*(x10*x21 - x11*x19 + x16*x41 - x24*x39) + x2*(x49 + x50) - x31 + x32 + x4*(x21*x25 + x28*x41)
    x52 = x0*x30*x35 + x51
    x53 = x2/x5**2
    x54 = x30*(x4*(-x19*(Z4 + x17) + x44) + x47)
    x55 = 2*x37*(x29*x48 + x35*x54 - x36*x53)
    return x37*(x29*x52*x55 + x29*(3*x0*x35*x53 - x0*x54 + x0*(x19 + x21*x6 - x22 + x23 - x38*x41) + x2*(x11*x18 + x25 - x26 + x27 - x39*x45) + x4*(x18*x21 - x41*x45) + x40*x51 + x46 - x49 - x50) - x35*(x11*x6 - x12 + x15 + x38*x39 - x7 + x9) - x40*x43 + x42*(x4*(x19*x45 + x44) + x47) - x43*x55 - x48*x52)/sqrt(x5)

def phi_dX2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = -Y3
    x2 = Y2 + x1
    x3 = -Z3
    x4 = Z2 + x3
    x5 = x0**2 + x2**2 + x4**2
    x6 = X1 - X2
    x7 = x2*x6
    x8 = Y1 - Y2
    x9 = x0*x8
    x10 = x7 - x9
    x11 = -Y4
    x12 = Y3 + x11
    x13 = -X4
    x14 = X3 + x13
    x15 = x0*x12 - x14*x2
    x16 = x4*x6
    x17 = Z1 - Z2
    x18 = x0*x17
    x19 = x16 - x18
    x20 = Z3 - Z4
    x21 = x0*x20
    x22 = x14*x4
    x23 = x21 - x22
    x24 = -x17*x2 + x4*x8
    x25 = x2*x20
    x26 = x12*x4
    x27 = x25 - x26
    x28 = x10*x15 + x19*x23 + x24*x27
    x29 = 1/x5
    x30 = x10*x23
    x31 = x15*x19
    x32 = x19*x27
    x33 = x23*x24
    x34 = x32 - x33
    x35 = x0*(x30 - x31) + x2*(x10*x27 - x15*x24) + x34*x4
    x36 = x35**2
    x37 = 1/(x28**2 + x29*x36)
    x38 = X2 + x13
    x39 = Z1 + x3
    x40 = x29*x4
    x41 = Y1 + x1
    x42 = -x10*x12 + x15*x41 - x19*x20 + x23*x39
    x43 = x35*x42
    x44 = x15*x6
    x45 = x10*x38
    x46 = Y2 + x11
    x47 = x10*x46
    x48 = x27*x6
    x49 = x24*x38
    x50 = x23*x8
    x51 = x19*x46
    x52 = -x19*x38 + x23*x6 - x24*x46 + x27*x8
    x53 = x27*x39
    x54 = x20*x24
    x55 = -x0*(x10*x20 - x12*x19 + x15*x39 - x23*x41) + x2*(x12*x24 + x27*x41) - x30 + x31 + x4*(x53 + x54)
    x56 = x0*x29*x35 + x55
    x57 = -x45
    x58 = x4/x5**2
    x59 = x29*(x0*(x15*(-X1 + X2) + x57) + x2*(x15*(-Y1 + Y2) - x47) + x34 - x4*(-x48 - x49 + x50 + x51))
    x60 = 2*x37*(x28*x52 + x35*x59 - x36*x58)
    return x37*(x28*x56*x60 + x28*(3*x0*x35*x58 - x0*x59 + x0*(-x12*x6 + x15 + x38*x41 - x7 + x9) + x2*(-x12*x8 + x41*x46) + x4*(-x20*x8 + x24 - x25 + x26 + x39*x46) + x40*x55 - x44 - x53 - x54 + x57) - x35*(-x16 + x18 + x20*x6 - x21 + x22 + x38*x39) - x40*x43 - x42*(x0*(x44 + x45) + x2*(x15*x8 + x47) - x32 + x33 - x4*(x48 + x49 - x50 - x51)) - x43*x60 - x52*x56)/sqrt(x5)

def phi_dX2_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = -Y3
    x2 = Y2 + x1
    x3 = x2**2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x0**2 + x3 + x6
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x0*x9 + x2*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x0*x11 - x12*x2
    x14 = Z1 - Z2
    x15 = -x0*x14 + x5*x8
    x16 = Z3 - Z4
    x17 = x0*x16 - x12*x5
    x18 = -x14*x2 + x5*x9
    x19 = -x11*x5 + x16*x2
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x7
    x22 = x10*x17
    x23 = x13*x15
    x24 = x0*(x22 - x23) + x2*(x10*x19 - x13*x18) + x5*(x15*x19 - x17*x18)
    x25 = 1/(x20**2 + x21*x24**2)
    x26 = Y1 + x1
    x27 = Z1 + x4
    x28 = -x10*x11 + x13*x26 - x15*x16 + x17*x27
    x29 = x15*x2
    x30 = x10*x5
    x31 = x0*(x29 - x30) + x18*x3 + x18*x6
    x32 = x0*x21
    x33 = x10*x2 + x15*x5
    x34 = -x0*(x10*x16 - x11*x15 + x13*x27 - x17*x26) + x2*(x11*x18 + x19*x26) - x22 + x23 + x24*x32 + x5*(x16*x18 + x19*x27)
    x35 = 2*x25*(x20*x33 - x21*x24*x31)
    return x25*(-x20*x34*x35 - x20*(-x0*(-x2*x27 + x26*x5) - x29 + x30 + x31*x32) + x24*x28*x35 - x24*(x2*x26 + x27*x5) + x28*x31 + x33*x34)/sqrt(x7)

def phi_dX2_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = -Y3
    x3 = Y2 + x2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x1 + x3**2 + x6
    x8 = -X2
    x9 = X1 + x8
    x10 = x3*x9
    x11 = Y1 - Y2
    x12 = x0*x11
    x13 = x10 - x12
    x14 = Y3 - Y4
    x15 = X3 - X4
    x16 = x0*x14 - x15*x3
    x17 = x5*x9
    x18 = Z1 - Z2
    x19 = x0*x18
    x20 = x17 - x19
    x21 = Z3 - Z4
    x22 = x0*x21 - x15*x5
    x23 = x11*x5 - x18*x3
    x24 = -x14*x5 + x21*x3
    x25 = x13*x16 + x20*x22 + x23*x24
    x26 = 1/x7
    x27 = x13*x22
    x28 = x16*x20
    x29 = x0*(x27 - x28) + x3*(x13*x24 - x16*x23) + x5*(x20*x24 - x22*x23)
    x30 = 1/(x25**2 + x26*x29**2)
    x31 = Y1 + x2
    x32 = Z1 + x4
    x33 = -x13*x14 + x16*x31 - x20*x21 + x22*x32
    x34 = x1*x20 + x20*x6
    x35 = x13*x5
    x36 = x3*(x0*x23 + x35) + x34
    x37 = X3 + x8
    x38 = x0*x26
    x39 = x0*x13 - x23*x5
    x40 = -x0*(x13*x21 - x14*x20 + x16*x32 - x22*x31) - x27 + x28 + x29*x38 + x3*(x14*x23 + x24*x31) + x5*(x21*x23 + x24*x32)
    x41 = 2*x30*(-x25*x39 + x26*x29*x36)
    return x30*(-x25*x40*x41 + x25*(-x0*x20 + x0*(-x17 + x19 + x37*(-Z1 + Z3)) - x3*(x23 - x31*x5) + x32*x6 + x38*(-x3*(x23*x37 - x35) + x34)) + x29*x33*x41 + x29*(x0*x31 - x10 + x12) - x33*x36 - x39*x40)/sqrt(x7)

def phi_dX2_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = -Y3
    x3 = Y2 + x2
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x1 + x4 + x6**2
    x8 = -X2
    x9 = X1 + x8
    x10 = x3*x9
    x11 = -Y2
    x12 = Y1 + x11
    x13 = x0*x12
    x14 = x10 - x13
    x15 = Y3 - Y4
    x16 = X3 - X4
    x17 = x0*x15 - x16*x3
    x18 = x6*x9
    x19 = Z1 - Z2
    x20 = x0*x19
    x21 = x18 - x20
    x22 = Z3 - Z4
    x23 = x0*x22 - x16*x6
    x24 = x12*x6 - x19*x3
    x25 = -x15*x6 + x22*x3
    x26 = x14*x17 + x21*x23 + x24*x25
    x27 = 1/x7
    x28 = x14*x23
    x29 = x17*x21
    x30 = x0*(x28 - x29) + x3*(x14*x25 - x17*x24) + x6*(x21*x25 - x23*x24)
    x31 = 1/(x26**2 + x27*x30**2)
    x32 = Y1 + x2
    x33 = Z1 + x5
    x34 = -x14*x15 + x17*x32 - x21*x22 + x23*x33
    x35 = x1*x14 + x14*x4
    x36 = x0*x24
    x37 = x21*x3
    x38 = x0*x27
    x39 = x0*x21 + x24*x3
    x40 = -x0*(x14*x22 - x15*x21 + x17*x33 - x23*x32) - x28 + x29 + x3*(x15*x24 + x25*x32) + x30*x38 + x6*(x22*x24 + x25*x33)
    x41 = 2*x31*(x26*x39 + x27*x30*(x35 + x6*(-x21*(Y3 + x11) + x24*(X3 + x8))))
    return x31*(x26*x40*x41 - x26*(-x0*x14 + x0*(x0*x32 - x10 + x13) + x32*x4 + x38*(x35 + x6*(-x36 + x37)) + x6*(x24 + x3*x33)) - x30*x34*x41 + x30*(x0*x33 - x18 + x20) + x34*(x35 - x6*(x36 - x37)) - x39*x40)/sqrt(x7)

def phi_dY2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x6**2
    x8 = x2 + x4 + x7
    x9 = X1 - X2
    x10 = Y1 - Y2
    x11 = -x1*x10 + x3*x9
    x12 = Y3 - Y4
    x13 = x1*x12
    x14 = X3 - X4
    x15 = x14*x3
    x16 = x13 - x15
    x17 = Z1 - Z2
    x18 = -x1*x17 + x6*x9
    x19 = Z3 - Z4
    x20 = x1*x19 - x14*x6
    x21 = x10*x6 - x17*x3
    x22 = x19*x3
    x23 = -x12*x6
    x24 = x22 + x23
    x25 = x11*x16 + x18*x20 + x21*x24
    x26 = 1/x8
    x27 = x11*x24
    x28 = x16*x21
    x29 = x1*(x11*x20 - x16*x18) + x3*(x27 - x28) + x6*(x18*x24 - x20*x21)
    x30 = 1/(x25**2 + x26*x29**2)
    x31 = X1 + x0
    x32 = Z1 + x5
    x33 = -x11*x14 + x16*x31 + x19*x21 - x24*x32
    x34 = x1*(-x16*x6 + x20*x3) + x24*x4 + x24*x7
    x35 = x26*x3
    x36 = x16*x3 + x20*x6
    x37 = -x1*(x14*x18 + x20*x31) - x27 + x28 + x29*x35 - x3*(x11*x19 + x14*x21 + x16*x32 + x24*x31) - x6*(x18*x19 + x20*x32)
    x38 = 2*x30*(x25*x36 + x26*x29*x34)
    return x30*(-x25*x37*x38 + x25*(-x19*x2 - x19*x7 - x24*x3 - x3*(2*x22 + x23) + x34*x35) - x29*x33*x38 + x29*(x13 - 2*x15) + x33*x34 + x36*x37)/sqrt(x8)

def phi_dY2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x2 + x3**2 + x6
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x1*x9 + x3*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x1*x11 - x12*x3
    x14 = Z1 - Z2
    x15 = -x1*x14 + x5*x8
    x16 = Z3 - Z4
    x17 = x1*x16
    x18 = x12*x5
    x19 = x17 - x18
    x20 = -x14*x3 + x5*x9
    x21 = -x11*x5 + x16*x3
    x22 = x10*x13 + x15*x19 + x20*x21
    x23 = 1/x7
    x24 = x10*x21
    x25 = x13*x20
    x26 = x1*(x10*x19 - x13*x15) + x3*(x24 - x25) + x5*(x15*x21 - x19*x20)
    x27 = 1/(x22**2 + x23*x26**2)
    x28 = X1 + x0
    x29 = Z1 + x4
    x30 = -x10*x12 + x13*x28 + x16*x20 - x21*x29
    x31 = x1*x21
    x32 = x13*x5
    x33 = x19*x2 + x19*x6 + x3*(x31 + x32)
    x34 = x23*x3
    x35 = x1*x13 - x21*x5
    x36 = -x1*(x12*x15 + x19*x28) - x24 + x25 + x26*x34 - x3*(x10*x16 + x12*x20 + x13*x29 + x21*x28) + x5*(-x15*x16 + x19*(-Z1 + Z3))
    x37 = 2*x27*(x22*x35 + x23*x26*x33)
    return x27*(x22*x36*x37 - x22*(x3*(-x17 + x18) - x31 - x32 + x33*x34) + x26*x30*x37 + x26*(x1*x12 + x16*x5) - x30*x33 - x35*x36)/sqrt(x7)

def phi_dY2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x6**2
    x8 = x2 + x4 + x7
    x9 = -X2
    x10 = X1 + x9
    x11 = -Y2
    x12 = Y1 + x11
    x13 = -x1*x12 + x10*x3
    x14 = Y3 - Y4
    x15 = x1*x14
    x16 = X3 - X4
    x17 = x16*x3
    x18 = x15 - x17
    x19 = Z1 - Z2
    x20 = -x1*x19 + x10*x6
    x21 = Z3 - Z4
    x22 = x1*x21 - x16*x6
    x23 = x12*x6 - x19*x3
    x24 = x21*x3
    x25 = -x14*x6
    x26 = x24 + x25
    x27 = x13*x18 + x20*x22 + x23*x26
    x28 = 1/x8
    x29 = x13*x26
    x30 = x18*x23
    x31 = x1*(x13*x22 - x18*x20) + x3*(x29 - x30) + x6*(x20*x26 - x22*x23)
    x32 = 1/(x27**2 + x28*x31**2)
    x33 = X1 + x0
    x34 = Z1 + x5
    x35 = -x13*x16 + x18*x33 + x21*x23 - x26*x34
    x36 = x18*x2 + x18*x4 + x6*(-x1*x26 + x22*x3)
    x37 = x18*x3
    x38 = Y3 + x11
    x39 = x28*x3
    x40 = x1*x22 + x26*x3
    x41 = -x1*(x16*x20 + x22*x33) - x29 - x3*(x13*x21 + x16*x23 + x18*x34 + x26*x33) + x30 + x31*x39 + x6*(-x20*x21 + x22*(-Z1 + Z3))
    x42 = X3 + x9
    x43 = 2*x32*(x27*x40 + x28*x31*(x1*x18*x42 + x37*x38 - x6*(-x22*x38 + x26*x42)))
    return x32*(x27*x41*x43 + x27*(x16*x2 + x16*x7 + x3*(-x15 + x17 + x38*(X4 + x0)) + x36*x39 - x37) + x31*x35*x43 - x31*(2*x24 + x25) + x35*x36 - x40*x41)/sqrt(x8)

def phi_dY2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1**2 + x3**2 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x3*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x1*x10 - x11*x3
    x13 = Z1 - Z2
    x14 = -x1*x13 + x5*x7
    x15 = Z3 - Z4
    x16 = x1*x15 - x11*x5
    x17 = -x13*x3 + x5*x8
    x18 = -x10*x5 + x15*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x16*x9
    x22 = x12*x14
    x23 = x21 - x22
    x24 = x18*x9
    x25 = x12*x17
    x26 = x24 - x25
    x27 = x1*x23 + x26*x3 + x5*(x14*x18 - x16*x17)
    x28 = x27**2
    x29 = 1/(x19**2 + x20*x28)
    x30 = X1 + x0
    x31 = Y1 + x2
    x32 = x1*x20
    x33 = x15*x17
    x34 = Z1 + x4
    x35 = x18*x34
    x36 = -x11*x9 + x12*x30 + x33 - x35
    x37 = x27*x36
    x38 = x16*x31
    x39 = x10*x14
    x40 = x12*x34
    x41 = x15*x9
    x42 = x10*x17 + x18*x31
    x43 = x3*x42
    x44 = x5*(x33 + x35)
    x45 = -x21 + x22 + x43 + x44
    x46 = -x14*x15
    x47 = -x10*x9 + x12*x31 + x16*x34 + x46
    x48 = x16*x30
    x49 = x11*x14
    x50 = x1*(x48 + x49)
    x51 = x5*(x16*(-Z1 + Z3) + x46)
    x52 = x40 + x41
    x53 = x3*(x11*x17 + x18*x30 + x52)
    x54 = x20*x27*x3 - x24 + x25 - x50 + x51 - x53
    x55 = x1/x6**2
    x56 = x1*(-x38 - x39 + x52)
    x57 = 2*x29*(x19*x47 + x20*x27*(x45 - x56) + x28*x55)
    return x29*(x19*x54*x57 + x19*(-x1*(-x11*x34 + x15*x30) + x20*x3*(x23 - x43 - x44 + x56) - 3*x27*x3*x55 - x3*(x10*x34 - x15*x31) + x32*(x26 + x50 - x51 + x53) + x42 - x48 - x49) + x27*(x10*x30 + x11*x31) - x32*x37 - x36*(x1*(x38 + x39 - x40 - x41) + x45) + x37*x57 - x47*x54)/sqrt(x6)

def phi_dY2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1**2 + x3 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x1*x10 - x11*x2
    x13 = Z1 - Z2
    x14 = -x1*x13 + x5*x7
    x15 = Z3 - Z4
    x16 = x1*x15 - x11*x5
    x17 = -x13*x2 + x5*x8
    x18 = -x10*x5 + x15*x2
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = -x12*x14 + x16*x9
    x22 = x18*x9
    x23 = x12*x17
    x24 = x22 - x23
    x25 = x14*x18 - x16*x17
    x26 = x1*x21 + x2*x24 + x25*x5
    x27 = x26**2
    x28 = 1/(x19**2 + x20*x27)
    x29 = X1 + x0
    x30 = Z1 + x4
    x31 = 2*x1*x21 + 2*x2*x24 + 2*x25*x5
    x32 = -x11*x9 + x12*x29 + x15*x17 - x18*x30
    x33 = x20*x26
    x34 = x2*x33
    x35 = x1*(x11*x14 + x16*x29)
    x36 = x14*x15
    x37 = x18*x29
    x38 = x11*x17
    x39 = x12*x30
    x40 = x15*x9
    x41 = x2*(x37 + x38 + x39 + x40)
    x42 = x24 + x35 + x41 + x5*(x16*x30 + x36)
    x43 = -x22 + x23 + x34 - x35 - x41 + x5*(x16*(-Z1 + Z3) - x36)
    x44 = 2*Y2 - 2*Y3
    x45 = x6**(-2)
    x46 = x28*(x19*x32 - x2*x27*x45 + x33*x42)
    return x28*(-2*x19*x43*x46 - x19*(-x20*x42*x44 + 3*x26*x3*x45 - x33 + 2*x37 + 2*x38 + 2*x39 + 2*x40 + x44*(-x11*x30 + x15*x29)) - x31*x32*x46 - x31*(x11*x29 + x15*x30) - x32*x34 + x32*x42 + x32*x43)/sqrt(x6)

def phi_dY2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1**2 + x3**2 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x3*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x1*x10 - x11*x3
    x13 = Z1 - Z2
    x14 = -x1*x13 + x5*x7
    x15 = Z3 - Z4
    x16 = x1*x15 - x11*x5
    x17 = -x13*x3 + x5*x8
    x18 = -x10*x5 + x15*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x18*x9
    x22 = x12*x17
    x23 = x21 - x22
    x24 = x14*x18
    x25 = x16*x17
    x26 = x1*(-x12*x14 + x16*x9) + x23*x3 + x5*(x24 - x25)
    x27 = x26**2
    x28 = 1/(x19**2 + x20*x27)
    x29 = Y1 + x2
    x30 = Z1 + x4
    x31 = x20*x5
    x32 = X1 + x0
    x33 = x12*x32
    x34 = x11*x9
    x35 = x15*x17 - x18*x30 + x33 - x34
    x36 = x26*x35
    x37 = x12*x29
    x38 = x10*x9
    x39 = x11*x17 + x18*x32
    x40 = -x24 + x25 - x5*(-x10*x14 - x16*x29 + x39)
    x41 = x16*x32
    x42 = x11*x14
    x43 = -x10*x17 + x18*x29 + x41 - x42
    x44 = x1*(x41 + x42)
    x45 = x14*x15
    x46 = x3*(x12*x30 + x15*x9 + x39)
    x47 = x20*x26*x3 - x21 + x22 - x44 - x46 + x5*(x16*(-Z1 + Z3) - x45)
    x48 = x16*x30 + x45
    x49 = x5/x6**2
    x50 = x20*(x1*(x33 - x9*(X4 + x0)) + x3*(x37 - x9*(Y4 + x2)) + x40)
    x51 = 2*x28*(x19*x43 - x26*x50 - x27*x49)
    return x28*(-x19*x47*x51 - x19*(3*x26*x3*x49 + x3*x50 - x3*(x10*x32 - x11*x29) - x31*(x23 + x44 + x46 + x48*x5) - x37 - x38 + x48 + x5*(-x11*x30 + x15*x32)) + x26*(x10*x30 + x15*x29) - x31*x36 - x35*(x1*(x33 + x34) + x3*(x37 + x38) + x40) - x36*x51 + x43*x47)/sqrt(x6)

def phi_dY2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = Y2 - Y3
    x3 = -Z3
    x4 = Z2 + x3
    x5 = x1**2 + x2**2 + x4**2
    x6 = X1 - X2
    x7 = x2*x6
    x8 = Y1 - Y2
    x9 = -x1*x8
    x10 = x7 + x9
    x11 = -Y4
    x12 = Y3 + x11
    x13 = X3 - X4
    x14 = x1*x12 - x13*x2
    x15 = Z1 - Z2
    x16 = -x1*x15 + x4*x6
    x17 = -Z4
    x18 = Z3 + x17
    x19 = x1*x18
    x20 = x13*x4
    x21 = x19 - x20
    x22 = -x15*x2 + x4*x8
    x23 = x18*x2
    x24 = x12*x4
    x25 = x23 - x24
    x26 = x10*x14 + x16*x21 + x22*x25
    x27 = 1/x5
    x28 = x10*x21
    x29 = x14*x16
    x30 = x10*x25
    x31 = x14*x22
    x32 = x30 - x31
    x33 = x1*(x28 - x29) + x2*x32 + x4*(x16*x25 - x21*x22)
    x34 = x33**2
    x35 = 1/(x26**2 + x27*x34)
    x36 = X1 + x0
    x37 = Y2 + x11
    x38 = x1*x27
    x39 = Z1 + x3
    x40 = -x10*x13 + x14*x36 + x18*x22 - x25*x39
    x41 = x33*x40
    x42 = x22*x37 + x25*x8
    x43 = Z2 + x17
    x44 = x1*(-x10*x43 - x14*x15 + x16*x37 + x21*x8) + x2*x42 - x28 + x29 + x4*(x15*x25 + x22*x43)
    x45 = -x10*x37 + x14*x8 + x15*x21 - x16*x43
    x46 = x21*x36
    x47 = x13*x16
    x48 = x1*(x46 + x47)
    x49 = x4*(x16*x18 + x21*x39)
    x50 = x2*(x10*x18 + x13*x22 + x14*x39 + x25*x36)
    x51 = x2*x27*x33 - x30 + x31 - x48 - x49 - x50
    x52 = x1/x5**2
    x53 = x27*x44
    x54 = 2*x35*(x26*x45 + x33*x53 + x34*x52)
    return x35*(-x26*x51*x54 - x26*(x1*(x13*x15 + x16 - x19 + x20 - x36*x43) - 3*x2*x33*x52 - x2*x53 + x2*(x18*x8 + x22 - x23 + x24 - x37*x39) + x38*(x32 + x48 + x49 + x50) + x4*(x15*x18 - x39*x43) + x42 - x46 - x47) - x33*(x13*x8 + x14 + x36*x37 + x7 + x9) + x38*x41 + x40*x44 - x41*x54 + x45*x51)/sqrt(x5)

def phi_dY2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1**2 + x3 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = -X4
    x12 = X3 + x11
    x13 = x1*x10 - x12*x2
    x14 = -Z2
    x15 = Z1 + x14
    x16 = -x1*x15 + x5*x7
    x17 = -Z4
    x18 = Z3 + x17
    x19 = x1*x18 - x12*x5
    x20 = -x15*x2 + x5*x8
    x21 = -x10*x5 + x18*x2
    x22 = x13*x9 + x16*x19 + x20*x21
    x23 = 1/x6
    x24 = x21*x9
    x25 = x13*x20
    x26 = -x25
    x27 = x24 + x26
    x28 = x1*(-x13*x16 + x19*x9) + x2*x27 + x5*(x16*x21 - x19*x20)
    x29 = x28**2
    x30 = 1/(x22**2 + x23*x29)
    x31 = X1 + x0
    x32 = X2 + x11
    x33 = Z1 + x4
    x34 = Z2 + x17
    x35 = -x12*x9 + x13*x31 + x18*x20 - x21*x33
    x36 = x23*x28
    x37 = x2*x36
    x38 = x15*x19
    x39 = x21*x7
    x40 = x20*x32
    x41 = x13*x15
    x42 = x34*x9
    x43 = x1*(x16*x32 + x19*x7) + x2*(x39 + x40 + x41 + x42) + x24 + x26
    x44 = x43 + x5*(x16*x34 + x38)
    x45 = x13*x7 - x15*x21 + x20*x34 - x32*x9
    x46 = x1*(x12*x16 + x19*x31)
    x47 = x5*(x16*x18 + x19*x33)
    x48 = x21*x31
    x49 = x12*x20
    x50 = x13*x33
    x51 = x18*x9
    x52 = x2*(x48 + x49 + x50 + x51)
    x53 = -x24 + x25 + x37 - x46 - x47 - x52
    x54 = x6**(-2)
    x55 = x2*x23
    x56 = 2*x30*(-x2*x29*x54 + x22*x45 + x36*(x43 + x5*(-x16*(Z4 + x14) + x38)))
    return x30*(x22*x53*x56 - x22*(-x2*(-x12*x15 + x18*x7 + x31*x34 - x32*x33) - 3*x28*x3*x54 + x36 - x39 - x40 - x41 - x42 + x44*x55 - x48 - x49 - x50 - x51 + x55*(x27 + x46 + x47 + x52)) + x28*x35*x56 + x28*(x12*x7 + x15*x18 + x31*x32 + x33*x34) + x35*x37 - x35*x44 - x45*x53)/sqrt(x6)

def phi_dY2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = Y2 - Y3
    x3 = -Z3
    x4 = Z2 + x3
    x5 = x1**2 + x2**2 + x4**2
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x1*x7 + x2*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = x1*x10
    x12 = -X4
    x13 = X3 + x12
    x14 = x13*x2
    x15 = x11 - x14
    x16 = Z1 - Z2
    x17 = -x1*x16 + x4*x6
    x18 = Z3 - Z4
    x19 = x1*x18
    x20 = x13*x4
    x21 = x19 - x20
    x22 = x4*x7
    x23 = x16*x2
    x24 = x22 - x23
    x25 = x18*x2
    x26 = x10*x4
    x27 = x25 - x26
    x28 = x15*x8 + x17*x21 + x24*x27
    x29 = 1/x5
    x30 = x27*x8
    x31 = x15*x24
    x32 = x30 - x31
    x33 = x17*x27
    x34 = x21*x24
    x35 = x33 - x34
    x36 = x1*(-x15*x17 + x21*x8) + x2*x32 + x35*x4
    x37 = x36**2
    x38 = 1/(x28**2 + x29*x37)
    x39 = Y2 + x9
    x40 = Z1 + x3
    x41 = x29*x4
    x42 = X1 + x0
    x43 = -x13*x8 + x15*x42 + x18*x24 - x27*x40
    x44 = x36*x43
    x45 = X2 + x12
    x46 = x45*x8
    x47 = x15*x7
    x48 = x39*x8
    x49 = x27*x6
    x50 = x24*x45
    x51 = x21*x7
    x52 = x17*x39
    x53 = -x17*x45 + x21*x6 - x24*x39 + x27*x7
    x54 = x1*(x13*x17 + x21*x42)
    x55 = x17*x18 + x21*x40
    x56 = x4*x55
    x57 = x2*(x13*x24 + x15*x40 + x18*x8 + x27*x42)
    x58 = x2*x29*x36 - x30 + x31 - x54 - x56 - x57
    x59 = -x48
    x60 = x4/x5**2
    x61 = x29*(x1*(x15*(-X1 + X2) - x46) + x2*(x15*(-Y1 + Y2) + x59) + x35 - x4*(-x49 - x50 + x51 + x52))
    x62 = 2*x38*(x28*x53 + x36*x61 - x37*x60)
    return x38*(x28*x58*x62 + x28*(x1*(x13*x6 - x42*x45) + 3*x2*x36*x60 - x2*x61 - x2*(-x11 - x13*x7 + x14 + x39*x42 + x8) - x4*(x17 - x18*x6 - x19 + x20 + x40*x45) - x41*(x32 + x54 + x56 + x57) - x47 + x55 + x59) - x36*(x18*x7 - x22 + x23 - x25 + x26 + x39*x40) + x41*x44 + x43*(x1*(x15*x6 + x46) + x2*(x47 + x48) - x33 + x34 - x4*(x49 + x50 - x51 - x52)) + x44*x62 - x53*x58)/sqrt(x5)

def phi_dY2_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x1**2 + x3 + x6
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x1*x9 + x2*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x1*x11 - x12*x2
    x14 = x5*x8
    x15 = Z1 - Z2
    x16 = x1*x15
    x17 = x14 - x16
    x18 = Z3 - Z4
    x19 = x1*x18 - x12*x5
    x20 = -x15*x2 + x5*x9
    x21 = -x11*x5 + x18*x2
    x22 = x10*x13 + x17*x19 + x20*x21
    x23 = 1/x7
    x24 = x10*x21
    x25 = x13*x20
    x26 = x1*(x10*x19 - x13*x17) + x2*(x24 - x25) + x5*(x17*x21 - x19*x20)
    x27 = 1/(x22**2 + x23*x26**2)
    x28 = X1 + x0
    x29 = Z1 + x4
    x30 = -x10*x12 + x13*x28 + x18*x20 - x21*x29
    x31 = x1*(-x10*x5 + x17*x2) + x20*x3 + x20*x6
    x32 = x2*x23
    x33 = x10*x2 + x17*x5
    x34 = -x1*(x12*x17 + x19*x28) - x2*(x10*x18 + x12*x20 + x13*x29 + x21*x28) - x24 + x25 + x26*x32 + x5*(-x17*x18 + x19*(-Z1 + Z3))
    x35 = 2*x27*(x22*x33 - x23*x26*x31)
    return x27*(-x22*x34*x35 - x22*(x1*(-x14 + x16 + x28*x5) - x2*x20 - x2*(-x2*x29 + x20) + x29*x6 + x31*x32) - x26*x30*x35 + x26*(x10 + x2*x28) - x30*x31 + x33*x34)/sqrt(x7)

def phi_dY2_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x2 + x3**2 + x6
    x8 = -X2
    x9 = X1 + x8
    x10 = Y1 - Y2
    x11 = -x1*x10 + x3*x9
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x1*x12 - x13*x3
    x15 = Z1 - Z2
    x16 = -x1*x15 + x5*x9
    x17 = Z3 - Z4
    x18 = x1*x17 - x13*x5
    x19 = x10*x5 - x15*x3
    x20 = -x12*x5 + x17*x3
    x21 = x11*x14 + x16*x18 + x19*x20
    x22 = 1/x7
    x23 = x11*x20
    x24 = x14*x19
    x25 = x1*(x11*x18 - x14*x16) + x3*(x23 - x24) + x5*(x16*x20 - x18*x19)
    x26 = 1/(x21**2 + x22*x25**2)
    x27 = X1 + x0
    x28 = Z1 + x4
    x29 = -x11*x13 + x14*x27 + x17*x19 - x20*x28
    x30 = x16*x2 + x16*x6
    x31 = x1*x19
    x32 = x11*x5
    x33 = x3*(x31 + x32) + x30
    x34 = -x32
    x35 = x22*x3
    x36 = x1*x11 - x19*x5
    x37 = -x1*(x13*x16 + x18*x27) - x23 + x24 + x25*x35 - x3*(x11*x17 + x13*x19 + x14*x28 + x20*x27) + x5*(-x16*x17 + x18*(-Z1 + Z3))
    x38 = 2*x26*(-x21*x36 + x22*x25*x33)
    return x26*(-x21*x37*x38 + x21*(-x3*(-x1*x28 + x27*x5) - x31 + x34 + x35*(-x3*(x19*(X3 + x8) + x34) + x30)) - x25*x29*x38 - x25*(x1*x27 + x28*x5) + x29*x33 - x36*x37)/sqrt(x7)

def phi_dY2_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x2 + x4 + x6**2
    x8 = -X2
    x9 = X1 + x8
    x10 = x3*x9
    x11 = -Y2
    x12 = Y1 + x11
    x13 = x1*x12
    x14 = x10 - x13
    x15 = Y3 - Y4
    x16 = X3 - X4
    x17 = x1*x15 - x16*x3
    x18 = Z1 - Z2
    x19 = -x1*x18 + x6*x9
    x20 = Z3 - Z4
    x21 = x1*x20 - x16*x6
    x22 = x12*x6
    x23 = x18*x3
    x24 = x22 - x23
    x25 = -x15*x6 + x20*x3
    x26 = x14*x17 + x19*x21 + x24*x25
    x27 = 1/x7
    x28 = x14*x25
    x29 = x17*x24
    x30 = x1*(x14*x21 - x17*x19) + x3*(x28 - x29) + x6*(x19*x25 - x21*x24)
    x31 = 1/(x26**2 + x27*x30**2)
    x32 = X1 + x0
    x33 = Z1 + x5
    x34 = -x14*x16 + x17*x32 + x20*x24 - x25*x33
    x35 = x14*x2 + x14*x4
    x36 = X3 + x8
    x37 = -Z1 + Z3
    x38 = x27*x3
    x39 = x35 + x6*(-x19*(Y3 + x11) + x24*x36)
    x40 = x1*x19 + x24*x3
    x41 = -x1*(x16*x19 + x21*x32) - x28 + x29 - x3*(x14*x20 + x16*x24 + x17*x33 + x25*x32) + x30*x38 + x6*(-x19*x20 + x21*x37)
    x42 = 2*x31*(x26*x40 + x27*x30*x39)
    return x31*(x26*x41*x42 - x26*(-x14*x3 - x2*x32 + x3*(-x10 + x13 - x3*x32) + x38*x39 - x6*(x19 + x36*x37)) + x30*x34*x42 + x30*(-x22 + x23 + x3*x33) - x34*(x35 + x6*(-x1*x24 + x19*x3)) - x40*x41)/sqrt(x7)

def phi_dZ2_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = -Y3
    x4 = Y2 + x3
    x5 = x4**2
    x6 = Z2 - Z3
    x7 = x6**2
    x8 = x2 + x5 + x7
    x9 = X1 - X2
    x10 = Y1 - Y2
    x11 = -x1*x10 + x4*x9
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x1*x12 - x13*x4
    x15 = Z1 - Z2
    x16 = -x1*x15 + x6*x9
    x17 = Z3 - Z4
    x18 = x1*x17
    x19 = x13*x6
    x20 = x18 - x19
    x21 = x10*x6 - x15*x4
    x22 = x17*x4
    x23 = x12*x6
    x24 = x22 - x23
    x25 = x11*x14 + x16*x20 + x21*x24
    x26 = 1/x8
    x27 = x16*x24
    x28 = x20*x21
    x29 = x1*(x11*x20 - x14*x16) + x4*(x11*x24 - x14*x21) + x6*(x27 - x28)
    x30 = 1/(x25**2 + x26*x29**2)
    x31 = X1 + x0
    x32 = Y1 + x3
    x33 = -x12*x21 - x13*x16 + x20*x31 + x24*x32
    x34 = x1*(-x14*x6 + x20*x4) + x24*x5 + x24*x7
    x35 = x26*x6
    x36 = x14*x4 + x20*x6
    x37 = x1*(-x11*(X4 + x0) + x14*x31) - x27 + x28 + x29*x35 + x4*(-x11*(Y4 + x3) + x14*x32) - x6*(-x12*x16 + x13*x21 - x20*x32 + x24*x31)
    x38 = 2*x30*(x25*x36 + x26*x29*x34)
    return x30*(-x25*x37*x38 + x25*(x12*x2 + x12*x5 - x24*x6 + x34*x35 - x6*(x22 - 2*x23)) - x29*x33*x38 + x29*(x18 - 2*x19) + x33*x34 + x36*x37)/sqrt(x8)

def phi_dZ2_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = -Y3
    x4 = Y2 + x3
    x5 = x4**2
    x6 = Z2 - Z3
    x7 = x6**2
    x8 = x2 + x5 + x7
    x9 = X1 - X2
    x10 = Y1 - Y2
    x11 = -x1*x10 + x4*x9
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x1*x12 - x13*x4
    x15 = Z1 - Z2
    x16 = -x1*x15 + x6*x9
    x17 = Z3 - Z4
    x18 = x1*x17
    x19 = x13*x6
    x20 = x18 - x19
    x21 = x10*x6 - x15*x4
    x22 = x17*x4
    x23 = x12*x6
    x24 = x22 - x23
    x25 = x11*x14 + x16*x20 + x21*x24
    x26 = 1/x8
    x27 = x16*x24
    x28 = x20*x21
    x29 = x1*(x11*x20 - x14*x16) + x4*(x11*x24 - x14*x21) + x6*(x27 - x28)
    x30 = 1/(x25**2 + x26*x29**2)
    x31 = X1 + x0
    x32 = Y1 + x3
    x33 = -x12*x21 - x13*x16 + x20*x31 + x24*x32
    x34 = x2*x20 + x20*x7 + x4*(x1*x24 + x14*x6)
    x35 = x26*x6
    x36 = x1*x14 - x24*x6
    x37 = x1*(-x11*(X4 + x0) + x14*x31) - x27 + x28 + x29*x35 + x4*(-x11*(Y4 + x3) + x14*x32) - x6*(-x12*x16 + x13*x21 - x20*x32 + x24*x31)
    x38 = 2*x30*(x25*x36 + x26*x29*x34)
    return x30*(x25*x37*x38 - x25*(x13*x2 + x13*x5 - x20*x6 + x34*x35 - x6*(x18 - 2*x19)) + x29*x33*x38 + x29*(x22 - 2*x23) - x33*x34 - x36*x37)/sqrt(x8)

def phi_dZ2_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = -Y3
    x4 = Y2 + x3
    x5 = x4**2
    x6 = Z2 - Z3
    x7 = x2 + x5 + x6**2
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x1*x9 + x4*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x1*x11 - x12*x4
    x14 = Z1 - Z2
    x15 = -x1*x14 + x6*x8
    x16 = Z3 - Z4
    x17 = x1*x16 - x12*x6
    x18 = -x14*x4 + x6*x9
    x19 = -x11*x6 + x16*x4
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x7
    x22 = x15*x19
    x23 = x17*x18
    x24 = x1*(x10*x17 - x13*x15) + x4*(x10*x19 - x13*x18) + x6*(x22 - x23)
    x25 = 1/(x20**2 + x21*x24**2)
    x26 = X1 + x0
    x27 = Y1 + x3
    x28 = -x11*x18 - x12*x15 + x17*x26 + x19*x27
    x29 = x13*x2 + x13*x5
    x30 = x1*x19
    x31 = x17*x4
    x32 = -x30 + x31
    x33 = x21*x6
    x34 = x29 + x32*x6
    x35 = x1*x17 + x19*x4
    x36 = x1*(-x10*(X4 + x0) + x13*x26) - x22 + x23 + x24*x33 + x4*(-x10*(Y4 + x3) + x13*x27) - x6*(-x11*x15 + x12*x18 - x17*x27 + x19*x26)
    x37 = 2*x25*(x20*x35 - x21*x24*x34)
    return x25*(x20*x36*x37 - x20*(x13*x6 + x32 - x33*x34) + x24*x28*x37 + x24*(x1*x12 + x11*x4) + x28*(x29 - x6*(x30 - x31)) - x35*x36)/sqrt(x7)

def phi_dZ2_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1**2 + x3**2 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x3*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x1*x10 - x11*x3
    x13 = Z1 - Z2
    x14 = -x1*x13 + x5*x7
    x15 = Z3 - Z4
    x16 = x1*x15 - x11*x5
    x17 = -x13*x3 + x5*x8
    x18 = -x10*x5 + x15*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x16*x9
    x22 = x12*x14
    x23 = x21 - x22
    x24 = x14*x18
    x25 = x16*x17
    x26 = x24 - x25
    x27 = x1*x23 + x26*x5 + x3*(-x12*x17 + x18*x9)
    x28 = x27**2
    x29 = 1/(x19**2 + x20*x28)
    x30 = X1 + x0
    x31 = Z1 + x4
    x32 = x1*x20
    x33 = Y1 + x2
    x34 = x18*x33
    x35 = x10*x17
    x36 = -x11*x14 + x16*x30 + x34 - x35
    x37 = x27*x36
    x38 = x16*x33
    x39 = x10*x14
    x40 = x12*x31
    x41 = x15*x9
    x42 = x3*(x34 + x35)
    x43 = x15*x17 + x18*x31
    x44 = x43*x5
    x45 = -x21 + x22 + x42 + x44
    x46 = x12*x33
    x47 = -x10*x9 - x14*x15 + x16*x31 + x46
    x48 = x12*x30
    x49 = X4 + x0
    x50 = x1*(x48 - x49*x9)
    x51 = Y4 + x2
    x52 = x3*(x46 - x51*x9)
    x53 = -x38 - x39
    x54 = x5*(x11*x17 + x18*x30 + x53)
    x55 = x20*x27*x5 - x24 + x25 + x50 + x52 - x54
    x56 = x1/x6**2
    x57 = x1*(x40 + x41 + x53)
    x58 = 2*x29*(x19*x47 + x20*x27*(x45 - x57) + x28*x56)
    return x29*(x19*x55*x58 + x19*(x1*(x10*x30 - x49*(-Y1 + Y3)) + x11*x9 + x20*x5*(x23 - x42 - x44 + x57) - 3*x27*x5*x56 + x32*(x26 - x50 - x52 + x54) + x43 + x48 + x5*(x15*x33 - x51*(-Z1 + Z3))) + x27*(x11*x31 + x15*x30) - x32*x37 - x36*(x1*(x38 + x39 - x40 - x41) + x45) + x37*x58 - x47*x55)/sqrt(x6)

def phi_dZ2_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1**2 + x3**2 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x3*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x1*x10 - x11*x3
    x13 = Z1 - Z2
    x14 = -x1*x13 + x5*x7
    x15 = Z3 - Z4
    x16 = x1*x15 - x11*x5
    x17 = -x13*x3 + x5*x8
    x18 = -x10*x5 + x15*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x18*x9
    x22 = -x12*x17
    x23 = x14*x18
    x24 = x16*x17
    x25 = x23 - x24
    x26 = x1*(-x12*x14 + x16*x9) + x25*x5 + x3*(x21 + x22)
    x27 = x26**2
    x28 = 1/(x19**2 + x20*x27)
    x29 = Y1 + x2
    x30 = Z1 + x4
    x31 = x20*x3
    x32 = X1 + x0
    x33 = x16*x32
    x34 = x11*x14
    x35 = -x10*x17 + x18*x29 + x33 - x34
    x36 = x26*x35
    x37 = x16*x30
    x38 = x14*x15
    x39 = x11*x17 + x18*x32
    x40 = x1*(x33 + x34) + x21 + x22 + x3*(x12*x30 + x15*x9 + x39)
    x41 = x40 + x5*(x37 + x38)
    x42 = x12*x32
    x43 = -x11*x9 + x15*x17 - x18*x30 + x42
    x44 = x1*(x42 - x9*(X4 + x0))
    x45 = x12*x29
    x46 = x3*(x45 - x9*(Y4 + x2))
    x47 = x5*(-x10*x14 - x16*x29 + x39)
    x48 = x20*x26*x5 - x23 + x24 + x44 + x46 - x47
    x49 = -x38
    x50 = x3/x6**2
    x51 = 2*x28*(x19*x43 + x20*x26*x41 - x27*x50)
    return x28*(-x19*x48*x51 + x19*(x10*x9 + x20*x5*(x40 - x5*(x16*(-Z1 + Z3) + x49)) - 3*x26*x5*x50 - x3*(-x10*x32 + x11*x29) + x31*(x25 - x44 - x46 + x47) - x37 + x45 + x49 - x5*(-x11*x30 + x15*x32)) + x26*(x10*x30 + x15*x29) - x31*x36 + x35*x41 - x36*x51 + x43*x48)/sqrt(x6)

def phi_dZ2_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1**2 + x3**2 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x3*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x1*x10 - x11*x3
    x13 = Z1 - Z2
    x14 = -x1*x13 + x4*x7
    x15 = Z3 - Z4
    x16 = x1*x15 - x11*x4
    x17 = -x13*x3 + x4*x8
    x18 = -x10*x4 + x15*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = -x12*x14 + x16*x9
    x22 = -x12*x17 + x18*x9
    x23 = x14*x18
    x24 = x16*x17
    x25 = x23 - x24
    x26 = x1*x21 + x22*x3 + x25*x4
    x27 = x26**2
    x28 = 1/(x19**2 + x20*x27)
    x29 = X1 + x0
    x30 = Y1 + x2
    x31 = 2*x1*x21 + 2*x22*x3 + 2*x25*x4
    x32 = -x10*x17 - x11*x14 + x16*x29 + x18*x30
    x33 = x20*x26
    x34 = x33*x4
    x35 = x12*x29
    x36 = x12*x30
    x37 = x18*x29
    x38 = x11*x17
    x39 = x16*x30
    x40 = x10*x14
    x41 = -x23 + x24 - x4*(x37 + x38 - x39 - x40)
    x42 = x1*(x35 - x9*(X4 + x0)) + x3*(x36 - x9*(Y4 + x2)) + x41
    x43 = x34 + x42
    x44 = 2*Z2 - 2*Z3
    x45 = x6**(-2)
    x46 = x28*(x19*x32 - x27*x4*x45 - x33*x42)
    return x28*(-2*x19*x43*x46 - x19*(x20*x42*x44 + 3*x26*x45*x5 - x33 + 2*x37 + 2*x38 - 2*x39 - 2*x40 - x44*(x10*x29 - x11*x30)) - x31*x32*x46 - x31*(x10*x30 + x11*x29) - x32*x34 + x32*x43 - x32*(x1*(x11*x9 + x35) + x3*(x10*x9 + x36) + x41))/sqrt(x6)

def phi_dZ2_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = Z2 - Z3
    x5 = x1**2 + x3**2 + x4**2
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x1*x7 + x3*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = x1*x10
    x12 = X3 - X4
    x13 = x12*x3
    x14 = x11 - x13
    x15 = x4*x6
    x16 = Z1 - Z2
    x17 = -x1*x16
    x18 = x15 + x17
    x19 = -Z4
    x20 = Z3 + x19
    x21 = x1*x20 - x12*x4
    x22 = -x16*x3 + x4*x7
    x23 = x20*x3
    x24 = x10*x4
    x25 = x23 - x24
    x26 = x14*x8 + x18*x21 + x22*x25
    x27 = 1/x5
    x28 = x21*x8
    x29 = x14*x18
    x30 = x18*x25
    x31 = x21*x22
    x32 = x1*(x28 - x29) + x3*(-x14*x22 + x25*x8) + x4*(x30 - x31)
    x33 = x32**2
    x34 = 1/(x26**2 + x27*x33)
    x35 = X1 + x0
    x36 = Z2 + x19
    x37 = x1*x27
    x38 = Y1 + x2
    x39 = -x10*x22 - x12*x18 + x21*x35 + x25*x38
    x40 = x32*x39
    x41 = Y2 + x9
    x42 = x16*x25
    x43 = x22*x36
    x44 = x1*(-x14*x16 + x18*x41 + x21*x7 - x36*x8) - x28 + x29 + x3*(x22*x41 + x25*x7) + x4*(x42 + x43)
    x45 = x14*x7 + x16*x21 - x18*x36 - x41*x8
    x46 = x14*x35
    x47 = x1*(x46 - x8*(X4 + x0)) + x3*(x14*x38 - x8*(Y4 + x2)) - x30 + x31 - x4*(-x10*x18 + x12*x22 - x21*x38 + x25*x35)
    x48 = x27*x32*x4 + x47
    x49 = x1/x5**2
    x50 = x27*x44
    x51 = 2*x34*(x26*x45 + x32*x50 + x33*x49)
    return x34*(-x26*x48*x51 + x26*(x1*(-x11 + x12*x7 + x13 - x35*x41 + x8) - x12*x8 + x3*(x10*x7 - x38*x41) + 3*x32*x4*x49 + x37*x47 + x4*x50 - x4*(-x10*x16 + x22 - x23 + x24 + x36*x38) - x42 - x43 - x46) - x32*(x12*x16 + x15 + x17 + x21 + x35*x36) + x37*x40 + x39*x44 - x40*x51 + x45*x48)/sqrt(x5)

def phi_dZ2_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = Z2 - Z3
    x5 = x1**2 + x3**2 + x4**2
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x1*x7 + x3*x6
    x9 = Y3 - Y4
    x10 = x1*x9
    x11 = -X4
    x12 = X3 + x11
    x13 = x12*x3
    x14 = x10 - x13
    x15 = -Z2
    x16 = Z1 + x15
    x17 = -x1*x16 + x4*x6
    x18 = -Z4
    x19 = Z3 + x18
    x20 = x1*x19
    x21 = x12*x4
    x22 = x20 - x21
    x23 = x4*x7
    x24 = -x16*x3
    x25 = x23 + x24
    x26 = x19*x3 - x4*x9
    x27 = x14*x8 + x17*x22 + x25*x26
    x28 = 1/x5
    x29 = x26*x8
    x30 = -x14*x25
    x31 = x17*x26
    x32 = x22*x25
    x33 = x1*(-x14*x17 + x22*x8) + x3*(x29 + x30) + x4*(x31 - x32)
    x34 = x33**2
    x35 = 1/(x27**2 + x28*x34)
    x36 = Y1 + x2
    x37 = Z2 + x18
    x38 = x28*x3
    x39 = X1 + x0
    x40 = -x12*x17 + x22*x39 - x25*x9 + x26*x36
    x41 = x33*x40
    x42 = x16*x22
    x43 = x17*x37 + x42
    x44 = X2 + x11
    x45 = x1*(x17*x44 + x22*x6) + x29 + x3*(x14*x16 + x25*x44 + x26*x6 + x37*x8) + x30
    x46 = x14*x6 - x16*x26 + x25*x37 - x44*x8
    x47 = x14*x36
    x48 = x1*(x14*x39 - x8*(X4 + x0)) + x3*(x47 - x8*(Y4 + x2)) - x31 + x32 - x4*(x12*x25 - x17*x9 - x22*x36 + x26*x39)
    x49 = x28*x33*x4 + x48
    x50 = x3/x5**2
    x51 = x28*(x4*(-x17*(Z4 + x15) + x42) + x45)
    x52 = 2*x35*(x27*x46 + x33*x51 - x34*x50)
    return x35*(x27*x49*x52 + x27*(-x1*(x12*x6 - x39*x44) + x3*(-x10 + x13 + x36*x44 - x6*x9 + x8) + 3*x33*x4*x50 + x38*x48 - x4*x51 + x4*(-x12*x16 + x17 - x20 + x21 + x37*x39) + x43 - x47 - x8*x9) - x33*(x16*x9 + x23 + x24 + x26 + x36*x37) + x38*x41 - x40*(x4*x43 + x45) + x41*x52 - x46*x49)/sqrt(x5)

def phi_dZ2_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1**2 + x3**2 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x3*x7
    x10 = -Y4
    x11 = Y3 + x10
    x12 = -X4
    x13 = X3 + x12
    x14 = x1*x11 - x13*x3
    x15 = Z1 - Z2
    x16 = -x1*x15 + x4*x7
    x17 = Z3 - Z4
    x18 = x1*x17 - x13*x4
    x19 = -x15*x3 + x4*x8
    x20 = -x11*x4 + x17*x3
    x21 = x14*x9 + x16*x18 + x19*x20
    x22 = 1/x6
    x23 = x16*x20
    x24 = x18*x19
    x25 = x23 - x24
    x26 = x1*(-x14*x16 + x18*x9) + x25*x4 + x3*(-x14*x19 + x20*x9)
    x27 = x26**2
    x28 = 1/(x21**2 + x22*x27)
    x29 = X1 + x0
    x30 = X2 + x12
    x31 = Y1 + x2
    x32 = Y2 + x10
    x33 = -x11*x19 - x13*x16 + x18*x29 + x20*x31
    x34 = x22*x26
    x35 = x34*x4
    x36 = -x23
    x37 = x30*x9
    x38 = x1*(x14*x7 + x37)
    x39 = x32*x9
    x40 = x3*(x14*x8 + x39)
    x41 = x20*x7
    x42 = x19*x30
    x43 = x18*x8
    x44 = x16*x32
    x45 = x4*(x41 + x42 - x43 - x44)
    x46 = -x16*x30 + x18*x7 - x19*x32 + x20*x8
    x47 = x20*x29
    x48 = x13*x19
    x49 = x18*x31
    x50 = x11*x16
    x51 = x24 + x36 - x4*(x47 + x48 - x49 - x50)
    x52 = x14*x29
    x53 = x14*x31
    x54 = x1*(x52 - x9*(X4 + x0)) + x3*(x53 - x9*(Y4 + x2)) + x35 + x51
    x55 = -x41 - x42 + x43 + x44
    x56 = x6**(-2)
    x57 = x22*x4
    x58 = 2*x28*(x21*x46 - x27*x4*x56 + x34*(x1*(x14*(-X1 + X2) - x37) + x25 + x3*(x14*(-Y1 + Y2) - x39) - x4*x55))
    return x28*(x21*x54*x58 - x21*(-3*x26*x5*x56 + x34 + x4*(x11*x7 - x13*x8 + x29*x32 - x30*x31) - x47 - x48 + x49 + x50 + x55 - x57*(x1*(x13*x9 + x52) + x3*(x11*x9 + x53) + x51) + x57*(x25 - x38 - x40 + x45)) + x26*x33*x58 + x26*(x11*x8 + x13*x7 + x29*x30 + x31*x32) + x33*x35 + x33*(x24 + x36 + x38 + x40 - x45) - x46*x54)/sqrt(x6)

def phi_dZ2_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = x3**2
    x5 = Z2 - Z3
    x6 = x5**2
    x7 = x1**2 + x4 + x6
    x8 = X1 - X2
    x9 = x3*x8
    x10 = Y1 - Y2
    x11 = x1*x10
    x12 = -x11 + x9
    x13 = Y3 - Y4
    x14 = X3 - X4
    x15 = x1*x13 - x14*x3
    x16 = Z1 - Z2
    x17 = -x1*x16 + x5*x8
    x18 = Z3 - Z4
    x19 = x1*x18 - x14*x5
    x20 = x10*x5 - x16*x3
    x21 = -x13*x5 + x18*x3
    x22 = x12*x15 + x17*x19 + x20*x21
    x23 = 1/x7
    x24 = x17*x21
    x25 = x19*x20
    x26 = x1*(x12*x19 - x15*x17) + x3*(x12*x21 - x15*x20) + x5*(x24 - x25)
    x27 = 1/(x22**2 + x23*x26**2)
    x28 = X1 + x0
    x29 = Y1 + x2
    x30 = -x13*x20 - x14*x17 + x19*x28 + x21*x29
    x31 = x1*(-x12*x5 + x17*x3) + x20*x4 + x20*x6
    x32 = x23*x5
    x33 = x12*x3 + x17*x5
    x34 = x1*(-x12*(X4 + x0) + x15*x28) - x24 + x25 + x26*x32 + x3*(-x12*(Y4 + x2) + x15*x29) - x5*(-x13*x17 + x14*x20 - x19*x29 + x21*x28)
    x35 = 2*x27*(x22*x33 - x23*x26*x31)
    return x27*(-x22*x34*x35 - x22*(-x1*(x11 + x28*x3 - x9) - x20*x5 - x29*x4 + x31*x32 - x5*(x20 + x29*x5)) - x26*x30*x35 + x26*(x17 + x28*x5) - x30*x31 + x33*x34)/sqrt(x7)

def phi_dZ2_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = -Y3
    x4 = Y2 + x3
    x5 = Z2 - Z3
    x6 = x5**2
    x7 = x2 + x4**2 + x6
    x8 = -X2
    x9 = X1 + x8
    x10 = x4*x9
    x11 = Y1 - Y2
    x12 = x1*x11
    x13 = x10 - x12
    x14 = Y3 - Y4
    x15 = X3 - X4
    x16 = x1*x14 - x15*x4
    x17 = Z1 - Z2
    x18 = -x1*x17 + x5*x9
    x19 = Z3 - Z4
    x20 = x1*x19 - x15*x5
    x21 = x11*x5 - x17*x4
    x22 = -x14*x5 + x19*x4
    x23 = x13*x16 + x18*x20 + x21*x22
    x24 = 1/x7
    x25 = x18*x22
    x26 = x20*x21
    x27 = x1*(x13*x20 - x16*x18) + x4*(x13*x22 - x16*x21) + x5*(x25 - x26)
    x28 = 1/(x23**2 + x24*x27**2)
    x29 = X1 + x0
    x30 = Y1 + x3
    x31 = -x14*x21 - x15*x18 + x20*x29 + x22*x30
    x32 = x18*x2 + x18*x6
    x33 = x13*x5
    x34 = x32 + x4*(x1*x21 + x33)
    x35 = X3 + x8
    x36 = x24*x5
    x37 = x1*x13 - x21*x5
    x38 = x1*(-x13*(X4 + x0) + x16*x29) - x25 + x26 + x27*x36 + x4*(-x13*(Y4 + x3) + x16*x30) - x5*(-x14*x18 + x15*x21 - x20*x30 + x22*x29)
    x39 = 2*x28*(-x23*x37 + x24*x27*x34)
    return x28*(-x23*x38*x39 + x23*(-x18*x5 - x2*x29 + x36*(x32 - x4*(x21*x35 - x33)) + x4*(-x10 + x12 + x30*x35) - x5*(x18 + x29*x5)) - x27*x31*x39 + x27*(x21 + x30*x5) + x31*x34 - x37*x38)/sqrt(x7)

def phi_dZ2_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = -Y3
    x4 = Y2 + x3
    x5 = x4**2
    x6 = Z2 - Z3
    x7 = x2 + x5 + x6**2
    x8 = -X2
    x9 = X1 + x8
    x10 = -Y2
    x11 = Y1 + x10
    x12 = -x1*x11 + x4*x9
    x13 = Y3 - Y4
    x14 = X3 - X4
    x15 = x1*x13 - x14*x4
    x16 = Z1 - Z2
    x17 = -x1*x16 + x6*x9
    x18 = Z3 - Z4
    x19 = x1*x18 - x14*x6
    x20 = x11*x6 - x16*x4
    x21 = -x13*x6 + x18*x4
    x22 = x12*x15 + x17*x19 + x20*x21
    x23 = 1/x7
    x24 = x17*x21
    x25 = x19*x20
    x26 = x1*(x12*x19 - x15*x17) + x4*(x12*x21 - x15*x20) + x6*(x24 - x25)
    x27 = 1/(x22**2 + x23*x26**2)
    x28 = X1 + x0
    x29 = Y1 + x3
    x30 = -x13*x20 - x14*x17 + x19*x28 + x21*x29
    x31 = x12*x2 + x12*x5
    x32 = x17*x4
    x33 = x1*x20
    x34 = x23*x6
    x35 = x31 + x6*(-x17*(Y3 + x10) + x20*(X3 + x8))
    x36 = x1*x17 + x20*x4
    x37 = x1*(-x12*(X4 + x0) + x15*x28) - x24 + x25 + x26*x34 + x4*(-x12*(Y4 + x3) + x15*x29) - x6*(-x13*x17 + x14*x20 - x19*x29 + x21*x28)
    x38 = 2*x27*(x22*x36 + x23*x26*x35)
    return x27*(x22*x37*x38 - x22*(-x32 + x33 + x34*x35 - x6*(-x1*x29 + x28*x4)) + x26*x30*x38 - x26*(x1*x28 + x29*x4) - x30*(x31 + x6*(x32 - x33)) - x36*x37)/sqrt(x7)

def phi_dX3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = -Y2
    x8 = Y1 + x7
    x9 = -x0*x8 + x1*x6
    x10 = -Y4
    x11 = Y3 + x10
    x12 = X3 - X4
    x13 = x0*x11 - x1*x12
    x14 = -Z2
    x15 = Z1 + x14
    x16 = -x0*x15 + x3*x6
    x17 = -Z4
    x18 = Z3 + x17
    x19 = x0*x18 - x12*x3
    x20 = -x1*x15 + x3*x8
    x21 = x1*x18 - x11*x3
    x22 = x13*x9 + x16*x19 + x20*x21
    x23 = 1/x5
    x24 = x19*x9
    x25 = x13*x16
    x26 = x0*(x24 - x25) + x1*(-x13*x20 + x21*x9) + x3*(x16*x21 - x19*x20)
    x27 = 1/(x22**2 + x23*x26**2)
    x28 = Y2 + x10
    x29 = Z2 + x17
    x30 = x13*x8 + x15*x19 - x16*x29 - x28*x9
    x31 = x1*x19
    x32 = x13*x3
    x33 = x0*(x31 - x32) + x2*x21 + x21*x4
    x34 = x0*x23
    x35 = x1*x13 + x19*x3
    x36 = x0*(-x13*x15 + x16*x28 + x19*x8 - x29*x9) + x1*(x20*x28 + x21*x8) - x24 + x25 + x26*x34 + x3*(x15*x21 + x20*x29)
    x37 = 2*x27*(x22*x35 + x23*x26*x33)
    return x27*(x22*x36*x37 - x22*(-x0*(-x1*(Z4 + x14) + x3*(Y4 + x7)) - x31 + x32 + x33*x34) - x26*x30*x37 - x26*(x1*x28 + x29*x3) + x30*x33 - x35*x36)/sqrt(x5)

def phi_dX3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x1 + x2**2 + x4
    x6 = -X2
    x7 = X1 + x6
    x8 = -Y2
    x9 = Y1 + x8
    x10 = -x0*x9 + x2*x7
    x11 = -Y4
    x12 = Y3 + x11
    x13 = X3 - X4
    x14 = x0*x12 - x13*x2
    x15 = -Z2
    x16 = Z1 + x15
    x17 = -x0*x16 + x3*x7
    x18 = -Z4
    x19 = Z3 + x18
    x20 = x0*x19 - x13*x3
    x21 = -x16*x2 + x3*x9
    x22 = -x12*x3 + x19*x2
    x23 = x10*x14 + x17*x20 + x21*x22
    x24 = 1/x5
    x25 = x10*x20
    x26 = x14*x17
    x27 = x0*(x25 - x26) + x2*(x10*x22 - x14*x21) + x3*(x17*x22 - x20*x21)
    x28 = 1/(x23**2 + x24*x27**2)
    x29 = Y2 + x11
    x30 = Z2 + x18
    x31 = -x10*x29 + x14*x9 + x16*x20 - x17*x30
    x32 = x1*x20 + x2*(x0*x22 + x14*x3) + x20*x4
    x33 = Z4 + x15
    x34 = X3 + x6
    x35 = x0*x24
    x36 = x0*x14 - x22*x3
    x37 = x0*(-x10*x30 - x14*x16 + x17*x29 + x20*x9) + x2*(x21*x29 + x22*x9) - x25 + x26 + x27*x35 + x3*(x16*x22 + x21*x30)
    x38 = 2*x28*(x23*x36 + x24*x27*x32)
    return x28*(-x23*x37*x38 + x23*(-x0*(x20 + x33*x34) - x2*(x22 - x3*(Y4 + x8)) + x20*x34 + x32*x35 + x33*x4) + x27*x31*x38 + x27*(x0*x29 + x14) - x31*x32 + x36*x37)/sqrt(x5)

def phi_dX3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x1 + x3 + x4**2
    x6 = -X2
    x7 = X1 + x6
    x8 = -Y2
    x9 = Y1 + x8
    x10 = -x0*x9 + x2*x7
    x11 = -Y4
    x12 = Y3 + x11
    x13 = X3 - X4
    x14 = x0*x12 - x13*x2
    x15 = -Z2
    x16 = Z1 + x15
    x17 = -x0*x16 + x4*x7
    x18 = -Z4
    x19 = Z3 + x18
    x20 = x0*x19 - x13*x4
    x21 = -x16*x2 + x4*x9
    x22 = x19*x2
    x23 = x12*x4
    x24 = x22 - x23
    x25 = x10*x14 + x17*x20 + x21*x24
    x26 = 1/x5
    x27 = x10*x20
    x28 = x14*x17
    x29 = x0*(x27 - x28) + x2*(x10*x24 - x14*x21) + x4*(x17*x24 - x20*x21)
    x30 = 1/(x25**2 + x26*x29**2)
    x31 = Y2 + x11
    x32 = Z2 + x18
    x33 = -x10*x31 + x14*x9 + x16*x20 - x17*x32
    x34 = x0*x14
    x35 = X3 + x6
    x36 = Y3 + x8
    x37 = x0*x26
    x38 = x14*x2*x36 + x34*x35 - x4*(-x20*x36 + x24*x35)
    x39 = x0*x20 + x2*x24
    x40 = x0*(-x10*x32 - x14*x16 + x17*x31 + x20*x9) + x2*(x21*x31 + x24*x9) - x27 + x28 + x29*x37 + x4*(x16*x24 + x21*x32)
    x41 = 2*x30*(x25*x39 + x26*x29*x38)
    return x30*(-x25*x40*x41 + x25*(x0*(x14 + x35*(Y4 + x8)) + x3*x31 + x34 + x37*x38 + x4*(-x22 + x23 + x36*(Z4 + x15))) + x29*x33*x41 + x29*(x0*x32 + x20) + x33*(x1*x14 + x14*x3 + x4*(-x0*x24 + x2*x20)) + x39*x40)/sqrt(x5)

def phi_dX3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = -Y3
    x3 = Y2 + x2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1 + x3**2 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x3*x7
    x10 = -Y4
    x11 = Y3 + x10
    x12 = X3 - X4
    x13 = x0*x11 - x12*x3
    x14 = Z1 - Z2
    x15 = -x0*x14 + x5*x7
    x16 = -Z4
    x17 = Z3 + x16
    x18 = x0*x17 - x12*x5
    x19 = -x14*x3 + x5*x8
    x20 = -x11*x5 + x17*x3
    x21 = x13*x9 + x15*x18 + x19*x20
    x22 = 1/x6
    x23 = x18*x9
    x24 = x13*x15
    x25 = x0*(x23 - x24) + x3*(-x13*x19 + x20*x9) + x5*(x15*x20 - x18*x19)
    x26 = x25**2
    x27 = 1/(x21**2 + x22*x26)
    x28 = Y1 + x2
    x29 = Y2 + x10
    x30 = Z1 + x4
    x31 = Z2 + x16
    x32 = x13*x8 + x14*x18 - x15*x31 - x29*x9
    x33 = x22*x25
    x34 = x0*x33
    x35 = x18*x28
    x36 = x11*x15
    x37 = x13*x30
    x38 = x17*x9
    x39 = x35 + x36 - x37 - x38
    x40 = -x23
    x41 = x24 + x3*(x11*x19 + x20*x28) + x40 + x5*(x17*x19 + x20*x30)
    x42 = -x11*x9 + x13*x28 - x15*x17 + x18*x30
    x43 = x18*x8
    x44 = x15*x29
    x45 = -x13*x14
    x46 = -x31*x9
    x47 = x0*(x43 + x44 + x45 + x46) + x24 + x3*(x19*x29 + x20*x8) + x40 + x5*(x14*x20 + x19*x31)
    x48 = x34 + x47
    x49 = x6**(-2)
    x50 = x0*x22
    x51 = -x0*(-x35 - x36 + x37 + x38) + x41
    x52 = 2*x27*(x0*x26*x49 + x21*x42 + x33*x51)
    return x27*(-x21*x48*x52 - x21*(x0*(-x11*x14 + x17*x8 + x28*x31 - x29*x30) - 3*x1*x25*x49 + x33 + x39 + x43 + x44 + x45 + x46 - x47*x50 - x50*x51) + x25*x32*x52 + x25*(x11*x8 + x14*x17 + x28*x29 + x30*x31) - x32*x34 - x32*(x0*x39 + x41) + x42*x48)/sqrt(x6)

def phi_dX3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = Y2 - Y3
    x3 = -Z3
    x4 = Z2 + x3
    x5 = x1**2 + x2**2 + x4**2
    x6 = X1 - X2
    x7 = x2*x6
    x8 = Y1 - Y2
    x9 = -x1*x8
    x10 = x7 + x9
    x11 = -Y4
    x12 = Y3 + x11
    x13 = X3 - X4
    x14 = x1*x12 - x13*x2
    x15 = -Z2
    x16 = Z1 + x15
    x17 = -x1*x16 + x4*x6
    x18 = -Z4
    x19 = Z3 + x18
    x20 = x1*x19
    x21 = x13*x4
    x22 = x20 - x21
    x23 = -x16*x2 + x4*x8
    x24 = x19*x2
    x25 = x12*x4
    x26 = x24 - x25
    x27 = x10*x14 + x17*x22 + x23*x26
    x28 = 1/x5
    x29 = x10*x22
    x30 = x14*x17
    x31 = x10*x26
    x32 = -x14*x23
    x33 = x1*(x29 - x30) + x2*(x31 + x32) + x4*(x17*x26 - x22*x23)
    x34 = x33**2
    x35 = 1/(x27**2 + x28*x34)
    x36 = X1 + x0
    x37 = Y2 + x11
    x38 = x2*x28
    x39 = Z2 + x18
    x40 = -x10*x37 + x14*x8 + x16*x22 - x17*x39
    x41 = x33*x40
    x42 = Z1 + x3
    x43 = x17*x19
    x44 = x13*x17 + x22*x36
    x45 = x1*x44 + x2*(x10*x19 + x13*x23 + x14*x42 + x26*x36) + x31 + x32
    x46 = x4*(x22*x42 + x43) + x45
    x47 = -x10*x13 + x14*x36 + x19*x23 - x26*x42
    x48 = x26*x8
    x49 = x23*x37
    x50 = x1*(-x10*x39 - x14*x16 + x17*x37 + x22*x8) + x2*(x48 + x49) - x29 + x30 + x4*(x16*x26 + x23*x39)
    x51 = x1*x28*x33 + x50
    x52 = -Z1 + Z3
    x53 = x2/x5**2
    x54 = 2*x35*(x27*x47 + x28*x33*x46 - x34*x53)
    return x35*(x27*x51*x54 + x27*(-x1*x28*(-x4*(x22*x52 - x43) + x45) + 3*x1*x33*x53 - x1*(x13*x16 + x17 - x20 + x21 - x36*x39) - x2*(x19*x8 + x23 - x24 + x25 - x37*x42) + x38*x50 + x4*(-x16*x19 + x52*(Z4 + x15)) + x44 - x48 - x49) - x33*(x13*x8 + x14 + x36*x37 + x7 + x9) - x38*x41 + x40*x46 - x41*x54 - x47*x51)/sqrt(x5)

def phi_dX3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = Z2 - Z3
    x5 = x1**2 + x3**2 + x4**2
    x6 = X1 - X2
    x7 = -Y2
    x8 = Y1 + x7
    x9 = -x1*x8 + x3*x6
    x10 = -Y4
    x11 = Y3 + x10
    x12 = x1*x11
    x13 = X3 - X4
    x14 = x13*x3
    x15 = x12 - x14
    x16 = x4*x6
    x17 = Z1 - Z2
    x18 = -x1*x17
    x19 = x16 + x18
    x20 = -Z4
    x21 = Z3 + x20
    x22 = x1*x21 - x13*x4
    x23 = -x17*x3 + x4*x8
    x24 = x21*x3
    x25 = x11*x4
    x26 = x24 - x25
    x27 = x15*x9 + x19*x22 + x23*x26
    x28 = 1/x5
    x29 = x22*x9
    x30 = x15*x19
    x31 = x19*x26
    x32 = x22*x23
    x33 = x31 - x32
    x34 = x1*(x29 - x30) + x3*(-x15*x23 + x26*x9) + x33*x4
    x35 = x34**2
    x36 = 1/(x27**2 + x28*x35)
    x37 = X1 + x0
    x38 = Z2 + x20
    x39 = x28*x4
    x40 = Y2 + x10
    x41 = x15*x8 + x17*x22 - x19*x38 - x40*x9
    x42 = x34*x41
    x43 = x15*x37
    x44 = x13*x9
    x45 = Y1 + x2
    x46 = x15*x45
    x47 = x4*(-x11*x19 + x13*x23 - x22*x45 + x26*x37)
    x48 = -x31 + x32 - x47
    x49 = -x11*x23 - x13*x19 + x22*x37 + x26*x45
    x50 = x17*x26
    x51 = x23*x38
    x52 = x1*(-x15*x17 + x19*x40 + x22*x8 - x38*x9) - x29 + x3*(x23*x40 + x26*x8) + x30 + x4*(x50 + x51)
    x53 = x1*x28*x34 + x52
    x54 = X4 + x0
    x55 = x4/x5**2
    x56 = x1*(x43 - x54*x9)
    x57 = x3*(x46 - x9*(Y4 + x2))
    x58 = 2*x36*(x27*x49 - x28*x34*(x48 + x56 + x57) - x35*x55)
    return x36*(x27*x53*x58 + x27*(-x1*x28*(x33 + x47 - x56 - x57) + 3*x1*x34*x55 + x1*(-x12 + x14 + x37*(Y4 + x7) - x54*x8 + x9) - x3*(-x11*x8 + x40*x45) + x39*x52 - x4*(-x11*x17 + x23 - x24 + x25 + x38*x45) - x43 - x44 - x50 - x51) - x34*(x13*x17 + x16 + x18 + x22 + x37*x38) - x39*x42 - x41*(x1*(x43 + x44) + x3*(x11*x9 + x46) + x48) - x42*x58 - x49*x53)/sqrt(x5)

def phi_dX3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x1 + x2**2 + x3**2
    x5 = X1 - X2
    x6 = Y1 - Y2
    x7 = -x0*x6 + x2*x5
    x8 = -Y4
    x9 = Y3 + x8
    x10 = X3 - X4
    x11 = x0*x9 - x10*x2
    x12 = Z1 - Z2
    x13 = -x0*x12 + x3*x5
    x14 = -Z4
    x15 = Z3 + x14
    x16 = x0*x15 - x10*x3
    x17 = -x12*x2 + x3*x6
    x18 = x15*x2 - x3*x9
    x19 = x11*x7 + x13*x16 + x17*x18
    x20 = 1/x4
    x21 = x16*x7
    x22 = x11*x13
    x23 = x21 - x22
    x24 = -x11*x17 + x18*x7
    x25 = x13*x18 - x16*x17
    x26 = x0*x23 + x2*x24 + x25*x3
    x27 = x26**2
    x28 = 1/(x19**2 + x20*x27)
    x29 = Y2 + x8
    x30 = Z2 + x14
    x31 = 2*x0*x23 + 2*x2*x24 + 2*x25*x3
    x32 = x11*x6 + x12*x16 - x13*x30 - x29*x7
    x33 = x20*x26
    x34 = x0*x33
    x35 = x16*x6
    x36 = x13*x29
    x37 = x11*x12
    x38 = x30*x7
    x39 = x0*(x35 + x36 - x37 - x38) + x2*(x17*x29 + x18*x6) - x21 + x22 + x3*(x12*x18 + x17*x30)
    x40 = x34 + x39
    x41 = 2*X2 - 2*X3
    x42 = x4**(-2)
    x43 = x28*(x0*x27*x42 + x19*x32 + x33*x39)
    return x28*(2*x19*x40*x43 - x19*(3*x1*x26*x42 + x20*x39*x41 - x33 - 2*x35 - 2*x36 + 2*x37 + 2*x38 - x41*(-x12*x29 + x30*x6)) - x31*x32*x43 - x31*(x12*x30 + x29*x6) + x32*x34 + x32*x39 - x32*x40)/sqrt(x4)

def phi_dX3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = Z2 - Z3
    x3 = x0**2 + x1**2 + x2**2
    x4 = X1 - X2
    x5 = Y1 - Y2
    x6 = -x0*x5 + x1*x4
    x7 = -Y4
    x8 = Y3 + x7
    x9 = -X4
    x10 = X3 + x9
    x11 = x0*x8 - x1*x10
    x12 = -Z2
    x13 = Z1 + x12
    x14 = -x0*x13 + x2*x4
    x15 = -Z4
    x16 = Z3 + x15
    x17 = x0*x16 - x10*x2
    x18 = -x1*x13 + x2*x5
    x19 = x1*x16 - x2*x8
    x20 = x11*x6 + x14*x17 + x18*x19
    x21 = 1/x3
    x22 = x17*x6
    x23 = x11*x14
    x24 = x19*x6
    x25 = -x11*x18
    x26 = x0*(x22 - x23) + x1*(x24 + x25) + x2*(x14*x19 - x17*x18)
    x27 = x26**2
    x28 = 1/(x20**2 + x21*x27)
    x29 = Y2 + x7
    x30 = X2 + x9
    x31 = x1*x21
    x32 = x13*x17
    x33 = Z2 + x15
    x34 = x14*x33
    x35 = x11*x5 - x29*x6 + x32 - x34
    x36 = x26*x35
    x37 = x14*x30 + x17*x4
    x38 = x11*x13
    x39 = x33*x6
    x40 = x0*x37 + x1*(x18*x30 + x19*x4 + x38 + x39) + x24 + x25
    x41 = x2*(x32 + x34) + x40
    x42 = x18*x33
    x43 = x13*x19
    x44 = x11*x4 - x30*x6 + x42 - x43
    x45 = x19*x5
    x46 = x18*x29
    x47 = x0*(x14*x29 + x17*x5 - x38 - x39) + x1*(x45 + x46) + x2*(x42 + x43) - x22 + x23
    x48 = x0*x21*x26 + x47
    x49 = x1/x3**2
    x50 = 2*x28*(x20*x44 + x21*x26*(x2*(-x14*(Z4 + x12) + x32) + x40) - x27*x49)
    return x28*(-x20*x48*x50 - x20*(-x0*x21*x41 + 3*x0*x26*x49 + x0*(-x13*x30 + x33*x4) - x1*(-x13*x29 + x33*x5) + x31*x47 + x37 - x45 - x46) + x26*(x29*x4 + x30*x5) + x31*x36 - x35*x41 + x36*x50 + x44*x48)/sqrt(x3)

def phi_dX3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = Z2 - Z3
    x3 = x0**2 + x1**2 + x2**2
    x4 = X1 - X2
    x5 = Y1 - Y2
    x6 = -x0*x5 + x1*x4
    x7 = -Y4
    x8 = Y3 + x7
    x9 = -X4
    x10 = X3 + x9
    x11 = x0*x8 - x1*x10
    x12 = Z1 - Z2
    x13 = -x0*x12 + x2*x4
    x14 = -Z4
    x15 = Z3 + x14
    x16 = x0*x15 - x10*x2
    x17 = -x1*x12 + x2*x5
    x18 = x1*x15 - x2*x8
    x19 = x11*x6 + x13*x16 + x17*x18
    x20 = 1/x3
    x21 = x16*x6
    x22 = x11*x13
    x23 = x13*x18
    x24 = x16*x17
    x25 = x23 - x24
    x26 = x0*(x21 - x22) + x1*(-x11*x17 + x18*x6) + x2*x25
    x27 = x26**2
    x28 = 1/(x19**2 + x20*x27)
    x29 = Z2 + x14
    x30 = X2 + x9
    x31 = x2*x20
    x32 = x11*x5
    x33 = Y2 + x7
    x34 = x33*x6
    x35 = -x34
    x36 = x12*x16 - x13*x29 + x32 + x35
    x37 = x26*x36
    x38 = x11*x4
    x39 = x30*x6
    x40 = x0*(x38 + x39)
    x41 = x1*(x32 + x34)
    x42 = x18*x4
    x43 = x17*x30
    x44 = x16*x5
    x45 = x13*x33
    x46 = x2*(x42 + x43 - x44 - x45)
    x47 = x18*x5
    x48 = x17*x33
    x49 = -x13*x30 + x16*x4 + x47 - x48
    x50 = x12*x18
    x51 = x17*x29
    x52 = x44 + x45
    x53 = x0*(-x11*x12 - x29*x6 + x52) + x1*(x47 + x48) + x2*(x50 + x51) - x21 + x22
    x54 = x0*x20*x26 + x53
    x55 = -x39
    x56 = x2/x3**2
    x57 = 2*x28*(x19*x49 + x20*x26*(x0*(x11*(-X1 + X2) + x55) + x1*(x11*(-Y1 + Y2) + x35) - x2*(-x42 - x43 + x52) + x25) - x27*x56)
    return x28*(-x19*x54*x57 - x19*(-x0*x20*(x25 - x40 - x41 + x46) + 3*x0*x26*x56 - x0*(-x30*x5 + x33*x4) - x2*(-x12*x33 + x29*x5) + x31*x53 - x38 - x50 - x51 + x55) + x26*(x12*x30 + x29*x4) + x31*x37 + x36*(-x23 + x24 + x40 + x41 - x46) + x37*x57 + x49*x54)/sqrt(x3)

def phi_dX3_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x1*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = X3 - X4
    x12 = x0*x10 - x1*x11
    x13 = Z1 - Z2
    x14 = -x0*x13 + x3*x6
    x15 = -Z4
    x16 = Z3 + x15
    x17 = x0*x16 - x11*x3
    x18 = -x1*x13 + x3*x7
    x19 = x1*x16 - x10*x3
    x20 = x12*x8 + x14*x17 + x18*x19
    x21 = 1/x5
    x22 = x17*x8
    x23 = x12*x14
    x24 = x0*(x22 - x23) + x1*(-x12*x18 + x19*x8) + x3*(x14*x19 - x17*x18)
    x25 = 1/(x20**2 + x21*x24**2)
    x26 = Y2 + x9
    x27 = Z2 + x15
    x28 = x12*x7 + x13*x17 - x14*x27 - x26*x8
    x29 = x18*x2 + x18*x4
    x30 = x1*x14
    x31 = x3*x8
    x32 = x0*(x30 - x31) + x29
    x33 = -x30 + x31
    x34 = x0*x21
    x35 = x1*x8 + x14*x3
    x36 = x0*(-x12*x13 + x14*x26 + x17*x7 - x27*x8) + x1*(x18*x26 + x19*x7) - x22 + x23 + x24*x34 + x3*(x13*x19 + x18*x27)
    x37 = 2*x25*(x20*x35 - x21*x24*x32)
    return x25*(x20*x36*x37 + x20*(-x0*x18 + x33 + x34*(-x0*x33 + x29)) - x24*x28*x37 + x24*(x1*x7 + x13*x3) - x28*x32 - x35*x36)/sqrt(x5)

def phi_dX3_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = x2*x7
    x9 = Y1 - Y2
    x10 = x0*x9
    x11 = -x10 + x8
    x12 = -Y4
    x13 = Y3 + x12
    x14 = X3 - X4
    x15 = x0*x13 - x14*x2
    x16 = x4*x7
    x17 = Z1 - Z2
    x18 = x0*x17
    x19 = x16 - x18
    x20 = -Z4
    x21 = Z3 + x20
    x22 = x0*x21 - x14*x4
    x23 = -x17*x2 + x4*x9
    x24 = -x13*x4 + x2*x21
    x25 = x11*x15 + x19*x22 + x23*x24
    x26 = 1/x6
    x27 = x11*x22
    x28 = x15*x19
    x29 = x0*(x27 - x28) + x2*(x11*x24 - x15*x23) + x4*(x19*x24 - x22*x23)
    x30 = 1/(x25**2 + x26*x29**2)
    x31 = Y2 + x12
    x32 = Z2 + x20
    x33 = -x11*x31 + x15*x9 + x17*x22 - x19*x32
    x34 = x1*x19 + x19*x5 + x2*(x0*x23 + x11*x4)
    x35 = x0*x26
    x36 = x0*x11 - x23*x4
    x37 = x0*(-x11*x32 - x15*x17 + x19*x31 + x22*x9) + x2*(x23*x31 + x24*x9) - x27 + x28 + x29*x35 + x4*(x17*x24 + x23*x32)
    x38 = 2*x30*(x25*x36 - x26*x29*x34)
    return x30*(-x25*x37*x38 - x25*(-x0*x19 - x0*(x16 - 2*x18) + x17*x3 + x17*x5 + x34*x35) + x29*x33*x38 + x29*(-2*x10 + x8) + x33*x34 + x36*x37)/sqrt(x6)

def phi_dX3_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = -X2
    x8 = X1 + x7
    x9 = x2*x8
    x10 = -Y2
    x11 = Y1 + x10
    x12 = x0*x11
    x13 = -x12 + x9
    x14 = -Y4
    x15 = Y3 + x14
    x16 = X3 - X4
    x17 = x0*x15 - x16*x2
    x18 = x4*x8
    x19 = Z1 - Z2
    x20 = x0*x19
    x21 = x18 - x20
    x22 = -Z4
    x23 = Z3 + x22
    x24 = x0*x23 - x16*x4
    x25 = x11*x4 - x19*x2
    x26 = -x15*x4 + x2*x23
    x27 = x13*x17 + x21*x24 + x25*x26
    x28 = 1/x6
    x29 = x13*x24
    x30 = x17*x21
    x31 = x0*(x29 - x30) + x2*(x13*x26 - x17*x25) + x4*(x21*x26 - x24*x25)
    x32 = 1/(x27**2 + x28*x31**2)
    x33 = Y2 + x14
    x34 = Z2 + x22
    x35 = x11*x17 - x13*x33 + x19*x24 - x21*x34
    x36 = x1*x13 + x13*x3
    x37 = x0*x28
    x38 = x36 + x4*(-x21*(Y3 + x10) + x25*(X3 + x7))
    x39 = x0*x21 + x2*x25
    x40 = x0*(x11*x24 - x13*x34 - x17*x19 + x21*x33) + x2*(x11*x26 + x25*x33) - x29 + x30 + x31*x37 + x4*(x19*x26 + x25*x34)
    x41 = 2*x32*(x27*x39 + x28*x31*x38)
    return x32*(-x27*x40*x41 + x27*(-x0*x13 - x0*(-2*x12 + x9) + x11*x3 + x11*x5 + x37*x38) + x31*x35*x41 + x31*(x18 - 2*x20) - x35*(x36 - x4*(x0*x25 - x2*x21)) + x39*x40)/sqrt(x6)

def phi_dY3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x1*x6
    x9 = Y3 - Y4
    x10 = x0*x9
    x11 = -X4
    x12 = X3 + x11
    x13 = x1*x12
    x14 = x10 - x13
    x15 = -Z2
    x16 = Z1 + x15
    x17 = -x0*x16 + x3*x6
    x18 = -Z4
    x19 = Z3 + x18
    x20 = x0*x19 - x12*x3
    x21 = -x1*x16 + x3*x7
    x22 = x1*x19
    x23 = x3*x9
    x24 = x22 - x23
    x25 = x14*x8 + x17*x20 + x21*x24
    x26 = 1/x5
    x27 = x24*x8
    x28 = x14*x21
    x29 = x0*(-x14*x17 + x20*x8) + x1*(x27 - x28) + x3*(x17*x24 - x20*x21)
    x30 = 1/(x25**2 + x26*x29**2)
    x31 = Z2 + x18
    x32 = X2 + x11
    x33 = x14*x6 - x16*x24 + x21*x31 - x32*x8
    x34 = x0*(x1*x20 - x14*x3) + x2*x24 + x24*x4
    x35 = x1*x26
    x36 = x1*x14 + x20*x3
    x37 = -x0*(x17*x32 + x20*x6) - x1*(x14*x16 + x21*x32 + x24*x6 + x31*x8) - x27 + x28 + x29*x35 - x3*(x16*x20 - x17*(Z4 + x15))
    x38 = 2*x30*(x25*x36 + x26*x29*x34)
    return x30*(x25*x37*x38 - x25*(-x0*(x20 + x3*x32) - x1*x24 + x1*(-x1*x31 - x22 + x23) - x31*x4 + x34*x35) + x29*x33*x38 + x29*(x1*x32 - x10 + x13) - x33*x34 - x36*x37)/sqrt(x5)

def phi_dY3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x1 + x2**2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = Y3 - Y4
    x10 = -X4
    x11 = X3 + x10
    x12 = x0*x9 - x11*x2
    x13 = -Z2
    x14 = Z1 + x13
    x15 = -x0*x14 + x3*x6
    x16 = -Z4
    x17 = Z3 + x16
    x18 = x0*x17 - x11*x3
    x19 = -x14*x2 + x3*x7
    x20 = x17*x2 - x3*x9
    x21 = x12*x8 + x15*x18 + x19*x20
    x22 = 1/x5
    x23 = x20*x8
    x24 = x12*x19
    x25 = x0*(-x12*x15 + x18*x8) + x2*(x23 - x24) + x3*(x15*x20 - x18*x19)
    x26 = 1/(x21**2 + x22*x25**2)
    x27 = Z2 + x16
    x28 = X2 + x10
    x29 = x12*x6 - x14*x20 + x19*x27 - x28*x8
    x30 = x0*x20 + x12*x3
    x31 = x1*x18 + x18*x4 + x2*x30
    x32 = x2*x22
    x33 = x0*x12 - x20*x3
    x34 = -x0*(x15*x28 + x18*x6) - x2*(x12*x14 + x19*x28 + x20*x6 + x27*x8) - x23 + x24 + x25*x32 - x3*(x14*x18 - x15*(Z4 + x13))
    x35 = 2*x26*(x21*x33 + x22*x25*x31)
    return x26*(-x21*x34*x35 - x21*(x2*(x0*x27 - x28*x3) + x30 - x31*x32) - x25*x29*x35 - x25*(x0*x28 + x27*x3) + x29*x31 + x33*x34)/sqrt(x5)

def phi_dY3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x1 + x3 + x4**2
    x6 = -X2
    x7 = X1 + x6
    x8 = -Y2
    x9 = Y1 + x8
    x10 = -x0*x9 + x2*x7
    x11 = Y3 - Y4
    x12 = -X4
    x13 = X3 + x12
    x14 = x0*x11 - x13*x2
    x15 = -Z2
    x16 = Z1 + x15
    x17 = -x0*x16 + x4*x7
    x18 = -Z4
    x19 = Z3 + x18
    x20 = x0*x19
    x21 = x13*x4
    x22 = x20 - x21
    x23 = -x16*x2 + x4*x9
    x24 = -x11*x4 + x19*x2
    x25 = x10*x14 + x17*x22 + x23*x24
    x26 = 1/x5
    x27 = x10*x24
    x28 = x14*x23
    x29 = x0*(x10*x22 - x14*x17) + x2*(x27 - x28) + x4*(x17*x24 - x22*x23)
    x30 = 1/(x25**2 + x26*x29**2)
    x31 = Z2 + x18
    x32 = X2 + x12
    x33 = -x10*x32 + x14*x7 - x16*x24 + x23*x31
    x34 = x14*x2
    x35 = Y3 + x8
    x36 = x2*x26
    x37 = X3 + x6
    x38 = x0*x14*x37 + x34*x35 - x4*(-x22*x35 + x24*x37)
    x39 = x0*x22 + x2*x24
    x40 = -x0*(x17*x32 + x22*x7) - x2*(x10*x31 + x14*x16 + x23*x32 + x24*x7) - x27 + x28 + x29*x36 - x4*(x16*x22 - x17*(Z4 + x15))
    x41 = 2*x30*(x25*x39 + x26*x29*x38)
    return x30*(-x25*x40*x41 + x25*(-x1*x32 + x2*(x14 + x32*x35) + x34 + x36*x38 - x4*(x0*x31 - x20 + x21)) - x29*x33*x41 + x29*(x2*x31 + x24) - x33*(x1*x14 + x14*x3 + x4*(-x0*x24 + x2*x22)) + x39*x40)/sqrt(x5)

def phi_dY3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = -Y3
    x2 = Y2 + x1
    x3 = -Z3
    x4 = Z2 + x3
    x5 = x0**2 + x2**2 + x4**2
    x6 = X1 - X2
    x7 = x2*x6
    x8 = Y1 - Y2
    x9 = x0*x8
    x10 = x7 - x9
    x11 = Y3 - Y4
    x12 = x0*x11
    x13 = -X4
    x14 = X3 + x13
    x15 = x14*x2
    x16 = x12 - x15
    x17 = x4*x6
    x18 = -Z2
    x19 = Z1 + x18
    x20 = x0*x19
    x21 = x17 - x20
    x22 = -Z4
    x23 = Z3 + x22
    x24 = x0*x23 - x14*x4
    x25 = x4*x8
    x26 = x19*x2
    x27 = x25 - x26
    x28 = -x11*x4 + x2*x23
    x29 = x10*x16 + x21*x24 + x27*x28
    x30 = 1/x5
    x31 = x10*x24
    x32 = x16*x21
    x33 = x31 - x32
    x34 = x10*x28
    x35 = x16*x27
    x36 = x0*x33 + x2*(x34 - x35) + x4*(x21*x28 - x24*x27)
    x37 = x36**2
    x38 = 1/(x29**2 + x30*x37)
    x39 = X2 + x13
    x40 = Y1 + x1
    x41 = x0*x30
    x42 = Z2 + x22
    x43 = -x10*x39 + x16*x6 - x19*x28 + x27*x42
    x44 = x36*x43
    x45 = x24*x40
    x46 = x11*x21
    x47 = Z1 + x3
    x48 = x16*x47
    x49 = x10*x23
    x50 = x28*x40
    x51 = x11*x27
    x52 = x2*(x50 + x51)
    x53 = x4*(x23*x27 + x28*x47)
    x54 = -x31 + x32 + x52 + x53
    x55 = -x10*x11 + x16*x40 - x21*x23 + x24*x47
    x56 = x21*x39 + x24*x6
    x57 = -x0*x56 - x2*(x10*x42 + x16*x19 + x27*x39 + x28*x6) - x34 + x35 - x4*(x19*x24 - x21*(Z4 + x18))
    x58 = x2*x30*x36 + x57
    x59 = x0/x5**2
    x60 = x0*(-x45 - x46 + x48 + x49)
    x61 = 2*x38*(x29*x55 + x30*x36*(x54 - x60) + x37*x59)
    return x38*(-x29*x58*x61 + x29*(-x0*(-x17 + x20 - x23*x6 + x24 + x39*x47) - x2*x30*(x33 - x52 - x53 + x60) + 3*x2*x36*x59 - x2*(-x11*x19 - x25 + x26 + x28 + x40*x42) - x4*(-x19*x23 + x42*x47) + x41*x57 - x50 - x51 + x56) - x36*(x11*x6 - x12 + x15 + x39*x40 - x7 + x9) + x41*x44 + x43*(x0*(x45 + x46 - x48 - x49) + x54) - x44*x61 + x55*x58)/sqrt(x5)

def phi_dY3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x1**2 + x3 + x5**2
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = -X4
    x12 = X3 + x11
    x13 = x1*x10 - x12*x2
    x14 = -Z2
    x15 = Z1 + x14
    x16 = -x1*x15 + x5*x7
    x17 = -Z4
    x18 = Z3 + x17
    x19 = x1*x18 - x12*x5
    x20 = -x15*x2 + x5*x8
    x21 = -x10*x5 + x18*x2
    x22 = x13*x9 + x16*x19 + x20*x21
    x23 = 1/x6
    x24 = x21*x9
    x25 = x13*x20
    x26 = x24 - x25
    x27 = x1*(-x13*x16 + x19*x9) + x2*x26 + x5*(x16*x21 - x19*x20)
    x28 = x27**2
    x29 = 1/(x22**2 + x23*x28)
    x30 = X1 + x0
    x31 = X2 + x11
    x32 = Z1 + x4
    x33 = Z2 + x17
    x34 = x13*x7 - x15*x21 + x20*x33 - x31*x9
    x35 = x23*x27
    x36 = x2*x35
    x37 = x21*x30
    x38 = x12*x20
    x39 = x13*x32
    x40 = x18*x9
    x41 = x1*(x12*x16 + x19*x30) + x2*(x37 + x38 + x39 + x40) + x26 + x5*(x16*x18 + x19*x32)
    x42 = -x12*x9 + x13*x30 + x18*x20 - x21*x32
    x43 = x1*(x16*x31 + x19*x7)
    x44 = x5*(x15*x19 - x16*(Z4 + x14))
    x45 = x21*x7
    x46 = x20*x31
    x47 = x13*x15
    x48 = x33*x9
    x49 = x2*(x45 + x46 + x47 + x48)
    x50 = -x24 + x25 + x36 - x43 - x44 - x49
    x51 = x6**(-2)
    x52 = x2*x23
    x53 = 2*x29*(-x2*x28*x51 + x22*x42 + x35*x41)
    return x29*(x22*x50*x53 - x22*(x2*(x12*x15 - x18*x7 - x30*x33 + x31*x32) - 3*x27*x3*x51 + x35 - x37 - x38 - x39 - x40 + x41*x52 - x45 - x46 - x47 - x48 + x52*(x26 + x43 + x44 + x49)) + x27*x34*x53 + x27*(x12*x7 + x15*x18 + x30*x31 + x32*x33) + x34*x36 - x34*x41 - x42*x50)/sqrt(x6)

def phi_dY3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = Z2 - Z3
    x5 = x1**2 + x3**2 + x4**2
    x6 = X1 - X2
    x7 = x3*x6
    x8 = Y1 - Y2
    x9 = x1*x8
    x10 = x7 - x9
    x11 = Y3 - Y4
    x12 = -X4
    x13 = X3 + x12
    x14 = x1*x11 - x13*x3
    x15 = -Z2
    x16 = Z1 + x15
    x17 = -x1*x16 + x4*x6
    x18 = -Z4
    x19 = Z3 + x18
    x20 = x1*x19
    x21 = x13*x4
    x22 = x20 - x21
    x23 = x4*x8
    x24 = -x16*x3
    x25 = x23 + x24
    x26 = -x11*x4 + x19*x3
    x27 = x10*x14 + x17*x22 + x25*x26
    x28 = 1/x5
    x29 = x10*x26
    x30 = x14*x25
    x31 = x17*x26
    x32 = x22*x25
    x33 = x31 - x32
    x34 = x1*(x10*x22 - x14*x17) + x3*(x29 - x30) + x33*x4
    x35 = x34**2
    x36 = 1/(x27**2 + x28*x35)
    x37 = Y1 + x2
    x38 = Z2 + x18
    x39 = x28*x4
    x40 = X2 + x12
    x41 = -x10*x40 + x14*x6 - x16*x26 + x25*x38
    x42 = x34*x41
    x43 = X1 + x0
    x44 = x14*x43
    x45 = x14*x37
    x46 = x10*x11
    x47 = x4*(-x11*x17 + x13*x25 - x22*x37 + x26*x43)
    x48 = -x31 + x32 - x47
    x49 = -x11*x25 - x13*x17 + x22*x43 + x26*x37
    x50 = x16*x22
    x51 = Z4 + x15
    x52 = -x1*(x17*x40 + x22*x6) - x29 - x3*(x10*x38 + x14*x16 + x25*x40 + x26*x6) + x30 - x4*(-x17*x51 + x50)
    x53 = x28*x3*x34 + x52
    x54 = X4 + x0
    x55 = x4/x5**2
    x56 = x1*(-x10*x54 + x44)
    x57 = x3*(-x10*(Y4 + x2) + x45)
    x58 = 2*x36*(x27*x49 - x28*x34*(x48 + x56 + x57) - x35*x55)
    return x36*(x27*x53*x58 + x27*(-x1*(x13*x6 - x40*x43) + x17*x38 - x28*x3*(x33 + x47 - x56 - x57) + 3*x3*x34*x55 - x3*(x11*x6 + x14 - x37*x40 - x7 + x9) + x39*x52 + x4*(x16*x54 + x17 - x20 + x21 - x43*x51) - x45 - x46 + x50) - x34*(x11*x16 + x23 + x24 + x26 + x37*x38) + x39*x42 + x41*(x1*(x10*x13 + x44) + x3*(x45 + x46) + x48) + x42*x58 - x49*x53)/sqrt(x5)

def phi_dY3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = Z2 - Z3
    x3 = x0**2 + x1**2 + x2**2
    x4 = X1 - X2
    x5 = Y1 - Y2
    x6 = -x0*x5 + x1*x4
    x7 = -Y4
    x8 = Y3 + x7
    x9 = -X4
    x10 = X3 + x9
    x11 = x0*x8 - x1*x10
    x12 = Z1 - Z2
    x13 = -x0*x12 + x2*x4
    x14 = -Z4
    x15 = Z3 + x14
    x16 = x0*x15 - x10*x2
    x17 = -x1*x12 + x2*x5
    x18 = x1*x15 - x2*x8
    x19 = x11*x6 + x13*x16 + x17*x18
    x20 = 1/x3
    x21 = x16*x6
    x22 = x11*x13
    x23 = x18*x6
    x24 = x11*x17
    x25 = x23 - x24
    x26 = x0*(x21 - x22) + x1*x25 + x2*(x13*x18 - x16*x17)
    x27 = x26**2
    x28 = 1/(x19**2 + x20*x27)
    x29 = Y2 + x7
    x30 = X2 + x9
    x31 = x0*x20
    x32 = Z2 + x14
    x33 = x17*x32
    x34 = x12*x18
    x35 = x11*x4 - x30*x6 + x33 - x34
    x36 = x26*x35
    x37 = x18*x5
    x38 = x17*x29
    x39 = x11*x12
    x40 = x32*x6
    x41 = x0*(x13*x29 + x16*x5 - x39 - x40) + x1*(x37 + x38) + x2*(x33 + x34) - x21 + x22
    x42 = x12*x16
    x43 = x13*x32
    x44 = x11*x5 - x29*x6 + x42 - x43
    x45 = x13*x30 + x16*x4
    x46 = x0*x45
    x47 = x2*(x42 + x43)
    x48 = x1*(x17*x30 + x18*x4 + x39 + x40)
    x49 = x1*x20*x26 - x23 + x24 - x46 - x47 - x48
    x50 = x0/x3**2
    x51 = x20*x41
    x52 = 2*x28*(x19*x44 + x26*x51 + x27*x50)
    return x28*(x19*x49*x52 - x19*(x0*(-x12*x30 + x32*x4) + 3*x1*x26*x50 + x1*x51 - x1*(-x12*x29 + x32*x5) - x31*(x25 + x46 + x47 + x48) - x37 - x38 + x45) + x26*(x29*x4 + x30*x5) - x31*x36 - x35*x41 + x36*x52 - x44*x49)/sqrt(x3)

def phi_dY3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x0**2 + x2 + x3**2
    x5 = X1 - X2
    x6 = Y1 - Y2
    x7 = -x0*x6 + x1*x5
    x8 = Y3 - Y4
    x9 = -X4
    x10 = X3 + x9
    x11 = x0*x8 - x1*x10
    x12 = -Z2
    x13 = Z1 + x12
    x14 = -x0*x13 + x3*x5
    x15 = -Z4
    x16 = Z3 + x15
    x17 = x0*x16 - x10*x3
    x18 = -x1*x13 + x3*x6
    x19 = x1*x16 - x3*x8
    x20 = x11*x7 + x14*x17 + x18*x19
    x21 = 1/x4
    x22 = -x11*x14 + x17*x7
    x23 = x19*x7
    x24 = x11*x18
    x25 = -x24
    x26 = x23 + x25
    x27 = x14*x19 - x17*x18
    x28 = x0*x22 + x1*x26 + x27*x3
    x29 = x28**2
    x30 = 1/(x20**2 + x21*x29)
    x31 = X2 + x9
    x32 = Z2 + x15
    x33 = 2*x0*x22 + 2*x1*x26 + 2*x27*x3
    x34 = x11*x5 - x13*x19 + x18*x32 - x31*x7
    x35 = x21*x28
    x36 = x1*x35
    x37 = x13*x17
    x38 = x0*(x14*x31 + x17*x5)
    x39 = x19*x5
    x40 = x18*x31
    x41 = x11*x13
    x42 = x32*x7
    x43 = x1*(x39 + x40 + x41 + x42)
    x44 = x23 + x25 + x38 + x43
    x45 = x3*(-x14*(Z4 + x12) + x37)
    x46 = -x23 + x24 + x36 - x38 - x43 - x45
    x47 = 2*Y2 - 2*Y3
    x48 = x4**(-2)
    x49 = x44 + x45
    x50 = x30*(x1*x29*x48 - x20*x34 - x35*x49)
    return x30*(2*x20*x46*x50 - x20*(3*x2*x28*x48 - x21*x47*x49 - x35 + 2*x39 + 2*x40 + 2*x41 + 2*x42 + x47*(-x13*x31 + x32*x5)) + x33*x34*x50 - x33*(x13*x32 + x31*x5) - x34*x36 + x34*x46 + x34*(x3*(x14*x32 + x37) + x44))/sqrt(x4)

def phi_dY3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = Z2 - Z3
    x3 = x0**2 + x1**2 + x2**2
    x4 = X1 - X2
    x5 = Y1 - Y2
    x6 = -x0*x5 + x1*x4
    x7 = -Y4
    x8 = Y3 + x7
    x9 = -X4
    x10 = X3 + x9
    x11 = x0*x8 - x1*x10
    x12 = Z1 - Z2
    x13 = -x0*x12 + x2*x4
    x14 = -Z4
    x15 = Z3 + x14
    x16 = x0*x15 - x10*x2
    x17 = -x1*x12 + x2*x5
    x18 = x1*x15 - x2*x8
    x19 = x11*x6 + x13*x16 + x17*x18
    x20 = 1/x3
    x21 = x18*x6
    x22 = x11*x17
    x23 = x21 - x22
    x24 = x13*x18
    x25 = x16*x17
    x26 = x24 - x25
    x27 = x0*(-x11*x13 + x16*x6) + x1*x23 + x2*x26
    x28 = x27**2
    x29 = 1/(x19**2 + x20*x28)
    x30 = Z2 + x14
    x31 = Y2 + x7
    x32 = x2*x20
    x33 = x11*x4
    x34 = X2 + x9
    x35 = x34*x6
    x36 = -x35
    x37 = -x12*x18 + x17*x30 + x33 + x36
    x38 = x27*x37
    x39 = x0*(x33 + x35)
    x40 = x11*x5
    x41 = x31*x6
    x42 = x1*(x40 + x41)
    x43 = x18*x4
    x44 = x17*x34
    x45 = x43 + x44
    x46 = x16*x5
    x47 = x13*x31
    x48 = x2*(x45 - x46 - x47)
    x49 = x16*x4
    x50 = x13*x34
    x51 = -x17*x31 + x18*x5 + x49 - x50
    x52 = x0*(x49 + x50)
    x53 = x12*x16 + x13*x30
    x54 = x2*x53
    x55 = x1*(x11*x12 + x30*x6 + x45)
    x56 = x1*x20*x27 - x21 + x22 - x52 - x54 - x55
    x57 = -x41
    x58 = x2/x3**2
    x59 = 2*x29*(x19*x51 + x20*x27*(x0*(x11*(-X1 + X2) + x36) + x1*(x11*(-Y1 + Y2) + x57) - x2*(-x43 - x44 + x46 + x47) + x26) - x28*x58)
    return x29*(-x19*x56*x59 - x19*(-x1*x20*(x26 - x39 - x42 + x48) + 3*x1*x27*x58 - x1*(x31*x4 - x34*x5) + x2*(-x12*x34 + x30*x4) - x32*(x23 + x52 + x54 + x55) - x40 + x53 + x57) + x27*(x12*x31 + x30*x5) - x32*x38 - x37*(-x24 + x25 + x39 + x42 - x48) - x38*x59 + x51*x56)/sqrt(x3)

def phi_dY3_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = x2*x7
    x9 = Y1 - Y2
    x10 = -x0*x9
    x11 = x10 + x8
    x12 = Y3 - Y4
    x13 = -X4
    x14 = X3 + x13
    x15 = x0*x12 - x14*x2
    x16 = -Z2
    x17 = Z1 + x16
    x18 = -x0*x17 + x4*x7
    x19 = -Z4
    x20 = Z3 + x19
    x21 = x0*x20 - x14*x4
    x22 = x4*x9
    x23 = x17*x2
    x24 = x22 - x23
    x25 = -x12*x4 + x2*x20
    x26 = x11*x15 + x18*x21 + x24*x25
    x27 = 1/x6
    x28 = x11*x25
    x29 = x15*x24
    x30 = x0*(x11*x21 - x15*x18) + x2*(x28 - x29) + x4*(x18*x25 - x21*x24)
    x31 = 1/(x26**2 + x27*x30**2)
    x32 = Z2 + x19
    x33 = X2 + x13
    x34 = -x11*x33 + x15*x7 - x17*x25 + x24*x32
    x35 = x24*x3 + x24*x5
    x36 = x18*x2
    x37 = x11*x4
    x38 = x0*(x36 - x37) + x35
    x39 = x2*x27
    x40 = x11*x2 + x18*x4
    x41 = -x0*(x18*x33 + x21*x7) - x2*(x11*x32 + x15*x17 + x24*x33 + x25*x7) - x28 + x29 + x30*x39 - x4*(x17*x21 - x18*(Z4 + x16))
    x42 = 2*x31*(x26*x40 - x27*x30*x38)
    return x31*(x26*x41*x42 + x26*(x1*x17 + x17*x5 - x2*x24 - x2*(x22 - 2*x23) + x39*(-x0*(-x36 + x37) + x35)) + x30*x34*x42 - x30*(x10 + 2*x8) + x34*x38 - x40*x41)/sqrt(x6)

def phi_dY3_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x1 + x2**2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = Y3 - Y4
    x10 = -X4
    x11 = X3 + x10
    x12 = x0*x9 - x11*x2
    x13 = Z1 - Z2
    x14 = -x0*x13 + x3*x6
    x15 = -Z4
    x16 = Z3 + x15
    x17 = x0*x16 - x11*x3
    x18 = -x13*x2 + x3*x7
    x19 = x16*x2 - x3*x9
    x20 = x12*x8 + x14*x17 + x18*x19
    x21 = 1/x5
    x22 = x19*x8
    x23 = x12*x18
    x24 = x0*(-x12*x14 + x17*x8) + x2*(x22 - x23) + x3*(x14*x19 - x17*x18)
    x25 = 1/(x20**2 + x21*x24**2)
    x26 = Z2 + x15
    x27 = X2 + x10
    x28 = x12*x6 - x13*x19 + x18*x26 - x27*x8
    x29 = x0*x18
    x30 = x3*x8
    x31 = x1*x14 + x14*x4 + x2*(x29 + x30)
    x32 = x2*x21
    x33 = x0*x8 - x18*x3
    x34 = -x0*(x14*x27 + x17*x6) - x2*(x12*x13 + x18*x27 + x19*x6 + x26*x8) - x22 + x23 + x24*x32 - x3*(x13*x17 + x14*x26)
    x35 = 2*x25*(x20*x33 - x21*x24*x31)
    return x25*(-x20*x34*x35 - x20*(-x14*x2 - x29 - x30 + x31*x32) - x24*x28*x35 + x24*(x0*x6 + x13*x3) - x28*x31 + x33*x34)/sqrt(x5)

def phi_dY3_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = -X2
    x8 = X1 + x7
    x9 = x2*x8
    x10 = -Y2
    x11 = Y1 + x10
    x12 = -x0*x11
    x13 = x12 + x9
    x14 = Y3 - Y4
    x15 = -X4
    x16 = X3 + x15
    x17 = x0*x14 - x16*x2
    x18 = Z1 - Z2
    x19 = -x0*x18 + x4*x8
    x20 = -Z4
    x21 = Z3 + x20
    x22 = x0*x21 - x16*x4
    x23 = x11*x4
    x24 = x18*x2
    x25 = x23 - x24
    x26 = -x14*x4 + x2*x21
    x27 = x13*x17 + x19*x22 + x25*x26
    x28 = 1/x6
    x29 = x13*x26
    x30 = x17*x25
    x31 = x0*(x13*x22 - x17*x19) + x2*(x29 - x30) + x4*(x19*x26 - x22*x25)
    x32 = 1/(x27**2 + x28*x31**2)
    x33 = Z2 + x20
    x34 = X2 + x15
    x35 = -x13*x34 + x17*x8 - x18*x26 + x25*x33
    x36 = x1*x13 + x13*x3
    x37 = x2*x28
    x38 = x36 + x4*(-x19*(Y3 + x10) + x25*(X3 + x7))
    x39 = x0*x19 + x2*x25
    x40 = -x0*(x19*x34 + x22*x8) - x2*(x13*x33 + x17*x18 + x25*x34 + x26*x8) - x29 + x30 + x31*x37 - x4*(x18*x22 + x19*x33)
    x41 = 2*x32*(x27*x39 + x28*x31*x38)
    return x32*(-x27*x40*x41 + x27*(-x1*x8 - x13*x2 - x2*(x12 + 2*x9) + x37*x38 - x5*x8) - x31*x35*x41 + x31*(x23 - 2*x24) + x35*(x36 - x4*(x0*x25 - x19*x2)) + x39*x40)/sqrt(x6)

def phi_dZ3_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x1*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = -X4
    x12 = X3 + x11
    x13 = x0*x10 - x1*x12
    x14 = Z1 - Z2
    x15 = -x0*x14 + x3*x6
    x16 = Z3 - Z4
    x17 = x0*x16
    x18 = x12*x3
    x19 = x17 - x18
    x20 = -x1*x14 + x3*x7
    x21 = x1*x16
    x22 = x10*x3
    x23 = x21 - x22
    x24 = x13*x8 + x15*x19 + x20*x23
    x25 = 1/x5
    x26 = x15*x23
    x27 = x19*x20
    x28 = x0*(-x13*x15 + x19*x8) + x1*(-x13*x20 + x23*x8) + x3*(x26 - x27)
    x29 = 1/(x24**2 + x25*x28**2)
    x30 = X2 + x11
    x31 = Y2 + x9
    x32 = -x15*x30 + x19*x6 - x20*x31 + x23*x7
    x33 = x0*(x1*x19 - x13*x3) + x2*x23 + x23*x4
    x34 = x25*x3
    x35 = x1*x13 + x19*x3
    x36 = -x0*(x13*(-X1 + X2) - x30*x8) - x1*(x13*(-Y1 + Y2) - x31*x8) - x26 + x27 + x28*x34 + x3*(x15*x31 + x19*x7 - x20*x30 - x23*x6)
    x37 = 2*x29*(x24*x35 + x25*x28*x33)
    return x29*(x24*x36*x37 - x24*(x0*(x1*x30 + x13) + x2*x31 - x23*x3 + x3*(-x21 + x22 + x3*x31) + x33*x34) + x28*x32*x37 + x28*(-x17 + x18 + x3*x30) - x32*x33 - x35*x36)/sqrt(x5)

def phi_dZ3_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x1 + x2**2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = -X4
    x12 = X3 + x11
    x13 = x0*x10 - x12*x2
    x14 = Z1 - Z2
    x15 = -x0*x14 + x3*x6
    x16 = Z3 - Z4
    x17 = x0*x16
    x18 = x12*x3
    x19 = x17 - x18
    x20 = -x14*x2 + x3*x7
    x21 = x16*x2
    x22 = x10*x3
    x23 = x21 - x22
    x24 = x13*x8 + x15*x19 + x20*x23
    x25 = 1/x5
    x26 = x15*x23
    x27 = x19*x20
    x28 = x0*(-x13*x15 + x19*x8) + x2*(-x13*x20 + x23*x8) + x3*(x26 - x27)
    x29 = 1/(x24**2 + x25*x28**2)
    x30 = X2 + x11
    x31 = Y2 + x9
    x32 = -x15*x30 + x19*x6 - x20*x31 + x23*x7
    x33 = x1*x19 + x19*x4 + x2*(x0*x23 + x13*x3)
    x34 = x25*x3
    x35 = x0*x13 - x23*x3
    x36 = -x0*(x13*(-X1 + X2) - x30*x8) - x2*(x13*(-Y1 + Y2) - x31*x8) - x26 + x27 + x28*x34 + x3*(x15*x31 + x19*x7 - x20*x30 - x23*x6)
    x37 = 2*x29*(x24*x35 + x25*x28*x33)
    return x29*(-x24*x36*x37 + x24*(x1*x30 - x19*x3 - x2*(-x0*x31 + x13) + x3*(-x17 + x18 + x3*x30) + x33*x34) - x28*x32*x37 + x28*(-x21 + x22 + x3*x31) + x32*x33 + x35*x36)/sqrt(x5)

def phi_dZ3_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x1 + x3 + x4**2
    x6 = -X2
    x7 = X1 + x6
    x8 = -Y2
    x9 = Y1 + x8
    x10 = -x0*x9 + x2*x7
    x11 = -Y4
    x12 = Y3 + x11
    x13 = -X4
    x14 = X3 + x13
    x15 = x0*x12 - x14*x2
    x16 = Z1 - Z2
    x17 = -x0*x16 + x4*x7
    x18 = Z3 - Z4
    x19 = x0*x18 - x14*x4
    x20 = -x16*x2 + x4*x9
    x21 = -x12*x4 + x18*x2
    x22 = x10*x15 + x17*x19 + x20*x21
    x23 = 1/x5
    x24 = x17*x21
    x25 = x19*x20
    x26 = x0*(x10*x19 - x15*x17) + x2*(x10*x21 - x15*x20) + x4*(x24 - x25)
    x27 = 1/(x22**2 + x23*x26**2)
    x28 = X2 + x13
    x29 = Y2 + x11
    x30 = -x17*x28 + x19*x7 - x20*x29 + x21*x9
    x31 = -x0*x21 + x19*x2
    x32 = x23*x4
    x33 = X3 + x6
    x34 = Y3 + x8
    x35 = x0*x15*x33 + x15*x2*x34 - x4*(-x19*x34 + x21*x33)
    x36 = x0*x19 + x2*x21
    x37 = -x0*(-x10*x28 + x15*(-X1 + X2)) - x2*(-x10*x29 + x15*(-Y1 + Y2)) - x24 + x25 + x26*x32 + x4*(x17*x29 + x19*x9 - x20*x28 - x21*x7)
    x38 = 2*x27*(x22*x36 + x23*x26*x35)
    return x27*(-x22*x37*x38 + x22*(x31 + x32*x35 - x4*(-x0*x29 + x2*x28)) - x26*x30*x38 - x26*(x0*x28 + x2*x29) - x30*(x1*x15 + x15*x3 + x31*x4) + x36*x37)/sqrt(x5)

def phi_dZ3_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = -Y3
    x2 = Y2 + x1
    x3 = -Z3
    x4 = Z2 + x3
    x5 = x0**2 + x2**2 + x4**2
    x6 = X1 - X2
    x7 = x2*x6
    x8 = Y1 - Y2
    x9 = x0*x8
    x10 = x7 - x9
    x11 = -Y4
    x12 = Y3 + x11
    x13 = -X4
    x14 = X3 + x13
    x15 = x0*x12 - x14*x2
    x16 = x4*x6
    x17 = Z1 - Z2
    x18 = x0*x17
    x19 = x16 - x18
    x20 = Z3 - Z4
    x21 = x0*x20
    x22 = x14*x4
    x23 = x21 - x22
    x24 = -x17*x2 + x4*x8
    x25 = x2*x20
    x26 = x12*x4
    x27 = x25 - x26
    x28 = x10*x15 + x19*x23 + x24*x27
    x29 = 1/x5
    x30 = x10*x23
    x31 = x15*x19
    x32 = x30 - x31
    x33 = x19*x27
    x34 = x23*x24
    x35 = x0*x32 + x2*(x10*x27 - x15*x24) + x4*(x33 - x34)
    x36 = x35**2
    x37 = 1/(x28**2 + x29*x36)
    x38 = X2 + x13
    x39 = Z1 + x3
    x40 = x0*x29
    x41 = Y2 + x11
    x42 = -x19*x38 + x23*x6 - x24*x41 + x27*x8
    x43 = x35*x42
    x44 = Y1 + x1
    x45 = x23*x44
    x46 = x12*x19
    x47 = x15*x39
    x48 = x10*x20
    x49 = x2*(x12*x24 + x27*x44)
    x50 = x27*x39
    x51 = x20*x24
    x52 = x4*(x50 + x51)
    x53 = -x30 + x31 + x49 + x52
    x54 = -x10*x12 + x15*x44 - x19*x20 + x23*x39
    x55 = -X1 + X2
    x56 = -x10*x38
    x57 = -Y1
    x58 = Y2 + x57
    x59 = -x0*(x15*x55 + x56) - x2*(-x10*x41 + x15*x58) - x33 + x34 + x4*(x19*x41 + x23*x8 - x24*x38 - x27*x6)
    x60 = x29*x35*x4 + x59
    x61 = Y3 + x57
    x62 = x0/x5**2
    x63 = x0*(-x45 - x46 + x47 + x48)
    x64 = 2*x37*(x28*x54 + x29*x35*(x53 - x63) + x36*x62)
    return x37*(-x28*x60*x64 + x28*(x0*(x12*x55 + x15 - x38*x61 - x7 + x9) - x15*x6 + x2*(x12*x58 - x41*x61) - x29*x4*(x32 - x49 - x52 + x63) + 3*x35*x4*x62 + x4*(x20*x58 + x24 - x25 + x26 - x41*(-Z1 + Z3)) + x40*x59 - x50 - x51 + x56) - x35*(-x16 + x18 + x20*x6 - x21 + x22 + x38*x39) + x40*x43 + x42*(x0*(x45 + x46 - x47 - x48) + x53) - x43*x64 + x54*x60)/sqrt(x5)

def phi_dZ3_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = Y2 - Y3
    x3 = -Z3
    x4 = Z2 + x3
    x5 = x1**2 + x2**2 + x4**2
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x1*x7 + x2*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = x1*x10
    x12 = -X4
    x13 = X3 + x12
    x14 = x13*x2
    x15 = x11 - x14
    x16 = Z1 - Z2
    x17 = -x1*x16 + x4*x6
    x18 = Z3 - Z4
    x19 = x1*x18
    x20 = x13*x4
    x21 = x19 - x20
    x22 = x4*x7
    x23 = x16*x2
    x24 = x22 - x23
    x25 = x18*x2
    x26 = x10*x4
    x27 = x25 - x26
    x28 = x15*x8 + x17*x21 + x24*x27
    x29 = 1/x5
    x30 = x27*x8
    x31 = -x15*x24
    x32 = x17*x27
    x33 = x21*x24
    x34 = x1*(-x15*x17 + x21*x8) + x2*(x30 + x31) + x4*(x32 - x33)
    x35 = x34**2
    x36 = 1/(x28**2 + x29*x35)
    x37 = Y2 + x9
    x38 = Z1 + x3
    x39 = x2*x29
    x40 = X2 + x12
    x41 = -x17*x40 + x21*x6 - x24*x37 + x27*x7
    x42 = x34*x41
    x43 = x17*x18
    x44 = x21*x38 + x43
    x45 = X1 + x0
    x46 = x1*(x13*x17 + x21*x45) + x2*(x13*x24 + x15*x38 + x18*x8 + x27*x45) + x30 + x31
    x47 = x4*x44 + x46
    x48 = -x13*x8 + x15*x45 + x18*x24 - x27*x38
    x49 = -X1 + X2
    x50 = -x37*x8
    x51 = -x1*(x15*x49 - x40*x8) - x2*(x15*(-Y1 + Y2) + x50) - x32 + x33 + x4*(x17*x37 + x21*x7 - x24*x40 - x27*x6)
    x52 = x29*x34*x4 + x51
    x53 = x2/x5**2
    x54 = 2*x36*(x28*x48 + x29*x34*x47 - x35*x53)
    return x36*(x28*x52*x54 + x28*(x1*(-x40*x45 + x49*(X4 + x0)) - x15*x7 - x2*(-x11 - x13*x7 + x14 + x37*x45 + x8) - x29*x4*(-x4*(x21*(-Z1 + Z3) - x43) + x46) + 3*x34*x4*x53 + x39*x51 - x4*(x17 - x18*x6 - x19 + x20 + x38*x40) + x44 + x50) - x34*(x18*x7 - x22 + x23 - x25 + x26 + x37*x38) + x39*x42 - x41*x47 + x42*x54 - x48*x52)/sqrt(x5)

def phi_dZ3_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1**2 + x3**2 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x3*x7
    x10 = -Y4
    x11 = Y3 + x10
    x12 = -X4
    x13 = X3 + x12
    x14 = x1*x11 - x13*x3
    x15 = Z1 - Z2
    x16 = -x1*x15 + x4*x7
    x17 = Z3 - Z4
    x18 = x1*x17 - x13*x4
    x19 = -x15*x3 + x4*x8
    x20 = -x11*x4 + x17*x3
    x21 = x14*x9 + x16*x18 + x19*x20
    x22 = 1/x6
    x23 = x16*x20
    x24 = x18*x19
    x25 = x23 - x24
    x26 = x1*(-x14*x16 + x18*x9) + x25*x4 + x3*(-x14*x19 + x20*x9)
    x27 = x26**2
    x28 = 1/(x21**2 + x22*x27)
    x29 = X1 + x0
    x30 = X2 + x12
    x31 = Y1 + x2
    x32 = Y2 + x10
    x33 = -x16*x30 + x18*x7 - x19*x32 + x20*x8
    x34 = x22*x26
    x35 = x34*x4
    x36 = x14*x29
    x37 = x14*x31
    x38 = -x23
    x39 = x20*x29
    x40 = x13*x19
    x41 = x18*x31
    x42 = x11*x16
    x43 = x24 + x38 - x4*(x39 + x40 - x41 - x42)
    x44 = -x11*x19 - x13*x16 + x18*x29 + x20*x31
    x45 = x1*(x14*(-X1 + X2) - x30*x9)
    x46 = x3*(x14*(-Y1 + Y2) - x32*x9)
    x47 = x16*x32 + x18*x8 - x19*x30 - x20*x7
    x48 = x4*x47
    x49 = x24 + x35 + x38 - x45 - x46 + x48
    x50 = x6**(-2)
    x51 = x22*x4
    x52 = x1*(x36 - x9*(X4 + x0)) + x3*(x37 - x9*(Y4 + x2)) + x43
    x53 = 2*x28*(x21*x44 - x27*x4*x50 - x34*x52)
    return x28*(x21*x49*x53 - x21*(-3*x26*x5*x50 + x34 - x39 + x4*(x11*x7 - x13*x8 + x29*x32 - x30*x31) - x40 + x41 + x42 + x47 - x51*x52 + x51*(x25 + x45 + x46 - x48)) + x26*x33*x53 + x26*(x11*x8 + x13*x7 + x29*x30 + x31*x32) + x33*x35 + x33*(x1*(x13*x9 + x36) + x3*(x11*x9 + x37) + x43) - x44*x49)/sqrt(x6)

def phi_dZ3_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = Z2 - Z3
    x3 = x0**2 + x1**2 + x2**2
    x4 = X1 - X2
    x5 = -Y2
    x6 = Y1 + x5
    x7 = -x0*x6 + x1*x4
    x8 = -Y4
    x9 = Y3 + x8
    x10 = -X4
    x11 = X3 + x10
    x12 = x0*x9 - x1*x11
    x13 = -Z2
    x14 = Z1 + x13
    x15 = -x0*x14 + x2*x4
    x16 = -Z4
    x17 = Z3 + x16
    x18 = x0*x17 - x11*x2
    x19 = -x1*x14 + x2*x6
    x20 = x1*x17 - x2*x9
    x21 = x12*x7 + x15*x18 + x19*x20
    x22 = 1/x3
    x23 = x18*x7
    x24 = x12*x15
    x25 = x15*x20
    x26 = x18*x19
    x27 = x25 - x26
    x28 = x0*(x23 - x24) + x1*(-x12*x19 + x20*x7) + x2*x27
    x29 = x28**2
    x30 = 1/(x21**2 + x22*x29)
    x31 = Z2 + x16
    x32 = X2 + x10
    x33 = x0*x22
    x34 = x20*x6
    x35 = Y2 + x8
    x36 = x19*x35
    x37 = -x15*x32 + x18*x4 + x34 - x36
    x38 = x28*x37
    x39 = x14*x20 + x19*x31
    x40 = x18*x6
    x41 = x15*x35
    x42 = x40 + x41
    x43 = x0*(-x12*x14 - x31*x7 + x42) + x1*(x34 + x36) + x2*x39 - x23 + x24
    x44 = x12*x6
    x45 = x35*x7
    x46 = -x45
    x47 = x14*x18 - x15*x31 + x44 + x46
    x48 = x12*x4
    x49 = x32*x7
    x50 = x20*x4
    x51 = x19*x32
    x52 = x0*(x48 + x49) + x1*(x44 + x45) + x2*x22*x28 - x2*(-x40 - x41 + x50 + x51) - x25 + x26
    x53 = -X1 + X2
    x54 = Y4 + x5
    x55 = -Y1 + Y2
    x56 = x0/x3**2
    x57 = x22*x43
    x58 = 2*x30*(x21*x47 + x28*x57 + x29*x56)
    return x30*(x21*x52*x58 + x21*(x0*(-x32*x6 + x53*x54) + x1*(-x35*x6 + x54*x55) - 3*x2*x28*x56 - x2*x57 + x2*(-x14*x35 + x55*(Z4 + x13)) + x33*(x0*(x12*x53 - x49) + x1*(x12*x55 + x46) - x2*(x42 - x50 - x51) + x27) + x39 + x48 + x49) + x28*(x14*x32 + x31*x4) - x33*x38 - x37*x43 + x38*x58 - x47*x52)/sqrt(x3)

def phi_dZ3_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = Z2 - Z3
    x3 = x0**2 + x1**2 + x2**2
    x4 = X1 - X2
    x5 = Y1 - Y2
    x6 = -x0*x5 + x1*x4
    x7 = -Y4
    x8 = Y3 + x7
    x9 = -X4
    x10 = X3 + x9
    x11 = x0*x8 - x1*x10
    x12 = -Z2
    x13 = Z1 + x12
    x14 = -x0*x13 + x2*x4
    x15 = -Z4
    x16 = Z3 + x15
    x17 = x0*x16 - x10*x2
    x18 = -x1*x13 + x2*x5
    x19 = x1*x16 - x2*x8
    x20 = x11*x6 + x14*x17 + x18*x19
    x21 = 1/x3
    x22 = x19*x6
    x23 = -x11*x18
    x24 = x14*x19
    x25 = x17*x18
    x26 = x24 - x25
    x27 = x0*(-x11*x14 + x17*x6) + x1*(x22 + x23) + x2*x26
    x28 = x27**2
    x29 = 1/(x20**2 + x21*x28)
    x30 = Z2 + x15
    x31 = Y2 + x7
    x32 = x1*x21
    x33 = x17*x4
    x34 = X2 + x9
    x35 = x14*x34
    x36 = -x18*x31 + x19*x5 + x33 - x35
    x37 = x27*x36
    x38 = x13*x17
    x39 = x14*x30
    x40 = x19*x4
    x41 = x18*x34
    x42 = x40 + x41
    x43 = x0*(x33 + x35) + x1*(x11*x13 + x30*x6 + x42) + x22 + x23
    x44 = x11*x4
    x45 = x34*x6
    x46 = -x45
    x47 = -x13*x19 + x18*x30 + x44 + x46
    x48 = x31*x6
    x49 = x11*x5 + x48
    x50 = x17*x5
    x51 = x14*x31
    x52 = x0*(x44 + x45) + x1*x49 + x2*x21*x27 - x2*(x42 - x50 - x51) - x24 + x25
    x53 = x1/x3**2
    x54 = x21*(x2*(-x14*(Z4 + x12) + x38) + x43)
    x55 = 2*x29*(x20*x47 + x27*x54 - x28*x53)
    return x29*(-x20*x52*x55 + x20*(x1*(x31*x4 - x34*x5) - 3*x2*x27*x53 + x2*x54 - x2*(-x13*x34 + x30*x4) + x32*(x0*(x11*(-X1 + X2) + x46) + x1*(x11*(-Y1 + Y2) - x48) - x2*(-x40 - x41 + x50 + x51) + x26) - x38 - x39 + x49) + x27*(x13*x31 + x30*x5) - x32*x37 + x36*(x2*(x38 + x39) + x43) - x37*x55 + x47*x52)/sqrt(x3)

def phi_dZ3_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = Z2 - Z3
    x3 = x2**2
    x4 = x0**2 + x1**2 + x3
    x5 = X1 - X2
    x6 = Y1 - Y2
    x7 = -x0*x6 + x1*x5
    x8 = -Y4
    x9 = Y3 + x8
    x10 = -X4
    x11 = X3 + x10
    x12 = x0*x9 - x1*x11
    x13 = Z1 - Z2
    x14 = -x0*x13 + x2*x5
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x2
    x17 = -x1*x13 + x2*x6
    x18 = x1*x15 - x2*x9
    x19 = x12*x7 + x14*x16 + x17*x18
    x20 = 1/x4
    x21 = -x12*x14 + x16*x7
    x22 = -x12*x17 + x18*x7
    x23 = x14*x18
    x24 = x16*x17
    x25 = x23 - x24
    x26 = x0*x21 + x1*x22 + x2*x25
    x27 = x26**2
    x28 = 1/(x19**2 + x20*x27)
    x29 = X2 + x10
    x30 = Y2 + x8
    x31 = 2*x0*x21 + 2*x1*x22 + 2*x2*x25
    x32 = -x14*x29 + x16*x5 - x17*x30 + x18*x6
    x33 = x20*x26
    x34 = x2*x33
    x35 = x29*x7
    x36 = x30*x7
    x37 = x18*x5
    x38 = x17*x29
    x39 = x16*x6
    x40 = x14*x30
    x41 = x0*(x12*(-X1 + X2) - x35)
    x42 = x1*(x12*(-Y1 + Y2) - x36)
    x43 = x2*(-x37 - x38 + x39 + x40)
    x44 = -x23 + x24 + x34 - x41 - x42 + x43
    x45 = 2*Z2 - 2*Z3
    x46 = x4**(-2)
    x47 = x25 + x41 + x42 - x43
    x48 = x28*(-x19*x32 + x2*x27*x46 - x33*x47)
    return x28*(2*x19*x44*x48 - x19*(-x20*x45*x47 + 3*x26*x3*x46 - x33 + 2*x37 + 2*x38 - 2*x39 - 2*x40 - x45*(-x29*x6 + x30*x5)) + x31*x32*x48 - x31*(x29*x5 + x30*x6) - x32*x34 + x32*x44 + x32*(-x0*(x12*x5 + x35) - x1*(x12*x6 + x36) + x2*(x37 + x38 - x39 - x40) + x25))/sqrt(x4)

def phi_dZ3_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x1*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = -X4
    x12 = X3 + x11
    x13 = x0*x10 - x1*x12
    x14 = x3*x6
    x15 = Z1 - Z2
    x16 = -x0*x15
    x17 = x14 + x16
    x18 = Z3 - Z4
    x19 = x0*x18 - x12*x3
    x20 = x3*x7
    x21 = x1*x15
    x22 = x20 - x21
    x23 = x1*x18 - x10*x3
    x24 = x13*x8 + x17*x19 + x22*x23
    x25 = 1/x5
    x26 = x17*x23
    x27 = x19*x22
    x28 = x0*(-x13*x17 + x19*x8) + x1*(-x13*x22 + x23*x8) + x3*(x26 - x27)
    x29 = 1/(x24**2 + x25*x28**2)
    x30 = X2 + x11
    x31 = Y2 + x9
    x32 = -x17*x30 + x19*x6 - x22*x31 + x23*x7
    x33 = x2*x22 + x22*x4
    x34 = x1*x17
    x35 = x3*x8
    x36 = x0*(x34 - x35) + x33
    x37 = -X1 + X2
    x38 = -Y1 + Y2
    x39 = x25*x3
    x40 = x1*x8 + x17*x3
    x41 = -x0*(x13*x37 - x30*x8) - x1*(x13*x38 - x31*x8) - x26 + x27 + x28*x39 + x3*(x17*x31 + x19*x7 - x22*x30 - x23*x6)
    x42 = 2*x29*(x24*x40 - x25*x28*x36)
    return x29*(x24*x41*x42 + x24*(x0*(x1*x37 + x8) - x2*x7 - x22*x3 + x3*(-x20 + x21 + x3*x38) + x39*(-x0*(-x34 + x35) + x33)) + x28*x32*x42 - x28*(2*x14 + x16) + x32*x36 - x40*x41)/sqrt(x5)

def phi_dZ3_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x1 + x2**2 + x4
    x6 = -X2
    x7 = X1 + x6
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = -Y4
    x11 = Y3 + x10
    x12 = -X4
    x13 = X3 + x12
    x14 = x0*x11 - x13*x2
    x15 = x3*x7
    x16 = Z1 - Z2
    x17 = x0*x16
    x18 = x15 - x17
    x19 = Z3 - Z4
    x20 = x0*x19 - x13*x3
    x21 = x3*x8
    x22 = -x16*x2
    x23 = x21 + x22
    x24 = -x11*x3 + x19*x2
    x25 = x14*x9 + x18*x20 + x23*x24
    x26 = 1/x5
    x27 = x18*x24
    x28 = x20*x23
    x29 = x0*(-x14*x18 + x20*x9) + x2*(-x14*x23 + x24*x9) + x3*(x27 - x28)
    x30 = 1/(x25**2 + x26*x29**2)
    x31 = X2 + x12
    x32 = Y2 + x10
    x33 = -x18*x31 + x20*x7 - x23*x32 + x24*x8
    x34 = x1*x18 + x18*x4 + x2*(x0*x23 + x3*x9)
    x35 = -Y1 + Y2
    x36 = x26*x3
    x37 = x0*x9 - x23*x3
    x38 = -x0*(x14*(-X1 + X2) - x31*x9) - x2*(x14*x35 - x32*x9) - x27 + x28 + x29*x36 + x3*(x18*x32 + x20*x8 - x23*x31 - x24*x7)
    x39 = 2*x30*(-x25*x37 + x26*x29*x34)
    return x30*(x25*x38*x39 - x25*(-x1*x7 - x18*x3 - x2*(x35*(X3 + x6) + x9) + x3*(-2*x15 + x17) + x34*x36) + x29*x33*x39 - x29*(2*x21 + x22) - x33*x34 + x37*x38)/sqrt(x5)

def phi_dZ3_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x1 + x3 + x4**2
    x6 = -X2
    x7 = X1 + x6
    x8 = -Y2
    x9 = Y1 + x8
    x10 = -x0*x9 + x2*x7
    x11 = -Y4
    x12 = Y3 + x11
    x13 = -X4
    x14 = X3 + x13
    x15 = x0*x12 - x14*x2
    x16 = Z1 - Z2
    x17 = -x0*x16 + x4*x7
    x18 = Z3 - Z4
    x19 = x0*x18 - x14*x4
    x20 = -x16*x2 + x4*x9
    x21 = -x12*x4 + x18*x2
    x22 = x10*x15 + x17*x19 + x20*x21
    x23 = 1/x5
    x24 = x17*x21
    x25 = x19*x20
    x26 = x0*(x10*x19 - x15*x17) + x2*(x10*x21 - x15*x20) + x4*(x24 - x25)
    x27 = 1/(x22**2 + x23*x26**2)
    x28 = X2 + x13
    x29 = Y2 + x11
    x30 = -x17*x28 + x19*x7 - x20*x29 + x21*x9
    x31 = x1*x10 + x10*x3
    x32 = x0*x20 - x17*x2
    x33 = x23*x4
    x34 = x31 + x4*(-x17*(Y3 + x8) + x20*(X3 + x6))
    x35 = x0*x17 + x2*x20
    x36 = x0*(x10*x28 + x15*x7) + x2*(x10*x29 + x15*x9) - x24 + x25 + x26*x33 - x4*(-x17*x29 - x19*x9 + x20*x28 + x21*x7)
    x37 = 2*x27*(x22*x35 + x23*x26*x34)
    return x27*(-x22*x36*x37 + x22*(-x10*x4 + x32 + x33*x34) - x26*x30*x37 + x26*(x0*x7 + x2*x9) + x30*(x31 - x32*x4) + x35*x36)/sqrt(x5)

def phi_dX4_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x2 + x4
    x6 = x0**2 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x1*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x0*x10 - x1*x11
    x13 = Z1 - Z2
    x14 = -x0*x13 + x3*x7
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x3
    x17 = -x1*x13 + x3*x8
    x18 = x1*x15 - x10*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x14 + x16*x9) + x1*(-x12*x17 + x18*x9) + x3*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x1*x9 + x14*x3
    x24 = x0*(x1*x16 - x12*x3) + x18*x2 + x18*x4
    x25 = x1*x12 + x16*x3
    x26 = x0*(x1*x14 - x3*x9) + x17*x2 + x17*x4
    x27 = 2*x22*(x19*x25 + x20*x21*x24)
    return x22*(-x19*x26*x27 - x21*x23*x27 + x21*x5 + x23*x24 + x25*x26)/sqrt(x6)

def phi_dX4_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X1 - X2
    x1 = Y2 - Y3
    x2 = X2 - X3
    x3 = Y1 - Y2
    x4 = x0*x1 - x2*x3
    x5 = Y3 - Y4
    x6 = X3 - X4
    x7 = -x1*x6 + x2*x5
    x8 = Z2 - Z3
    x9 = Z1 - Z2
    x10 = x0*x8 - x2*x9
    x11 = Z3 - Z4
    x12 = x11*x2 - x6*x8
    x13 = -x1*x9 + x3*x8
    x14 = x1*x11 - x5*x8
    x15 = x10*x12 + x13*x14 + x4*x7
    x16 = x2**2
    x17 = x1**2
    x18 = x8**2
    x19 = x16 + x17 + x18
    x20 = 1/x19
    x21 = x1*(-x13*x7 + x14*x4) + x2*(-x10*x7 + x12*x4) + x8*(x10*x14 - x12*x13)
    x22 = 1/(x15**2 + x20*x21**2)
    x23 = sqrt(x19)
    x24 = 1/x23
    x25 = x1*x4 + x10*x8
    x26 = x1*(x14*x2 + x7*x8) + x12*x16 + x12*x18
    x27 = -x14*x8 + x2*x7
    x28 = x13*x17 + x13*x18 + x2*(x1*x10 - x4*x8)
    x29 = 2*x22*(x15*x27 + x20*x21*x26)
    return x22*(-x1*x2*x21*x24 + x15*x23*x8 + x15*x24*x28*x29 + x21*x24*x25*x29 - x24*x25*x26 - x24*x27*x28)

def phi_dX4_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X2
    x1 = X1 + x0
    x2 = Y2 - Y3
    x3 = X2 - X3
    x4 = -Y2
    x5 = Y1 + x4
    x6 = x1*x2 - x3*x5
    x7 = Y3 - Y4
    x8 = X3 - X4
    x9 = -x2*x8 + x3*x7
    x10 = Z2 - Z3
    x11 = Z1 - Z2
    x12 = x1*x10 - x11*x3
    x13 = Z3 - Z4
    x14 = -x10*x8 + x13*x3
    x15 = x10*x5 - x11*x2
    x16 = -x10*x7 + x13*x2
    x17 = x12*x14 + x15*x16 + x6*x9
    x18 = x3**2
    x19 = x2**2
    x20 = x10**2
    x21 = x18 + x19 + x20
    x22 = 1/x21
    x23 = x10*(x12*x16 - x14*x15) + x2*(-x15*x9 + x16*x6) + x3*(-x12*x9 + x14*x6)
    x24 = 1/(x17**2 + x22*x23**2)
    x25 = sqrt(x21)
    x26 = 1/x25
    x27 = x10*x12 + x2*x6
    x28 = x14*x3 + x16*x2
    x29 = x15*x19 + x15*x20 + x3*(-x10*x6 + x12*x2)
    x30 = X3 + x0
    x31 = Y3 + x4
    x32 = 2*x24*(x17*x28 + x22*x23*(-x10*(-x14*x31 + x16*x30) + x2*x31*x9 + x3*x30*x9))
    return x24*(-x10*x23*x26*x3 - x17*x2*x25 + x17*x26*x29*x32 + x23*x26*x27*x32 + x26*x27*(x10*(x14*x2 - x16*x3) + x18*x9 + x19*x9) - x26*x28*x29)

def phi_dX4_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = -Y3
    x2 = Y2 + x1
    x3 = x2**2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x0**2 + x3 + x6
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x0*x9 + x2*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x0*x11 - x12*x2
    x14 = Z1 - Z2
    x15 = -x0*x14 + x5*x8
    x16 = Z3 - Z4
    x17 = x0*x16 - x12*x5
    x18 = -x14*x2 + x5*x9
    x19 = -x11*x5 + x16*x2
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x7
    x22 = x10*x17
    x23 = x13*x15
    x24 = x0*(x22 - x23) + x2*(x10*x19 - x13*x18) + x5*(x15*x19 - x17*x18)
    x25 = x24**2
    x26 = 1/(x20**2 + x21*x25)
    x27 = Y1 + x1
    x28 = Z1 + x4
    x29 = -x10*x5 + x15*x2
    x30 = -x10*x11 + x13*x27 - x15*x16 + x17*x28
    x31 = x0*x29 + x18*x3 + x18*x6
    x32 = x0*x21
    x33 = x20*x31
    x34 = x10*x2 + x15*x5
    x35 = x24*x34
    x36 = x17*x27
    x37 = x11*x15
    x38 = x13*x28
    x39 = x10*x16
    x40 = x2*(x11*x18 + x19*x27) - x22 + x23 + x5*(x16*x18 + x19*x28)
    x41 = 2*x26*(x0*x25/x7**2 + x20*x30 + x21*x24*(-x0*(-x36 - x37 + x38 + x39) + x40))
    return x26*(x20*(x0*(-x2*x28 + x27*x5) + x29) - x24*(x2*x27 + x28*x5) - x30*x31 - x32*x33 - x32*x35 + x33*x41 - x34*(x0*(x36 + x37 - x38 - x39) + x40) + x35*x41)/sqrt(x7)

def phi_dX4_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x1**2 + x3 + x6
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x1*x9 + x2*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x1*x11 - x12*x2
    x14 = x5*x8
    x15 = Z1 - Z2
    x16 = x1*x15
    x17 = x14 - x16
    x18 = Z3 - Z4
    x19 = x1*x18 - x12*x5
    x20 = -x15*x2 + x5*x9
    x21 = -x11*x5 + x18*x2
    x22 = x10*x13 + x17*x19 + x20*x21
    x23 = 1/x7
    x24 = x10*x21 - x13*x20
    x25 = x1*(x10*x19 - x13*x17) + x2*x24 + x5*(x17*x21 - x19*x20)
    x26 = x25**2
    x27 = 1/(x22**2 + x23*x26)
    x28 = Z1 + x4
    x29 = X1 + x0
    x30 = -x10*x12 + x13*x29 + x18*x20 - x21*x28
    x31 = x1*(-x10*x5 + x17*x2) + x20*x3 + x20*x6
    x32 = x2*x23
    x33 = x22*x31
    x34 = x10*x2 + x17*x5
    x35 = x25*x34
    x36 = x1*(x12*x17 + x19*x29) + x2*(x10*x18 + x12*x20 + x13*x28 + x21*x29) + x24 + x5*(x17*x18 + x19*x28)
    x37 = 2*x27*(-x2*x26/x7**2 + x22*x30 + x23*x25*x36)
    return x27*(-x22*(x1*(-x14 + x16 + x29*x5) - 2*x2*x20 + x28*x3 + x28*x6) + x25*(x10 + x2*x29) + x30*x31 - x32*x33 - x32*x35 - x33*x37 + x34*x36 - x35*x37)/sqrt(x7)

def phi_dX4_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = -Y3
    x3 = Y2 + x2
    x4 = x3**2
    x5 = Z2 - Z3
    x6 = x5**2
    x7 = x1**2 + x4 + x6
    x8 = X1 - X2
    x9 = x3*x8
    x10 = Y1 - Y2
    x11 = x1*x10
    x12 = -x11 + x9
    x13 = Y3 - Y4
    x14 = X3 - X4
    x15 = x1*x13 - x14*x3
    x16 = Z1 - Z2
    x17 = -x1*x16 + x5*x8
    x18 = Z3 - Z4
    x19 = x1*x18 - x14*x5
    x20 = x10*x5 - x16*x3
    x21 = -x13*x5 + x18*x3
    x22 = x12*x15 + x17*x19 + x20*x21
    x23 = 1/x7
    x24 = x17*x21
    x25 = x19*x20
    x26 = x1*(x12*x19 - x15*x17) + x3*(x12*x21 - x15*x20) + x5*(x24 - x25)
    x27 = x26**2
    x28 = 1/(x22**2 + x23*x27)
    x29 = Y1 + x2
    x30 = X1 + x0
    x31 = -x13*x20 - x14*x17 + x19*x30 + x21*x29
    x32 = x1*(-x12*x5 + x17*x3) + x20*x4 + x20*x6
    x33 = x23*x5
    x34 = x22*x32
    x35 = x12*x3 + x17*x5
    x36 = x26*x35
    x37 = x15*x30
    x38 = x15*x29
    x39 = -x24 + x25 - x5*(-x13*x17 + x14*x20 - x19*x29 + x21*x30)
    x40 = 2*x28*(x22*x31 - x23*x26*(x1*(-x12*(X4 + x0) + x37) + x3*(-x12*(Y4 + x2) + x38) + x39) - x27*x5/x7**2)
    return x28*(x22*(x1*(x11 + x3*x30 - x9) + 2*x20*x5 + x29*x4 + x29*x6) + x26*(x17 + x30*x5) + x31*x32 - x33*x34 - x33*x36 - x34*x40 - x35*(x1*(x12*x14 + x37) + x3*(x12*x13 + x38) + x39) - x36*x40)/sqrt(x7)

def phi_dX4_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x1*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = X3 - X4
    x12 = x0*x10 - x1*x11
    x13 = Z1 - Z2
    x14 = -x0*x13 + x3*x6
    x15 = -Z4
    x16 = Z3 + x15
    x17 = x0*x16 - x11*x3
    x18 = -x1*x13 + x3*x7
    x19 = x1*x16 - x10*x3
    x20 = x12*x8 + x14*x17 + x18*x19
    x21 = 1/x5
    x22 = x17*x8
    x23 = x12*x14
    x24 = x0*(x22 - x23) + x1*(-x12*x18 + x19*x8) + x3*(x14*x19 - x17*x18)
    x25 = x24**2
    x26 = 1/(x20**2 + x21*x25)
    x27 = x1*x14 - x3*x8
    x28 = Y2 + x9
    x29 = Z2 + x15
    x30 = x12*x7 + x13*x17 - x14*x29 - x28*x8
    x31 = x0*x27 + x18*x2 + x18*x4
    x32 = x0*x21
    x33 = x20*x31
    x34 = x1*x8 + x14*x3
    x35 = x24*x34
    x36 = x0*(-x12*x13 + x14*x28 + x17*x7 - x29*x8) + x1*(x18*x28 + x19*x7) - x22 + x23 + x3*(x13*x19 + x18*x29)
    x37 = 2*x26*(x0*x25/x5**2 + x20*x30 + x21*x24*x36)
    return x26*(-x20*(x0*x18 + x27) + x24*(x1*x7 + x13*x3) + x30*x31 + x32*x33 + x32*x35 - x33*x37 + x34*x36 - x35*x37)/sqrt(x5)

def phi_dX4_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = x2*x7
    x9 = Y1 - Y2
    x10 = -x0*x9
    x11 = x10 + x8
    x12 = Y3 - Y4
    x13 = -X4
    x14 = X3 + x13
    x15 = x0*x12 - x14*x2
    x16 = -Z2
    x17 = Z1 + x16
    x18 = -x0*x17 + x4*x7
    x19 = -Z4
    x20 = Z3 + x19
    x21 = x0*x20 - x14*x4
    x22 = -x17*x2 + x4*x9
    x23 = -x12*x4 + x2*x20
    x24 = x11*x15 + x18*x21 + x22*x23
    x25 = 1/x6
    x26 = x11*x23
    x27 = -x15*x22
    x28 = x0*(x11*x21 - x15*x18) + x2*(x26 + x27) + x4*(x18*x23 - x21*x22)
    x29 = x28**2
    x30 = 1/(x24**2 + x25*x29)
    x31 = Z2 + x19
    x32 = X2 + x13
    x33 = -x11*x32 + x15*x7 - x17*x23 + x22*x31
    x34 = x0*(-x11*x4 + x18*x2) + x22*x3 + x22*x5
    x35 = x2*x25
    x36 = x24*x34
    x37 = x11*x2 + x18*x4
    x38 = x28*x37
    x39 = x17*x21
    x40 = x0*(x18*x32 + x21*x7) + x2*(x11*x31 + x15*x17 + x22*x32 + x23*x7) + x26 + x27
    x41 = 2*x30*(x2*x29/x6**2 - x24*x33 - x25*x28*(x4*(-x18*(Z4 + x16) + x39) + x40))
    return x30*(x24*(x1*x17 + x17*x3 + x17*x5 - 2*x2*x22) - x28*(x10 + 2*x8) - x33*x34 + x35*x36 + x35*x38 - x36*x41 - x37*(x4*(x18*x31 + x39) + x40) - x38*x41)/sqrt(x6)

def phi_dX4_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x1*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = -X4
    x12 = X3 + x11
    x13 = x0*x10 - x1*x12
    x14 = x3*x6
    x15 = Z1 - Z2
    x16 = -x0*x15
    x17 = x14 + x16
    x18 = Z3 - Z4
    x19 = x0*x18 - x12*x3
    x20 = -x1*x15 + x3*x7
    x21 = x1*x18 - x10*x3
    x22 = x13*x8 + x17*x19 + x20*x21
    x23 = 1/x5
    x24 = x17*x21 - x19*x20
    x25 = x0*(-x13*x17 + x19*x8) + x1*(-x13*x20 + x21*x8) + x24*x3
    x26 = x25**2
    x27 = 1/(x22**2 + x23*x26)
    x28 = -X1 + X2
    x29 = X2 + x11
    x30 = Y2 + x9
    x31 = -x17*x29 + x19*x6 - x20*x30 + x21*x7
    x32 = x0*(x1*x17 - x3*x8) + x2*x20 + x20*x4
    x33 = x23*x3
    x34 = x22*x32
    x35 = x1*x8 + x17*x3
    x36 = x25*x35
    x37 = x29*x8
    x38 = x30*x8
    x39 = x21*x6
    x40 = x20*x29
    x41 = x19*x7
    x42 = x17*x30
    x43 = 2*x27*(-x22*x31 - x23*x25*(x0*(x13*x28 - x37) + x1*(x13*(-Y1 + Y2) - x38) + x24 - x3*(-x39 - x40 + x41 + x42)) + x26*x3/x5**2)
    return x27*(-x22*(-x0*(x1*x28 + x8) + x2*x7 + 2*x20*x3 + x4*x7) - x25*(2*x14 + x16) - x31*x32 + x33*x34 + x33*x36 - x34*x43 - x35*(-x0*(x13*x6 + x37) - x1*(x13*x7 + x38) + x24 + x3*(x39 + x40 - x41 - x42)) - x36*x43)/sqrt(x5)

def phi_dX4_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = Y2 - Y3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x0**2 + x2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x1*x6
    x9 = Y3 - Y4
    x10 = X3 - X4
    x11 = x0*x9 - x1*x10
    x12 = Z1 - Z2
    x13 = -x0*x12 + x3*x6
    x14 = Z3 - Z4
    x15 = x0*x14 - x10*x3
    x16 = -x1*x12 + x3*x7
    x17 = x1*x14 - x3*x9
    x18 = x11*x8 + x13*x15 + x16*x17
    x19 = 1/x5
    x20 = x0*(-x11*x13 + x15*x8) + x1*(-x11*x16 + x17*x8) + x3*(x13*x17 - x15*x16)
    x21 = x0*(x1*x13 - x3*x8) + x16*x2 + x16*x4
    x22 = x1*x8 + x13*x3
    return -2*(x18*x21 + x20*x22)*(x18*x22 - x19*x20*x21)/(sqrt(x5)*(x18**2 + x19*x20**2)**2)

def phi_dX4_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x0*x10 - x11*x2
    x13 = Z1 - Z2
    x14 = -x0*x13 + x4*x7
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x4
    x17 = -x13*x2 + x4*x8
    x18 = -x10*x4 + x15*x2
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x14 + x16*x9) + x2*(-x12*x17 + x18*x9) + x4*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x14*x4 + x2*x9
    x24 = x4*x9
    x25 = x1*x14 + x14*x5 + x2*(x0*x17 + x24)
    x26 = x0*x9 - x17*x4
    x27 = x0*(x14*x2 - x24) + x17*x3 + x17*x5
    x28 = 2*x22*(-x19*x26 + x20*x21*x25)
    return x22*(-x19*x27*x28 - x21*x23*x28 + x23*x25 - x26*x27)/sqrt(x6)

def phi_dX4_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = -X2
    x8 = X1 + x7
    x9 = -Y2
    x10 = Y1 + x9
    x11 = -x0*x10 + x2*x8
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x0*x12 - x13*x2
    x15 = Z1 - Z2
    x16 = -x0*x15 + x4*x8
    x17 = Z3 - Z4
    x18 = x0*x17 - x13*x4
    x19 = x10*x4 - x15*x2
    x20 = -x12*x4 + x17*x2
    x21 = x11*x14 + x16*x18 + x19*x20
    x22 = 1/x6
    x23 = x0*(x11*x18 - x14*x16) + x2*(x11*x20 - x14*x19) + x4*(x16*x20 - x18*x19)
    x24 = 1/(x21**2 + x22*x23**2)
    x25 = x0*x16 + x19*x2
    x26 = x16*x2
    x27 = x0*(-x11*x4 + x26) + x19*x3 + x19*x5
    x28 = x11*x2 + x16*x4
    x29 = x1*x11 + x11*x3
    x30 = 2*x24*(x21*x25 + x22*x23*(x29 + x4*(-x16*(Y3 + x9) + x19*(X3 + x7))))
    return x24*(x21*x27*x30 + x23*x28*x30 - x25*x27 - x28*(x29 + x4*(-x0*x19 + x26)))/sqrt(x6)

def phi_dY4_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X1 - X2
    x1 = Y2 - Y3
    x2 = X2 - X3
    x3 = Y1 - Y2
    x4 = x0*x1 - x2*x3
    x5 = Y3 - Y4
    x6 = X3 - X4
    x7 = -x1*x6 + x2*x5
    x8 = Z2 - Z3
    x9 = Z1 - Z2
    x10 = x0*x8 - x2*x9
    x11 = Z3 - Z4
    x12 = x11*x2 - x6*x8
    x13 = -x1*x9 + x3*x8
    x14 = x1*x11 - x5*x8
    x15 = x10*x12 + x13*x14 + x4*x7
    x16 = x2**2
    x17 = x1**2
    x18 = x8**2
    x19 = x16 + x17 + x18
    x20 = 1/x19
    x21 = x1*(-x13*x7 + x14*x4) + x2*(-x10*x7 + x12*x4) + x8*(x10*x14 - x12*x13)
    x22 = 1/(x15**2 + x20*x21**2)
    x23 = sqrt(x19)
    x24 = x1*x7 + x12*x8
    x25 = 1/x23
    x26 = x1*(x13*x2 + x4*x8) + x10*x16 + x10*x18
    x27 = -x13*x8 + x2*x4
    x28 = x14*x17 + x14*x18 + x2*(x1*x12 - x7*x8)
    x29 = 2*x22*(x15*x24 + x20*x21*x28)
    return x22*(-x1*x2*x21*x25 - x15*x23*x8 + x15*x25*x26*x29 + x21*x25*x27*x29 - x24*x25*x26 - x25*x27*x28)

def phi_dY4_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = Y2 - Y3
    x1 = X2 - X3
    x2 = x1**2
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x2 + x4
    x6 = x0**2 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = x0*x7 - x1*x8
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = -x0*x11 + x1*x10
    x13 = Z1 - Z2
    x14 = -x1*x13 + x3*x7
    x15 = Z3 - Z4
    x16 = x1*x15 - x11*x3
    x17 = -x0*x13 + x3*x8
    x18 = x0*x15 - x10*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x17 + x18*x9) + x1*(-x12*x14 + x16*x9) + x3*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x1*x9 - x17*x3
    x24 = x0*(x1*x18 + x12*x3) + x16*x2 + x16*x4
    x25 = x1*x12 - x18*x3
    x26 = x0*(x1*x17 + x3*x9) + x14*x2 + x14*x4
    x27 = 2*x22*(x19*x25 + x20*x21*x24)
    return x22*(-x19*x26*x27 - x21*x23*x27 + x21*x5 + x23*x24 + x25*x26)/sqrt(x6)

def phi_dY4_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X2
    x1 = X1 + x0
    x2 = Y2 - Y3
    x3 = X2 - X3
    x4 = -Y2
    x5 = Y1 + x4
    x6 = x1*x2 - x3*x5
    x7 = Y3 - Y4
    x8 = X3 - X4
    x9 = -x2*x8 + x3*x7
    x10 = Z2 - Z3
    x11 = Z1 - Z2
    x12 = x1*x10 - x11*x3
    x13 = Z3 - Z4
    x14 = -x10*x8 + x13*x3
    x15 = x10*x5 - x11*x2
    x16 = -x10*x7 + x13*x2
    x17 = x12*x14 + x15*x16 + x6*x9
    x18 = x3**2
    x19 = x2**2
    x20 = x10**2
    x21 = x18 + x19 + x20
    x22 = 1/x21
    x23 = x10*(x12*x16 - x14*x15) + x2*(-x15*x9 + x16*x6) + x3*(-x12*x9 + x14*x6)
    x24 = 1/(x17**2 + x22*x23**2)
    x25 = sqrt(x21)
    x26 = x14*x3 + x16*x2
    x27 = 1/x25
    x28 = x12*x18 + x12*x20 + x2*(x10*x6 + x15*x3)
    x29 = -x10*x15 + x3*x6
    x30 = X3 + x0
    x31 = Y3 + x4
    x32 = 2*x24*(x17*x26 + x22*x23*(-x10*(-x14*x31 + x16*x30) + x2*x31*x9 + x3*x30*x9))
    return x24*(-x10*x2*x23*x27 + x17*x25*x3 - x17*x27*x28*x32 - x23*x27*x29*x32 + x26*x27*x28 - x27*x29*(x10*(x14*x2 - x16*x3) + x18*x9 + x19*x9))

def phi_dY4_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = -Y3
    x3 = Y2 + x2
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x1 + x3**2 + x6
    x8 = X1 - X2
    x9 = x3*x8
    x10 = Y1 - Y2
    x11 = x0*x10
    x12 = -x11 + x9
    x13 = Y3 - Y4
    x14 = X3 - X4
    x15 = x0*x13 - x14*x3
    x16 = Z1 - Z2
    x17 = -x0*x16 + x5*x8
    x18 = Z3 - Z4
    x19 = x0*x18 - x14*x5
    x20 = x10*x5
    x21 = x16*x3
    x22 = x20 - x21
    x23 = -x13*x5 + x18*x3
    x24 = x12*x15 + x17*x19 + x22*x23
    x25 = 1/x7
    x26 = x12*x19
    x27 = x15*x17
    x28 = x0*(x26 - x27) + x3*(x12*x23 - x15*x22) + x5*(x17*x23 - x19*x22)
    x29 = x28**2
    x30 = 1/(x24**2 + x25*x29)
    x31 = Z1 + x4
    x32 = Y1 + x2
    x33 = -x12*x13 + x15*x32 - x17*x18 + x19*x31
    x34 = x1*x17 + x17*x6 + x3*(x0*x22 + x12*x5)
    x35 = x0*x25
    x36 = x24*x34
    x37 = x0*x12 - x22*x5
    x38 = x28*x37
    x39 = x19*x32
    x40 = x13*x17
    x41 = x15*x31
    x42 = x12*x18
    x43 = -x26 + x27 + x3*(x13*x22 + x23*x32) + x5*(x18*x22 + x23*x31)
    x44 = 2*x30*(x0*x29/x7**2 + x24*x33 + x25*x28*(-x0*(-x39 - x40 + x41 + x42) + x43))
    return x30*(x24*(-2*x0*x17 + x1*x31 + x3*(-x20 + x21 + x32*x5) + x31*x6) + x28*(x0*x32 + x11 - x9) + x33*x34 + x35*x36 + x35*x38 - x36*x44 + x37*(x0*(x39 + x40 - x41 - x42) + x43) - x38*x44)/sqrt(x7)

def phi_dY4_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = -Z3
    x5 = Z2 + x4
    x6 = x5**2
    x7 = x2 + x3**2 + x6
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x1*x9 + x3*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x1*x11 - x12*x3
    x14 = Z1 - Z2
    x15 = -x1*x14 + x5*x8
    x16 = Z3 - Z4
    x17 = x1*x16 - x12*x5
    x18 = -x14*x3 + x5*x9
    x19 = -x11*x5 + x16*x3
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x7
    x22 = x10*x19 - x13*x18
    x23 = x1*(x10*x17 - x13*x15) + x22*x3 + x5*(x15*x19 - x17*x18)
    x24 = x23**2
    x25 = 1/(x20**2 + x21*x24)
    x26 = X1 + x0
    x27 = Z1 + x4
    x28 = x1*x18 + x10*x5
    x29 = -x10*x12 + x13*x26 + x16*x18 - x19*x27
    x30 = x15*x2 + x15*x6 + x28*x3
    x31 = x21*x3
    x32 = x20*x30
    x33 = x1*x10 - x18*x5
    x34 = x23*x33
    x35 = x1*(x12*x15 + x17*x26) + x22 + x3*(x10*x16 + x12*x18 + x13*x27 + x19*x26) + x5*(x15*x16 + x17*x27)
    x36 = 2*x25*(x20*x29 + x21*x23*x35 - x24*x3/x7**2)
    return x25*(-x20*(x28 + x3*(-x1*x27 + x26*x5)) - x23*(x1*x26 + x27*x5) - x29*x30 + x31*x32 + x31*x34 + x32*x36 - x33*x35 + x34*x36)/sqrt(x7)

def phi_dY4_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = -Y3
    x4 = Y2 + x3
    x5 = Z2 - Z3
    x6 = x5**2
    x7 = x2 + x4**2 + x6
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x1*x9 + x4*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x1*x11 - x12*x4
    x14 = Z1 - Z2
    x15 = -x1*x14 + x5*x8
    x16 = Z3 - Z4
    x17 = x1*x16 - x12*x5
    x18 = -x14*x4 + x5*x9
    x19 = -x11*x5 + x16*x4
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x7
    x22 = x15*x19
    x23 = x17*x18
    x24 = x1*(x10*x17 - x13*x15) + x4*(x10*x19 - x13*x18) + x5*(x22 - x23)
    x25 = x24**2
    x26 = 1/(x20**2 + x21*x25)
    x27 = X1 + x0
    x28 = Y1 + x3
    x29 = -x11*x18 - x12*x15 + x17*x27 + x19*x28
    x30 = x15*x2 + x15*x6 + x4*(x1*x18 + x10*x5)
    x31 = x21*x5
    x32 = x20*x30
    x33 = x1*x10 - x18*x5
    x34 = x24*x33
    x35 = x13*x27
    x36 = x13*x28
    x37 = -x22 + x23 - x5*(-x11*x15 + x12*x18 - x17*x28 + x19*x27)
    x38 = 2*x26*(x20*x29 - x21*x24*(x1*(-x10*(X4 + x0) + x35) + x37 + x4*(-x10*(Y4 + x3) + x36)) - x25*x5/x7**2)
    return x26*(-x20*(2*x15*x5 + x2*x27 + x27*x6 + x4*(x1*x28 + x10)) + x24*(x18 + x28*x5) - x29*x30 + x31*x32 + x31*x34 + x32*x38 + x33*(x1*(x10*x12 + x35) + x37 + x4*(x10*x11 + x36)) + x34*x38)/sqrt(x7)

def phi_dY4_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = x2*x7
    x9 = Y1 - Y2
    x10 = x0*x9
    x11 = -x10 + x8
    x12 = -Y4
    x13 = Y3 + x12
    x14 = X3 - X4
    x15 = x0*x13 - x14*x2
    x16 = Z1 - Z2
    x17 = -x0*x16 + x4*x7
    x18 = -Z4
    x19 = Z3 + x18
    x20 = x0*x19 - x14*x4
    x21 = -x16*x2 + x4*x9
    x22 = -x13*x4 + x19*x2
    x23 = x11*x15 + x17*x20 + x21*x22
    x24 = 1/x6
    x25 = x11*x20
    x26 = x15*x17
    x27 = x0*(x25 - x26) + x2*(x11*x22 - x15*x21) + x4*(x17*x22 - x20*x21)
    x28 = x27**2
    x29 = 1/(x23**2 + x24*x28)
    x30 = Y2 + x12
    x31 = Z2 + x18
    x32 = -x11*x30 + x15*x9 + x16*x20 - x17*x31
    x33 = x1*x17 + x17*x5 + x2*(x0*x21 + x11*x4)
    x34 = x0*x24
    x35 = x23*x33
    x36 = x0*x11 - x21*x4
    x37 = x27*x36
    x38 = x0*(-x11*x31 - x15*x16 + x17*x30 + x20*x9) + x2*(x21*x30 + x22*x9) - x25 + x26 + x4*(x16*x22 + x21*x31)
    x39 = 2*x29*(x0*x28/x6**2 + x23*x32 + x24*x27*x38)
    return x29*(-x23*(-2*x0*x17 + x1*x16 + x16*x3 + x16*x5) + x27*(-2*x10 + x8) - x32*x33 - x34*x35 - x34*x37 + x35*x39 - x36*x38 + x37*x39)/sqrt(x6)

def phi_dY4_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x1 + x2**2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = Y3 - Y4
    x10 = -X4
    x11 = X3 + x10
    x12 = x0*x9 - x11*x2
    x13 = -Z2
    x14 = Z1 + x13
    x15 = -x0*x14 + x3*x6
    x16 = -Z4
    x17 = Z3 + x16
    x18 = x0*x17 - x11*x3
    x19 = -x14*x2 + x3*x7
    x20 = x17*x2 - x3*x9
    x21 = x12*x8 + x15*x18 + x19*x20
    x22 = 1/x5
    x23 = x20*x8
    x24 = -x12*x19
    x25 = x0*(-x12*x15 + x18*x8) + x2*(x23 + x24) + x3*(x15*x20 - x18*x19)
    x26 = x25**2
    x27 = 1/(x21**2 + x22*x26)
    x28 = x0*x19 + x3*x8
    x29 = Z2 + x16
    x30 = X2 + x10
    x31 = x12*x6 - x14*x20 + x19*x29 - x30*x8
    x32 = x1*x15 + x15*x4 + x2*x28
    x33 = x2*x22
    x34 = x21*x32
    x35 = x0*x8 - x19*x3
    x36 = x25*x35
    x37 = x14*x18
    x38 = x0*(x15*x30 + x18*x6) + x2*(x12*x14 + x19*x30 + x20*x6 + x29*x8) + x23 + x24
    x39 = 2*x27*(-x2*x26/x5**2 + x21*x31 + x22*x25*(x3*(-x15*(Z4 + x13) + x37) + x38))
    return x27*(x21*(x15*x2 + x28) + x25*(x0*x6 + x14*x3) + x31*x32 - x33*x34 - x33*x36 - x34*x39 + x35*(x3*(x15*x29 + x37) + x38) - x36*x39)/sqrt(x5)

def phi_dY4_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = -Y4
    x11 = Y3 + x10
    x12 = -X4
    x13 = X3 + x12
    x14 = x0*x11 - x13*x2
    x15 = Z1 - Z2
    x16 = -x0*x15 + x4*x7
    x17 = Z3 - Z4
    x18 = x0*x17 - x13*x4
    x19 = x4*x8
    x20 = -x15*x2
    x21 = x19 + x20
    x22 = -x11*x4 + x17*x2
    x23 = x14*x9 + x16*x18 + x21*x22
    x24 = 1/x6
    x25 = x16*x22
    x26 = x18*x21
    x27 = x25 - x26
    x28 = x0*(-x14*x16 + x18*x9) + x2*(-x14*x21 + x22*x9) + x27*x4
    x29 = x28**2
    x30 = 1/(x23**2 + x24*x29)
    x31 = X2 + x12
    x32 = Y2 + x10
    x33 = -x16*x31 + x18*x7 - x21*x32 + x22*x8
    x34 = x1*x16 + x16*x5 + x2*(x0*x21 + x4*x9)
    x35 = x24*x4
    x36 = x23*x34
    x37 = x0*x9 - x21*x4
    x38 = x28*x37
    x39 = x31*x9
    x40 = x32*x9
    x41 = x22*x7
    x42 = x21*x31
    x43 = x18*x8
    x44 = x16*x32
    x45 = 2*x30*(x23*x33 + x24*x28*(x0*(x14*(-X1 + X2) - x39) + x2*(x14*(-Y1 + Y2) - x40) + x27 - x4*(-x41 - x42 + x43 + x44)) - x29*x4/x6**2)
    return x30*(x23*(x1*x7 + 2*x16*x4 + x3*x7 + x5*x7) - x28*(2*x19 + x20) + x33*x34 - x35*x36 - x35*x38 - x36*x45 - x37*(x0*(x14*x7 + x39) + x2*(x14*x8 + x40) - x25 + x26 - x4*(x41 + x42 - x43 - x44)) - x38*x45)/sqrt(x6)

def phi_dY4_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x0*x10 - x11*x2
    x13 = Z1 - Z2
    x14 = -x0*x13 + x4*x7
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x4
    x17 = -x13*x2 + x4*x8
    x18 = -x10*x4 + x15*x2
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x14 + x16*x9) + x2*(-x12*x17 + x18*x9) + x4*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x14*x4 + x2*x9
    x24 = x4*x9
    x25 = x1*x14 + x14*x5 + x2*(x0*x17 + x24)
    x26 = x0*x9 - x17*x4
    x27 = x0*(x14*x2 - x24) + x17*x3 + x17*x5
    x28 = 2*x22*(x19*x23 - x20*x21*x27)
    return x22*(x19*x25*x28 + x21*x26*x28 - x23*x25 + x26*x27)/sqrt(x6)

def phi_dY4_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = Z2 - Z3
    x4 = x3**2
    x5 = x1 + x2**2 + x4
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = Y3 - Y4
    x10 = X3 - X4
    x11 = x0*x9 - x10*x2
    x12 = Z1 - Z2
    x13 = -x0*x12 + x3*x6
    x14 = Z3 - Z4
    x15 = x0*x14 - x10*x3
    x16 = -x12*x2 + x3*x7
    x17 = x14*x2 - x3*x9
    x18 = x11*x8 + x13*x15 + x16*x17
    x19 = 1/x5
    x20 = x0*(-x11*x13 + x15*x8) + x2*(-x11*x16 + x17*x8) + x3*(x13*x17 - x15*x16)
    x21 = x1*x13 + x13*x4 + x2*(x0*x16 + x3*x8)
    x22 = x0*x8 - x16*x3
    return 2*(x18*x21 + x20*x22)*(-x18*x22 + x19*x20*x21)/(sqrt(x5)*(x18**2 + x19*x20**2)**2)

def phi_dY4_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = -X2
    x8 = X1 + x7
    x9 = -Y2
    x10 = Y1 + x9
    x11 = -x0*x10 + x2*x8
    x12 = Y3 - Y4
    x13 = X3 - X4
    x14 = x0*x12 - x13*x2
    x15 = Z1 - Z2
    x16 = -x0*x15 + x4*x8
    x17 = Z3 - Z4
    x18 = x0*x17 - x13*x4
    x19 = x10*x4 - x15*x2
    x20 = -x12*x4 + x17*x2
    x21 = x11*x14 + x16*x18 + x19*x20
    x22 = 1/x6
    x23 = x0*(x11*x18 - x14*x16) + x2*(x11*x20 - x14*x19) + x4*(x16*x20 - x18*x19)
    x24 = 1/(x21**2 + x22*x23**2)
    x25 = x0*x16 + x19*x2
    x26 = x0*x19
    x27 = x1*x16 + x16*x5 + x2*(x11*x4 + x26)
    x28 = x0*x11 - x19*x4
    x29 = x1*x11 + x11*x3
    x30 = 2*x24*(x21*x25 + x22*x23*(x29 + x4*(-x16*(Y3 + x9) + x19*(X3 + x7))))
    return x24*(-x21*x27*x30 - x23*x28*x30 + x25*x27 + x28*(x29 - x4*(-x16*x2 + x26)))/sqrt(x6)

def phi_dZ4_dX1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X1 - X2
    x1 = Y2 - Y3
    x2 = X2 - X3
    x3 = Y1 - Y2
    x4 = x0*x1 - x2*x3
    x5 = Y3 - Y4
    x6 = X3 - X4
    x7 = -x1*x6 + x2*x5
    x8 = Z2 - Z3
    x9 = Z1 - Z2
    x10 = x0*x8 - x2*x9
    x11 = Z3 - Z4
    x12 = x11*x2 - x6*x8
    x13 = -x1*x9 + x3*x8
    x14 = x1*x11 - x5*x8
    x15 = x10*x12 + x13*x14 + x4*x7
    x16 = x2**2
    x17 = x1**2
    x18 = x8**2
    x19 = x16 + x17 + x18
    x20 = 1/x19
    x21 = x1*(-x13*x7 + x14*x4) + x2*(-x10*x7 + x12*x4) + x8*(x10*x14 - x12*x13)
    x22 = 1/(x15**2 + x20*x21**2)
    x23 = sqrt(x19)
    x24 = x1*x7 + x12*x8
    x25 = 1/x23
    x26 = x16*x4 + x17*x4 + x8*(x1*x10 - x13*x2)
    x27 = x1*x13 + x10*x2
    x28 = x14*x17 + x14*x18 + x2*(x1*x12 - x7*x8)
    x29 = 2*x22*(x15*x24 + x20*x21*x28)
    return x22*(x1*x15*x23 - x15*x25*x26*x29 - x2*x21*x25*x8 + x21*x25*x27*x29 + x24*x25*x26 - x25*x27*x28)

def phi_dZ4_dY1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X1 - X2
    x1 = Y2 - Y3
    x2 = X2 - X3
    x3 = Y1 - Y2
    x4 = x0*x1 - x2*x3
    x5 = Y3 - Y4
    x6 = X3 - X4
    x7 = -x1*x6 + x2*x5
    x8 = Z2 - Z3
    x9 = Z1 - Z2
    x10 = x0*x8 - x2*x9
    x11 = Z3 - Z4
    x12 = x11*x2 - x6*x8
    x13 = -x1*x9 + x3*x8
    x14 = x1*x11 - x5*x8
    x15 = x10*x12 + x13*x14 + x4*x7
    x16 = x2**2
    x17 = x1**2
    x18 = x8**2
    x19 = x16 + x17 + x18
    x20 = 1/x19
    x21 = x1*(-x13*x7 + x14*x4) + x2*(-x10*x7 + x12*x4) + x8*(x10*x14 - x12*x13)
    x22 = 1/(x15**2 + x20*x21**2)
    x23 = sqrt(x19)
    x24 = 1/x23
    x25 = x1*x13 + x10*x2
    x26 = x1*(x14*x2 + x7*x8) + x12*x16 + x12*x18
    x27 = -x14*x8 + x2*x7
    x28 = x16*x4 + x17*x4 + x8*(x1*x10 - x13*x2)
    x29 = 2*x22*(x15*x27 + x20*x21*x26)
    return x22*(-x1*x21*x24*x8 - x15*x2*x23 + x15*x24*x28*x29 - x21*x24*x25*x29 + x24*x25*x26 - x24*x27*x28)

def phi_dZ4_dZ1(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = Z2 - Z3
    x1 = X2 - X3
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = x3**2
    x5 = x2 + x4
    x6 = x0**2 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x1*x8 + x3*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x1*x10 - x11*x3
    x13 = Z1 - Z2
    x14 = x0*x7 - x1*x13
    x15 = Z3 - Z4
    x16 = -x0*x11 + x1*x15
    x17 = x0*x8 - x13*x3
    x18 = -x0*x10 + x15*x3
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(x14*x18 - x16*x17) + x1*(-x12*x14 + x16*x9) + x3*(-x12*x17 + x18*x9)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x1*x14 + x17*x3
    x24 = x12*x2 + x12*x4
    x25 = x1*x18
    x26 = x16*x3
    x27 = x1*x16 + x18*x3
    x28 = -x0*(x1*x17 - x14*x3) + x2*x9 + x4*x9
    x29 = 2*x22*(x19*x27 - x20*x21*(x0*(-x25 + x26) + x24))
    return x22*(x19*x28*x29 - x21*x23*x29 + x21*x5 - x23*(-x0*(x25 - x26) + x24) - x27*x28)/sqrt(x6)

def phi_dZ4_dX2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = -Y3
    x3 = Y2 + x2
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x1 + x4 + x6**2
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x0*x9 + x3*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x0*x11 - x12*x3
    x14 = x6*x8
    x15 = Z1 - Z2
    x16 = x0*x15
    x17 = x14 - x16
    x18 = Z3 - Z4
    x19 = x0*x18 - x12*x6
    x20 = -x15*x3 + x6*x9
    x21 = -x11*x6 + x18*x3
    x22 = x10*x13 + x17*x19 + x20*x21
    x23 = 1/x7
    x24 = x10*x19
    x25 = x13*x17
    x26 = x0*(x24 - x25) + x3*(x10*x21 - x13*x20) + x6*(x17*x21 - x19*x20)
    x27 = x26**2
    x28 = 1/(x22**2 + x23*x27)
    x29 = Y1 + x2
    x30 = Z1 + x5
    x31 = -x10*x11 + x13*x29 - x17*x18 + x19*x30
    x32 = x1*x10 + x10*x4 + x6*(-x0*x20 + x17*x3)
    x33 = x0*x23
    x34 = x22*x32
    x35 = x0*x17 + x20*x3
    x36 = x26*x35
    x37 = x19*x29
    x38 = x11*x17
    x39 = x13*x30
    x40 = x10*x18
    x41 = -x24 + x25 + x3*(x11*x20 + x21*x29) + x6*(x18*x20 + x21*x30)
    x42 = 2*x28*(x0*x27/x7**2 + x22*x31 + x23*x26*(-x0*(-x37 - x38 + x39 + x40) + x41))
    return x28*(-x22*(-2*x0*x10 + x1*x29 + x29*x4 + x6*(x20 + x3*x30)) + x26*(x0*x30 - x14 + x16) - x31*x32 - x33*x34 + x33*x36 + x34*x42 + x35*(x0*(x37 + x38 - x39 - x40) + x41) - x36*x42)/sqrt(x7)

def phi_dZ4_dY2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = Y2 - Y3
    x4 = x3**2
    x5 = -Z3
    x6 = Z2 + x5
    x7 = x2 + x4 + x6**2
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x1*x9 + x3*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x1*x11 - x12*x3
    x14 = Z1 - Z2
    x15 = -x1*x14 + x6*x8
    x16 = Z3 - Z4
    x17 = x1*x16 - x12*x6
    x18 = x6*x9
    x19 = x14*x3
    x20 = x18 - x19
    x21 = -x11*x6 + x16*x3
    x22 = x10*x13 + x15*x17 + x20*x21
    x23 = 1/x7
    x24 = x10*x21 - x13*x20
    x25 = x1*(x10*x17 - x13*x15) + x24*x3 + x6*(x15*x21 - x17*x20)
    x26 = x25**2
    x27 = 1/(x22**2 + x23*x26)
    x28 = X1 + x0
    x29 = Z1 + x5
    x30 = -x10*x12 + x13*x28 + x16*x20 - x21*x29
    x31 = x10*x2 + x10*x4 - x6*(x1*x20 - x15*x3)
    x32 = x23*x3
    x33 = x22*x31
    x34 = x1*x15 + x20*x3
    x35 = x25*x34
    x36 = x1*(x12*x15 + x17*x28) + x24 + x3*(x10*x16 + x12*x20 + x13*x29 + x21*x28) + x6*(x15*x16 + x17*x29)
    x37 = 2*x27*(x22*x30 + x23*x25*x36 - x26*x3/x7**2)
    return x27*(x22*(2*x10*x3 + x2*x28 + x28*x4 + x6*(x1*x29 + x15)) + x25*(-x18 + x19 + x29*x3) + x30*x31 - x32*x33 + x32*x35 - x33*x37 - x34*x36 + x35*x37)/sqrt(x7)

def phi_dZ4_dZ2(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = -X3
    x1 = X2 + x0
    x2 = x1**2
    x3 = -Y3
    x4 = Y2 + x3
    x5 = x4**2
    x6 = Z2 - Z3
    x7 = x2 + x5 + x6**2
    x8 = X1 - X2
    x9 = Y1 - Y2
    x10 = -x1*x9 + x4*x8
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x1*x11 - x12*x4
    x14 = Z1 - Z2
    x15 = -x1*x14 + x6*x8
    x16 = Z3 - Z4
    x17 = x1*x16 - x12*x6
    x18 = -x14*x4 + x6*x9
    x19 = -x11*x6 + x16*x4
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x7
    x22 = x15*x19
    x23 = x17*x18
    x24 = x1*(x10*x17 - x13*x15) + x4*(x10*x19 - x13*x18) + x6*(x22 - x23)
    x25 = x24**2
    x26 = 1/(x20**2 + x21*x25)
    x27 = X1 + x0
    x28 = Y1 + x3
    x29 = -x1*x18 + x15*x4
    x30 = -x11*x18 - x12*x15 + x17*x27 + x19*x28
    x31 = x10*x2 + x10*x5 + x29*x6
    x32 = x21*x6
    x33 = x20*x31
    x34 = x1*x15 + x18*x4
    x35 = x24*x34
    x36 = x13*x27
    x37 = x13*x28
    x38 = -x22 + x23 - x6*(-x11*x15 + x12*x18 - x17*x28 + x19*x27)
    x39 = 2*x26*(x20*x30 - x21*x24*(x1*(-x10*(X4 + x0) + x36) + x38 + x4*(-x10*(Y4 + x3) + x37)) - x25*x6/x7**2)
    return x26*(x20*(x29 + x6*(-x1*x28 + x27*x4)) - x24*(x1*x27 + x28*x4) + x30*x31 - x32*x33 + x32*x35 - x33*x39 + x34*(x1*(x10*x12 + x36) + x38 + x4*(x10*x11 + x37)) + x35*x39)/sqrt(x7)

def phi_dZ4_dX3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = -Y4
    x11 = Y3 + x10
    x12 = X3 - X4
    x13 = x0*x11 - x12*x2
    x14 = x4*x7
    x15 = Z1 - Z2
    x16 = x0*x15
    x17 = x14 - x16
    x18 = -Z4
    x19 = Z3 + x18
    x20 = x0*x19 - x12*x4
    x21 = -x15*x2 + x4*x8
    x22 = -x11*x4 + x19*x2
    x23 = x13*x9 + x17*x20 + x21*x22
    x24 = 1/x6
    x25 = x20*x9
    x26 = x13*x17
    x27 = x0*(x25 - x26) + x2*(-x13*x21 + x22*x9) + x4*(x17*x22 - x20*x21)
    x28 = x27**2
    x29 = 1/(x23**2 + x24*x28)
    x30 = Y2 + x10
    x31 = Z2 + x18
    x32 = x13*x8 + x15*x20 - x17*x31 - x30*x9
    x33 = x1*x9 + x3*x9 - x4*(x0*x21 - x17*x2)
    x34 = x0*x24
    x35 = x23*x33
    x36 = x0*x17 + x2*x21
    x37 = x27*x36
    x38 = x0*(-x13*x15 + x17*x30 + x20*x8 - x31*x9) + x2*(x21*x30 + x22*x8) - x25 + x26 + x4*(x15*x22 + x21*x31)
    x39 = 2*x29*(x0*x28/x6**2 + x23*x32 + x24*x27*x38)
    return x29*(x23*(-2*x0*x9 + x1*x8 + x3*x8 + x5*x8) + x27*(x14 - 2*x16) + x32*x33 + x34*x35 - x34*x37 - x35*x39 - x36*x38 + x37*x39)/sqrt(x6)

def phi_dZ4_dY3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = -X4
    x12 = X3 + x11
    x13 = x0*x10 - x12*x2
    x14 = -Z2
    x15 = Z1 + x14
    x16 = -x0*x15 + x4*x7
    x17 = -Z4
    x18 = Z3 + x17
    x19 = x0*x18 - x12*x4
    x20 = x4*x8
    x21 = x15*x2
    x22 = x20 - x21
    x23 = -x10*x4 + x18*x2
    x24 = x13*x9 + x16*x19 + x22*x23
    x25 = 1/x6
    x26 = x23*x9
    x27 = -x13*x22
    x28 = x0*(-x13*x16 + x19*x9) + x2*(x26 + x27) + x4*(x16*x23 - x19*x22)
    x29 = x28**2
    x30 = 1/(x24**2 + x25*x29)
    x31 = Z2 + x17
    x32 = X2 + x11
    x33 = x13*x7 - x15*x23 + x22*x31 - x32*x9
    x34 = x1*x9 + x3*x9 - x4*(x0*x22 - x16*x2)
    x35 = x2*x25
    x36 = x24*x34
    x37 = x0*x16 + x2*x22
    x38 = x28*x37
    x39 = x15*x19
    x40 = x0*(x16*x32 + x19*x7) + x2*(x13*x15 + x22*x32 + x23*x7 + x31*x9) + x26 + x27
    x41 = 2*x30*(-x2*x29/x6**2 + x24*x33 + x25*x28*(x4*(-x16*(Z4 + x14) + x39) + x40))
    return x30*(-x24*(x1*x7 + 2*x2*x9 + x3*x7 + x5*x7) + x28*(x20 - 2*x21) - x33*x34 + x35*x36 - x35*x38 + x36*x41 + x37*(x4*(x16*x31 + x39) + x40) - x38*x41)/sqrt(x6)

def phi_dZ4_dZ3(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x1 + x3 + x4**2
    x6 = X1 - X2
    x7 = Y1 - Y2
    x8 = -x0*x7 + x2*x6
    x9 = -Y4
    x10 = Y3 + x9
    x11 = -X4
    x12 = X3 + x11
    x13 = x0*x10 - x12*x2
    x14 = Z1 - Z2
    x15 = -x0*x14 + x4*x6
    x16 = Z3 - Z4
    x17 = x0*x16 - x12*x4
    x18 = -x14*x2 + x4*x7
    x19 = -x10*x4 + x16*x2
    x20 = x13*x8 + x15*x17 + x18*x19
    x21 = 1/x5
    x22 = x15*x19
    x23 = x17*x18
    x24 = x22 - x23
    x25 = x0*(-x13*x15 + x17*x8) + x2*(-x13*x18 + x19*x8) + x24*x4
    x26 = x25**2
    x27 = 1/(x20**2 + x21*x26)
    x28 = x15*x2
    x29 = x0*x18
    x30 = X2 + x11
    x31 = Y2 + x9
    x32 = -x15*x30 + x17*x6 - x18*x31 + x19*x7
    x33 = x1*x8 + x3*x8 - x4*(-x28 + x29)
    x34 = x21*x4
    x35 = x20*x33
    x36 = x0*x15 + x18*x2
    x37 = x25*x36
    x38 = x30*x8
    x39 = x31*x8
    x40 = x19*x6
    x41 = x18*x30
    x42 = x17*x7
    x43 = x15*x31
    x44 = 2*x27*(x20*x32 + x21*x25*(x0*(x13*(-X1 + X2) - x38) + x2*(x13*(-Y1 + Y2) - x39) + x24 - x4*(-x40 - x41 + x42 + x43)) - x26*x4/x5**2)
    return x27*(-x20*(x28 - x29 + x4*x8) + x25*(x0*x6 + x2*x7) - x32*x33 + x34*x35 - x34*x37 + x35*x44 - x36*(x0*(x13*x6 + x38) + x2*(x13*x7 + x39) - x22 + x23 - x4*(x40 + x41 - x42 - x43)) - x37*x44)/sqrt(x5)

def phi_dZ4_dX4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x0*x10 - x11*x2
    x13 = Z1 - Z2
    x14 = -x0*x13 + x4*x7
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x4
    x17 = -x13*x2 + x4*x8
    x18 = -x10*x4 + x15*x2
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x14 + x16*x9) + x2*(-x12*x17 + x18*x9) + x4*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x0*x14 + x17*x2
    x24 = x14*x2
    x25 = x0*(x24 - x4*x9) + x17*x3 + x17*x5
    x26 = x14*x4 + x2*x9
    x27 = x1*x9 + x3*x9 - x4*(x0*x17 - x24)
    x28 = 2*x22*(x19*x26 - x20*x21*x25)
    return x22*(-x19*x27*x28 + x21*x23*x28 + x23*x25 + x26*x27)/sqrt(x6)

def phi_dZ4_dY4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x4**2
    x6 = x1 + x3 + x5
    x7 = X1 - X2
    x8 = Y1 - Y2
    x9 = -x0*x8 + x2*x7
    x10 = Y3 - Y4
    x11 = X3 - X4
    x12 = x0*x10 - x11*x2
    x13 = Z1 - Z2
    x14 = -x0*x13 + x4*x7
    x15 = Z3 - Z4
    x16 = x0*x15 - x11*x4
    x17 = -x13*x2 + x4*x8
    x18 = -x10*x4 + x15*x2
    x19 = x12*x9 + x14*x16 + x17*x18
    x20 = 1/x6
    x21 = x0*(-x12*x14 + x16*x9) + x2*(-x12*x17 + x18*x9) + x4*(x14*x18 - x16*x17)
    x22 = 1/(x19**2 + x20*x21**2)
    x23 = x0*x14 + x17*x2
    x24 = x0*x17
    x25 = x1*x14 + x14*x5 + x2*(x24 + x4*x9)
    x26 = x0*x9 - x17*x4
    x27 = x1*x9 + x3*x9 + x4*(x14*x2 - x24)
    x28 = 2*x22*(-x19*x26 + x20*x21*x25)
    return x22*(-x19*x27*x28 + x21*x23*x28 - x23*x25 - x26*x27)/sqrt(x6)

def phi_dZ4_dZ4(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):
    x0 = X2 - X3
    x1 = x0**2
    x2 = Y2 - Y3
    x3 = x2**2
    x4 = Z2 - Z3
    x5 = x1 + x3 + x4**2
    x6 = -X2
    x7 = X1 + x6
    x8 = -Y2
    x9 = Y1 + x8
    x10 = -x0*x9 + x2*x7
    x11 = Y3 - Y4
    x12 = X3 - X4
    x13 = x0*x11 - x12*x2
    x14 = Z1 - Z2
    x15 = -x0*x14 + x4*x7
    x16 = Z3 - Z4
    x17 = x0*x16 - x12*x4
    x18 = -x14*x2 + x4*x9
    x19 = -x11*x4 + x16*x2
    x20 = x10*x13 + x15*x17 + x18*x19
    x21 = 1/x5
    x22 = x0*(x10*x17 - x13*x15) + x2*(x10*x19 - x13*x18) + x4*(x15*x19 - x17*x18)
    x23 = x1*x10 + x10*x3
    x24 = x0*x15 + x18*x2
    return 2*(x20*x24 + x21*x22*(x23 + x4*(-x15*(Y3 + x8) + x18*(X3 + x6))))*(x20*(x23 + x4*(-x0*x18 + x15*x2)) - x22*x24)/(sqrt(x5)*(x20**2 + x21*x22**2)**2)

