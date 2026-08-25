"""
Day Challenge: GS1 Application Identifier (AI) Barcode Parser
"""
import re
from typing import Dict

# Common GS1 AI specifications: AI -> (length_type, fixed_length_or_max)
AI_SPECS = {
    "01": ("FIXED", 14),   # GTIN
    "10": ("VAR", 20),     # Batch / Lot
    "17": ("FIXED", 6),    # Expiration (YYMMDD)
    "21": ("VAR", 20),     # Serial
    "00": ("FIXED", 18),   # SSCC
    "30": ("VAR", 8),      # Count
}


def parse_gs1_string(raw_data: str) -> Dict[str, str]:
    """
    Parse a GS1 barcode data string into a dictionary of AI -> value.
    
    Supports:
    1. Human readable bracketed format: '(01)00012345678905(17)261231(10)BATCH1'
    2. Raw scanner format with FNC1 / group separators (\x1d or <GS>):
       '01000123456789051726123110BATCH1\x1d21SER123'
       
    Args:
        raw_data: Raw barcode string.
        
    Returns:
        Dict[str, str]: Dictionary mapping AI code strings to their values.
    """
    # TODO: Check if raw_data is bracketed format e.g. '(01)...(17)...'
    # TODO: If bracketed, extract AI and values using regex
    # TODO: If raw stream, iterate through AI prefixes, consume fixed length for fixed AIs,
    #       and consume up to group separator (\x1d, <GS>) or max length for variable AIs
    # TODO: Return parsed key-value dictionary
    raise NotImplementedError("TODO: Implement parse_gs1_string")
