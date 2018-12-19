from copy import deepcopy


def double_eq(d1, d2):
    return abs(d1 - d2) < 0.00001

def alternate_pairs(curr_path, edge_r_to_c, edge_c_to_r):
    n_vertexes = len(curr_path)
    assert n_vertexes % 2 == 0

    for i in range(n_vertexes - 1):
        if i % 2 == 0:
            r = curr_path[i]
            c = curr_path[i+1]

            edge_r_to_c[r] = c
            edge_c_to_r[c] = r

    return True


def DFS(idx, r_or_c, curr_path, edge_r_to_c, edge_c_to_r, is_r_visited, is_c_visited,
        r_visited_overall, c_visited_overall, u, v, T, n_pairs_found):

    if r_or_c == 'r':
        r = idx

        r_visited_overall[r] = True
        is_r_visited[r] = True
        curr_path.append(r)

        for c in range(len(T)):
            if is_c_visited[c]:
                continue

            if double_eq(T[r][c] - u[r] - v[c], 0):
                if DFS(c, 'c', curr_path, edge_r_to_c, edge_c_to_r,
                       is_r_visited, is_c_visited,
                       r_visited_overall, c_visited_overall, u, v, T, n_pairs_found):
                    return True

        curr_path.pop()
        is_r_visited[r] = False

        return False

    if r_or_c == 'c':
        c = idx

        c_visited_overall[c] = True
        is_c_visited[c] = True
        curr_path.append(c)

        # 'c' IS NOT saturated
        if edge_c_to_r[c] == -1:
            ok = alternate_pairs(curr_path, edge_r_to_c, edge_c_to_r)

            if ok:
                n_pairs_found[0] += 1
                return True
            else:
                curr_path.pop()
                is_c_visited[c] = False
                return False

        # 'c' IS saturated
        r = edge_c_to_r[c]

        if not is_r_visited[r] and double_eq(T[r][c] - u[r] - v[c], 0):
            if DFS(r, 'r', curr_path, edge_r_to_c, edge_c_to_r,
                   is_r_visited, is_c_visited,
                   r_visited_overall, c_visited_overall, u, v, T, n_pairs_found):
                return True
            else:
                is_c_visited[c] = False
                curr_path.pop()
                return False


    assert False


def hungarrian_solution(T, n_pairs_needed):
    assert len(T) == len(T[0])
    n = len(T)

    u = [0 for _ in range(n)]
    v = [0 for _ in range(n)]

    # egde_r_to_c[r] = c - means that there is a edge between 'r' and 'c'
    # if edge_r_to_c[r] = -1 then there is no edge starting in 'r'
    edge_r_to_c = [-1 for _ in range(n)]
    edge_c_to_r = [-1 for _ in range(n)]

    is_r_visited = [False for _ in range(n)]
    is_c_visited = [False for _ in range(n)]

    r_visited_overall = [False for _ in range(n)]
    c_visited_overall = [False for _ in range(n)]

    curr_path = []
    n_pairs_found = [0]

    while n_pairs_found[0] < n_pairs_needed:
        for r in range(n):
            if edge_r_to_c[r] == -1:
                DFS(r, 'r', curr_path, edge_r_to_c, edge_c_to_r,
                    is_r_visited, is_c_visited,
                    r_visited_overall, c_visited_overall, u, v, T, n_pairs_found)

                if n_pairs_found[0] == n_pairs_needed:
                    break

        # clean up after we are done with this potential
        for i in range(n):
            is_r_visited[i] = False
            is_c_visited[i] = False
        curr_path.clear()

        # calculate new potential and clean up 'r_visited_overall' & 'c_visited_overall'
        delta = 100000000000000
        for r in range(n):
            if not r_visited_overall[r]:
                continue

            for c in range(n):
                if c_visited_overall[c]:
                    continue

                d = T[r][c] - u[r] - v[c]
                delta = d if d < delta else delta

        for i in range(n):
            if r_visited_overall[i]:
                u[i] += delta

            if c_visited_overall[i]:
                v[i] -= delta

        for i in range(n):
            r_visited_overall[i] = False
            c_visited_overall[i] = False

    # prepare 'x' output matrix from egde_r_to_c
    x = deepcopy(T)
    for r in range(n):
        for c in range(n):
            x[r][c] = 0

    for r, c in enumerate(edge_r_to_c):
        if c != -1:
            x[r][c] = 1

    return x
