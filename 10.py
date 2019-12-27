from math import atan2


def get_dims(asteroid_map):
    width = asteroid_map.find('\n')
    height = asteroid_map.count('\n') + 1
    return width, height


def get_coords(asteroid_map):
    w, h = get_dims(asteroid_map)
    am = asteroid_map.split('\n')
    return [(x,y) for x in range(w) for y in range(h) if am[y][x] == '#']


def get_angles(coords, c):
    return [atan2(b[1]-c[1], b[0]-c[0]) for b in coords if b != c]


def part_one(asteroid_map):
    coords = get_coords(asteroid_map)
    counts = [len(set(get_angles(coords, c))) for c in coords]
    return coords[counts.index(max(counts))], max(counts)


if __name__ == "__main__":
    inputs = open('inputs/10.txt', 'r')
    asteroid_map = inputs.read()

    # Part 1
    best, n = part_one(asteroid_map)
    print("Best is {} with {} other asteroids detected.".format(best, n))