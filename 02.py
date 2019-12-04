def intcode_processor(intcode):
    for i in range(0, len(intcode)-1, 4):
        opcode = intcode[i]
        if opcode == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        elif opcode == 2:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
        elif opcode == 99:
            break
        else:
            return
    return intcode


def part_one(intcode):
    new_intcode = intcode.copy()
    new_intcode[1] = 12
    new_intcode[2] = 2
    result = intcode_processor(new_intcode)
    return result[0]


def part_two(intcode):
    for noun in range(100):
        for verb in range(100):
            new_intcode = intcode.copy()
            new_intcode[1] = noun
            new_intcode[2] = verb
            result = intcode_processor(new_intcode)
            if result[0] == 19690720:
                return 100 * noun + verb


if __name__ == "__main__":
    inputs = open('inputs/02.txt', 'r')
    intcode = list(map(int, inputs.read().split(',')))
    print("Answer (part 1): {}".format(part_one(intcode)))
    print("Answer (part 2): {}".format(part_two(intcode)))
