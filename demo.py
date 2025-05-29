"""
demo.py - A simple addition example.
"""

def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def main():
    """Main function to run the addition."""
    a = 4
    b = 5
    addition = add_numbers(a, b)
    print(f"Addition: {addition}")