import time


def transform_local_time(now):
    time_structure = time.localtime(now)
    year = time_structure.tm_year
    month = time_structure.tm_mon
    day = time_structure.tm_mday
    hour = time_structure.tm_hour
    minute = time_structure.tm_min
    second = time_structure.tm_sec
    if minute < 10:
        minute = '0{}'.format(str(minute))
    if hour < 10:
        hour = '0{}'.format(str(hour))
    if month < 10:
        month = '0{}'.format(str(month))
    if day < 10:
        month = '0{}'.format(str(day))
    if second < 10:
        second = '0{}'.format(str(second))
    result = '{}-{}-{} {}:{}:{}'.format(year, month, day, hour, minute, second)
    return result
