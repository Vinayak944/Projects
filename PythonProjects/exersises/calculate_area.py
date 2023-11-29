def calculate_area(b, h, s):

    if s==1:
        shape_name = "triangle"
        a = (1/2)*b*h

    elif s==2:
        shape_name = "rectangle"
        a = b*h

    else :
        shape_name = "triangle"
        a = (1/2)*b*h
    
    return a, shape_name

try:
    inputs = list(map(float,input("Enter the shape of the figure (1 = triangle, 2 = rectangle) and the dimensions(length and breadth or base and height) ").split()))
    if len(inputs) == 2:
        h1, b1 = inputs
        s1 = 1
    elif len(inputs) == 3:
        h1,b1,s1 = inputs
    else :
        raise ValueError("Enter 2 or 3 numbers")
     
    area, shape_name = calculate_area(b1, h1, s1)
    print("Area of ",shape_name," = ", area )

except ValueError as e:
    print(f"Invalid input. {e}")
    exit()   