#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-15 15:10
# @Author  : Gin (gin.lance.inside@hotmail.com)
# @Link    : 
# @Disc    : haishoku main function

import sys
import haishoku

def main():
    image_path = sys.argv[1]
    image_colors = haishoku.get_colors(image_path)
    print("hello haishoku.")
    for color in image_colors:
        print(color)

if __name__ == "__main__":
    main()