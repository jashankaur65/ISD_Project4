from .service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_fee):
        self._overdraft_fee = overdraft_fee

    def calculate_service_charges(self, account):
        return self.BASE_SERVICE_CHARGE + (self._overdraft_fee if account.balance < 0 else 0)