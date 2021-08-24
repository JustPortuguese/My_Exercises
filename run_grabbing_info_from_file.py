"""
This is an exercise to grab information from big files without using huge amounts of memory,
    being able to reduce the info grabbed to only what you need from the file.

This is for training purposes only.
"""

import re
import pandas as pd

file_path = input("FILE'S PATH")

create_groups = input('CREATE THE GROUPS TO GRAB THE RIGHT INFO')

group_1, group_2, group_3 = [], [], []

def get_info_from_file():
    with open(file_path) as file:
        for line in file:
            result = re.match(create_groups, line)
            if result:
                """
                group_1.append(result.group(1))
                group_2.append(result.group(3))
                group_3.append(result.group(4))
        return pd.DataFrame([group_1, group_2, group_3]).T
                """
        
get_info_from_file()
