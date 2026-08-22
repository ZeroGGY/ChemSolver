"""
Input validation utilities for ChemSolver 9-10.
"""

def validate_positive(value: float, field_name: str) -> str | None:
    if value <= 0:
        return f"**Error:** {field_name} must be greater than 0."
    return None

def validate_non_negative(value: float, field_name: str) -> str | None:
    if value < 0:
        return f"**Error:** {field_name} cannot be negative."
    return None

def validate_temperature_kelvin(temp_celsius: float) -> str | None:
    if temp_celsius < -273.15:
        return "**Error:** Temperature cannot be below Absolute Zero (-273.15 °C)."
    return None

def validate_ph_range(ph_value: float) -> str | None:
    if ph_value < 0.0 or ph_value > 14.0:
        return "**Error:** pH value must be between 0.0 and 14.0."
    return None