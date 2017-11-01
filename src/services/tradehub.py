import json
import settings


class TradeHub(object):
    def get_trades(self):
        with open(settings.PROJECT_ROOT+"\\src\\samples\\trades.json") as file:
            return json.load(file)