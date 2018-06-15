import numpy as np
from datetime import datetime as dt
from random import randint

def get_most_color(weighted_colors):
    rgb_cube = group_colors_by_cube(weighted_colors)
    start = dt.now()
    weight = 0
    color = None
    for i in range(3):
        for j in range(3):
            for k in range(3):
                tmp_weight = len(rgb_cube[i][j][k])
                if tmp_weight > weight:
                    weight = tmp_weight
                    npa_rgbs = np.array(rgb_cube[i][j][k])
                    ave_rgb = list(np.average(npa_rgbs, axis=0))
                    color = list(map(int, ave_rgb))
    end = dt.now()
    return color


def group_colors_by_cube(weighted_colors):
    """
    group colors to a 3*3*3 cube,
    three axis stand for r, g, b
    departed by the value like
    [0,85) -> 0, [85,170) -> 1, [170, 256) -> 2

    :param weighted_colors: [(weight, (r, g, b)), ...]
    :return:
    """

    rgb_cube = [
            [[[], [], []], [[], [], []], [[], [], []]],
            [[[], [], []], [[], [], []], [[], [], []]],
            [[[], [], []], [[], [], []], [[], [], []]]
        ]

    for weighted_color in weighted_colors:
        weight = weighted_color[0]
        color_rgb = weighted_color[1]
        x, y, z = __locate_color_by_cube(color_rgb)
        for w in range(weight):
            rgb_cube[x][y][z].append(list(color_rgb))
    return rgb_cube


def __locate_color_by_cube(color_rgb):
    x = y = z = None
    location = [x, y, z]
    for i in range(3):
        elem = color_rgb[i]
        if elem < 85:
            location[i] = 0
        elif 85 <= elem < 170:
            location[i] = 1
        else:
            location[i] = 2

    return location


# ==================================================================

def k_means(k, weighted_colors):
    # k 个cluster的而为数组
    clusters_arr = __init_clusters(k, weighted_colors, True)
    # 所有颜色的二维数组
    # 解包为[weight, r, g, b]
    colors_arr = __tile_weighted_colors(weighted_colors)

    palette = []
    weights = []

    recursion_times = 0
    old_offset_sum = None
    new_offset_sum = None

    while new_offset_sum is None \
            or old_offset_sum is None \
            or (new_offset_sum / old_offset_sum < 0.99 and recursion_times < 10):
        if new_offset_sum is not None and old_offset_sum is not None:
            print("Recursion {0} gets an optimization rate: {1}".format(
                recursion_times, new_offset_sum / old_offset_sum
            ))

        start = dt.now()
        old_offset_sum = new_offset_sum
        new_offset_sum = 0

        palette = []
        weights = []

        clusted_colors = []
        for _ in range(k):
            clusted_colors.append(np.array([]))

        for color_arr in colors_arr:
            tile_color_arr = np.tile(color_arr[1:], (k, 1))
            tmp_arr = (tile_color_arr - clusters_arr) ** 2
            tmp_distance_arr = np.sqrt(np.sum(tmp_arr, axis=1))
            nearest_cluster_index = tmp_distance_arr.argmin()
            clusted_colors[nearest_cluster_index] = np.append(clusted_colors[nearest_cluster_index], color_arr)

        for i in range(k):
            # 算入palette & weights
            clusted_colors[i] = clusted_colors[i].reshape(len(clusted_colors[i]) // 4, 4)
            tmp_arr = clusted_colors[i].copy()
            tmp_weights = np.sum(tmp_arr[:, 0])
            for j in range(3):
                tmp_arr[:, 1+j] = tmp_arr[:, 1+j] * tmp_arr[:, 0]
            average_rgb_i = (np.sum(tmp_arr[:, 1:], axis=0) / tmp_weights).tolist()
            # average_rgb_i = np.average(clusted_colors[i][:, 1:] * clusted_colors[i][:, 0], axis=0).tolist()
            average_rgb_i = list(map(int, average_rgb_i))
            palette.append(average_rgb_i)
            weights.append(tmp_weights)

        # 使用新形成的palette作为cluster，计算offset
        palette_arr = np.array(palette)
        for i in range(k):
            ave_color_arr = palette_arr[i]
            clusted_color_arr = clusted_colors[i]
            tile_ave_arr = np.tile(ave_color_arr, (len(clusted_color_arr), 1))
            tmp_arr = (tile_ave_arr - clusted_color_arr[:, 1:]) ** 2
            tmp_distance_arr = np.sqrt(np.sum(tmp_arr, axis=1))
            new_offset_sum += np.sum(tmp_distance_arr)

        end = dt.now()
        print("K-MEANS recursion {0} time, takes {1}".format(recursion_times + 1, end - start))

        clusters_arr = palette_arr.copy()
        recursion_times += 1

    print("Stop Recursion by a Optimization Rate: {}".format(new_offset_sum / old_offset_sum))
    print()

    return palette, weights


def __init_clusters(k, weighted_colors, random=False):
    clusters = []
    length = len(weighted_colors)
    if random:
        for i in range(k):
            r = randint(0, length)
            cluster = weighted_colors[r][1]
            clusters.append(cluster)
    else:
        for i in range(k):
            clusters.append(list(weighted_colors[i * length // k][1]))
    return np.array(clusters)


def __tile_weighted_colors(weighted_colors):
    colors = []
    for weight, color in weighted_colors:
        colors.append([weight, *color])
    return np.array(colors)
