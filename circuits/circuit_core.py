"""The Circuit Core"""

from circuits.circuit_connector import CircuitConnector
from circuits.circuit_charger import CircuitCharger
from circuits.circuit_red import CircuitRed
from circuits.circuit_blue import CircuitBlue
from circuits.circuit_green import CircuitGreen

class CircuitCore:
    """Paragon Relay Circuit Circuit Core

    The circuit core for core circuits,
    which is activated by the core.
    """

    def __init__(self):
        self.circuits = []
        self.connector = CircuitConnector()
        self.charger = CircuitCharger()
        self.red_circuit = CircuitRed()
        self.blue_circuit = CircuitBlue()
        self.green_circuit = CircuitGreen()

    def run(self) -> None:
        """Starts the core."""
        self.launch_message()
        self.initialize_circuits()
        self.connector.connect_all(self.circuits)
        self.charger.charge_circuits(self.circuits)

    def launch_message(self) -> None:
        """Renders core status."""
        print("\n=============================")
        print("    Circuit Core Status       ")
        print("=============================")
        print(f"{'CORE'.center(14)}{'STATUS'.center(14)}")
        print("=============================")
        print(f"{self.red_circuit.color.center(14)}{'ACTIVE'.center(14)}")
        print(f"{self.blue_circuit.color.center(14)}{'ACTIVE'.center(14)}")
        print(f"{self.green_circuit.color.center(14)}{'ACTIVE'.center(14)}")
        print("=============================\n")

    def initialize_circuits(self) -> None:
        """Builds list of circuits."""
        self.circuits = [
            self.red_circuit,
            self.blue_circuit,
            self.green_circuit
        ]
