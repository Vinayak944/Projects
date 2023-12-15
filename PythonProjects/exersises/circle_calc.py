# Write circle_calc() function that takes radius of a circle as an input from user and then it calculates
# and returns area, circumference and diameter. You should get these values in your main program by 
# calling circle_calc function and then print them

def main():
    while True:
        try:
            r = float(input("Enter the radius of the circle: "))
            break
        except ValueError:
            print("Invalid Input. Enter any number")
    area = 3.14*r*r
    circum = 2*3.14*r
    dia = 2*r
    print(f"The area of the circle is {round(area,2)} \n The circumference of the circle is {circum} \n The diameter of the circle is {dia}")

if __name__ == "__main__":
    main()