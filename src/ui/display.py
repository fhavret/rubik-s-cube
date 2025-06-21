from typing import TypeAlias

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import settings
from logic.cube import Cube
from logic.rubiks_cube import RubiksCube


Vertex: TypeAlias = list[float]
Edge: TypeAlias = list[Vertex]


class RubiksCubeDisplay:
    def __init__(
        self,
        rubiks_cube: RubiksCube,
        cube_size: float,
        number_of_frames: int,
    ):
        if number_of_frames <= 0:
            raise ValueError("`'number_of_frames' must be greater than 0")
        if cube_size <= 0:
            raise ValueError("'cube_size' must be greater than 0")

        self.rubiks_cube = rubiks_cube
        self.cubedisplay_mapper = {}
        self.cube_size = cube_size
        self.number_of_frames = number_of_frames
        self.angle_to_rotate = np.pi / (2 * self.number_of_frames)
        self.center = self.cube_size * self.rubiks_cube.size / 2

        self.fig = plt.figure()
        self.fig.suptitle("Rubik's Cube")
        self.ax = self.fig.add_subplot(projection="3d")
        self.ax.set_axis_off()

    def display(self):
        self._add_cubes_to_ax()

        reset_button = Button(plt.axes([0.62, 0.05, 0.1, 0.075]), "Reset")
        reset_button.on_clicked(self._reset)

        shuffle_button = Button(plt.axes([0.73, 0.05, 0.1, 0.075]), "Shuffle")
        shuffle_button.on_clicked(self._shuffle)

        is_finished_button = Button(plt.axes([0.84, 0.05, 0.13, 0.075]), "Finished ?")
        is_finished_button.on_clicked(self._is_finished)

        plt.show()

    def _add_cubes_to_ax(self):
        for y in range(self.rubiks_cube.size):  # slice
            for z in range(self.rubiks_cube.size):  # row
                for x in range(self.rubiks_cube.size):  # cube in a row
                    cube = self.rubiks_cube.cubes[x, y, z]
                    cube_display = self.cubedisplay_mapper.setdefault(
                        cube,
                        CubeDisplay(
                            cube,
                            self.cube_size,
                            x * self.cube_size,
                            y * self.cube_size,
                            z * self.cube_size,
                        ),
                    )

                    self.ax.add_collection3d(cube_display.cube3d)

    def _reset(self, event):
        self.rubiks_cube.reset()

        self.ax.clear()
        self.ax.set_axis_off()
        self._add_cubes_to_ax()
        plt.draw()

    def _shuffle(self, event):
        for (
            slice_was_rotated,
            row_was_rotated,
            column_was_rotated,
            number,
        ) in self.rubiks_cube.shuffle(settings.SHUFFLE_NUMBER_OF_ROTATIONS):
            print(slice_was_rotated, row_was_rotated, column_was_rotated, number)
            if slice_was_rotated:
                f = self._rotate_slice
            elif row_was_rotated:
                f = self._rotate_row
            elif column_was_rotated:
                f = self._rotate_column

            anim = FuncAnimation(
                self.fig,
                f,
                frames=np.full(self.number_of_frames, number),
                init_func=lambda: None,
                interval=30,
                repeat=False,
            )

            plt.draw()
            plt.pause(2)

    def _is_finished(self, event):
        is_finished = self.rubiks_cube.is_finished()
        print(is_finished)

    def _rotate_slice(self, number: int):
        for cube in self.rubiks_cube.cubes[:, number, :].flatten():
            cubedisplay = self.cubedisplay_mapper[cube]
            cubedisplay.rotate(self.center, 0, self.center, self.angle_to_rotate)

    def _rotate_row(self, number: int):
        for cube in self.rubiks_cube.cubes[:, :, number].flatten():
            cubedisplay = self.cubedisplay_mapper[cube]
            cubedisplay.rotate(self.center, self.center, 0, self.angle_to_rotate)

    def _rotate_column(self, number: int):
        for cube in self.rubiks_cube.cubes[number, :, :].flatten():
            cubedisplay = self.cubedisplay_mapper[cube]
            cubedisplay.rotate(0, self.center, self.center, self.angle_to_rotate)


class CubeDisplay:
    def __init__(
        self,
        cube: Cube,
        cube_size: float,
        x_start: float,
        y_start: float,
        z_start: float,
    ):
        facecolors = [color.value for color in cube.facecolors.values()]
        self.verts = self._get_verts(cube_size, x_start, y_start, z_start)
        self.cube3d = Poly3DCollection(
            self.verts, facecolors=facecolors, edgecolor="#000000"
        )

    def rotate(self, x: float, y: float, z: float, alpha: float):
        if x == 0:  # column
            rotation = np.array(
                [
                    [1, 0, 0],
                    [0, np.cos(alpha), -np.sin(alpha)],
                    [0, np.sin(alpha), np.cos(alpha)],
                ]
            )
        elif y == 0:  # slice
            rotation = np.array(
                [
                    [np.cos(alpha), 0, np.sin(alpha)],
                    [0, 1, 0],
                    [-np.sin(alpha), 0, np.cos(alpha)],
                ]
            )
        elif z == 0:  # row
            rotation = np.array(
                [
                    [np.cos(alpha), -np.sin(alpha), 0],
                    [np.sin(alpha), np.cos(alpha), 0],
                    [0, 0, 1],
                ]
            )

        def _rotate(arr):
            for x in range(arr.shape[0]):
                for y in range(arr.shape[1]):
                    arr[x, y, :] = np.dot(arr[x, y, :], rotation)
            return arr

        reference_point = np.full((6, 4, 3), [x, y, z])
        self.verts = _rotate(self.verts - reference_point) + reference_point
        self.cube3d.set_verts(self.verts)

    def _get_verts(
        self, cube_size: float, x_start: float, y_start: float, z_start: float
    ) -> list[Edge]:
        return [
            [
                [x_start, y_start, z_start],
                [x_start + cube_size, y_start, z_start],
                [x_start + cube_size, y_start, z_start + cube_size],
                [x_start, y_start, z_start + cube_size],
            ],
            [
                [x_start + cube_size, y_start, z_start],
                [x_start + cube_size, y_start + cube_size, z_start],
                [x_start + cube_size, y_start + cube_size, z_start + cube_size],
                [x_start + cube_size, y_start, z_start + cube_size],
            ],
            [
                [x_start, y_start + cube_size, z_start],
                [x_start + cube_size, y_start + cube_size, z_start],
                [x_start + cube_size, y_start + cube_size, z_start + cube_size],
                [x_start, y_start + cube_size, z_start + cube_size],
            ],
            [
                [x_start, y_start, z_start],
                [x_start, y_start + cube_size, z_start],
                [x_start, y_start + cube_size, z_start + cube_size],
                [x_start, y_start, z_start + cube_size],
            ],
            [
                [x_start, y_start, z_start],
                [x_start + cube_size, y_start, z_start],
                [x_start + cube_size, y_start + cube_size, z_start],
                [x_start, y_start + cube_size, z_start],
            ],
            [
                [x_start, y_start, z_start + cube_size],
                [x_start + cube_size, y_start, z_start + cube_size],
                [x_start + cube_size, y_start + cube_size, z_start + cube_size],
                [x_start, y_start + cube_size, z_start + cube_size],
            ],
        ]
