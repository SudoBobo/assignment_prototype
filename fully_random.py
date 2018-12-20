from random import randint, uniform
import math

from brute import brute_solution
from normal import normal_solution
from utils import cmp_matrix, print_matrix


def prepare_random_data(min_v, max_v):
    rows = randint(3, 7)
    columns = rows

    C = [[-1 for c in range(columns)] for r in range(rows)]

    for r in range(rows):
        for c in range(columns):
            C[r][c] = uniform(min_v, max_v)

    c_to_group = []
    b = []

    groups_ends = []
    last = 0
    while last < columns - 1:
        groups_ends.append(randint(last + 1, columns - 1))
        last = groups_ends[-1]

    beg = 0
    for g, end in enumerate(groups_ends):
        b.append(randint(1, 1 + math.ceil((end - beg) / 2)))
        while beg <= end:
            c_to_group.append(g)
            beg += 1

    n_groups = len(groups_ends)
    assert len(c_to_group) == columns
    assert n_groups == len(b)

    # generate appropriate G
    G = [[[None for _ in range(columns)] for _ in range(rows)] for _ in range(n_groups)]

    for group_number in range(n_groups):
        for r in range(rows):
            for c in range(columns):
                if c_to_group[c] == group_number:
                    G[group_number][r][c] = 1
                else:
                    G[group_number][r][c] = 0

    n_pairs_needed = randint(1, rows)
    return C, c_to_group, b, G, n_pairs_needed

min_v = 100.0
max_v = 10000.0


n_cases = 10
for case in range(n_cases):
    print("case {}".format(case))

    C, c_to_group, b, G, n_pairs_needed = prepare_random_data(min_v, max_v)

    a = 1
    # TODO fix this, it's really strange
    lmbd = [min_v] * len(b)

    N = 10000

    x = normal_solution(C, b, G, a, lmbd, N, c_to_group, n_pairs_needed)
    x_exp = brute_solution(C, b, c_to_group, n_pairs_needed, max_v)

    if not cmp_matrix(x, x_exp):
        print("b")
        print(*b, sep=' ')
        print("c_to_group")
        print(*c_to_group, sep=' ')
        print("attempt number " + str(case) + " broke")
        # print_matrix(C)
        print("expected")
        print_matrix(x_exp)
        print("calculated")
        print_matrix(x)
        assert False

print("all {} cases passed successful".format(n_cases))