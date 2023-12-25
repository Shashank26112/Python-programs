import matplotlib.pyplot as plt
import numpy as np
array=np.array([15,11,22,24,22,31,32,35,37,45,66,55,45,24,66,56,55,78,74,72,78,90,88,82,84,88,84,90,95,90])
figure,axis=plt.subplots(figsize=(8,3))
axis.hist(array,bins=[20,30,40,50,60,70,80,90,100])
plt.show()