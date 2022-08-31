#!/usr/bin/python3
def roman_to_int(roman_string):
        ROMAN_MAP = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        total = 0
        prev = 0
        for i in range(len(roman_string)):
            curr = ROMAN_MAP[roman_string[i]]
            if curr > prev:
                total += curr - 2 * prev
            else:
                total += curr
            prev = curr
        return total
