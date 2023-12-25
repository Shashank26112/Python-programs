import matplotlib.pyplot as plt
import numpy as np 
np.random.seed(10)
dataset1=np.random.normal(100,10,200)
dataset2=np.random.normal(80,20,200)
dataset3=np.random.normal(60,35,220)
dataset4=np.random.normal(50,40,200)
dataset =[dataset1,dataset2,dataset3,dataset4]
figure= plt.figure(figsize =(10, 7))
ax=figure.add_axes([0,0,1,1])
bp=ax.boxplot(dataset) S
plt.show()