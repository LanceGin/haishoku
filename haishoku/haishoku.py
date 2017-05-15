#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 15:10
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : about Pillow Apis

from PIL import Image

def get_image(image_path):
    image = Image.open(image_path)
    return image

def get_thumbnail(image):
    image.thumbnail((30, 30))
    return image

def get_colors(image_path):
    """ image instance
    """
    image = get_image(image_path)

    """ image thumbnail
        size: 256 * 256
        reduce the calculate time 
    """
    thumbnail = get_thumbnail(image)


    """ calculate the max colors the image cound have
        if the color is different in every pixel, the color counts may be the max.
        so : 
        max_colors = image.height * image.width
    """
    image_height = thumbnail.height
    image_width = thumbnail.width
    max_colors = image_height * image_width
    print(max_colors)

    image_colors = image.getcolors(max_colors)
    return image_colors
