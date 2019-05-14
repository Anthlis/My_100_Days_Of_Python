import os
import csv
from collections import namedtuple
from typing import List

data = []


# Record = namedtuple(
#     'Record',
#     'In general, how worried are you about earthquakes?,'
#     'How worried are you about the Big One, a massive, catastrophic earthquake?,'
#     'Do you think the ""Big One"" will occur in your lifetime?,'
#     'Have you ever experienced an earthquake?,'
#     'Have you or anyone in your household taken any precautions for an earthquake '
#     '(packed an earthquake survival kit, prepared an evacuation plan, etc.)?,'
#     'How familiar are you with the San Andreas Fault line?,'
#     'How familiar are you with the Yellowstone Supervolcano?,'
#     'Age, What is your gender?,'
#     'How much total combined money did all members of your HOUSEHOLD earn last year?,'
#     'US Region'
# )


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'earthquake_data.csv')

    with open(filename, 'r', encoding='utf-8') as file_stream:
        # print(fin.read())

        # instead of print (fin.read()), do this instead after importing csv
        reader = csv.DictReader(file_stream)

        for row in reader:
            print("ROW --> {}".format(row))
