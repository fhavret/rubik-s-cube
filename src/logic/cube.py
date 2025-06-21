from logic.enums.colors import Color
from logic.enums.faces import Face


class Cube:
    def __init__(self, facecolors: dict[Face, Color]):
        self.facecolors = facecolors

    def rotate_xz(self):
        self.facecolors = {
            Face.FRONT: self.facecolors[Face.FRONT],
            Face.RIGHT: self.facecolors[Face.TOP],
            Face.BACK: self.facecolors[Face.BACK],
            Face.LEFT: self.facecolors[Face.BOTTOM],
            Face.BOTTOM: self.facecolors[Face.RIGHT],
            Face.TOP: self.facecolors[Face.LEFT],
        }

    def rotate_xy(self):
        self.facecolors = {
            Face.FRONT: self.facecolors[Face.RIGHT],
            Face.RIGHT: self.facecolors[Face.BACK],
            Face.BACK: self.facecolors[Face.LEFT],
            Face.LEFT: self.facecolors[Face.FRONT],
            Face.BOTTOM: self.facecolors[Face.BOTTOM],
            Face.TOP: self.facecolors[Face.TOP],
        }

    def rotate_yz(self):
        self.facecolors = {
            Face.FRONT: self.facecolors[Face.BOTTOM],
            Face.RIGHT: self.facecolors[Face.RIGHT],
            Face.BACK: self.facecolors[Face.TOP],
            Face.LEFT: self.facecolors[Face.LEFT],
            Face.BOTTOM: self.facecolors[Face.BACK],
            Face.TOP: self.facecolors[Face.FRONT],
        }
