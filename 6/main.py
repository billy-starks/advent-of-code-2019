def main1():
    orbits = {}
    orbittingSet = set()
    relationsCount = 0
    with open('input', 'r') as file:
        for line in file.readlines():
            line = line.strip()
            orbitee, orbiter = line.split(')')
            if orbitee in orbits:
                orbits[orbitee].add(orbiter)
            else:
                orbits[orbitee] = set([orbiter])
            orbittingSet.add(orbiter)

    # First, find planets that aren't orbiting anything
    tops = set(orbits.keys()) - orbittingSet

    #Their children contribute 1 orbit.
    #Their children's childrens contribute 2 orbits
    #In general, each n-generation child contributes n orbits
    children = [child for top in tops for child in orbits[top]]
    generation = 1
    while len(children) != 0:
        relationsCount += generation * len(children)
        children = [child for top in children for child in orbits.get(top, [])]
        generation += 1
    return relationsCount

def main2():
    neighbors = {}
    with open('input', 'r') as file:
        for line in file.readlines():
            line = line.strip()
            orbitee, orbiter = line.split(')')
            
            if orbitee in neighbors:
                neighbors[orbitee].add(orbiter)
            else:
                neighbors[orbitee] = set([orbiter])

            if orbiter in neighbors:
                neighbors[orbiter].add(orbitee)
            else:
                neighbors[orbiter] = set([orbitee])

    #Do BFS to find shortest path between YOU and SAN
    #Then subtract 2 from that number
    current = set(['YOU'])
    next = set()
    distance = 0
    while 'SAN' not in current:
        for curr in current:
            next.update(neighbors.get(curr, set()))
        current = next
        next = set()
        distance += 1
    return distance - 2
    
    
        

print(main1())
print(main2())
