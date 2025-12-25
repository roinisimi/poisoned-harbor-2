"""Docking and berth management module."""

from typing import Dict, List, Optional
from datetime import datetime


class Berth:
    """Represents a berth in the harbor."""
    
    def __init__(self, berth_id: str, capacity: int):
        self.berth_id = berth_id
        self.capacity = capacity
        self.occupied_by: Optional[str] = None
        self.available = True

    def assign_ship(self, ship_imo: str):
        """Assign berth to a ship."""
        self.occupied_by = ship_imo
        self.available = False

    def release(self):
        """Release berth from ship."""
        self.occupied_by = None
        self.available = True


class DockingManager:
    """Manages berth assignments and docking schedules."""
    
    def __init__(self):
        self.berths: Dict[str, Berth] = {}

    def add_berth(self, berth_id: str, capacity: int) -> Berth:
        """Add a new berth to the harbor."""
        berth = Berth(berth_id, capacity)
        self.berths[berth_id] = berth
        return berth

    def get_available_berths(self) -> List[Berth]:
        """Get list of available berths."""
        return [b for b in self.berths.values() if b.available]
