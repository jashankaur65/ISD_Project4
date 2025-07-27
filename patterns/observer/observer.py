class Observer:
    """Creating base class for observers in the Observer Pattern."""
    def update(self, message):
        raise ValueError("This method should be implemented in subclasses.")