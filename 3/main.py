def generate_coords(dirStr):
    instructions = dirStr.split(',')
    posX = 0
    posY = 0
    visited = []
    for instruction in instructions:
        direction = instruction[0]
        length = int(instruction[1:])
        dx = 1 if direction == "R" else -1 if direction == "L" else 0
        dy = 1 if direction == "U" else -1 if direction == "D" else 0
        for _ in range(length):
            posX += dx
            posY += dy
            visited.append((posX,posY))
    return visited

def main1():
    intersections = set()
    with open("input", 'r') as file:
        path1 = set(generate_coords(file.readline()))
        path2 = set(generate_coords(file.readline()))
        intersections = path1 & path2
    smallest = (10000, 10000)
    for intersection in intersections:
        if sum(map(abs, intersection)) < sum(map(abs, smallest)):
            smallest = intersection
    return smallest

def main2():
    intersections = set()
    with open("input", 'r') as file:
        path1 = generate_coords(file.readline())
        path2 = generate_coords(file.readline())
        intersections = set(path1) & set(path2)
    best = (0,0)
    bestSteps = 10000000
    for intersection in intersections:
        steps = 2 + path1.index(intersection) + path2.index(intersection)
        if steps < bestSteps:
            best = intersection
            bestSteps = steps
    return best, bestSteps

print(main1())
print(main2())
