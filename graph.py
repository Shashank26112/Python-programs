import matplotlib.pyplot as plt
waterfall=['Jog','Kalhatti','Hebbe','Gokak','Chuchanakatte','Jhari']
height=[824,403,551,170,66,70]
colors=['Blue','Yellow','Aqua','Green','Red']
plt.bar(waterfall,height,color=colors)
plt.title('waterfall vc height',fontsize=14)
plt.xlabel('waterfall',fontsize=14)
plt.ylabel('height',fontsize=14)
plt.grid(True)
plt.show()