# Решите систему уравнений:
# 4x + 2y + z = 4
# x + 3y = 12
# 5y + 4z = -3
import numpy as np
a = np.array([[4, 2, 1], [1, 3, 0], [0, 5, 4]])
b = np.array([4, 12, -3])
from numpy import linalg
print(linalg.solve(a, b))
print(np.allclose(np.dot(a, linalg.solve(a, b)), b))
