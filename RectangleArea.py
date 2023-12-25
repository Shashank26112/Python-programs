class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w;
    def area(self):
        area=self.length*self.width
        print("Area of Rectangle",area)
    def perimeter(self):
        p=2*(self.length+self.width)
        print("The perieter of the rectangle",p)
class Box(Rectangle):
    def __init__(self,l,w,h):
        super().__init__(l,w)
        self.height=h
    def volume(self):
        v=self.length*self.width*self.height
        print("The Volume of the box",v)
    def perimeter(self):
        p=4*(self.length+self.width+self.height)
        print("The perimeter of the box",p)
a,b,c=[float(x)for x in input("Enter three measurement:").split()]
r1=Rectangle(a,b)
r1.area()
r1.perimeter()
b1=Box(a,b,c)
b1.volume()
b1.perimeter()
    
    