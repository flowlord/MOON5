# -*- coding: utf-8 -*-

"""
Word Generator: Generates words based on trigram probabilities with weighted length distribution.
"""

import json
import os
from uuid import uuid4
from random import randint, choice


# Load settings
SETTINGS_PATH = "settings.json"
with open(SETTINGS_PATH, 'r', encoding='utf-8') as file:
    data = json.load(file)

MIN_LENGTH = data["MIN_LENGTH"]
MAX_LENGTH = data["MAX_LENGTH"]
# Ensure output directory exists
OUTPUT_DIR = data["OUTPUT_DIR"]
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

FILE_PATH = data["word_lst_pth"]

characters = open("database.txt", "r", encoding="utf-8").read()

WORD_LIST = open(data["word_lst_pth"], "r", encoding="utf-8").read().splitlines()


#Generate weighted length distribution

def gen_weigthed_length(min_length, max_length):
    dict_wighted_length = {}

    F = max_length

    for e in range(3, max_length):
        dict_wighted_length[e] = randint(min_length, F)
        F = F - 1
    return dict_wighted_length


def gen_c(length):
    c = ""
    for _ in range(length):
        c = c + choice(characters)
    return c


def gen_key():

    LENGTH_WEIGHTS = gen_weigthed_length(MIN_LENGTH, MAX_LENGTH)
    LENGTH_DISTRIBUTION = []

    for length, weight in LENGTH_WEIGHTS.items():
        LENGTH_DISTRIBUTION.extend([length] * weight)
    
    output_file = os.path.join(OUTPUT_DIR, f"{uuid4().hex[:3]}.txt")

    with open(output_file, "w", encoding="utf-8") as file:
        for e in range(len(WORD_LIST)):
            file.write(gen_c(choice(LENGTH_DISTRIBUTION))+"\n")
    
    f =  open(output_file, "r", encoding="utf-8").read()
    ff = open(output_file, "w", encoding="utf-8").write(f[0:-1])

def gen_many_key(n):
    for _ in range(n):
        gen_key()


gen_many_key(51)





