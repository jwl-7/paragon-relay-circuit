"""Core Launcher"""

from core.launcher_messages import LAUNCH_BANNER_ACTUAL
from core.launcher_messages import ParagonRelayCircuitCoreLauncherMessages

class ParagonRelayCircuitLauncher:
    """Launcher class for the entire Paragon Relay Circuit.

    Absolute starter that uses spherical quantazolation
    to orchestrate a recursive vectronic cascade initialization.
    """
    def __init__(self):
        """Initialization."""
        self.launcher_messages = ParagonRelayCircuitCoreLauncherMessages()

    def run(self):
        """Initiate launch."""
        print(self.launcher_messages.decrypt(LAUNCH_BANNER_ACTUAL))
