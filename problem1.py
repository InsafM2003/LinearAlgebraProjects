import numpy as np
import sympy
import scipy.linalg as linalg

# (a)
A = np.array([[3, 8, -5], [3, -6, -7], [3, 4, 2]])

A_sympy = sympy.Matrix(A)

A_rref = A_sympy.rref()

A_rref = np.array(A_rref[0].tolist()) 
print('Reduced Echelon Form of A:\n', A_rref)

#(b)
columnspaceA = A_sympy.columnspace()
print("\nThe column space of A is:")
print(columnspaceA)

#(c)
b = np.array([-1, -1, 3])
x = np.linalg.solve(A, b)
print('\nSolution to matrix equation :\n', x)

#(d)
nullspaceA = linalg.null_space(A)
print("\nThe null space of A is:\n",nullspaceA)