"""The Circuit Core"""

from circuits.circuit_connector import CircuitConnector
from circuits.circuit_charger import CircuitCharger
from circuits.circuit_printer import CircuitPrinter
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
        self.charger = CircuitCharger()
        self.printer = CircuitPrinter()
        self.red_circuit = CircuitRed()
        self.blue_circuit = CircuitBlue()
        self.green_circuit = CircuitGreen()
        self.circuits = [
            self.red_circuit,
            self.blue_circuit,
            self.green_circuit
        ]

    def run(self) -> None:
        """Starts the core."""
        self.core_status()
        self.connector.connect_circuits(self.circuits)
        self.charger.charge_circuits(self.circuits)

    def core_status(self) -> None:
        """Displays core status."""
        self.printer.section('CORE STATUS')
        self.printer.status(self.red_circuit)
        self.printer.status(self.blue_circuit)
        self.printer.status(self.green_circuit)
