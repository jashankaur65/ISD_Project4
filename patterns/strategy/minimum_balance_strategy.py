from .service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    def __init__(self, min_balance, penalty_fee):
        self._min_balance = min_balance
        self._penalty_fee = penalty_fee
        

    def calculate_service_charges(self, account):
        if account.balance < self._min_balance:
            return self.BASE_SERVICE_CHARGE + self._penalty_fee
        return self.BASE_SERVICE_CHARGE