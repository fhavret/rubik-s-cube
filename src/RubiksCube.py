#/usr/bin/python3
# -*- coding:Utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
from numpy import pi, isclose
import random

from cube import Cube
from cube import taille_cube


# Initialisation de la figure
fig = plt.figure()
fig.canvas.set_window_title('Rubik\'s Cube')
ax = fig.gca(projection='3d')
ax.set_axis_off()

pi_divided_by_2 = pi/2
frame_number = 4 # number of display between the two states when rotating
angle_to_rotate = pi_divided_by_2/(frame_number + 1)


colors = {'orange': "#ff6f00",
          'white': "#fdfdfd",
          'green': "#009f0f",
          'yellow': "#ffcf00",
          'red': "#cf0000",
          'blue': "#00008f",
          'black': "#000000"}

colorss = {"#ff6f00":"orange",
           "#fdfdfd":"white",
           "#009f0f":"green",
           "#ffcf00":"yellow",
           "#cf0000":"red",
           "#00008f":"blue",
           "#000000":"black"}


class RubiksCube():

    def __init__(self, size):
	    # Création des cubes du Rubik's cube
        self.cube_list = [[[0 for i in range(size)] for j in range(size)] for k in range(size)]
        self.size = size
        self.center = (1.0*taille_cube*self.size)/2

        # Initialisation des couleurs des cubes
        for i in range(size): # slice
            for j in range(size): # row
                for k in range(size): # cube in a row
                    cube_colors = [colors['black'],
		                   colors['black'],
		                   colors['black'],
		                   colors['black'],
		                   colors['black'],
		                   colors['black']]
                    if i==0:
                        cube_colors[0] = colors['orange']
                    elif i==size-1:
                        cube_colors[2] = colors['red']
                    if j==0:
                        cube_colors[4] = colors['yellow']
                    elif j==size-1:
                        cube_colors[5] = colors['white']
                    if k==0:
                        cube_colors[3] = colors['blue']
                    elif k==size-1:
                        cube_colors[1] = colors['green']

                    self.cube_list[i][j][k] = Cube(taille_cube*k, taille_cube*i, taille_cube*j, cube_colors)
                    

    def display(self):
        for i in range(self.size): # slice
            for j in range(self.size): # row
                for k in range(self.size): # cube in a row
                    ax.add_collection3d(self.cube_list[i][j][k].cube)

        # boutons
        breset = Button(plt.axes([0.7, 0.05, 0.1, 0.075]), 'Reset')
        bshuffle = Button(plt.axes([0.81, 0.05, 0.1, 0.075]), 'Shuffle')
        bfinished = Button(plt.axes([0.92, 0.05, 0.1, 0.075]), 'Finished ?')
        # effet des boutons
        breset.on_clicked(self.reset)
        bshuffle.on_clicked(self.shuffle)
        bfinished.on_clicked(self.is_finished)

        plt.show()

    def rotate_xy(self, row, left):
        if left:
            for cube in self.cubes_to_rotate:
                cube.rotate(self.center, self.center, 0, -angle_to_rotate)
                #ax.add_collection3d(cube.cube)
        else:
            for cube in self.cubes_to_rotate:
                cube.rotate(self.center, self.center, 0, angle_to_rotate)
                #ax.add_collection3d(cube.cube)
        ax.cla()
        ax.set_axis_off()
        for i in range(self.size): # slice
            for j in range(self.size): # row
                for k in range(self.size): # cube in a row
                    ax.add_collection3d(self.cube_list[i][j][k].cube)

    def rotate_xz(self, slice, left):
        if left:
            for cube in self.cubes_to_rotate:
                cube.rotate(self.center, 0, self.center, -angle_to_rotate)
                #ax.add_collection3d(cube.cube)
        else:
            for cube in self.cubes_to_rotate:
                cube.rotate(self.center, 0, self.center, angle_to_rotate)
                #ax.add_collection3d(cube.cube)
        ax.cla()
        ax.set_axis_off()
        for i in range(self.size): # slice
            for j in range(self.size): # row
                for k in range(self.size): # cube in a rowself.center
                    ax.add_collection3d(self.cube_list[i][j][k].cube)

    def rotate_yz(self, column, left):
        if left:
            for cube in self.cubes_to_rotate:
                cube.rotate(0, self.center, self.center, -angle_to_rotate)
                #ax.add_collection3d(cube.cube)
        else:
            for cube in self.cubes_to_rotate:
                cube.rotate(0, self.center, self.center, angle_to_rotate)
                #ax.add_collection3d(cube.cube)
        ax.cla()
        ax.set_axis_off()
        for i in range(self.size): # slice
            for j in range(self.size): # row
                for k in range(self.size): # cube in a row
                    ax.add_collection3d(self.cube_list[i][j][k].cube)

    def rotate(self, xy, xz, yz, row_slice_column, left):
        if xy:
            self.get_cube_xy(row_slice_column*taille_cube)
            self.animation = FuncAnimation(fig, self.rotate_xy,
                                                frames=np.array([row_slice_column for i in range(frame_number)]),
                                                fargs=(left,),
                                                interval=25,
                                                repeat=False)
            plt.draw()
            plt.pause(0.1)
        if xz:
            self.get_cube_xz(row_slice_column*taille_cube)
            self.animation = FuncAnimation(fig, self.rotate_xz,
                                                frames=np.array([row_slice_column for i in range(frame_number)]),
                                                fargs=(left,),
                                                interval=25,
                                                repeat=False)
            plt.draw()
            plt.pause(0.1)
        if yz:
            self.get_cube_yz(row_slice_column*taille_cube)
            self.animation = FuncAnimation(fig, self.rotate_yz,
                                                frames=np.array([row_slice_column for i in range(frame_number)]),
                                                fargs=(left,),
                                                interval=25,
                                                repeat=False)
            plt.draw()
            plt.pause(0.1)

    def get_cube_xy(self, row, return_value=False):
        cubes = []
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    append = True
                    verts = self.cube_list[i][j][k].cube.verts
                    for vert in verts:
                        for point in vert:
                            if not(isclose(point[2], row, 0.1) or isclose(point[2] - taille_cube, row, 0.1)):
                                append = False
                                break
                        if not(append):
                            break
                    if append:
                        cubes.append(self.cube_list[i][j][k])
        if return_value:
            return cubes
        else:
            self.cubes_to_rotate = cubes

    def get_cube_xz(self, slice, return_value=False):
        cubes = []
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    append = True
                    verts = self.cube_list[i][j][k].cube.verts
                    for vert in verts:
                        for point in vert:
                            if not(isclose(point[1], slice, 0.1) or isclose(point[1] - taille_cube, slice, 0.1)):
                                append = False
                                break
                        if not(append):
                            break
                    if append:
                        cubes.append(self.cube_list[i][j][k])
        if return_value:
            return cubes
        else:
            self.cubes_to_rotate = cubes

    def get_cube_yz(self, column, return_value=False):
        cubes = []
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    append = True
                    verts = self.cube_list[i][j][k].cube.verts
                    for vert in verts:
                        for point in vert:
                            if not(isclose(point[0], column, 0.1) or isclose(point[0] - taille_cube, column, 0.1)):
                                append = False
                                break
                        if not(append):
                            break
                    if append:
                        cubes.append(self.cube_list[i][j][k])
        if return_value:
            return cubes
        else:
            self.cubes_to_rotate = cubes

    def __same_color_on_face(self, cubes_color):
        for i in range(6):
            color = cubes_color[0][i] # color on the first face of a cube
            for j in range(len(cubes_color)):
                if cubes_color[j][i] == "#000000" or cubes_color[j][i] != color: # black face or color different
                    break
                elif j == len(cubes_color)-1: # all cube faces are the same and not black
                    return True

        return False

    def is_finished(self, event):
        is_finished = True

        # face 1
        cubes = self.get_cube_xz(0, return_value=True)
        cubes_color = [cube.cube.facecolors for cube in cubes]

        is_finished &= self.__same_color_on_face(cubes_color)

        # face 2
        cubes = self.get_cube_yz((self.size-1) * taille_cube, return_value=True)
        cubes_color = [cube.cube.facecolors for cube in cubes]

        is_finished &= self.__same_color_on_face(cubes_color)

        # face 3
        cubes = self.get_cube_xz((self.size-1) * taille_cube, return_value=True)
        cubes_color = [cube.cube.facecolors for cube in cubes]

        is_finished &= self.__same_color_on_face(cubes_color)

        # face 4
        cubes = self.get_cube_yz(0, return_value=True)
        cubes_color = [cube.cube.facecolors for cube in cubes]

        is_finished &= self.__same_color_on_face(cubes_color)

        print(is_finished)
        #return is_finished


    def score(self):
        return

    def reset(self, event):
        ax.cla()
        ax.set_axis_off()

        # Initialisation des couleurs des cubes
        for i in range(self.size): # slice
            for j in range(self.size): # row
                for k in range(self.size): # cube in a row
                    cube_colors = [colors['black'],
		                   colors['black'],
		                   colors['black'],
		                   colors['black'],
		                   colors['black'],
		                   colors['black']]
                    if i==0:
                        cube_colors[0] = colors['orange']
                    elif i==self.size-1:
                        cube_colors[2] = colors['red']
                    if j==0:
                        cube_colors[4] = colors['yellow']
                    elif j==self.size-1:
                        cube_colors[5] = colors['white']
                    if k==0:
                        cube_colors[3] = colors['blue']
                    elif k==self.size-1:
                        cube_colors[1] = colors['green']

                    self.cube_list[i][j][k] = Cube(taille_cube*k, taille_cube*i, taille_cube*j, cube_colors)
                    ax.add_collection3d(self.cube_list[i][j][k].cube)

    def shuffle(self, event):
        number_of_rotations = 30

        for i in range(number_of_rotations):
            row_slice_column = random.randint(0,self.size-1)
            left = bool(random.randint(0,1))
            direction = random.randint(0,2)
            if direction == 0:
                xy, xz, yz = True, False, False
            elif direction == 1:
                xy, xz, yz = False, True, False
            else:
                xy, xz, yz = False, False, True

            self.rotate(xy, xz, yz, row_slice_column, left)
