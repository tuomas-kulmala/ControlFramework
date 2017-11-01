from services.customer import CustomerService
from services import log

class SanctionedCustomer(object):
    def __init__(self):
        self.customer_service = CustomerService();
        self.russian_sanctions = self.customer_service.get_russian_sanctions_list()

    def is_covered_by_sanctions(self,object):

        if self.find_in_sanctions(object["customer_id"]):
            log.log_message(log.WARNING,object,"failure due to hit on sanctions list")
            return True
        else:
            log.log_message(log.SUCCESS, object)
            return False


    def find_in_sanctions(self,needle):
        result = False
        for element in self.russian_sanctions:
            if element["id"] == needle:
                result = True
                break
        return result