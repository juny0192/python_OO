"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = self.next = start
    
    def __repr__(self):
        return f"Serial Number: (start: {self.start}, next: {self.next})"

    def generate(self):
        """Add 1 to start number everytime when this function called"""
        self.next += 1
        return self.next

    def reset(self):
        """Reset the current number and go back to start number"""
        self.next = self.start

