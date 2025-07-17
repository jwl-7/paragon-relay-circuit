"""Circuit"""

from circuits.circuit import Circuit

class CircuitRed(Circuit):
    """Red Circuit

    Circuit that is red.
    """

    def __init__(self):
        super().__init__()
        self.color = self.colorizer.get_color(self.colorizer.red)
