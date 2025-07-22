"""Core Printer"""

import time

class CorePrinter:
    """Core Printer

    Core functions and utilities to print core stuff
        for the core,
        from the core,
        by the core,
        part of the core,
        and nothing more.
    """

    GREY = '\033[90m'
    YELLOW = '\033[93m'
    WHITE = '\033[97m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

    IRIDESCENT = [
        (255, 255, 255),
        (240, 255, 255),
        (255, 240, 255),
        (255, 255, 240),
        (240, 255, 240),
        (240, 240, 255),
    ]

    TRIANGLE = [
        '       ▄▄▄      ',
        '      ████▄     ',
        '     █▀▀▀▀█▄    ',
        '    █ █▄▄█ █▄   ',
        '   █  ████  █▄  ',
        '  █   ████   █▄ ',
        ' █    ████    █▄',
        '████████████████',
    ]

    BANNER_HEIGHT = 14
    BANNER_WIDTH = 64
    CONTENT_WIDTH = BANNER_WIDTH - 2

    def __init__(self):
        pass

    def get_ansi_code(self, r: int, g: int, b: int) -> str:
        """Returns the ANSI escape code for this color (foreground)."""
        return f'\033[38;2;{r};{g};{b}m'

    def _get_fade_color(self, color_start: tuple, color_end: tuple, step: int, total_steps: int) -> str:
        """Calculates transition color from start color to end color based on step."""
        if total_steps <= 1:
            return self.get_ansi_code(*color_start)

        factor = step / (total_steps - 1)
        r = int(color_start[0] + (color_end[0] - color_start[0]) * factor)
        g = int(color_start[1] + (color_end[1] - color_start[1]) * factor)
        b = int(color_start[2] + (color_end[2] - color_start[2]) * factor)

        return self.get_ansi_code(r, g, b)

    def _clear_banner(self, lines: int) -> None:
        """Clears lines in terminal and resets cursor."""
        clear_line = '\x1b[2K'
        cursor_up = '\x1b[1A'
        reset_cursor = '\r'

        for _ in range(lines):
            print(f'{cursor_up}{clear_line}', end='')
            print(reset_cursor, end='', flush=True)

    def _banner(self, message: str, triangle_color_code: str) -> None:
        """Prints Paragon Relay Circuit banner."""
        triangle_lines = [
            f"{self.GREY}║{triangle_color_code}{line.center(self.CONTENT_WIDTH)}{self.RESET}{self.GREY}║"
            for line in self.TRIANGLE
        ]
        banner_lines = [
            f"{self.GREY}╔{'═' * self.CONTENT_WIDTH}╗",
            f"{self.GREY}║{' ' * self.CONTENT_WIDTH}║",
            *triangle_lines,
            f"{self.GREY}║{' ' * self.CONTENT_WIDTH}║",
            f"{self.GREY}║{self.YELLOW}{'PARAGON RELAY CIRCUIT'.center(self.CONTENT_WIDTH)}{self.RESET}{self.GREY}║",
            f"{self.GREY}║{self.CYAN}{message.center(self.CONTENT_WIDTH)}{self.RESET}{self.GREY}║",
            f"{self.GREY}║{' ' * self.CONTENT_WIDTH}║",
            f"{self.GREY}╚{'═' * self.CONTENT_WIDTH}╝{self.RESET}",
        ]
        print('\n'.join(banner_lines), end='', flush=True)

    def banner(self) -> None:
        """Prints animated Paragon Relay Circuit banner."""
        states = [
            'INITIALIZING SYSTEM...',
            'LOADING MODULES...',
            'CONFIGURING...',
            'FINALIZING SETUP...',
            'ACTIVE'
        ]

        fade_steps = 20
        frame_delay = 0.06
        n = fade_steps / len(self.IRIDESCENT)

        for state in states:
            for step in range(fade_steps):
                i = int(step / n)
                j = (i + 1) % len(self.IRIDESCENT)
                k = step % n
                t = k / (n - 1) if n > 1 else 1
                eased_t = 3 * (t ** 2) - 2 * (t ** 3)

                r1, g1, b1 = self.IRIDESCENT[i]
                r2, g2, b2 = self.IRIDESCENT[j]
                r = int(r1 + (r2 - r1) * eased_t)
                g = int(g1 + (g2 - g1) * eased_t)
                b = int(b1 + (b2 - b1) * eased_t)

                fade_color = self.get_ansi_code(r, g, b)
                self._clear_banner(self.BANNER_HEIGHT)
                self._banner(state, fade_color)
                time.sleep(frame_delay)

        print(flush=True)


if __name__ == '__main__':
    CorePrinter().banner()
