"""The Circuit Core"""

from circuits.circuit_connector import CircuitConnector
from circuits.circuit_red import CircuitRed
from circuits.circuit_blue import CircuitBlue
from circuits.circuit_green import CircuitGreen

class CircuitCore:
    """Paragon Relay Circuit Circuit Core

    The circuit core for core circuits,
    which is activated by the core.
    """

    def __init__(self):
        self.connector = CircuitConnector()
        self.red_circuit = CircuitRed()
        self.blue_circuit = CircuitBlue()
        self.green_circuit = CircuitGreen()

    def run(self) -> None:
        """Starts the core."""
        self.launch_message()
        self.initialize_connector()

    def launch_message(self) -> None:
        """Renders core status."""
        print("\n=============================")
        print("    Circuit Core Status       ")
        print("=============================")
        print(f"{'CORE'.center(14)}{'STATUS'.center(14)}")
        print("=============================")
        print(f"{self.red_circuit.color.center(14)}{'Active'.center(14)}")
        print(f"{self.blue_circuit.color.center(14)}{'Active'.center(14)}")
        print(f"{self.green_circuit.color.center(14)}{'Active'.center(14)}")
        print("=============================\n")

    def initialize_connector(self) -> None:
        """Initializes connector and connects all the circuits."""
        self.connector.circuits = [
            self.red_circuit,
            self.blue_circuit,
            self.green_circuit
        ]
        self.connector.connect_all()
