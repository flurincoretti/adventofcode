def run_diagnostic_program(program):
    instruction_lengths = [0, 4, 4, 2, 2, 3, 3, 4, 4]
    i = 0
    while i < len(program):
        opcode = program[i] % 100
        modes = [(program[i] // 10**j) % 10 for j in range(2, 5)]
        if opcode == 99:
            break
        instruction_length = instruction_lengths[opcode]
        params = [program[i+k] for k in range(1, instruction_length)]
        values = [p if modes[j] else program[p] for j, p in enumerate(params)] 
        i  += instruction_length
        if opcode == 1:
            program[params[2]] = values[0] + values[1]
        elif opcode == 2:
            program[params[2]] = values[0] * values[1]
        elif opcode == 3:
            program[params[0]] = int(input("Input: "))
        elif opcode == 4:
            print("Output: {}".format(values[0]))
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


if __name__ == "__main__":
    inputs = open('inputs/05.txt', 'r')
    program = list(map(int, inputs.read().split(',')))
    run_diagnostic_program(program)