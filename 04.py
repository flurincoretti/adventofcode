def has_adjacent_digits(password):
    digit = password % 10
    while password != 0:
        password = password // 10
        if digit == password % 10:
            return True
        else:
            digit = password % 10
    return False


def has_two_adjacent_digits(password):
    adjacent_digits = {}
    digit = password % 10
    while password != 0:
        password = password // 10
        if digit == password % 10:
            if digit in adjacent_digits.keys():
                adjacent_digits[digit] += 1
            else:
                adjacent_digits[digit] = 2
        else: 
            digit = password % 10
    if 2 in adjacent_digits.values():
        return True
    else:
        return False


def has_decreasing_digits(password):
    digit = password % 10
    while password != 0:
        password = password // 10
        if digit < password % 10:
            return True
        else:
            digit = password % 10
    return False


def part_one(passwords):
    count = 0
    for password in passwords:
        if has_adjacent_digits(password) and \
            not has_decreasing_digits(password):
            count += 1
    print("Number of passwords meeting the criteria: {}".format(count))


def part_two(passwords):
    count = 0
    for password in passwords:
        if has_two_adjacent_digits(password) and \
            not has_decreasing_digits(password):
            count += 1
    print("Number of passwords meeting the criteria: {}".format(count))


if __name__ == "__main__":
    passwords = range(152085, 670283)
    part_one(passwords)
    part_two(passwords)