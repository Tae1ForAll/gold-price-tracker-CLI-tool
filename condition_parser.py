import re
from dataclasses import dataclass
from enum import Enum

class Direction(Enum):
    UP = "up"
    DOWN = "down"
    
@dataclass(frozen=True)
class Condition:
    direction: Direction
    amount: float

def parse_conditions(tokens: list[str]) -> list[Condition]:
    COND_RE = re.compile(r"^(up|down)\[(\d+(?:\.\d+)?)\]$", re.IGNORECASE)
    
    if not tokens:
        raise ValueError("Missing -if conditions. Example: -if up[200] down[200]")

    cons: list[Condition] = []

    for t in tokens:
        t = t.strip()
        m = COND_RE.fullmatch(t)
        if not m:
            raise ValueError(f"Bad condition: {t!r}. Use up[NUMBER] or down[NUMBER]")

        direction_str = m.group(1).lower()
        amount = float(m.group(2))

        if amount <= 0:
            raise ValueError(f"Condition amount must be > 0: {t!r}")

        cons.append(
            Condition(
                direction=Direction(direction_str),
                amount=amount
            )
        )

    return cons
