_SAFE_COMB_EXAMPLE = [(0, 0), (6, 1), (4, 2), (7, 3),
                      (1, 4), (3, 5), (5, 6), (2, 7)]


def check_intersecting_lines(combinations: list) -> bool:
    tempo_dict = {}
    revers_dict = {}
    for i in combinations:
        tempo_dict[i[0]] = i[1]
        revers_dict[i[1]] = i[0]
    if tempo_dict.__len__() != 8 or revers_dict.__len__() != 8:
        return False
    return True


print(check_intersecting_lines(_SAFE_COMB_EXAMPLE))
