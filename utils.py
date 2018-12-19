def print_matrix(m):
    rows = len(m)
    columns = len(m[0])

    for r in range(rows):
        print(" ")
        for c in range(columns):
            if m[r][c] == -1:
                end = '  '
            else:
                end = ' '
            print(m[r][c], end=end)
    print(" ")


def cmp_matrix(m1, m2):
    rows = len(m1)
    columns = len(m1[0])

    for r in range(rows):
        for c in range(columns):
            if m1[r][c] != m2[r][c]:
                return False
    return True


def matrix_copy_from_to(from_m, to_x):
    rows = len(from_m)
    columns = len(from_m[0])

    for r in range(rows):
        for c in range(columns):
            to_x[r][c] = from_m[r][c]


def can_procced_with_group(group_number, constraints, b):
    return constraints[group_number] < b[group_number]

def print_vec(v):
    for e in v:
        print(e, end=' ')
    print('\n')