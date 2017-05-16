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

    print(grouped_image_colors[0][0][0])


if __name__ == "__main__":
    print("hello haishoku.")
    main()