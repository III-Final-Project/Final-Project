import time


def transform_local_time(now):
    time_structure = time.localtime(now)
    year = time_structure.tm_year
    month = time_structure.tm_mon
    day = time_structure.tm_mday
    hour = time_structure.tm_hour
    minute = time_structure.tm_min
    second = time_structure.tm_sec
    result = '{}-{}-{} {}:{}:{}'.format(year, month, day, hour, minute, second)
    return result
