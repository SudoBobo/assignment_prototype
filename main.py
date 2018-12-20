import random
from utils import print_matrix, cmp_matrix
from normal import normal_solution
from brute import brute_solution, brute_solution_no_restrictions
from hungarrian_solution import hungarrian_solution

rows = 4
columns = 4

min_v = 300.0
max_v = 3000.0

attempts = 10
print("attempts " + str(attempts))
for i in range(attempts):
    C = [[-1 for c in range(columns)] for r in range(rows)]
    for r in range(rows):
        for c in range(columns):
            C[r][c] = random.uniform(min_v, max_v)

    # C = [
    #     [1330.1526173036332, 2955.8492202132848, 1364.7301690624388, 1871.450083667714],
    #     [1081.7282287679386, 1537.7877635505254, 1753.1006904216633, 2446.1148165942736],
    #     [1838.1094737402227, 2274.609279030032, 1049.9066183529856, 1952.9468231189599],
    #     [1473.6446717239182, 2372.550047682343, 1522.3678850970944, 301.80743491199837],
    # ]

    # C = [
    #     [1787.0674817309773, 527.3881430327431, 668.602849005842, 2289.600489287004],
    #     [1779.803354085787, 2830.8608614469017, 2110.569070184975, 2378.3034466882327],
    #     [2454.9269934359263, 1428.4210257424468, 1281.4336401889386, 2538.626794757056],
    #     [631.1945775522822, 2492.307738309523, 837.7167730054113, 764.2822661052675],
    # ]

    # number of constraints (groups)
    k = 2
    c_to_group = [0, 0, 1, 1]

    # b_k
    b = [1, 2]

    # d_ij_k
    G = [
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
        ],
        [
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 1, 1],
        ]
    ]

    # step size
    a = 1
    # TODO fix this, it's really strange

    lmbd = [min_v, min_v]

    N = 10000

    n_pairs_wanted = 2

    x = normal_solution(C, b, G, a, lmbd, N, c_to_group, n_pairs_wanted)
    x_exp = brute_solution(C, b, c_to_group, n_pairs_wanted, max_v)

    if not cmp_matrix(x, x_exp):
        print("attempt number " + str(i) + " broke")
        print_matrix(C)
        print("expected")
        print_matrix(x_exp)
        print("calculated")
        print_matrix(x)
        assert False

print("all fine")