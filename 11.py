from collections import defaultdict


D = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
L = {"U": "L", "R": "U", "L": "D", "D": "R"}
R = {"U": "R", "R": "D", "L": "U", "D": "L"}


def run_intcode_program(program, program_input=[]):
    memory = defaultdict(int, enumerate(program))
    instruction_lengths = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]
    i = relative_base = 0
    while True:
        opcode = memory[i] % 100
        modes = [(memory[i] // 10**j) % 10 for j in range(2, 5)]
        if opcode == 99:
            return
        instruction_length = instruction_lengths[opcode]
        args = [memory[i+k] for k in range(1, instruction_length)]
        values = [[memory[arg], arg, memory[arg + relative_base]][modes[j]] \
            for j, arg in enumerate(args)]
        addresses = [[arg, None, arg + relative_base][modes[j]] \
            for j, arg in enumerate(args)]
        i  += instruction_length
        if opcode == 1:
            memory[addresses[2]] = values[0] + values[1]
        elif opcode == 2:
            memory[addresses[2]] = values[0] * values[1]
        elif opcode == 3:
            if program_input == None:
                memory[addresses[0]] = int(input("Input: "))
            else:
                memory[addresses[0]] = program_input.pop(0)
        elif opcode == 4:
            yield values[0]
        elif opcode == 5:
            if values[0] != 0:
                i = values[1]
        elif opcode == 6:
            if values[0] == 0:
                i = values[1]
        elif opcode == 7:
            memory[addresses[2]] = int(values[0] < values[1])
        elif opcode == 8:
            memory[addresses[2]] = int(values[0] == values[1])
        elif opcode == 9:
            relative_base += values[0]


def run_robot(program, color):
    panels = {}
    colors = []
    generator = run_intcode_program(program, colors)
    x, y, d = 0, 0, 'U'
    while True:
        colors.append(panels.get((x, y), color))
        try:
            panels[(x, y)] = next(generator)
            d = [L, R][next(generator)][d]
            x += D[d][0]
            y += D[d][1]
        except StopIteration:
            return panels


def print_registration_identifier(panels):
    x, y = zip(*panels)
    xmin, xmax = min(x), max(x)
    ymin, ymax = min(y), max(y)
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            color = 'x' if panels.get((x, y)) else ' '
            print(color, end='')
        print()


if __name__ == "__main__":
    inputs = open('inputs/11.txt', 'r')
    program = list(map(int, inputs.read().split(',')))

    print("Part 1:")
    panels = run_robot(program, 0)
    print("Panels painted at least once: {}".format(len(panels)))

    print("Part 2:")
    panels = run_robot(program, 1)
    print_registration_identifier(panels)