#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:53:53 2023

@author: marieprimdahl
"""

import numpy as np
import pandas as pd

df_ma = pd.read_csv("/Users/marieprimdahl/Documents/Studie/Programmer/GitHub/posthink_master/data/Kun_gjenta_svar.csv")
pos_answer_list = list(df_ma["Default Report"])

# make clean list, exclude instruction
pos_answer = pos_answer_list[3:]

# trying to make  a list with variation of dennis's (350 appereances accourding to vectorizer):
pos_list = ["positiv", "positivt"]

# word_counts = {word: 0 for word in pos_list}
total_count = 0

# loop through each string in the list
for string in pos_answer:
    # loop through each word in the list
    for word in pos_list:
        # count the number of times the word appears in the string
        word_count = string.count(word)
        total_count += word_count

print("The total time a variation of positiv i s mentioned is:", total_count)

