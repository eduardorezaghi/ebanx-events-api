from src.models.balance import Balance


class BalanceRepository:
    def __init__(self, objs: list[Balance] | None = None):
        self.balances: dict[str, Balance] = {}
        if objs:
            for obj in objs:
                self.balances[str(obj.account_id)] = obj

    def get_all_balances(self) -> list[Balance]:
        return list(self.balances.values())

    def get_balance(self, user_id: str) -> Balance | None:
        return self.balances.get(user_id)
