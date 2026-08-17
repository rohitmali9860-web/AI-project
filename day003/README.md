# Day 003: GS1 Application Identifier (AI) Barcode Parser

- **Date:** 2026-08-17
- **Category:** GS1 / Barcode Utilities
- **Difficulty:** Intermediate

---

# GS1 Application Identifier (AI) Barcode Parser

## Background
In supply chain and logistics, GS1-128 and GS1 DataMatrix barcodes encode multiple data elements prefixed by 2-4 digit Application Identifiers (AIs).
Common AIs include:
- `01`: Global Trade Item Number (GTIN-14) - Fixed 14 numeric digits.
- `10`: Batch / Lot Number - Variable up to 20 alphanumeric characters (ended by `<GS>` / `\x1d` if not at end).
- `17`: Expiration Date (YYMMDD) - Fixed 6 numeric digits.
- `21`: Serial Number - Variable up to 20 alphanumeric characters.
- `310x`: Net weight in kg (where x is decimal point).

## Requirements
Implement `parse_gs1_string(raw_data: str) -> dict[str, str]` in `solution.py`:
1. Parse bracketed format: `(01)00012345678905(17)261231(10)LOT42(21)SER999`
2. Parse raw FNC1 / `<GS>` delimited format: `01000123456789051726123110LOT42\x1d21SER999`
3. Return a clean dictionary mapping AI code to parsed value:
   ```python
   {
       "01": "00012345678905",
       "17": "261231",
       "10": "LOT42",
       "21": "SER999"
   }
   ```

## Run Tests
```bash
python test_solution.py
```
