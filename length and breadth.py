# prompt the user to input the length and breadth
length = float(input("Enter the length:"))
breadth = float(input("Enterthe breadth:"))
# Determine whether it's a square or a rectangle
if length == breadth:
    shape_name = "square"
else:
    shape_name = "rectangle"

# Calculate the perimeter and area
perimeter = 2 * (length + breadth)
area = length * breadth

# Display the results
print(f"This shape is a {shape_name}")
print(f"The {shape_name} has Perimeter: {perimeter} and Area: {area}")
