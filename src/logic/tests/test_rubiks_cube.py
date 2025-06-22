import pytest
from unittest import mock

from logic.cube import Cube
from logic.rubiks_cube import RubiksCube
from logic.enums.colors import Color
from logic.enums.faces import Face


@pytest.fixture
def rubiks_cube_3x3():
    return RubiksCube(3)


class TestRubiksCube:
    def test_init(self, rubiks_cube_3x3):
        assert rubiks_cube_3x3.cubes[0, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )

    def test_rotate_slice(self, rubiks_cube_3x3):
        rubiks_cube_3x3._rotate_slice(0)

        assert rubiks_cube_3x3.cubes[0, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.YELLOW,
                Face.BOTTOM: Color.BLUE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLUE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.WHITE,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLUE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.YELLOW,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.WHITE,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.YELLOW,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.GREEN,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.GREEN,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.WHITE,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.GREEN,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )

    def test_rotate_row(self, rubiks_cube_3x3):
        rubiks_cube_3x3._rotate_row(0)

        assert rubiks_cube_3x3.cubes[0, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.GREEN,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.ORANGE,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.GREEN,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.GREEN,
                Face.RIGHT: Color.RED,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.ORANGE,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.RED,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLUE,
                Face.LEFT: Color.ORANGE,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLUE,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.RED,
                Face.BACK: Color.BLUE,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )

    def test_rotate_column(self, rubiks_cube_3x3):
        rubiks_cube_3x3._rotate_column(0)

        assert rubiks_cube_3x3.cubes[0, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.WHITE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.RED,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.WHITE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.WHITE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.ORANGE,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[0, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.ORANGE,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.RED,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.ORANGE,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[1, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.BLACK,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.YELLOW,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.RED,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 0, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.WHITE,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.YELLOW,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 1, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.BLACK,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 0] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.YELLOW,
                Face.LEFT: Color.BLUE,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.ORANGE,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 1] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.BLACK,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
        assert rubiks_cube_3x3.cubes[2, 2, 2] == Cube(
            facecolors={
                Face.FRONT: Color.BLACK,
                Face.RIGHT: Color.GREEN,
                Face.BACK: Color.RED,
                Face.LEFT: Color.BLACK,
                Face.BOTTOM: Color.BLACK,
                Face.TOP: Color.YELLOW,
            }
        )
