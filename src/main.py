import settings
from logic.rubiks_cube import RubiksCube
from ui.display import RubiksCubeDisplay


rubiks_cube = RubiksCube(settings.RUBIKS_CUBE_SIZE)
RubiksCubeDisplay(rubiks_cube, settings.CUBE_SIZE, settings.NUMBER_OF_FRAMES).display()
