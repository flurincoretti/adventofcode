def calc_fuel(mass):
    return mass // 3 - 2


def rec_calc_fuel(mass):
    fuel = calc_fuel(mass)
    if fuel <= 0: 
        return 0
    else:
        return fuel + rec_calc_fuel(fuel)


def main():
    with open('inputs/01.txt', 'r') as inputs:
        masses = list(map(int, inputs))
        # Part 1
        fuel = [calc_fuel(mass) for mass in masses]
        print("Fuel requirements (part 1): {}".format(sum(fuel)))
        # Part 2
        fuel = [rec_calc_fuel(mass) for mass in masses]
        print("Fuel requirements (part 2): {}".format(sum(fuel)))


if __name__ == "__main__":
    main()