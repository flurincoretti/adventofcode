directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


def get_points(path):
    x, y = 0, 0
    points = []
    for instruction in path.split(','):
        dx, dy = directions[instruction[0]]
        for _ in range(int(instruction[1:])):
            x += dx
            y += dy
            points.append((x, y))
    return points


def part_one(paths):
    wire_1 = set(get_points(paths[0]))
    wire_2 = set(get_points(paths[1]))
    common_points = [point for point in wire_1.intersection(wire_2)]
    min_distance = min(sum(map(abs, points)) for points in common_points)
    print("Distance to closest intersection: {}".format(min_distance))


if __name__ == "__main__":
    inputs = open('inputs/03.txt', 'r')
    paths = inputs.read().split('\n')
    part_one(paths)
