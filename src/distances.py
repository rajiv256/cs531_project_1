'''
Run from the root of the project

python3 src/distances.py
'''
import numpy as np
import random
import os
import pandas as pd
from constants import DATA_DIR, ROOT, SRC_DIR


def euclidean(p, q):
	return math.sqrt((p[0]-q[0])**2 + (p[1]+q[1])**2)


def is_fully_matched(matched, parent):
    b = True
    for item in matched:
        if item == []:
            b = False
    for item in parent:
        if item == []:
            b = True
    return b

def dtw(matched):
    return 1


def find_minimal_matching(
	t1,
	t2,
	matched,
	parent,
	t1_idx,
	t2_from_idx,
	distance_measure='dtw'
	):
    
    if is_fully_matched(matched, parent):
        return dtw(matched), matched

    for t2_idx in range(t2_from_idx, len(t2))
        matched[t1_idx].append(t2_idx)
        parent[t2_idx].append(t1_idx)
        



        




def find_minimal_matching_wrapper(t1, t2, distance_measure='dtw'):
	'''Finds the minimal possible matching between `t1` and `t2`
	by utilizing the distance measure as well.'''

	# Keeps track of the correspondence
	matched = [[] for _ in t1]

	# Keeps track of the correspondence in the opposite direction.
	parent = [[] for _ in t2]

	# Index into t1 of the point to be matched...recursive definition
	to_match = 0

	# Index into t2 to give the start index of the available points to match with
	match_from = 0
	score, matching = find_minimal_matching(t1, t2, matched, parent, to_match, match_from, distance_measure)

	return score, matching
