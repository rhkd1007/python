import numpy as np
import matplotlib.pyplot as plt

x = [1, 4, 9, 16, 25, 36, 49, 64]

# plt.plot(x)
# plt.show()

y = [i for i in range(1, 9)]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('matplotlib sample')
# plt.show()

y1 = [13, 16, 15, 18, 16, 17, 16]
plt.plot(y1)
# plt.show()

###############################
points = np.array([[1,1],[1,2],[1,3],
                    [2,1],[2,2],[2,3],
                    [3,1],[3,2],[3,3],
])
print(points)
print(points.shape)
plt.plot(points[:, 0], points[:, 1])
plt.show()