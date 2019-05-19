import pandas as pd
import os

this_file_path = os.path.dirname(__file__)
filepath = this_file_path + "\\dates"
with open(filepath) as fp:
    dates = fp.readlines()
dates = [x[:-1] for x in dates]
dates = [pd.to_datetime(x) for x in dates]

def get_corrected_timestamp(timestamp):
    return dates[get_date(dates, timestamp)]

def get_date(dates, pivot):
    for i in range(0, len(dates)):
        if dates[i] < pivot:
            return i
        if dates[i] > pivot:
            if i == len(dates) - 1:
                return i
            elif dates[i + 1] < pivot:
                return i + 1
