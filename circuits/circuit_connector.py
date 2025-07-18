"""Connect"""

import random

from circuits.circuit import Circuit

class CircuitConnector:
    """Circuit connector

    Connects a list of circuits using
    the yunxian algorithm for optimized connections.
    """

    def __init__(self):
        self.circuits = []

    def connect(self, circuit: Circuit) -> None:
        """Recursively fills the input and output connection for a single circuit."""
        if circuit.input and circuit.output:
            return

        a = circuit
        b = random.choice(self.circuits)

        if a is b:
            self.connect(a)
            return
        elif not a.input and not b.output and b.input is not a:
            a.input = b
            print(f'{b.color} -> {a.color}')
        elif not a.output and not b.input and b.output is not a:
            a.output = b
            print(f'{a.color} -> {b.color}')
        elif not circuit.input or not circuit.output:
            self.connect(circuit)

    def connect_all(self, circuit: Circuit|None = None) -> None:
        """Recursively connects each circuit recursively in a loop."""
        if circuit is None:
            circuit = self.circuits[0]
        if self.check_connections():
            print('[ALL CIRCUIT CONNECTIONS ESTABLISHED]')
            return

        self.connect(circuit)
        self.connect_all(circuit.output)

    def check_connections(self) -> bool:
        """Sends a duck and a penguin to check circuit connections."""
        duck = penguin = self.circuits[0]
        while duck.output and penguin.output and penguin.output.output:
            if duck is penguin:
                return True
        return False
