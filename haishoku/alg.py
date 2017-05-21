#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 15:10
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : alg about palette

import random

def clusterGen(k):
    """ generate k random colors
    """
    cluster = []
    for i in range(k):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        cluster.append((r, g, b))

    return cluster

def sort_by_rgb(colors_tuple):
    """ colors_tuple contains color count and color RGB
        we want to sort the tuple by RGB
        tuple[1]
    """
    sorted_tuple = sorted(colors_tuple, key=lambda x:x[1])
    return sorted_tuple

def group_by_accuracy(sorted_tuple, accuracy=3):
    """ group the colors by the accuaracy was given
        the R G B colors will be depart to accuracy parts
        default accuracy = 3

        [0, 85), [85, 170), [170, 256)
    """
    rgb = [
            [[[], [], []], [[], [], []], [[], [], []]],
            [[[], [], []], [[], [], []], [[], [], []]],
            [[[], [], []], [[], [], []], [[], [], []]]
        ]
    for color_tuple in sorted_tuple:
        r_tmp_i = color_tuple[1][0]
        g_tmp_i = color_tuple[1][1]
        b_tmp_i = color_tuple[1][2]
        if 0 <= r_tmp_i and 85 > r_tmp_i:
            if 0 <= g_tmp_i and 85 > g_tmp_i:
                if 0 <= b_tmp_i and 85 > b_tmp_i:
                    rgb[0][0][0].append(color_tuple)
                elif 85 <= b_tmp_i and 170 > b_tmp_i:
                    rgb[0][0][1].append(color_tuple)
                else:
                    rgb[0][0][2].append(color_tuple)

            elif 85 <= g_tmp_i and 170 > g_tmp_i:
                if 0 <= b_tmp_i and 85 > b_tmp_i:
                    rgb[0][1][0].append(color_tuple)
                elif 85 <= b_tmp_i and 170 > b_tmp_i:
                    rgb[0][1][1].append(color_tuple)
                else:
                    rgb[0][1][2].append(color_tuple)
            else:
                if 0 <= b_tmp_i and 85 > b_tmp_i:
                    rgb[0][2][0].append(color_tuple)
                elif 85 <= b_tmp_i and 170 > b_tmp_i:
                    rgb[0][2][1].append(color_tuple)
                else:
                    rgb[0][2][2].append(color_tuple) 
        elif 85 <= r_tmp_i and 170 > r_tmp_i:
            if 0 <= g_tmp_i and 85 > g_tmp_i:
                if 0 <= b_tmp_i and 85 > b_tmp_i:
                    rgb[1][0][0].append(color_tuple)
                elif 85 <= b_tmp_i and 170 > b_tmp_i:
                    rgb[1][0][1].append(color_tuple)
                else:
                    rgb[1][0][2].append(color_tuple)
            elif 85 <= g_tmp_i and 170 > g_tmp_i:
                if 0 <= b_tmp_i and 85 > b_tmp_i:
                    rgb[1][1][0].append(color_tuple)
                elif 85 <= b_tmp_i and 170 > b_tmp_i:
                    rgb[1][1][1].append(color_tuple)
                else:
                    rgb[1][1][2].append(color_tuple)
            else:
                if 0 <= b_tmp_i and 85 > b_tmp_i:
                    rgb[1][2][0].append(color_tuple)
                elif 85 <= b_tmp_i and 170 > b_tmp_i:
                    rgb[1][2][1].append(color_tuple)
                else:
                    rgb[1][2][2].append(color_tuple) 
        else:
            if 0 <= g_tmp_i and 85 > g_tmp_i:
                if 0 <= b_tmp_i and 85 > b_tmp_i:
                    rgb[2][0][0].append(color_tuple)
                elif 85 <= b_tmp_i and 170 > b_tmp_i:
                    rgb[2][0][1].append(color_tuple)
                else:
                    rgb[2][0][2].append(color_tuple)
            elif 85 <= g_tmp_i and 170 > g_tmp_i:
                if 0 <= b_tmp_i and 85 > b_tmp_i:
                    rgb[2][1][0].append(color_tuple)
                elif 85 <= b_tmp_i and 170 > b_tmp_i:
                    rgb[2][1][1].append(color_tuple)
                else:
                    rgb[2][1][2].append(color_tuple)
            else:
                if 0 <= b_tmp_i and 85 > b_tmp_i:
                    rgb[2][2][0].append(color_tuple)
                elif 85 <= b_tmp_i and 170 > b_tmp_i:
                    rgb[2][2][1].append(color_tuple)
                else:
                    rgb[2][2][2].append(color_tuple) 

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
