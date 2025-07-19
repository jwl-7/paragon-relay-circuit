"""Circuit"""

from circuits.circuit_colors import CircuitColors

class Circuit:
    """Parent Circuit class.

    Not the child Circuit class.
    """

    def __init__(self):
        self.colorizer: CircuitColors = CircuitColors()
        self.color: str|None = None
        self.input: 'Circuit|None' = None
        self.output: 'Circuit|None' = None
        self.flux: float = 0
