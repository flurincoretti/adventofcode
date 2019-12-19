def part_one(image, width, height):
    layers = [image[i:i+width*height] for i in range(0, len(image), width*height)]
    zeros = [layer.count(0) for layer in layers]
    index = zeros.index(min(zeros))
    result = layers[index].count(1) * layers[index].count(2)
    print(result)


if __name__ == "__main__":
    inputs = open('inputs/08.txt', 'r')
    encoded_image = list(map(int, inputs.read()))
    part_one(encoded_image, 25, 6)