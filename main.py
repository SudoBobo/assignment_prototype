import random
from utils import print_matrix, cmp_matrix
from normal import normal_solution
from brute import brute_solution, brute_solution_no_restrictions

rows = 4
columns = 4

min_v = 300.0
max_v = 3000.0

# C = [[-1 for c in range(columns)] for r in range(rows)]
# for r in range(rows):
#     for c in range(columns):
#         C[r][c] = random.uniform(min_v, max_v)

C = [
    [1330.1526173036332, 2955.8492202132848, 1364.7301690624388, 1871.450083667714],
    [1081.7282287679386, 1537.7877635505254, 1753.1006904216633, 2446.1148165942736],
    [1838.1094737402227, 2274.609279030032, 1049.9066183529856, 1952.9468231189599],
    [1473.6446717239182, 2372.550047682343, 1522.3678850970944, 301.80743491199837],
]

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
a = 0.01
lmbd = [0, 0]

N = 100

n_pairs_wanted = 4
x = normal_solution(C, b, G, a, lmbd, N, c_to_group)
x_exp = brute_solution(C, b, c_to_group, n_pairs_wanted, max_v)
x_dumb = brute_solution_no_restrictions(C)

# print_matrix(x_dumb)
print(cmp_matrix(x, x_exp))

print_matrix(C)
print("expected")
print_matrix(x_exp)
print("calculated")
print_matrix(x)