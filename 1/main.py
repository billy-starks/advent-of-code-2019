def calculate_fuel(mass):
    from math import floor
    return floor(mass / 3) - 2

def calculate_fuel_2(mass):
    from math import floor
    fuel = floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    return fuel + calculate_fuel_2(fuel)

with open("./input", 'r') as file:
    sum = 0
    sum2 = 0
    for mass in map(int, file.readlines()):
        sum += calculate_fuel(mass)
        sum2 += calculate_fuel_2(mass)
    print(sum, sum2)
