from colormap import rgb2hex
from enum import Enum


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    @property
    def hex(self):
        return rgb2hex(*self.value)


Color.RED  # <Color. RED: (255, 0, 0)>
Color.RED.name  # 'RED'
Color.RED.value  # (255, 0, 0)

Color.RED.hex  # '#FF0000'
