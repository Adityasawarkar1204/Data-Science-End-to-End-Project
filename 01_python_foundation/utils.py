"""
Utility Functions Library
Reusable helper functions for data processing
"""

import numpy as np
from datetime import datetime


def remove_duplicates(data: list) -> list:
    """
    Removes duplicate values from a list while preserving order.
    """
    seen = set()
    unique_list = []
    for item in data:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list


def normalize_text(text: str) -> str:
    """
    Converts text to lowercase and removes leading/trailing spaces.
    """
    if not isinstance(text, str):
        return ""
    return text.lower().strip()


def calculate_zscore(value: float, mean: float, std: float) -> float:
    """
    Calculates Z-score of a given value.
    """
    if std == 0:
        return 0.0
    return (value - mean) / std


def date_formatter(date_string: str, input_format: str = "%Y-%m-%d") -> str:
    """
    Converts a date string to standard YYYY-MM-DD format.
    """
    try:
        date_obj = datetime.strptime(date_string, input_format)
        return date_obj.strftime("%Y-%m-%d")
    except Exception:
        return None


if __name__ == "__main__":
    # Small test block
    print("Testing Utility Functions...\n")

    print("Remove Duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
    print("Normalize Text:", normalize_text("  Data Science  "))
    print("Z-score:", calculate_zscore(80, 70, 5))
    print("Formatted Date:", date_formatter("2024-01-15"))
