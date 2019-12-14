"""
https://adventofcode.com/2019/day/2
"""
import itertools
from operator import add, mul


with open('day-2.input_1', 'r') as input_f1, open('day-2.input_2', 'r') as input_f2:
    program = [int(value) for value in input_f1.read().split(',')]
    expected_output = int(input_f2.read())


# Star 1
operations = {
    1: add,
    2: mul,
}


def run_program(program, index):
    opcode = program[index]
    if opcode == 99:
        return program

    op1, op2 = [program[j] for j in program[index + 1:index + 3]]
    result_index = program[index + 3]
    program[result_index] = operations[opcode](op1, op2)

    return run_program(program, index + 4)


memory = [program[0]] + [12, 2] + program[3:]
answer_1 = run_program(memory, 0)[0]
print(f'Answer 1: {answer_1}')


# Star 2
for noun, verb in itertools.product(range(100), range(100)):
    memory = [program[0]] + [noun, verb] + program[3:]
    if run_program(memory, 0)[0] == expected_output:
        break

answer_2 = 100 * noun + verb
print(f'Answer 2: {answer_2}')
