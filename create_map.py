import numpy as np
import random


def put_zeros_before_int(i):
    i = str(i)
    l = len(i)
    while l < 2:
        i = '0' + i
        l += 1
    return i


class Error(Exception):
    pass


class MapDimensionError(Error):
    pass


def create_random_map(map_dimensions: tuple, percentage_obstacles: float):
    try:
        if map_dimensions[0] > 100 or map_dimensions[1] > 100:
            raise MapDimensionError
    except MapDimensionError:
        print('Dimensions of the map should be inferior than 100')
        return
    map_arr = np.ones(map_dimensions)
    allowed_cells = []
    blocked_cells = []
    for i in range(map_dimensions[0]):
        for j in range(map_dimensions[1]):
            if random.uniform(0, 1) < percentage_obstacles:
                map_arr[i, j] = 0
                blocked_cells.append(put_zeros_before_int(i) + put_zeros_before_int(j))
            else:
                allowed_cells.append(put_zeros_before_int(i) + put_zeros_before_int(j))
    map_dict = {}
    for i in range(map_dimensions[0]):
        for j in range(map_dimensions[1]):
            if put_zeros_before_int(i) + put_zeros_before_int(j) in allowed_cells:
                map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)] = {}
                if put_zeros_before_int(i - 1) + put_zeros_before_int(j - 1) in allowed_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i - 1) + put_zeros_before_int(j - 1)] = 14
                if put_zeros_before_int(i - 1) + put_zeros_before_int(j + 1) in allowed_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i - 1) + put_zeros_before_int(j + 1)] = 14
                if put_zeros_before_int(i + 1) + put_zeros_before_int(j - 1) in allowed_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i + 1) + put_zeros_before_int(j - 1)] = 14
                if put_zeros_before_int(i + 1) + put_zeros_before_int(j + 1) in allowed_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i + 1) + put_zeros_before_int(j + 1)] = 14
                if put_zeros_before_int(i) + put_zeros_before_int(j - 1) in allowed_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i) + put_zeros_before_int(j - 1)] = 10
                if put_zeros_before_int(i - 1) + put_zeros_before_int(j) in allowed_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i - 1) + put_zeros_before_int(j)] = 10
                if put_zeros_before_int(i) + put_zeros_before_int(j + 1) in allowed_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i) + put_zeros_before_int(j + 1)] = 10
                if put_zeros_before_int(i + 1) + put_zeros_before_int(j) in allowed_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i + 1) + put_zeros_before_int(j)] = 10
    return map_arr, map_dict


def create_map_visualizer(map_dims, blocked_cells):
    map_dict = {}
    for i in range(map_dims[0]):
        for j in range(map_dims[1]):
            if put_zeros_before_int(i) + put_zeros_before_int(j) not in blocked_cells:
                map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)] = {}
                if put_zeros_before_int(i - 1) + put_zeros_before_int(j - 1) not in blocked_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i - 1) + put_zeros_before_int(j - 1)] = 14
                if put_zeros_before_int(i - 1) + put_zeros_before_int(j + 1) not in blocked_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i - 1) + put_zeros_before_int(j + 1)] = 14
                if put_zeros_before_int(i + 1) + put_zeros_before_int(j - 1) not in blocked_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i + 1) + put_zeros_before_int(j - 1)] = 14
                if put_zeros_before_int(i + 1) + put_zeros_before_int(j + 1) not in blocked_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i + 1) + put_zeros_before_int(j + 1)] = 14
                if put_zeros_before_int(i) + put_zeros_before_int(j - 1) not in blocked_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i) + put_zeros_before_int(j - 1)] = 10
                if put_zeros_before_int(i - 1) + put_zeros_before_int(j) not in blocked_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i - 1) + put_zeros_before_int(j)] = 10
                if put_zeros_before_int(i) + put_zeros_before_int(j + 1) not in blocked_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i) + put_zeros_before_int(j + 1)] = 10
                if put_zeros_before_int(i + 1) + put_zeros_before_int(j) not in blocked_cells:
                    map_dict[put_zeros_before_int(i) + put_zeros_before_int(j)][
                        put_zeros_before_int(i + 1) + put_zeros_before_int(j)] = 10
    return map_dict