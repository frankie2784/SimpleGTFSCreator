import csv
from datetime import time

Peaks = {
    'AM':(time(7,00), time(9,00)),
    'IP':(time(9,00), time(15,00)), 
    'PM':(time(15,00), time(18,00)),
    'OP':(time(18,00), time(7,00))
    }

def set_headways(headways):
    VITM_peaks = []
    for period in headways.keys():
        if headways[period] != 0:
            VITM_peaks.append(Peaks[period] + (int(headways[period]),period))
    return VITM_peaks

def set_dates(year):
    START_DATE_STR = str(year)+'0101'
    END_DATE_STR = str(year)+'1231'
    return START_DATE_STR, END_DATE_STR