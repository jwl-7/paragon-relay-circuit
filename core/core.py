"""Paragon Relay Circuit Core"""

from circuits.circuit_core import CircuitCore
from core.core_printer import CorePrinter

class ParagonRelayCircuitCore:
    """The Core

    Controls the core and facilitates core
    processes such as the core transposition of
    the core xantrius neural protocols based off
    the core flumpunium traxalok archirithm.
    """

    def __init__(self):
        self.circuit_core = CircuitCore()
        self.printer = CorePrinter()

    def run(self) -> None:
        """Starts the core."""
        self.printer.banner()
        self.circuit_core.run()
