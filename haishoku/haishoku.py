#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 15:10
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : haishoku main function

import sys
from . import haillow
from . import alg

class Haishoku(object):

    """ init Haishoku obj
    """
    def __init__(self):
        self.image = None
        self.dominant = None
        self.palette = None

    """ load the Haishoku obj
        the obj will have all properties and function
    """
    @classmethod
    def loadHaishoku(self, image):
        # get colors mean
        colors_mean = Haishoku.getColorsMean(image)

        # calculate the palette
        palette = []
        for c_m in colors_mean:
            palette.append(c_m[1])

        # calculate the dominant
        colors_mean = sorted(colors_mean, reverse=True)
        dominant_tuple = colors_mean[0]
        dominant = dominant_tuple[1]

        # set the obj property value
        self.image = image
        self.palette = palette
        self.dominant = dominant
        return self

    """ get the properties
    """
    @property
    def dominant(self):
        return self.dominant

    @property
    def palette(self):
        return self.palette




    # 
    # 
    # K-Means algorithm implement
    # 
    # 

    def getSortedColors(image_path):
        image_colors = haillow.get_colors(image_path)
        sorted_image_colors = alg.sort_by_rgb(image_colors)
        return sorted_image_colors

    def getPalette(image_path):
        sorted_image_colors = Haishoku.getSortedColors(image_path)

        # k-means alg default set k to 8
        k = 8
        # generate k random colors
        clusters = alg.clusterGen(k, sorted_image_colors)

        for i in range(k):
            # calculate the palette with sorted_colors and clusters
            color_clusters = alg.groupColorsByClusters(sorted_image_colors, clusters)

            # calculate the offset of each color cluster and the new clusters value
            offset_sum = 0
            clusters_new = []
            for color_cluster in color_clusters:

                cc_index = color_clusters.index(color_cluster)
                cluster = clusters[cc_index]
                offset = alg.calOffsetOfCluster(color_cluster, cluster)
                offset_sum += offset

                cluster_new = alg.newCluster(color_cluster)
                clusters_new.append(cluster_new)
            
            clusters = clusters_new

        palette = sorted(clusters)
        return palette


    """ immediate api

        1. showPalette
        2. showDominant
        3. getDominant
        4. getPalette
    """
    def getColorsMean(image_path):
        if image_path is None:
            print("image is none")

        # get colors tuple with haillow module
        image_colors = haillow.get_colors(image_path)

        # sort the image colors tuple
        sorted_image_colors = alg.sort_by_rgb(image_colors)

        # group the colors by the accuaracy
        grouped_image_colors = alg.group_by_accuracy(sorted_image_colors)

        # get the weighted mean of all colors
        colors_mean = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    grouped_image_color = grouped_image_colors[i][j][k]
                    if 0 != len(grouped_image_color):
                        color_mean = alg.get_weighted_mean(grouped_image_color)
                        colors_mean.append(color_mean)

        # return the most 8 colors
        temp_sorted_colors_mean = sorted(colors_mean)
        if 8 < len(temp_sorted_colors_mean):
            colors_mean = temp_sorted_colors_mean[len(temp_sorted_colors_mean)-8 : len(temp_sorted_colors_mean)]
        else:
            colors_mean = temp_sorted_colors_mean

        # sort the colors_mean
        colors_mean = sorted(colors_mean, key=lambda x:x[1])

        return colors_mean
        
    def showPalette(image_path):
        # get the palette first
        palette = Haishoku.getPalette(image_path)

        # getnerate colors boxes
        images = []
        for color_mean in palette:
            color_box = haillow.new_image('RGB', (50, 20), color_mean)
            images.append(color_box)

        # generate and show the palette
        haillow.joint_image(images)

    def showDominant(image_path):
        # get the dominant color
        dominant = Haishoku.getDominant(image_path)

        # generate colors boxes
        images = []
        dominant_box = haillow.new_image('RGB', (50, 20), dominant)
        for i in range(8):
            images.append(dominant_box)

        # show dominant color
        haillow.joint_image(images)


    def getDominant(image_path=None):
        # get the colors_mean
        colors_mean = Haishoku.getColorsMean(image_path)
        colors_mean = sorted(colors_mean, reverse=True)

        # get the dominant color
        dominant_tuple = colors_mean[0]
        dominant = dominant_tuple[1]
        return dominant