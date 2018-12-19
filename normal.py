from brute import brute_solution_no_restrictions, brute_solution
from copy import deepcopy

def calc_subgradient(x, G, b):
    subgradient = [-1.0 * b[k] for k in range(len(b))]

    for k in range(len(b)):
        for r in range(len(x)):
            for c in range(len(x[0])):
                subgradient[k] += (G[k][r][c] * x[r][c])

    return subgradient


def normal_solution(C, b, G, a, lmbd, N, c_to_group):
    rows = len(C)
    columns = len(C[0])

    solution = None
    while N > 0:
        # calc new matrix
        T = deepcopy(C)
        for r in range(rows):
            for c in range(columns):
                for k in range(len(lmbd)):
                    T[r][c] += (G[k][r][c] * lmbd[k])

        # x = brute_solution_no_restrictions(T)

        max_v = 100000000000
        x = brute_solution(T, b, c_to_group, len(C), max_v)
        solution = x

        subgradient = calc_subgradient(x, G, b)
        eq_zero = True
        for v in subgradient:
            if abs(v) > 0.0001:
                eq_zero = False

        if eq_zero:
            break

        # TODO add this abs magic here
        for l in range(len(lmbd)):
            lmbd[l] += (a * subgradient[l])
            lmbd[l] = abs(lmbd[l])

        N -= 1

    return solution
