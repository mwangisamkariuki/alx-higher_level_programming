#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is not None and set_2 is not None:
        return set_1.symmetric_difference(set_2)
    return None
