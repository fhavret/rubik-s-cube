import pytest

from logic.cube import Cube
from logic.enums.colors import Color
from logic.enums.faces import Face


@pytest.fixture
def cube():
    return Cube(
        facecolors={
            Face.FRONT: Color.ORANGE,
            Face.RIGHT: Color.GREEN,
            Face.BACK: Color.RED,
            Face.LEFT: Color.BLUE,
            Face.BOTTOM: Color.WHITE,
            Face.TOP: Color.YELLOW,
        }
    )


class TestCube:
    def test_rotate_xz(self, cube):
        cube.rotate_xz()
        assert cube.facecolors == {
            Face.FRONT: Color.ORANGE,
            Face.RIGHT: Color.WHITE,
            Face.BACK: Color.RED,
            Face.LEFT: Color.YELLOW,
            Face.BOTTOM: Color.BLUE,
            Face.TOP: Color.GREEN,
        }

    def test_rotate_xy(self, cube):
        cube.rotate_xy()
        assert cube.facecolors == {
            Face.FRONT: Color.GREEN,
            Face.RIGHT: Color.RED,
            Face.BACK: Color.BLUE,
            Face.LEFT: Color.ORANGE,
            Face.BOTTOM: Color.WHITE,
            Face.TOP: Color.YELLOW,
        }

    def test_rotate_yz(self, cube):
        cube.rotate_yz()
        assert cube.facecolors == {
            Face.FRONT: Color.WHITE,
            Face.RIGHT: Color.GREEN,
            Face.BACK: Color.YELLOW,
            Face.LEFT: Color.BLUE,
            Face.BOTTOM: Color.RED,
            Face.TOP: Color.ORANGE,
        }
