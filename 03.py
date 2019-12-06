directions = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1]
}


def get_points(path):
    x, y = 0, 0
    points = []
    for instruction in path.split(','):
        dx, dy = directions[instruction[0]]
        for _ in range(int(instruction[1:])):
            x += dx
            y += dy
            points.append([x, y])
    return points


def part_one(paths):
    wire_1 = [(p[0], p[1]) for p in get_points(paths[0])]
    wire_2 = [(p[0], p[1]) for p in get_points(paths[1])]
    common_points = [point for point in set(wire_1).intersection(set(wire_2))]
    min_distance = min(sum(map(abs, points)) for points in common_points)
    print("Distance to closest intersection: {}".format(min_distance))


def part_two(paths):
    wire_1 = [(p[0], p[1]) for p in get_points(paths[0])]
    wire_2 = [(p[0], p[1]) for p in get_points(paths[1])]
    common_points = [point for point in set(wire_1).intersection(set(wire_2))]
    steps_1 = [wire_1.index(point) + 1 for point in common_points]
    steps_2 = [wire_2.index(point) + 1 for point in common_points]
    min_steps = min([x + y for x, y in zip(steps_1, steps_2)])
    print("Fewest combined steps: {}".format(min_steps))


if __name__ == "__main__":
    inputs = open('inputs/03.txt', 'r')
    paths = inputs.read().split('\n')
    part_one(paths)
    part_two(paths)
