from collections import defaultdict


def run_diagnostic_program(program, program_input = None):
    memory = defaultdict(int, enumerate(program))
    instruction_lengths = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]
    i = relative_base = 0
    while True:
        opcode = memory[i] % 100
        modes = [(memory[i] // 10**j) % 10 for j in range(2, 5)]
        if opcode == 99:
            break
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
                memory[addresses[0]] = program_input
        elif opcode == 4:
            print("Output: {}".format(values[0]))
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


if __name__ == "__main__":
    inputs = open('inputs/09.txt', 'r')
    program = list(map(int, inputs.read().split(',')))

    print("Part 1:")
    run_diagnostic_program(program, 1)

    print("Part 2:")
    run_diagnostic_program(program, 2)