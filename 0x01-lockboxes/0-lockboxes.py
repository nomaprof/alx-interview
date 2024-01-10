#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
     a method that tells if all boxes can be opened

    :parameter boxes:
    :return: True or False for Success or Failure
    """
    if not boxes or type(boxes) is not list:
        return False

    opened = [0]
    for n in opened:
        for key in boxes[n]:
            if key not in opened and key < len(boxes):
                opened.append(key)
    if len(opened) == len(boxes):
        return True
    return False
