"""
An image is represented by a 2-D array of integers,
each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel
(row and column) of the flood fill, and a pixel value newColor,
"flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any
pixels connected 4-directionally to the starting pixel of the same color
as the starting pixel, plus any pixels connected 4-directionally to those
pixels (also with the same color as the starting pixel), and so on. Replace
the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
"""
from typing import List

def fill(image, row, col, new_color, old_color):
    if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]):
        return
    if image[row][col] != old_color:
        return
    image[row][col] = new_color
    fill(image, row + 1, col, new_color, old_color)
    fill(image, row - 1, col, new_color, old_color)
    fill(image, row , col + 1, new_color, old_color)
    fill(image, row , col - 1, new_color, old_color)

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    if image[sr][sc]==newColor:
        return image
    fill(image, sr, sc, newColor, image[sr][sc])
    return image

print(floodFill([[0,0,0],[0,1,0]],1,1,1))
