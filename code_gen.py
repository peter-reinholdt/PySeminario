from sympy import diff, symbols, simplify, acos, cse, Matrix, atan2
X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4 = symbols('X1 Y1 Z1 X2 Y2 Z2 X3 Y3 Z3 X4 Y4 Z4', real=True)

genfile = open("fullhessian_generated.py","w+")

genfile.write("import numpy as np\n")
genfile.write("from math import sqrt\n\n")


radius = ((X1-X2)**2 + (Y1-Y2)**2 + (Z1-Z2)**2)**0.5
radius = simplify(radius)
theta = acos(((X2-X1)*(X2-X3)+(Y2-Y1)*(Y2-Y3)+(Z2-Z1)*(Z2-Z3))/(((X2-X1)**2+(Y2-Y1)**2+(Z2-Z1)**2)**0.5 * ((X2-X3)**2+(Y2-Y3)**2+(Z2-Z3)**2)**0.5))
theta = simplify(theta)
b1 = Matrix([X2-X1, Y2-Y1, Z2-Z1])
b2 = Matrix([X3-X2, Y3-Y2, Z3-Z2])
b3 = Matrix([X4-X3, Y4-Y3, Z4-Z3])
phi = atan2((b1.cross(b2).cross(b2.cross(b3))).dot(b2/b2.norm()),b1.cross(b2).dot(b2.cross(b3)))
phi = simplify(phi)

# functions to call
genfile.write("def radius_first_derivative(X1,Y1,Z1,X2,Y2,Z2,d1):\n")
genfile.write("    output = 0.0\n")
diff_var = [X1,Y1,Z1,X2,Y2,Z2]
elif_check = 0
for i in diff_var:
    if elif_check == 0:
        genfile.write("    if d1.upper() == \""+str(i)+"\":\n")
        genfile.write("        output = radius_d"+str(i)+"(X1,Y1,Z1,X2,Y2,Z2)\n")
        elif_check = 1
    else:
        genfile.write("    elif d1.upper() == \""+str(i)+"\":\n")
        genfile.write("        output = radius_d"+str(i)+"(X1,Y1,Z1,X2,Y2,Z2)\n")
genfile.write("    else:\n")
genfile.write("        print(\"radius_first_derivative not understood\")\n")
genfile.write("    return output\n\n")

genfile.write("def theta_first_derivative(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,d1):\n")
genfile.write("    output = 0.0\n")
diff_var = [X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3]
elif_check = 0
for i in diff_var:
    if elif_check == 0:
        genfile.write("    if d1.upper() == \""+str(i)+"\":\n")
        genfile.write("        output = theta_d"+str(i)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)\n")
        elif_check = 1
    else:
        genfile.write("    elif d1.upper() == \""+str(i)+"\":\n")
        genfile.write("        output = theta_d"+str(i)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)\n")
genfile.write("    else:\n")
genfile.write("        print(\"theta_first_derivative not understood\")\n")
genfile.write("    return output\n\n")

genfile.write("def phi_first_derivative(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4,d1):\n")
genfile.write("    output = 0.0\n")
diff_var = [X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4]
elif_check = 0
for i in diff_var:
    if elif_check == 0:
        genfile.write("    if d1.upper() == \""+str(i)+"\":\n")
        genfile.write("        output = phi_d"+str(i)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)\n")
        elif_check = 1
    else:
        genfile.write("    elif d1.upper() == \""+str(i)+"\":\n")
        genfile.write("        output = phi_d"+str(i)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)\n")
genfile.write("    else:\n")
genfile.write("        print(\"phi_first_derivative not understood\")\n")
genfile.write("    return output\n\n")

genfile.write("def radius_second_derivative(X1,Y1,Z1,X2,Y2,Z2,d1,d2):\n")
genfile.write("    output = 0.0\n")
diff_var = [X1,Y1,Z1,X2,Y2,Z2]
elif_check = 0
for i in diff_var:
    for j in diff_var:
        if elif_check == 0:
            genfile.write("    if d1 .upper()== \""+str(i)+"\" and d2.upper() == \""+str(j)+"\":\n")
            genfile.write("        output = radius_d"+str(i)+"_d"+str(j)+"(X1,Y1,Z1,X2,Y2,Z2)\n")
            elif_check = 1
        else:
            genfile.write("    elif d1.upper() == \""+str(i)+"\" and d2.upper() == \""+str(j)+"\":\n")
            genfile.write("        output = radius_d"+str(i)+"_d"+str(j)+"(X1,Y1,Z1,X2,Y2,Z2)\n")
genfile.write("    else:\n")
genfile.write("        print(\"radius_second_derivative not understood\")\n")
genfile.write("    return output\n\n")
    
genfile.write("def theta_second_derivative(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,d1,d2):\n")
genfile.write("    output = 0.0\n")
diff_var = [X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3]
elif_check = 0
for i in diff_var:
    for j in diff_var:
        if elif_check == 0:
            genfile.write("    if d1.upper() == \""+str(i)+"\" and d2.upper() == \""+str(j)+"\":\n")
            genfile.write("        output = theta_d"+str(i)+"_d"+str(j)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)\n")
            elif_check = 1
        else:
            genfile.write("    elif d1.upper() == \""+str(i)+"\" and d2.upper() == \""+str(j)+"\":\n")
            genfile.write("        output = theta_d"+str(i)+"_d"+str(j)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3)\n")
genfile.write("    else:\n")
genfile.write("        print(\"theta_second_derivative not understood\")\n")
genfile.write("    return output\n\n")

genfile.write("def theta_second_derivative(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4,d1,d2):\n")
genfile.write("    output = 0.0\n")
diff_var = [X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4]
elif_check = 0
for i in diff_var:
    for j in diff_var:
        if elif_check == 0:
            genfile.write("    if d1.upper() == \""+str(i)+"\" and d2.upper() == \""+str(j)+"\":\n")
            genfile.write("        output = phi_d"+str(i)+"_d"+str(j)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)\n")
            elif_check = 1
        else:
            genfile.write("    elif d1.upper() == \""+str(i)+"\" and d2.upper() == \""+str(j)+"\":\n")
            genfile.write("        output = phi_d"+str(i)+"_d"+str(j)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4)\n")
genfile.write("    else:\n")
genfile.write("        print(\"phi_second_derivative not understood\")\n")
genfile.write("    return output\n\n")


# First derivatives
diff_var = [X1,Y1,Z1,X2,Y2,Z2]
for i in diff_var:
    A = cse(diff(radius, i))
    genfile.write("def radius_d"+str(i)+"(X1,Y1,Z1,X2,Y2,Z2):\n")
    for k in range(0, len(A[0])):
        genfile.write("    "+str(A[0][k][0])+" = "+str(A[0][k][1])+"\n")
    genfile.write("    return "+str(A[1][0])+"\n\n")
diff_var = [X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3]
for i in diff_var:
    A = cse(diff(theta, i))
    genfile.write("def theta_d"+str(i)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):\n")
    for k in range(0, len(A[0])):
        genfile.write("    "+str(A[0][k][0])+" = "+str(A[0][k][1])+"\n")
    genfile.write("    return "+str(A[1][0])+"\n\n")
diff_var = [X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4]
for i in diff_var:
    A = cse(diff(phi, i))
    genfile.write("def phi_d"+str(i)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):\n")
    for k in range(0, len(A[0])):
        genfile.write("    "+str(A[0][k][0])+" = "+str(A[0][k][1])+"\n")
    genfile.write("    return "+str(A[1][0])+"\n\n")

# Second derivatives
diff_var = [X1,Y1,Z1,X2,Y2,Z2]
for i in diff_var:
    for j in diff_var:
        A = cse(diff(radius, i, j))
        genfile.write("def radius_d"+str(i)+"_d"+str(j)+"(X1,Y1,Z1,X2,Y2,Z2):\n")
        for k in range(0, len(A[0])):
            genfile.write("    "+str(A[0][k][0])+" = "+str(A[0][k][1])+"\n")
        genfile.write("    return "+str(A[1][0])+"\n\n")
diff_var = [X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3]
for i in diff_var:
    for j in diff_var:
        A = cse(diff(theta, i, j))
        genfile.write("def theta_d"+str(i)+"_d"+str(j)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3):\n")
        for k in range(0, len(A[0])):
            genfile.write("    "+str(A[0][k][0])+" = "+str(A[0][k][1])+"\n")
        genfile.write("    return "+str(A[1][0])+"\n\n")
diff_var = [X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4]
for i in diff_var:
    for j in diff_var:
        A = cse(diff(phi, i, j))
        genfile.write("def phi_d"+str(i)+"_d"+str(j)+"(X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4):\n")
        for k in range(0, len(A[0])):
            genfile.write("    "+str(A[0][k][0])+" = "+str(A[0][k][1])+"\n")
        genfile.write("    return "+str(A[1][0])+"\n\n")

genfile.close()