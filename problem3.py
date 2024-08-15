import numpy as np
import matplotlib.pyplot as plt

# Loading the dataset
data = np.loadtxt('dataset1.txt')

# Setting up x and y variable using np.array
x = np.array(data[:, 0])
y = np.array(data[:, 1])

# Using normal equation
A = np.vstack([x, np.ones(len(x))]).T
B = A.T @ y
normal_solution = np.linalg.solve(A.T @ A, B)

# Using QR factorization
Q,R = np.linalg.qr(A)
B = np.linalg.inv(R) @ (Q.T @ y)

print("Normal Solution:", normal_solution)
print("QR Solution:", B)

# Plotting
plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, B[0] * x + B[1], 'r', label='Fitted line')
plt.legend()
plt.show()

