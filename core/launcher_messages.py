"""Core Launcher Messages"""
import base64

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

class ParagonRelayCircuitCoreLauncherMessages:
    """Class text message protocol with letters and not letters.

    Letters include those from the Paleotonic alphabet used in the Carbon era.
    """

    def __init__(self):
        """Initialization."""
        self.launch_banner = LAUNCH_BANNER_ACTUAL

    def decrypt(self, s: str) -> str:
        """Decrypts a base64 byte string."""
        encoded = s.encode('utf-8')
        encodeded = base64.b85encode(encoded)
        decodeded = base64.b85decode(encodeded)
        encodededed = base64.b64encode(decodeded)
        decodededed = base64.b64decode(encodededed)
        encodedededed = base64.b32encode(decodededed)
        decodedededed = base64.b32decode(encodedededed)

        return decodedededed.decode('utf-8')
