"""
https://adventofcode.com/2019/day/4
"""
with open('day-4.input', 'r') as input_f:
    range_min, range_max = input_f.read().split('-')


# Star 1
def valid_passwords(range_min, range_max, extra_adjacency_check_func=lambda partial: True):
    options = '0123456789'
    partials = [(options[i], False) for i in range(int(range_min[0]), int(range_max[0]) + 1)]
    valid = []
    while partials:
        partial, has_adjacent_numbers = partials.pop()
        if len(partial) == 6 and has_adjacent_numbers and extra_adjacency_check_func(partial):
            valid.append(partial)
        elif len(partial) < 6:
            for option in options[int(partial[-1]):]:
                new_partial = partial + option
                if int(range_min[:len(new_partial)]) <= int(new_partial) <= int(range_max[:len(new_partial)]):
                    partials.append((new_partial, has_adjacent_numbers or option == partial[-1]))

    return valid


answer_1 = len(valid_passwords(range_min, range_max))
print(f'Answer 1: {answer_1}')


# Star 2
def valid_adjacency(partial):
    # TODO: find another way of checking this in the while loop.
    occurrences = {n: 0 for n in partial}
    for n in partial:
        occurrences[n] += 1
    return any([occurrences[n] == 2 for n in occurrences.keys()])


answer_2 = len(valid_passwords(range_min, range_max, valid_adjacency))
print(f'Answer 2: {answer_2}')
