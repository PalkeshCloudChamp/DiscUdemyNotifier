from plyer import notification
from datetime import datetime
def DiscUdemyNotification():

    title = "Some Notification  DiscUdemy."
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    message = "Found new courses in DiscUdemy Website at ." +  dt_string

    notification.notify(title = title,
    message = message , 
    app_icon = None,
    timeout = 10,
    toast = False)