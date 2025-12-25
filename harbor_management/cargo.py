"""Cargo operations module."""

from typing import Dict, List, Optional
from enum import Enum


class CargoType(Enum):
    """Types of cargo handled by the harbor."""
    CONTAINER = "container"
    BULK = "bulk"
    LIQUID = "liquid"
    VEHICLE = "vehicle"


class Cargo:
    """Represents cargo in the harbor."""
    
    def __init__(self, cargo_id: str, cargo_type: CargoType, weight: float):
        self.cargo_id = cargo_id
        self.cargo_type = cargo_type
        self.weight = weight
        self.ship_imo: Optional[str] = None
        self.loaded = False

    def load_to_ship(self, ship_imo: str):
        """Load cargo onto a ship."""
        self.ship_imo = ship_imo
        self.loaded = True

    def unload(self):
        """Unload cargo from ship."""
        self.ship_imo = None
        self.loaded = False


class CargoManager:
    """Manages cargo inventory and operations."""
    
    def __init__(self):
        self.cargo_inventory: Dict[str, Cargo] = {}

    def register_cargo(self, cargo_id: str, cargo_type: CargoType, weight: float) -> Cargo:
        """Register new cargo in the system."""
        cargo = Cargo(cargo_id, cargo_type, weight)
        self.cargo_inventory[cargo_id] = cargo
        return cargo

    def list_cargo(self, ship_imo: Optional[str] = None) -> List[Cargo]:
        """List cargo, optionally filtered by ship."""
        if ship_imo:
            return [c for c in self.cargo_inventory.values() if c.ship_imo == ship_imo]
        return list(self.cargo_inventory.values())
