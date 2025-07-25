"""Circuit"""

from circuits.circuit_colors import CircuitColors

class Circuit:
    """Parent Circuit class.

    Not the child Circuit class.
    """

    def __init__(self):
        self.colorizer = CircuitColors()
        self.color = self.colorizer.empty
        self.input = None
        self.output = None
        self.flux = 0.0
