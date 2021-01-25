import itertools


def possible_lower_and_upper_case_permutations(input_string):
    # uses the cartesian product https://docs.python.org/3/library/itertools.html#itertools.product
    map_object = map(
        "".join,
        itertools.product(
            *((letter.upper(), letter.lower()) for letter in input_string)
        ),
    )
    map_set = set(map_object)

    return list(map_set)
