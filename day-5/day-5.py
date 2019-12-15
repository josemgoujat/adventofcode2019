"""
https://adventofcode.com/2019/day/5
"""
with open('day-5.input', 'r') as input_f:
    program = [value for value in input_f.read().split(',')]


# Star 1
class EndOfProgramException(Exception):
    pass


def parse_operand(program, mode, operand):
    return program[int(operand)] if mode == '0' else operand


def op_add(program, operands):
    program[int(operands[2][1])] = str(int(parse_operand(program, *operands[0])) + int(parse_operand(program, *operands[1])))
    return program


def op_mul(program, operands):
    program[int(operands[2][1])] = str(int(parse_operand(program, *operands[0])) * int(parse_operand(program, *operands[1])))
    return program


def op_write(program, operands):
    program[int(operands[0][1])] = input()
    return program


def op_read(program, operands):
    print(program[int(operands[0][1])])
    return program


def op_exit(program, operands):
    raise EndOfProgramException()


operations = {
    '01': {
        'n_operands': 3,
        'function': op_add,
    },
    '02': {
        'n_operands': 3,
        'function': op_mul,
    },
    '03': {
        'n_operands': 1,
        'fixed_modes': ['1'],
        'function': op_write,
    },
    '04': {
        'n_operands': 1,
        'fixed_modes': ['1'],
        'function': op_read,
    },
    '99': {
        'n_operands': 0,
        'function': op_exit,
    },
}


def run_instruction(program, i):
    code = program[i][-2:].zfill(2)
    n_operands = operations[code]['n_operands']

    operands = program[i + 1:i + 1 + n_operands] if n_operands else []
    modes = operations[code].get('fixed_modes') or (reversed(list(program[i][:-2].zfill(n_operands))) if n_operands else [])
    modes_and_operands = [(mode, operand) for mode, operand in zip(modes, operands)]

    program = operations[code]['function'](program, modes_and_operands)
    return program, i + n_operands + 1


def run(program):
    i = 0
    try:
        while True:
            program, i = run_instruction(program, i)
    except EndOfProgramException:
        return


run(program)
