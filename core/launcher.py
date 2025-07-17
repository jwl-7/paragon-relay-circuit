"""Core Launcher"""

from core.launcher_messages import CoreLauncherMessages
from core.core import ParagonRelayCircuitCore

class CoreLauncher:
    """Core launcher class for the Paragon Relay Circuit.

    Absolute starter that uses spherical quantazolation
    to orchestrate a recursive vectronic cascade initialization.
    """

    def __init__(self):
        self.launcher_messages = CoreLauncherMessages()
        self.core = ParagonRelayCircuitCore()

    def run(self):
        """Initiate launch."""
        print(self.launcher_messages.decrypt(self.launcher_messages.launch_banner))
        self.core.run()
