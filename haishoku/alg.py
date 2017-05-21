#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 15:10
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : alg about palette

import random
import math

def clusterGen(k):
    """ Generate k random colors
        The palette will show k colors.
        Also, the k's value will effect the accuracy
    """
    clusters = []
    for i in range(k):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        clusters.append((r, g, b))

    return clusters

def groupColorsByClusters(colors, clusters):
    """ this function will group all colors to the 
        cluster that is closest to.
    """

    # define a color_clusters array
    color_clusters = []
    for i in range(len(clusters)):
        temp_array = []
        color_clusters.append(temp_array)

    # group the colors by clusters
    for color in colors:
        # calculate the distance between color and each cluster
        diff_temp = []
        for cluster in clusters:
            diff_sum = 0
            for i in range(len(cluster)):
                diff_i = color[1][i] - cluster[i]
                diff_sum += math.pow( diff_i, 2 )
            diff_sqrt = math.sqrt(diff_sum)
            diff_temp.append(diff_sqrt)
        # get the smallest diff
        diff_min = min(diff_temp)
        diff_min_index = diff_temp.index(diff_min)
        color_clusters[diff_min_index].append(color)

    return color_clusters

def calOffsetOfCluster(color_cluster, cluster):
    """ this function will calculate the offset of the cluster
        (cl_i - cc_i) ** 2
    """
    offset = 0
    for cc in color_cluster:
        l = len(cluster)
        for i in range(l):
            offset_temp = math.pow( (cc[1][i] - cluster[i]), 2 )
            offset += offset_temp
    return offset

def newCluster(color_cluster):
    """ calculate the new cluster
        just calculate the mean of each color_cluster
    """
    r = 0
    g = 0
    b = 0
    count = 0
    for cc in color_cluster:
        count += cc[0]
        r += cc[1][0] * cc[0]
        g += cc[1][1] * cc[0]
        b += cc[1][2] * cc[0]

    print("r: " + str(r))
    print("g: " + str(g))
    print("b: " + str(b))
    print("count: " + str(count))
    r_mean = int(r / count)
    g_mean = int(g / count)
    b_mean = int(b / count)
    cluster = (r_mean, g_mean, b_mean)
    print(cluster)
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
