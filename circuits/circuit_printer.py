"""Circuit Printer"""

from circuits.circuit import Circuit

class CircuitPrinter:
    """Circuit Printer

    Print utils to print circuits in print form.
    """

    def __init__(self):
        pass

    def section(self, text: str, width: int = 40) -> None:
        """Prints section header."""
        border = '=' * width
        print(f'\n{border}')
        print(text.center(width))
        print(f'{border}\n')

    def status(self, circuit: Circuit) -> None:
        """Prints circuit status."""
        colored_name = circuit.color.paint(circuit.color.name.center(14))
        colored_status = '\033[32m' + 'ACTIVE'.center(14) + '\033[0m'
        print(f'{colored_name}{colored_status}')

    def connection(self, a: Circuit, b: Circuit) -> None:
        """Prints circuit connection."""
        width = 40
        arrow = '->'
        arrow_pos = width // 2
        left_pos = arrow_pos - len(b.color.name) - 2
        right_pos = arrow_pos + len(arrow) + 2
        line = [' '] * width

        for i, ch in enumerate(b.color.name):
            if 0 <= left_pos + i < width:
                line[left_pos + i] = ch

        for i, ch in enumerate(arrow):
            line[arrow_pos + i] = ch

        for i, ch in enumerate(a.color.name):
            if 0 <= right_pos + i < width:
                line[right_pos + i] = ch

        print(''.join(line))

    def charging(self, circuit, progress: float, bar_width: int = 30) -> None:
        """Prints circuit charging bar."""
        blocks = int(bar_width * progress)
        filled = f"{circuit.color.code}{'#' * blocks}\033[0m"
        empty = '-' * (bar_width - blocks)
        _bar = filled + empty
        percent = int(progress * 100)
        print(f'\r{circuit.color.name} charging [{_bar}] {percent}%', end='', flush=True)

    def charged(self, circuit, bar_width: int = 30) -> None:
        """Prints complete circuit charging bar."""
        filled = f"{circuit.color.code}{'#' * bar_width}\033[0m"
        print(f'\r{circuit.color.name} charged  [{filled}] 100%      ')
