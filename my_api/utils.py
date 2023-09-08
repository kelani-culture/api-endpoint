from datetime import datetime
from datetime import timezone

def get_current_day():
    """
        A function that returns the
        current day
    """
    dt = datetime.now()
    day_name =  dt.strftime('%A')
    return day_name

def get_current_time():
    """
    A function that returns the
    current in utc format time
    """
    dt = datetime.now()
    utc_datetime = datetime.strftime(dt,\
                                     "%Y-%m-%dT%H:%M:%SZ"
                                     )
    return utc_datetime
