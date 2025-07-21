"""Core Launcher"""

import base64

from core.core import ParagonRelayCircuitCore

LAUNCH_BANNER_ACTUAL = '''
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                           ▄▄▄                                ║
║                          ████▄                               ║
║                         █▀▀▀▀█▄                              ║
║                        █ █▄▄█ █▄                             ║
║                       █  ████  █▄                            ║
║                      █   ████   █▄                           ║
║                     █    ████    █▄                          ║
║                    ████████████████                          ║
║                                                              ║
║                   PARAGON RELAY CIRCUIT                      ║
║                   INITIALIZING SYSTEM...                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
'''

class CoreLauncher:
    """Core launcher class for the Paragon Relay Circuit.

    Absolute starter that uses spherical quantazolation
    to orchestrate a recursive vectronic cascade initialization.
    """

    def __init__(self):
        self.core = ParagonRelayCircuitCore()

    def run(self) -> None:
        """Initiate launch."""
        self.launch_message(LAUNCH_BANNER_ACTUAL)
        self.core.run()

    def launch_message(self, s: str) -> str:
        """Processes the message for core launch."""
        encoded = s.encode('utf-8')
        encodeded = base64.b85encode(encoded)
        decodeded = base64.b85decode(encodeded)
        encodededed = base64.b64encode(decodeded)
        decodededed = base64.b64decode(encodededed)
        encodedededed = base64.b32encode(decodededed)
        decodedededed = base64.b32decode(encodedededed)

        return decodedededed.decode('utf-8')
