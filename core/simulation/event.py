from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Event:
    tick: int
    entity_name: str
    action: str
    reason: str
    before: Dict[str, Any]
    after: Dict[str, Any]

