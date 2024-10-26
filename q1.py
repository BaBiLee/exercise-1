from typing import List

def most_frequent_lengths(strings: List[str]) -> List[str]:
    length_counts = {}
    for s in strings:
        length = len(s)
        if length in length_counts:
            length_counts[length] += 1
        else:
            length_counts[length] = 1

    max_frequency = max(length_counts.values())

    most_frequent_lengths = [
        length for length, count in length_counts.items() if count == max_frequency
    ]

    longest_frequent_length = max(most_frequent_lengths)

    result = [s for s in strings if len(s) == longest_frequent_length]

    return result

