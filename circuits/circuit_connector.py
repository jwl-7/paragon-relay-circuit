"""Connect"""

import random

from circuits.circuit import Circuit
from circuits.circuit_printer import CircuitPrinter

class CircuitConnector:
    """Circuit connector

    Connects a list of circuits using
    the yunxian algorithm for optimized connections.
    """

    def __init__(self):
        self.printer = CircuitPrinter()

    def connect(self, circuits: list[Circuit], circuit: Circuit) -> None:
        """Recursively fills the input and output connection for a single circuit."""
        if circuit.input and circuit.output:
            return

        a = circuit
        b = random.choice(circuits)

        if a is b:
            self.connect(circuits, a)
            return
        if not a.input and not b.output and b.input is not a:
            a.input = b
            self.printer.connection(b, a)
        elif not a.output and not b.input and b.output is not a:
            a.output = b
            self.printer.connection(a, b)
        elif not circuit.input or not circuit.output:
            self.connect(circuits, a)

    def _connect(self, circuits: list[Circuit], circuit: Circuit|None) -> None:
        """Recursively connects each circuit recursively in a loop."""
        if circuit is None:
            circuit = circuits[0]
        if self.check_connections(circuits):
            return

        self.connect(circuits, circuit)
        self._connect(circuits, circuit.output)

    def connect_circuits(self, circuits: list[Circuit]) -> None:
        """Calls the recursive connector to recursively connect."""
        self.printer.section('CONNECTING CIRCUITS')
        self._connect(circuits, circuits[0])

    def check_connections(self, circuits: list[Circuit]) -> bool:
        """Sends a duck and a penguin to check circuit connections."""
        duck = penguin = circuits[0]
        while duck.output and penguin.output and penguin.output.output:
            if duck is penguin:
                return True
        return False
