from itertools import permutations


def run_diagnostic_program(program, program_input=[]):
    instruction_lengths = [0, 4, 4, 2, 2, 3, 3, 4, 4]
    i = 0
    while i < len(program):
        opcode = program[i] % 100
        modes = [(program[i] // 10**j) % 10 for j in range(2, 5)]
        if opcode == 99:
            return
        instruction_length = instruction_lengths[opcode]
        params = [program[i+k] for k in range(1, instruction_length)]
        values = [p if modes[j] else program[p] for j, p in enumerate(params)] 
        i  += instruction_length
        if opcode == 1:
            program[params[2]] = values[0] + values[1]
        elif opcode == 2:
            program[params[2]] = values[0] * values[1]
        elif opcode == 3:
            if program_input == []:
                program[params[0]] = int(input("Input: "))
            else:
                program[params[0]] = program_input.pop(0)
        elif opcode == 4:
            return values[0]
        elif opcode == 5:
            if values[0] != 0:
                i = values[1]
        elif opcode == 6:
            if values[0] == 0:
                i = values[1]
        elif opcode == 7:
            program[params[2]] = int(values[0] < values[1])
        elif opcode == 8:
            program[params[2]] = int(values[0] == values[1])


def part_one(program):
    max_signal = 0
    for p in permutations(range(5)):
        output = run_diagnostic_program(program, [p[0], 0])
        for i in range(1,5):
            output = run_diagnostic_program(program, [p[i], output])
        if max_signal < output: max_signal = output
    print("Largest output signal: {}".format(max_signal))


if __name__ == "__main__":
    inputs = open('inputs/07.txt', 'r')
    program = list(map(int, inputs.read().split(',')))
    part_one(program)