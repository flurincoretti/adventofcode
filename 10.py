from math import atan2


def get_dimensions(asteroid_map):
    width = asteroid_map.find('\n')
    height = asteroid_map.count('\n') + 1
    return width, height


def get_asteroids(asteroid_map):
    w, h = get_dimensions(asteroid_map)
    am = asteroid_map.split('\n')
    return [(x,y) for x in range(w) for y in range(h) if am[y][x] == '#']


def count_visible_asteroids(asteroids, a):
    return len(set(atan2(b[1]-a[1], b[0]-a[0]) for b in asteroids if b != a))


def part_one(asteroid_map):
    asteroids = get_asteroids(asteroid_map)
    counts = [count_visible_asteroids(asteroids, a) for a in asteroids]
    print("Best is {} with {} other asteroids detected.".format(
        asteroids[counts.index(max(counts))], max(counts)
    ))


if __name__ == "__main__":
    inputs = open('inputs/10.txt', 'r')
    asteroid_map = inputs.read()
    part_one(asteroid_map)