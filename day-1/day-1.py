"""
https://adventofcode.com/2019/day/1
"""
with open('day-1.input', 'r') as input_f:
    modules_mass = [int(line) for line in input_f.read().splitlines()]


# Star 1
def simple_fuel_calculator(mass):
    return mass // 3 - 2

answer_1 = sum(map(simple_fuel_calculator, modules_mass))

print(f'Answer 1: {answer_1}')


# Star 2
def accurate_fuel_calculator(mass):
    required_fuel_mass = simple_fuel_calculator(mass)
    if required_fuel_mass <= 0:
        return 0
    else:
        return required_fuel_mass + accurate_fuel_calculator(required_fuel_mass)

answer_2 = sum(map(accurate_fuel_calculator, modules_mass))

print(f'Answer 2: {answer_2}')
