import copy
import numpy as np
import random
from typing import Iterable

from logic.cube import Cube
from logic.enums.colors import Color
from logic.enums.faces import Face
from logic.utils import are_all_values_equal


class RubiksCube:
    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("'size' must be greater than 0")
        self.size = size
        self.cubes = np.full((size, size, size), None)
        self.reset()

    def is_finished(self) -> bool:
        is_finished = True

        front_cubes = self.cubes[:, 0, :].flatten()
        get_front_colors = lambda cube: cube.facecolors[Face.FRONT]
        front_colors = np.frompyfunc(get_front_colors, 1, 1)(front_cubes)

        is_finished &= are_all_values_equal(front_colors)

        right_cubes = self.cubes[self.size - 1, :, :].flatten()
        get_right_colors = lambda cube: cube.facecolors[Face.RIGHT]
        right_colors = np.frompyfunc(get_right_colors, 1, 1)(right_cubes)

        is_finished &= are_all_values_equal(right_colors)

        back_cubes = self.cubes[:, self.size - 1, :].flatten()
        get_back_colors = lambda cube: cube.facecolors[Face.BACK]
        back_colors = np.frompyfunc(get_back_colors, 1, 1)(back_cubes)

        is_finished &= are_all_values_equal(back_colors)

        left_cubes = self.cubes[0, :, :].flatten()
        get_left_colors = lambda cube: cube.facecolors[Face.LEFT]
        left_colors = np.frompyfunc(get_left_colors, 1, 1)(left_cubes)

        is_finished &= are_all_values_equal(left_colors)

        bottom_cubes = self.cubes[:, :, 0].flatten()
        get_bottom_colors = lambda cube: cube.facecolors[Face.BOTTOM]
        bottom_colors = np.frompyfunc(get_bottom_colors, 1, 1)(bottom_cubes)

        is_finished &= are_all_values_equal(bottom_colors)

        top_cubes = self.cubes[:, :, self.size - 1].flatten()
        get_top_colors = lambda cube: cube.facecolors[Face.TOP]
        top_colors = np.frompyfunc(get_top_colors, 1, 1)(top_cubes)

        is_finished &= are_all_values_equal(top_colors)

        return is_finished

    def reset(self):
        for y in range(self.size):  # slice
            for z in range(self.size):  # row
                for x in range(self.size):  # cube in a row
                    facecolors = {
                        Face.FRONT: Color.BLACK,
                        Face.RIGHT: Color.BLACK,
                        Face.BACK: Color.BLACK,
                        Face.LEFT: Color.BLACK,
                        Face.BOTTOM: Color.BLACK,
                        Face.TOP: Color.BLACK,
                    }

                    if x == 0:
                        facecolors[Face.LEFT] = Color.BLUE
                    if x == self.size - 1:
                        facecolors[Face.RIGHT] = Color.GREEN
                    if z == 0:
                        facecolors[Face.BOTTOM] = Color.WHITE
                    if z == self.size - 1:
                        facecolors[Face.TOP] = Color.YELLOW
                    if y == 0:
                        facecolors[Face.FRONT] = Color.ORANGE
                    if y == self.size - 1:
                        facecolors[Face.BACK] = Color.RED

                    self.cubes[y, z, x] = Cube(facecolors)

    def shuffle(self, number_of_rotations: int) -> Iterable:
        for _ in range(number_of_rotations):
            number = random.randint(0, self.size - 1)
            slice_or_row_or_column = random.randint(0, 2)

            rotate_slice = slice_or_row_or_column == 0
            rotate_row = slice_or_row_or_column == 1
            rotate_column = slice_or_row_or_column == 2

            if rotate_slice:
                self._rotate_slice(number)
            elif rotate_row:
                self._rotate_row(number)
            elif rotate_column:
                self._rotate_column(number)

            yield rotate_slice, rotate_row, rotate_column, number

    def _rotate_slice(self, number: int):
        cubes_copy = copy.copy(self.cubes[number, :, :])

        for z in range(self.size):
            for x in range(self.size):
                self.cubes[number, z, x] = cubes_copy[self.size - 1 - x, z]
                self.cubes[number, z, x].rotate_xz()

    def _rotate_row(self, number: int):
        cubes_copy = copy.copy(self.cubes[:, number, :])

        for y in range(self.size):
            for x in range(self.size):
                self.cubes[y, number, x] = cubes_copy[x, self.size - 1 - y]
                self.cubes[y, number, x].rotate_xy()

    def _rotate_column(self, number: int):
        cubes_copy = copy.copy(self.cubes[:, :, number])

        for y in range(self.size):
            for z in range(self.size):
                self.cubes[y, z, number] = cubes_copy[self.size - 1 - z, y]
                self.cubes[y, z, number].rotate_yz()
