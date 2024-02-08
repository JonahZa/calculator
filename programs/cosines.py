import math

def find_angle(a, b, c):
    angle_c = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
    return math.degrees(angle_c)

def find_side_c(a, b, angle_c):
    angle_c_rad = math.radians(angle_c)
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle_c_rad))
    return c

def main():
    print("COSINES")
    print("Choose one of the following:")
    print("1. Find the angle opposite to side C")
    print("2. Find the length of side C")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        a = float(input("Enter the length of side A: "))
        b = float(input("Enter the length of side B: "))
        c = float(input("Enter the length of side C: "))
        angle_C = find_angle(a, b, c)
        print("The angle opposite to side C is:", round(angle_C, 4), "degrees")
    elif choice == 2:
        a = float(input("Enter the length of side A: "))
        b = float(input("Enter the length of side B: "))
        angle_C = float(input("Enter the angle opposite to side C in degrees: "))
        side_C = find_side_c(a, b, angle_C)
        print("The length of side C is:", round(side_C, 4))
        
    else:
        print("Invalid choice. Exiting...")
        exit()

main()