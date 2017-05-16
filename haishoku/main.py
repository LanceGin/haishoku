#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 15:10
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : haishoku main function

import sys
import haishoku
import alg

def main():
    # get image_path from system args
    image_path = sys.argv[1]
    # get colors tuple with haishoku module
    image_colors = haishoku.get_colors(image_path)

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

    for color_mean in sorted(colors_mean):
        print(color_mean)


if __name__ == "__main__":
    print("hello haishoku.")
    main()