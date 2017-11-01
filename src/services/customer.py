import json
import settings

class CustomerService(object):
    def get_russian_sanctions_list(self):
        with open(settings.PROJECT_ROOT+"\\src\\samples\\customers.json") as file:
            return json.load(file)