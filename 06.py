import itertools


def get_line(line, orbits):
    last = line.split(')', 1)[0]
    try:
        line = orbits[last] + ")" + line
        return get_line(line, orbits)
    except KeyError:
        return line


def get_lines(orbits):
    objects = set(list(itertools.chain.from_iterable(
        [orbit.split(')') for orbit in orbits]
    )))
    vals = [orbit.split(')')[0] for orbit in orbits]
    keys = [orbit.split(')')[1] for orbit in orbits]
    orbits = dict(zip(keys, vals))
    lines = [get_line(obj, orbits) for obj in objects]
    return lines


def verify_map(orbits):
    lines = get_lines(orbits)
    count_direct = len(lines) - 1 
    count_indirect = 0
    for objects in [line.split(')') for line in lines]:
        if len(objects) > 2:
            count_indirect += len(objects) - 2
    return count_direct + count_indirect


if __name__ == "__main__":
    inputs = open('inputs/06.txt', 'r')
    orbit_map = inputs.read().split('\n')
    print(verify_map(orbit_map))
