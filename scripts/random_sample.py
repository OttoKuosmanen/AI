# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:09:42 2023

@author: Otto
"""
import json
import random

relative_location_name = '../../reddit_data/results/DATA.json'
output_file = '../data/sample_new.json' # name has been changed NOTE

#Sample size
n = 50

def read(relative_location_name):
    with open(relative_location_name, 'r') as f:
        out = json.load(f)
        return out
    
def save_file(file):
    with open(output_file, 'w') as f:
        json.dump(file, f, indent=4)


# reading in data
analysis_data = read(relative_location_name)

# Taking a random sample
sample = random.sample(analysis_data, n)

# Saving the sample in the data folder

save_file(sample)