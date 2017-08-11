#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 15:10
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : alg about palette

def sort_by_rgb(colors_tuple):
    """ colors_tuple contains color count and color RGB
        we want to sort the tuple by RGB
        tuple[1]
    """
    sorted_tuple = sorted(colors_tuple, key=lambda x:x[1])
    return sorted_tuple

def rgb_maximum(colors_tuple):
    """ 
        colors_r max min
        colors_g max min
        colors_b max min

    """
    r_sorted_tuple = sorted(colors_tuple, key=lambda x:x[1][0])
    g_sorted_tuple = sorted(colors_tuple, key=lambda x:x[1][1])
    b_sorted_tuple = sorted(colors_tuple, key=lambda x:x[1][2])

    r_min = r_sorted_tuple[0][1][0]
    g_min = g_sorted_tuple[0][1][1]
    b_min = b_sorted_tuple[0][1][2]

    r_max = r_sorted_tuple[len(colors_tuple)-1][1][0]
    g_max = g_sorted_tuple[len(colors_tuple)-1][1][1]
    b_max = b_sorted_tuple[len(colors_tuple)-1][1][2]

    return {
        "r_max":r_max,
        "r_min":r_min,
        "g_max":g_max,
        "g_min":g_min,
        "b_max":b_max,
        "b_min":b_min,
        "r_dvalue":(r_max-r_min)/3,
        "g_dvalue":(g_max-g_min)/3,
        "b_dvalue":(b_max-b_min)/3
    }

def group_by_accuracy(sorted_tuple, accuracy=3):
    """ group the colors by the accuaracy was given
        the R G B colors will be depart to accuracy parts
        default accuracy = 3
        d_value = (max-min)/3
        [min, min+d_value), [min+d_value, min+d_value*2), [min+d_value*2, max)
    """
    rgb_maximum_json = rgb_maximum(sorted_tuple)
    r_min = rgb_maximum_json["r_min"]
    g_min = rgb_maximum_json["g_min"]
    b_min = rgb_maximum_json["b_min"]
    r_dvalue = rgb_maximum_json["r_dvalue"]
    g_dvalue = rgb_maximum_json["g_dvalue"]
    b_dvalue = rgb_maximum_json["b_dvalue"]

    rgb = [
            [[[], [], []], [[], [], []], [[], [], []]],
            [[[], [], []], [[], [], []], [[], [], []]],
            [[[], [], []], [[], [], []], [[], [], []]]
        ]

    for color_tuple in sorted_tuple:
        r_tmp_i = color_tuple[1][0]
        g_tmp_i = color_tuple[1][1]
        b_tmp_i = color_tuple[1][2]
        r_idx = 0 if r_tmp_i < (r_min+r_dvalue) else 1 if r_tmp_i < (r_min+r_dvalue*2) else 2
        g_idx = 0 if g_tmp_i < (g_min+g_dvalue) else 1 if g_tmp_i < (g_min+g_dvalue*2) else 2
        b_idx = 0 if b_tmp_i < (b_min+b_dvalue) else 1 if b_tmp_i < (b_min+b_dvalue*2) else 2
        rgb[r_idx][g_idx][b_idx].append(color_tuple)

    return rgb


def get_weighted_mean(grouped_image_color):
    """ calculate every group's weighted mean

        r_weighted_mean = sigma(r * count) / sigma(count)
        g_weighted_mean = sigma(g * count) / sigma(count)
        b_weighted_mean = sigma(b * count) / sigma(count)
    """
    sigma_count = 0
    sigma_r = 0
    sigma_g = 0
    sigma_b = 0

    for item in grouped_image_color:
        sigma_count += item[0]
        sigma_r += item[1][0] * item[0]
        sigma_g += item[1][1] * item[0]
        sigma_b += item[1][2] * item[0]

    r_weighted_mean = int(sigma_r / sigma_count)
    g_weighted_mean = int(sigma_g / sigma_count)
    b_weighted_mean = int(sigma_b / sigma_count)
    
    weighted_mean = (sigma_count, (r_weighted_mean, g_weighted_mean, b_weighted_mean))
    return weighted_mean
