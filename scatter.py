import matplotlib.pyplot as plt
import numpy as np
x_axis_value=np.array([4,5,7,8,11,12,19,4,22,18,6,21,19])
y_axis_value=np.array([90,80,89,88,101,82,102,80,91,76,77,88,66])
plt.scatter(x_axis_value,y_axis_value,color='red')
x=np.array([1,2,66,54,22,34,67,77,88])
y=np.array([12,45,32,55,67,26,66,72,88])
plt.scatter(x,y,color='Green')
plt.show()