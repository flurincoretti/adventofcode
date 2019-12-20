def get_pixel_color(stack):
    i = 0
    while stack[i] == 2: 
        i += 1
    return stack[i]


def print_image(image, width, height):
    for y in range(height):
        for x in range(width):
            if image[y][x] == 1:
                print('x', end='')
            else:
                print(' ', end='')
        print('')


def part_one(encoded_image, width, height):
    layers = [encoded_image[i:i+width*height] \
        for i in range(0, len(encoded_image), width*height)]
    zeros = [layer.count(0) for layer in layers]
    index = zeros.index(min(zeros))
    result = layers[index].count(1) * layers[index].count(2)
    print(result)


def part_two(encoded_image, width, height):
    layers = [encoded_image[i:i+width*height] \
        for i in range(0, len(encoded_image), width*height)]
    stacks = [[layer[i] for layer in layers] for i in range(width * height)]
    colors = [get_pixel_color(stack) for stack in stacks]
    image = [colors[i:i+width] for i in range(0, len(colors), width)]
    print_image(image, 25, 6)


if __name__ == "__main__":
    inputs = open('inputs/08.txt', 'r')
    encoded_image = list(map(int, inputs.read()))

    print("Part 1:")
    part_one(encoded_image, 25, 6)

    print("Part 2:")
    part_two(encoded_image, 25, 6)