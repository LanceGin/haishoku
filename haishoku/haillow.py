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
    image.thumbnail((256, 256))
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

    image_colors = image.getcolors(max_colors)
    return image_colors

def new_image(mode, size, color):
    """ generate a new color block
        to generate the palette
    """
    new_image = Image.new(mode, size, color)
    return new_image

def joint_image(images):
    """ generate the palette
        size: 50 x 400
        color_block_size: 50 x 50
    """
    palette = Image.new('RGB', (400, 20))

    # init the box position
    init_ul = 0

    for image in images:
        palette.paste(image, (init_ul, 0))
        init_ul += image.width

    palette.show()