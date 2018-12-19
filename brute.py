from copy import deepcopy
from utils import matrix_copy_from_to, can_procced_with_group

def brute(C, b, constraints, c_to_group, x, n_pairs_wanted, n_pairs_found, curr_min,
          curr_min_x, is_r_used, is_c_used):

    is_full = True
    for c, v in enumerate(constraints):
        if v < b[c]:
            is_full = False

    # this route can't be continued
    if is_full or n_pairs_found == n_pairs_wanted:
        new_min = 0
        for r in range(len(x)):
            for c in range(len(x[0])):
                if x[r][c] == 1:
                    new_min += C[r][c]

        if new_min < curr_min[0]:
            curr_min[0] = new_min
            matrix_copy_from_to(x, curr_min_x)

        return

    # this route can be continued - try all possible variants
    for r in range(len(x)):
        if is_r_used[r]:
            continue

        is_r_used[r] = True
        for c in range(len(x[0])):

            if is_c_used[c]:
                continue

            if x[r][c] == 1:
                continue

            group_number = c_to_group[c]
            if not can_procced_with_group(group_number, constraints, b):
                continue

            n_pairs_found += 1
            constraints[group_number] += 1
            x[r][c] = 1
            is_c_used[c] = True

            brute(C, b, constraints, c_to_group, x, n_pairs_wanted, n_pairs_found,
                  curr_min, curr_min_x, is_r_used, is_c_used)

            n_pairs_found -= 1
            constraints[group_number] -= 1
            x[r][c] = 0
            is_c_used[c] = False

        is_r_used[r] = False


def brute_solution(C, b, c_to_group, n_pairs_wanted, max_v):
    constraints = deepcopy(b)
    for c in range(len(constraints)):
        constraints[c] = 0

    curr_min_x = [[0 for c in range(len(C[0]))] for r in range(len(C))]
    x = deepcopy(curr_min_x)

    is_r_used = [False for r in range(len(C))]
    is_c_used = [False for c in range(len(C[0]))]

    curr_min = [max_v * 10 * n_pairs_wanted]
    brute(C, b, constraints, c_to_group, x, n_pairs_wanted, 0, curr_min, curr_min_x,
          is_r_used, is_c_used)
    return curr_min_x


def brute_no_restrictions(C, x, curr_min_x, curr_min, is_r_used, is_c_used, n_pairs_found):
    # no steps can be done, try to update min
    if n_pairs_found == len(x):
        new_min = 0
        for r in range(len(x)):
            for c in range(len(x[0])):
                new_min += C[r][c] * x[r][c]

        if new_min < curr_min[0]:
            curr_min[0] = new_min
            matrix_copy_from_to(x, curr_min_x)

        return

    # some steps can be done
    for r in range(len(x)):
        if is_r_used[r]:
            continue

        is_r_used[r] = True
        for c in range(len(x[0])):
            if is_c_used[c]:
                continue

            is_c_used[c] = True
            x[r][c] = 1

            brute_no_restrictions(C, x, curr_min_x, curr_min, is_r_used, is_c_used,
                                  n_pairs_found+1)

            x[r][c] = 0
            is_c_used[c] = False

        is_r_used[r] = False


def brute_solution_no_restrictions(C):
    x = deepcopy(C)
    for r in range(len(x)):
        for c in range(len(x[0])):
            x[r][c] = 0

    curr_min_x = deepcopy(x)
    curr_min = [1000000000000000000]

    is_r_used = [False for r in range(len(C))]
    is_c_used = [False for c in range(len(C[0]))]

    brute_no_restrictions(C, x, curr_min_x, curr_min, is_r_used, is_c_used, 0)

    return curr_min_x
