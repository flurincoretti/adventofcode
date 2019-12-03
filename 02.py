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


def main():
    inputs = open('inputs/02.txt', 'r')
    intcode = list(map(int, inputs.read().split(',')))
    intcode[1] = 12
    intcode[2] = 2
    result = intcode_processor(intcode)
    print(result[0])


if __name__ == "__main__":
    main()