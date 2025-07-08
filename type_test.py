def add( a, b):
    """Add two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers.")
    if type(a) != type(b):
        raise TypeError("Both arguments must be numbers, not strings.")
    return a + b

if __name__ == "__main__":
   a = "cat"
   b = "5"

   add(a, b)