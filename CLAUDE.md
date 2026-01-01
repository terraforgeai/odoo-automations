# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains automation scripts and AI solutions for Odoo ERP implementation and business operations. It's designed to streamline Odoo administration and business process automation.

## Development Commands

This is a Python-based project. Run scripts directly with Python:

```bash
python odoo_api.py
```

No package manager configuration files (requirements.txt, pyproject.toml) are present, so dependencies need to be installed manually as needed.

## Core Architecture

### OdooAPI Class (`odoo_api.py`)
The main component is a Python wrapper for Odoo's XML-RPC API:

- **OdooConfig**: Configuration dataclass holding connection parameters (URL, database, username, password/API key)
- **OdooAPI**: Main API wrapper class with lazy-loaded XML-RPC endpoints
- **Authentication**: Handles login and maintains user session
- **CRUD Operations**: Provides methods for search, read, create, write, and unlink operations
- **Model Abstraction**: Generic execute method for calling any Odoo model method

### Connection Details
- Target Odoo instance: `fwapparel.odoo.com`
- Database: `fwapparel` 
- Authentication: Username/password or API key via XML-RPC

### Key Methods
- `authenticate()`: Establishes connection and gets user ID
- `execute()`: Generic method executor for any Odoo model/method
- `search_read()`: Combined search and read operation
- CRUD shortcuts: `create()`, `write()`, `unlink()`

## Security Notes

- API credentials are configured in the main() function
- Replace placeholder "YOUR_API_KEY_HERE" with actual credentials when running
- Credentials should not be committed to version control