def check_intersecting_lines(combinations: list) -> bool:
    values_x_axis: set = {}
    values_y_axis: set = {}
    for i in combinations:
        values_x_axis[i[0]] = i[1]
        values_y_axis[i[1]] = i[0]
    if values_x_axis.__len__() != 8 or values_y_axis.__len__() != 8:
        return False
    return True
