import csv
import random
from datetime import datetime
# CONSTANT
FILENAME = 'writing_csv.csv'
COLUMN_NAMES = ['employee_id', 'entered_at', 'enter_for']
MAX_NUMBER_LOGS = 300
# FUNCTION
def fake_enter_for():
    enter_for_list = ['suppliement', 'reports', 'meeting', 'payment', 'bathroom', 'call', 'lunch']
    return random.choice(enter_for_list)
def fake_employee_id():
    employee_id_list = ['1002', '2009', '3478', '8623', '92873', '9872', '9823', '1267', '9812', '5432']
    return random.choice(employee_id_list)
def fake_timestamp():
    now = datetime.now()
    now = now.replace(hour=random.randint(7, 18), minute=random.randint(0, 59))
    ts = datetime.timestamp(now)
    return int(ts)
with open(FILENAME, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=COLUMN_NAMES)
    # WRITING HEADERS
    writer.writeheader()
    counter = 1
    while counter <= MAX_NUMBER_LOGS:
        writer.writerow({
            'employee_id': fake_employee_id(),
            'entered_at': fake_timestamp(),
            'enter_for': fake_enter_for()
        })
        counter += 1







