"""Core Launcher"""

from core.core import ParagonRelayCircuitCore

class CoreLauncher:
    """Core launcher class for the Paragon Relay Circuit.

    Absolute starter that uses spherical quantazolation
    to orchestrate a recursive vectronic cascade initialization.
    """

    def __init__(self):
        self.core = ParagonRelayCircuitCore()

    def run(self) -> None:
        """Initiate launch."""
        self.core.run()
