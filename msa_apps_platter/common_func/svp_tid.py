from datetime import datetime
from datetime import timedelta
import pandas as pd

def format_num_to_datetime(year:int, month:int, day:int, hour:int, minute:int, second:int):
    date_time_value = datetime(year,month,day,hour,minute,second)
    return date_time_value

def format_datetime_to_str(date_time_value:datetime):
    year = str(date_time_value.year)
    month = str(date_time_value.month)
    day = str(date_time_value.day)
    hour = str(date_time_value.hour)
    minute = str(date_time_value.minute)
    second = str(date_time_value.second)
    return [year,month,day,hour,minute,second]

def format_str_to_datetime_num(year:str, month:str, day:str, hour:str, minute:str, second:str):
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    minute = int(minute)
    second = int(second)
    return year,month,day,hour,minute,second