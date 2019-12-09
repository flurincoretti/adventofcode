def run_diagnostic_program(program):
    i = 0
    while i < len(program):
        opcode = program[i] % 100
        mode_1 = (program[i] // 100) % 10
        mode_2 = (program[i] // 1000) % 10
        mode_3 = (program[i] // 10000) % 10
        if opcode == 1:
            instruction_length = 4
            if mode_1 == 0 and mode_2 == 0:
                program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
            elif mode_1 == 1 and mode_2 == 0:
                program[program[i+3]] = program[i+1] + program[program[i+2]]
            elif mode_1 == 0 and mode_2 == 1:
                program[program[i+3]] = program[program[i+1]] + program[i+2]
            else:
                program[program[i+3]] = program[i+1] + program[i+2]
        elif opcode == 2:
            instruction_length = 4
            if mode_1 == 0 and mode_2 == 0:
                program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
            elif mode_1 == 1 and mode_2 == 0:
                program[program[i+3]] = program[i+1] * program[program[i+2]]
            elif mode_1 == 0 and mode_2 == 1:
                program[program[i+3]] = program[program[i+1]] * program[i+2]
            else:
                program[program[i+3]] = program[i+1] * program[i+2]
        elif opcode == 3:
            instruction_length = 2
            program[program[i+1]] = int(input("Input: "))
        elif opcode == 4:
            instruction_length = 2
            print("Output: {}".format(program[program[i+1]]))
        elif opcode == 99:
            break
        else:
            return
        i += instruction_length
    return program


def part_one(program):
    run_diagnostic_program(program)


if __name__ == "__main__":
    inputs = open('inputs/05.txt', 'r')
    program = list(map(int, inputs.read().split(',')))
    part_one(program)