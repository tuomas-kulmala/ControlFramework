import json
import settings
from datetime import datetime

SUCCESS = "success"
WARNING = "warning"
FAILURE = "failure"


def log_message(type,object, message=None):
    time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    msg = "%s %s object:%s message:%s \n" % (time,type,object,message)
    with open(settings.PROJECT_ROOT + "\\log.txt","a") as file:
        file.write(msg)
