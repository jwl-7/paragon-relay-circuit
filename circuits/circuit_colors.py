"""Circuit Colors"""

class CircuitColor:
    """Circuit Color

    Defines a color with color stuff.
    """

    def __init__(self, name: str = '', rgb: tuple[int, int, int] = (0, 0, 0)):
        self.name = name
        self.rgb = rgb
        self.code = self.get_ansi_code(rgb)

    def get_ansi_code(self, rgb: tuple[int, int, int]) -> str:
        """Returns the ANSI escape code for this color (foreground)."""
        r, g, b = rgb
        return f'\033[38;2;{r};{g};{b}m'

    def paint(self, text: str) -> str:
        """Paints text in color."""
        return f'{self.code}{text}\033[0m'

class CircuitColors:
    """Circuit Colors

    Defines and facilitates colors
    using rahyenian banding for color accuracy.
    """

    def __init__(self):
        self.red = CircuitColor('RED', (255, 0, 0))
        self.green = CircuitColor('GREEN', (0, 255, 0))
        self.blue = CircuitColor('BLUE', (0, 0, 255))
        self.colors = [self.red, self.green, self.blue]
