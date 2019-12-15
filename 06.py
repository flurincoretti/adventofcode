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


def get_transfers(orbits):
    lines = get_lines(orbits)
    try:
        you_line = [l for l in lines if 'YOU' in l][0].split(')')
        san_line = [l for l in lines if 'SAN' in l][0].split(')')
        common_object = ''
        for i in range(min(len(you_line), len(san_line) - 1)):
            if you_line[i] == san_line[i]:
                if you_line[i+1] != san_line[i+1]:
                    common_object = you_line[i]
                    break
        transfers = you_line[you_line.index(common_object)+1:-1][::-1]
        transfers += san_line[san_line.index(common_object):-1]
        return len(transfers) - 1
    except IndexError:
        print('Error')


if __name__ == "__main__":
    inputs = open('inputs/06.txt', 'r')
    orbit_map = inputs.read().split('\n')
    print("Total number of direct and indirect orbits: {}".format(
        verify_map(orbit_map)))
    print("Minimum number of orbital transfers: {}".format(
        get_transfers(orbit_map)))