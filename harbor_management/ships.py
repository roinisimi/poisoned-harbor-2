"""Ship management module."""

from typing import List, Dict, Optional
from datetime import datetime


class Ship:
    """Represents a maritime vessel."""
    
    def __init__(self, name: str, imo_number: str, flag: str):
        self.name = name
        self.imo_number = imo_number
        self.flag = flag
        self.arrival_time: Optional[datetime] = None
        self.departure_time: Optional[datetime] = None
        self.status = "pending"

    def dock(self):
        """Record ship docking."""
        self.arrival_time = datetime.now()
        self.status = "docked"

    def depart(self):
        """Record ship departure."""
        self.departure_time = datetime.now()
        self.status = "departed"


class ShipManager:
    """Manages ship registry and operations."""
    
    def __init__(self):
        self.ships: Dict[str, Ship] = {}

    def register_ship(self, name: str, imo_number: str, flag: str) -> Ship:
        """Register a new ship in the harbor."""
        ship = Ship(name, imo_number, flag)
        self.ships[imo_number] = ship
        return ship

    def get_ship(self, imo_number: str) -> Optional[Ship]:
        """Retrieve ship by IMO number."""
        return self.ships.get(imo_number)

    def list_ships(self, status: Optional[str] = None) -> List[Ship]:
        """List all ships, optionally filtered by status."""
        if status:
            return [s for s in self.ships.values() if s.status == status]
        return list(self.ships.values())
