import math
#largest of three numbers
def Largest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
# Function to calculate volume of different shapes
def calculate_volume(shape, **dimensions):
    if shape == 'cylinder':
        radius = dimensions.get('radius', 0)
        height = dimensions.get('height', 0)
        return 3.14159 * radius ** 2 * height
    elif shape == 'cube':
        side = dimensions.get('side', 0)
        return side ** 3
    elif shape == 'rectangular_box':
        length = dimensions.get('length', 0)
        width = dimensions.get('width', 0)
        height = dimensions.get('height', 0)
        return length * width * height
    else:
        return 'Invalid shape'



def area_Rectangle(length,breadth):
    return length*breadth
#circumference of a cirle
def circumference(radius):
    return (2*math.pi*radius)
#SWAP
def swap(a,b):
    a = a + b  #  a becomes the sum of a and b
    b = a - b  #  b becomes the original value of a
    a = a - b  #  a becomes the original value of b

#distance between two points
def distance(x,y):
     return math.dist(x,y)

feature = int(input("Enter 1 for finding the largest of 3 numbers \n \
                    Enter 2 for Finding the volume of a shape\n \
                    Enter 3 to find the area of a rectangle\n\
                    Enter 4 to find the circumference of a circle \n \
                    Enter 5 to swap values of two variables(integers) \n \
                    Enter 6 to find the distance between two points\n"))

if(feature==1):
    x=2 
    y=6 
    z=10
    print(Largest(x,y,z))
elif(feature==2):
    print(calculate_volume('cylinder', radius=3, height=5))
    print(calculate_volume('cube', side=3))               
    print(calculate_volume('rectangular_box', length=2, width=3, height=4))
elif(feature==3):
    l = 20
    b= 30
    print(area_Rectangle(l,b))
elif(feature==4):
    r= 12
    print(circumference(r))
elif(feature==5):
    a=2
    b=3
    swap(a,b)
    print("a= ",a)
    print("b = ",b)
elif(feature==6):
    a = 3
    b = 6
    print(distance(a,b))