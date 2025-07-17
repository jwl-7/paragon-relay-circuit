"""Circuit"""

from circuits.circuit import Circuit

class CircuitGreen(Circuit):
    """Green Circuit

    Circuit that is Green.
    """

    def __init__(self):
        super().__init__()
        self.color = self.colorizer.get_color(self.colorizer.green)
