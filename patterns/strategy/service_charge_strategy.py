class ServiceChargeStrategy:
    """Creating a base class for service class strategies."""
    BASE_SERVICE_CHARGE = 5.0

    def calculate_service_charges(self, account):
        raise ValueError("This method should be implemented in subclasses.")