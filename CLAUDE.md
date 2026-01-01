# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains automation scripts and AI solutions for Faith Wear Apparel's Odoo ERP implementation. FWA operates a CMT (Cut-Make-Trim) subcontracting business model for corporate uniform manufacturing, currently tracking 345+ active orders that need automation.

## Project Structure

```
FaithWearApparel/
├── odoo-automations/           # Main automation scripts (this repo)
├── business-analysis/          # Business requirements and analysis
├── configuration/             # Odoo setup and configuration docs
├── design-docs/              # System design and workflow docs
├── implementation-notes/     # Implementation guides and plans
├── odoo-audit/              # System audit reports (A+ grade - 9.6/10)
└── reference-data/          # Product catalogs, staff guides, pricing
```

## Business Context

### Core Business Model
- **Primary Products**: Golf shirts (72 SKUs: 9 colors × 8 sizes), corporate uniforms
- **Manufacturing**: Subcontracting model with CMT Factory Harare
- **Services**: Embroidery (Embroidery House Greendale), custom branding
- **Target Market**: Corporate clients requiring custom uniforms

### Key Business Processes for Automation
1. **Sales Order → Subcontracting PO → Material Transfer → Manufacturing → Delivery**
2. **Excel-to-Odoo Migration** (345 active orders with 17 tracking fields)
3. **Multi-stage Progress Tracking** (Quotation → Fabric → Manufacturing → Branding → Fiscal → Payment)
4. **Raw Material Management** (fabrics, trims, buttons transferred to subcontractors)
5. **Quality Control & Branding** (embroidery, printing services)

### Product Structure
```
FINISHED GOODS
├── Golf Shirts (Primary - 9 colors: White, Black, Red, Orange, Navy, Blue, Green, Putty, Mayo)
├── T-Shirts (Men's, Ladies, Kids variants)
├── Bottoms (Trousers, Tracksuit bottoms)
└── Accessories (Caps, Bags, Aprons)

RAW MATERIALS
├── Fabrics/Knits (9 colors × 150mm width)
└── Trims (Labels, Buttons)

SERVICES
├── CMT (Cut-Make-Trim subcontracting)
├── EMBROIDERY
└── PRINTING
```

## Development Commands

This is a Python-based project. Run scripts directly with Python:

```bash
python odoo_api.py
```

No package manager configuration files are present, so install dependencies manually:
```bash
pip install xmlrpc
```

## Core Architecture

### OdooAPI Class (`odoo_api.py`)
Production-ready API wrapper for FWA's Odoo instance:

- **OdooConfig**: Configuration dataclass holding connection parameters
- **OdooAPI**: Main API wrapper class with lazy-loaded XML-RPC endpoints  
- **Authentication**: Handles login and maintains user session
- **CRUD Operations**: Methods for search, read, create, write, and unlink operations
- **Model Abstraction**: Generic execute method for any Odoo model method

### Connection Details
- **Odoo instance**: `fwapparel.odoo.com`
- **Database**: `fwapparel`
- **Authentication**: Username/password or API key via XML-RPC
- **Status**: Production-ready (A+ grade audit - 9.6/10)

### Implementation Status
**Phase 1 - COMPLETED:**
- ✅ 6 Core apps configured: Sales, CRM, Inventory, Purchase, Manufacturing, Accounting
- ✅ Automated CMT workflow with subcontracting POs
- ✅ 72 golf shirt SKUs with size variants
- ✅ BOM configuration (1.5m fabric, 3 buttons, 1 label per shirt)
- ✅ 17 custom fields replicating Excel tracking system

**Phase 2 - IMMEDIATE PRIORITIES:**
1. Data migration of 345 active orders from Excel
2. User training (4 sessions planned)
3. Go-live support
4. Minor config fixes (color attributes, list views)

### Key Automation Points
1. **Sales Order Creation** → Auto-generates Purchase Orders to CMT subcontractor
2. **Material Transfer** → Auto-transfers raw materials to subcontractor location
3. **Manufacturing Receipt** → Auto-receives finished goods back to main warehouse
4. **Progress Tracking** → Replaces manual Excel checkboxes with automated workflow
5. **Inventory Management** → Real-time visibility vs Excel limitations

### Business Value
- **Projected ROI**: 74% first-year return ($11,500 value from $8,500 investment)
- **Time Savings**: 300 hours/year in admin time
- **Scalability**: Can handle 10x order volume (vs Excel limitations)
- **Accuracy**: Eliminates manual PO creation and material transfer errors

## Security Notes

- API credentials configured in main() function
- Replace "YOUR_API_KEY_HERE" with actual API key for production use  
- Never commit credentials to version control
- Production system already configured with proper user access controls

## Key Files for Automation Development

- **business-analysis/client_summary.md**: Complete business requirements
- **odoo-audit/AUDIT_COMPLETE.md**: System configuration audit and status
- **reference-data/FWA_Product_Category_Hierarchy.md**: Complete product catalog
- **configuration/**: Detailed Odoo setup documentation for all modules