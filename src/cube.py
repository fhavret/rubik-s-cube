#/usr/bin/python3
# -*- coding:Utf-8 -*-


import matplotlib.pyplot as plt

from poly import Poly3DCollection

taille_cube = 0.3

class Cube:

    def __init__(self, x_begin, y_begin, z_begin, colors):
        cube = []

        x = [x_begin, x_begin + taille_cube, x_begin + taille_cube, x_begin]
        y = [y_begin, y_begin, y_begin, y_begin]
        z = [z_begin, z_begin, z_begin + taille_cube, z_begin + taille_cube]
        cube.append(list(zip(x, y, z)))

        x = [x_begin + taille_cube, x_begin + taille_cube, x_begin + taille_cube, x_begin + taille_cube]
        y = [y_begin, y_begin + taille_cube, y_begin + taille_cube, y_begin]
        z = [z_begin, z_begin, z_begin + taille_cube, z_begin + taille_cube]
        cube.append(list(zip(x, y, z)))

        x = [x_begin, x_begin + taille_cube, x_begin + taille_cube, x_begin]
        y = [y_begin + taille_cube, y_begin + taille_cube, y_begin + taille_cube, y_begin + taille_cube]
        z = [z_begin, z_begin, z_begin + taille_cube, z_begin + taille_cube]
        cube.append(list(zip(x, y, z)))

        x = [x_begin, x_begin, x_begin, x_begin]
        y = [y_begin, y_begin + taille_cube, y_begin + taille_cube, y_begin]
        z = [z_begin, z_begin, z_begin + taille_cube, z_begin + taille_cube]
        cube.append(list(zip(x, y, z)))

        x = [x_begin, x_begin + taille_cube, x_begin + taille_cube, x_begin]
        y = [y_begin, y_begin, y_begin + taille_cube, y_begin + taille_cube]
        z = [z_begin, z_begin, z_begin, z_begin]
        cube.append(list(zip(x, y, z)))

        x = [x_begin, x_begin + taille_cube, x_begin + taille_cube, x_begin]
        y = [y_begin, y_begin, y_begin + taille_cube, y_begin + taille_cube]
        z = [z_begin + taille_cube, z_begin + taille_cube, z_begin + taille_cube, z_begin + taille_cube]
        cube.append(list(zip(x, y, z)))

        self.cube = Poly3DCollection(cube, facecolors=colors, edgecolor='#000000')


    def rotate(self, x, y, z, angle):
        self.cube.rotate(x, y, z, angle)

    def get_color(self):
        return
