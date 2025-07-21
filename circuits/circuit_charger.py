"""Beam me up"""

import math
import random
import time

from circuits.circuit import Circuit
from circuits.circuit_printer import CircuitPrinter

class CircuitCharger:
    """Charges circuits

    Uses vretonic easing functions for optimal charging.
    """

    EASING = [
    lambda t: 0.5 + 0.5 * math.sin(12 * math.pi * t) * (1 - t),
    lambda t: 1 - 4 * (t**2) if t < 0.3 else max(0, 1 - 10 * (t - 0.3)),
    lambda t: ((math.exp(t) - 1) / (math.e - 1)) * abs(math.sin(10 * math.pi * t)),
    lambda t: abs((t * 10) % 2 - 1),
    lambda t: (t ** 3) * math.cos(7 * math.pi * t),
    lambda t: math.sqrt(t) * abs(math.sin(5 * math.pi * t)),
    lambda t: 4 * (t - 0.5)**3 + 0.5,
    lambda t: 0.5 + 0.5 * (math.sin(15 * math.pi * t) + math.cos(20 * math.pi * t)) / 2,
]

    def __init__(self):
        self.printer = CircuitPrinter()
        self.rate = 0.02

    def charge(self, circuit: Circuit) -> None:
        """Charges circuit."""
        ease = random.choice(EASING)
        t = 0.0
        last_printed = -1
        bar_width = 30

        while t < 1.0:
            t = min(1.0, t + self.rate)
            circuit.flux = ease(t)
            percent = int(t * 100)

            if percent != last_printed:
                self.printer.charging(circuit, t, bar_width)
                last_printed = percent

            time.sleep(0.02)

        self.printer.charged(circuit, bar_width)

    def charge_circuits(self, circuits: list[Circuit]) -> None:
        """Charges all circuits."""
        self.printer.section('CHARGING CIRCUITS')
        for circuit in circuits:
            self.charge(circuit)
