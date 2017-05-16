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


