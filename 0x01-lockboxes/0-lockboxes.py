#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from
0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    n : number of boxes
    opend: opend boxes
    keys: available keys
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while True:
        new_keys = []
        for key in keys:
            for new_key in boxes[key]:
                if new_key < n and not opened[new_key]:
                    opened[new_key] = True
                    new_keys.append(new_key)

        if not new_keys:
            break

        keys = new_keys

    return all(opened)
