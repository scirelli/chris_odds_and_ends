#!/usr/bin/env python3

import csv
import pandas as pd
import os
import sys

Dict = {}

with open('./citibike.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		Value = row['birth_year']
		
		try: 
			year = int(Value[:4])
		except:
			print('"' + Value + '"')
