import matplotlib.pyplot as plt
amount=[1500,200,500,200,100,50]
product=['Milk','Crd','Ghee','Icecream','Paneer','Kova']
plt.pie(amount,labels=product,autopct='%1.1f%%')
plt.axis('equal')
plt.show()