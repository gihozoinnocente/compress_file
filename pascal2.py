#!/usr/bin/python3


def pascals_triangle(n):
    if n <= 0:
        return 0

    T = []
    for i in range(n):
        r = [1]
        if i > 0:
            prev_r = T[-1]
            for j in range(1, i):
                r.append(prev_r[j - 1] + prev_r[j])
            r.append(1)
        T.append(r)
    return T


n = 5
result = pascals_triangle(n)
print(result)
