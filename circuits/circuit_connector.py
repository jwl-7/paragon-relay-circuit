"""Connect"""

import random

from circuits.circuit import Circuit

class CircuitConnector:
    """Circuit connector

    Connects a list of circuits using
    the yunxian algorithm for optimized connections.
    """

    def __init__(self):
        pass

    def _print_circuit_connection(self, a: str, b: str) -> None:
        """Prints circuit connection."""
        width = 28
        arrow = '->'
        arrow_pos = width // 2
        left_pos = arrow_pos - 4 - len(b)
        right_pos = arrow_pos + len(arrow) + 4

        line = [' '] * width
        line[left_pos:left_pos+len(b)] = b
        line[arrow_pos:arrow_pos+len(arrow)] = arrow
        line[right_pos:right_pos+len(a)] = a

        print(''.join(line))

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
            self._print_circuit_connection(b.color, a.color)
        elif not a.output and not b.input and b.output is not a:
            a.output = b
            self._print_circuit_connection(a.color, b.color)
        elif not circuit.input or not circuit.output:
            self.connect(circuits, a)

    def _connect_all(self, circuits: list[Circuit], circuit: Circuit|None) -> None:
        """Recursively connects each circuit recursively in a loop."""
        if circuit is None:
            circuit = circuits[0]
        if self.check_connections(circuits):
            return

        self.connect(circuits, circuit)
        self._connect_all(circuits, circuit.output)

    def connect_all(self, circuits: list[Circuit]) -> None:
        """Calls the recursive connector to recursively connect."""
        print('\n-> [ CONNECTING CIRCUITS ] <-')
        self._connect_all(circuits, circuits[0])
        print('<- [ CIRCUITS CONNECTED ] ->\n')

    def check_connections(self, circuits: list[Circuit]) -> bool:
        """Sends a duck and a penguin to check circuit connections."""
        duck = penguin = circuits[0]
        while duck.output and penguin.output and penguin.output.output:
            if duck is penguin:
                return True
        return False
