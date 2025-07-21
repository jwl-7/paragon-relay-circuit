"""Circuit Printer"""

import time
import sys

from circuits.circuit import Circuit

class CircuitPrinter:
    """Circuit Printer

    Print utils to print circuits in print form.
    """

    ARROW = '->'
    WIDTH = 40
    BAR_WIDTH = 30
    GREY = '\033[90m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    def __init__(self):
        pass

    def section(self, text: str) -> None:
        """Prints section header."""
        border = '=' * self.WIDTH
        print(f'\n{border}')
        print(f'{self.YELLOW}{text.center(self.WIDTH)}{self.RESET}')
        print(f'{border}\n')

    def status(self, circuit: Circuit) -> None:
        """Prints circuit status with transition."""
        states = [
            ('INACTIVE', self.GREY),
            ('BOOTING', self.YELLOW),
            ('ACTIVE', self.GREEN),
        ]
        name_width = 10
        status_width = 14
        padding_width = self.WIDTH - (name_width + status_width)

        for state, color_code in states:
            line = (
                ' ' * (padding_width // 2) +
                circuit.color.paint(circuit.color.name.rjust(name_width)) +
                f'{color_code}{state.center(status_width)}{self.RESET}' +
                ' ' * (padding_width - (padding_width // 2))
            )
            print(f'\r{line}', end='', flush=True)
            time.sleep(0.4)

        print()

    def connection(self, a: Circuit, b: Circuit) -> None:
        """Prints circuit connection."""
        arrow_pos = self.WIDTH // 2
        left_pos = arrow_pos - len(b.color.name) - 2
        right_pos = arrow_pos + len(self.ARROW) + 2

        line = (
            ' ' * left_pos +
            b.color.paint(b.color.name) +
            ' ' * (arrow_pos - (left_pos + len(b.color.name))) +
            self.YELLOW + self.ARROW + self.RESET +
            ' ' * (right_pos - (arrow_pos + len(self.ARROW))) +
            a.color.paint(a.color.name) +
            ' ' * (self.WIDTH - (right_pos + len(a.color.name)))
        )

        print(line)

    def charging(self, circuit, progress: float) -> None:
        """Prints circuit charging bar."""
        blocks = int(self.BAR_WIDTH * progress)
        filled = f"{circuit.color.code}{'#' * blocks}{self.RESET}"
        empty = '-' * (self.BAR_WIDTH - blocks)
        _bar = filled + empty
        percent = int(progress * 100)
        name_colored = circuit.color.paint(circuit.color.name)
        padding = ' ' * (5 - len(circuit.color.name))

        print(f'\r{name_colored}{padding} charging [{_bar}] {percent}%', end='', flush=True)

    def charged(self, circuit) -> None:
        """Prints complete circuit charging bar."""
        max_name_len = 5
        filled = f"{circuit.color.code}{'#' * self.BAR_WIDTH}{self.RESET}"
        name_colored = circuit.color.paint(circuit.color.name)
        padding = ' ' * (max_name_len - len(circuit.color.name))

        print(f'\r{name_colored}{padding} charged  [{filled}] 100%      ')
