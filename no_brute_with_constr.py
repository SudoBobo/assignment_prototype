import sys
from fully_random import prepare_random_data
from normal import normal_solution

def is_constraints_satisfied(x, b, c_to_group):
    group_counters = [0 for _ in range(len(b))]

    for r in range(len(x)):
        for c in range(len(x)):
            if x[r][c] == 1:
                group_counters[c_to_group[c]] += 1

    for g in range(len(b)):
        if b[g] < group_counters[g]:
            return False
    return True

def main():
    min_v = 100.0
    max_v = 10000.0
    min_n = 20
    max_n = 20


    n_cases = 10
    n_cases_constr_broken = 0
    for case in range(n_cases):
        C, c_to_group, b, G, n_pairs_needed = prepare_random_data(min_v, max_v, min_n, max_n)

        a = 1
        lmbd = [min_v] * len(b)
        N = 10000

        x = normal_solution(C, b, G, a, lmbd, N, c_to_group, n_pairs_needed)
        if not is_constraints_satisfied(x, b, c_to_group):
            n_cases_constr_broken += 1

    print("constraints violated in {}/{} cases".format(n_cases_constr_broken, n_cases))



if __name__ == "__main__":
    sys.exit(main())
