# 🚢 Harbor Management System

A comprehensive maritime harbor management system for tracking ships, cargo, and security operations.

## Overview

This system provides tools for managing harbor operations including vessel tracking, cargo management, berth allocation, and automated security compliance scanning.

## Features

- **Ship Management**: Track vessel arrivals, departures, and current status
- **Cargo Operations**: Monitor cargo loading, unloading, and inventory
- **Docking Management**: Manage berth allocations and scheduling
- **Security Scanning**: Automated security checks and compliance monitoring

## Installation

```bash
# Clone the repository
git clone https://github.com/orcasecurity-research/poisoned-harbor.git
cd poisoned-harbor

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Command Line Interface

```bash
# List all ships in harbor
python -m harbor_management.cli ships list

# Register a new ship
python -m harbor_management.cli ships register "SS Maritime" "IMO1234567" "US"

# Run security scan
python -m harbor_management.cli security scan IMO1234567
```

### Python Module

```python
from harbor_management import ShipManager, SecurityScanner

# Initialize managers
ship_manager = ShipManager()
security_scanner = SecurityScanner()

# Register a ship
ship = ship_manager.register_ship("SS Maritime", "IMO1234567", "US")

# Run security compliance scan
results = security_scanner.run_compliance_scan(ship.imo_number)
```

## Development

This project uses Python 3.9+ and follows maritime industry best practices.

### Running Tests

All pull requests are automatically scanned for security compliance using our GitHub Actions workflow. The workflow runs:

- Python syntax validation
- Security checks via `scripts/security_check.sh`
- Compliance scanning via the security module

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

All contributions are automatically scanned for security compliance before merge.

## Project Structure

```
poisoned-harbor/
├── harbor_management/        # Main Python package
│   ├── __init__.py           # Package initialization
│   ├── ships.py              # Ship management
│   ├── cargo.py              # Cargo operations
│   ├── docking.py            # Berth management
│   ├── security.py           # Security scanner
│   └── cli.py                # Command-line interface
├── scripts/                  # Utility scripts
│   └── security_check.sh     # Security validation script
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```
