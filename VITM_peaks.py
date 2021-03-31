import csv
from datetime import time

headways_new = []

VITM_peaks = {
    'AM':(time(7,00), time(9,00), 8, True),
    'IP':(time(9,00), time(15,00), 10, False), 
    'PM':(time(15,00), time(18,00), 8, True),
    'OP':(time(18,00), time(7,00), 20, False)
    }

with csv.DictReader(open("sample_input/Headways.csv", "rb")) as headways:
    insert_headways(headways, 1, 2021)

def insert_headways(headways, route, year):
    for h in headways:
        if h['route'] == route and h['year'] == year:
            headways_new.appeand(VITM_peaks[h[['period']][:2] + (h['headway'],) + (VITM_peaks[h[['period']][-1],))
    print(headways_new)

VITM_SERVICE_INFO = [("monfri", headways_new)]