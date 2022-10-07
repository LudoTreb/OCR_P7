class Action:
    def __init__(self, name, cost, profit_rate):
        """
        Initiate an action
        :param name: str
        :param cost: int
        :param profit_rate: int
        """
        self.name = name
        self.cost = cost
        self.profit_rate = profit_rate

    def __repr__(self):
        return f"{self.name} - {self.cost}€ - {self.profit_rate}%"
