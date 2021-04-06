import os
import re
import time

EPOCHE_PER_DAY = 24 * 3600 / 30

location = '/var/logs/sectors'


def get_current_epoch_by_current_time():
    current_timestamp = int(time.time())
    current_epoch = int((current_timestamp - 1598306471) / 30)
    return current_epoch

for filename in os.listdir(location):
    if filename == 'sectors.log':
        print(filename)
        file = open(os.path.join(location, filename), "r")
        lines = file.read().splitlines()
        file.close()
        current_epoch = get_current_epoch_by_current_time()

        for line in lines:
            sector_pattern = re.compile(r"([0-9]+) .* ")
            sector_number = sector_pattern.findall(line)

            expiration_pattern = re.compile(r"\D(\d{3,})\D")
            expiration = expiration_pattern.findall(line)

            if expiration and expiration:
                remaining_days = (int(expiration[0]) - current_epoch) / (EPOCHE_PER_DAY)
                if remaining_days < 30:
                    expiration_weeks = remaining_days / 7
                    expiration_days = remaining_days % 7
                    print(line)
