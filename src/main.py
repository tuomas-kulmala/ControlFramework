from services.tradehub import TradeHub
from control.sanctioned_customer import SanctionedCustomer

class Runner(object):
    def __init__(self):
        self.trade_service = TradeHub()
        self.queue = self.trade_service.get_trades()

    def execute_queue(self):
        for element in self.queue:
            sanctioned = SanctionedCustomer()
            sanctioned.is_covered_by_sanctions(element)

if __name__ == '__main__':
    runner = Runner()
    runner.execute_queue()



