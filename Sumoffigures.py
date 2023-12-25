from math import pi
def rect_area(l,b):
    return l*b
def tri_area(b,h):
    return 0.5*b*h
def sqr_area(a):
    return a*a
def cir_area(r):
    return pi*r**2
while(True):
    print('1.Rectangle \n 2.Traingle \n 3.square \n 4.circle')
    ch=int(input('Enter your choice: '))
    if ch==1:
        l=int(input('Enter the length of Rectangle: '))
        b=int(input('Enter the breadth of Rectanagle: '))
        print('Area of the rectangle: ',rect_area(l,b))
    elif ch==2:
        b=int(input('Enter the base of Triangle: '))
        h=int(input('Enter the height of Triangle: '))
        print('Area of the triangle: ',tri_area(b,h))
    elif ch==3:
        a=int(input('Enter the side of Square: '))
        print('Area of the square: ',sqr_area(a))
    elif ch==4:
        r=int(input('Enter the radius of circle: '))
        print('Area of the circle %0.2f' %cir_area(r))
    else:
        break
    