import math

def cal_circle_area(radius):
    return math.pi * radius * radius

circle_number = int(input("Give me the number of circles: "))

areas = []

for i in range(1, circle_number + 1):
    area = cal_circle_area(i)
    areas.append(area)
    print(f"The area of circle with radius {i} is {area}")

areas.pop(0)

areas.append(10)

total_sum = sum(areas)

print(f"Sum of all areas (after modifications): {total_sum}")

grades = {'Save': 'A', 'Jib': 'B'}

print(grades['Save'])
print("Save")
