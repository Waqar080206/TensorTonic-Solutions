def frequency_encoding(values):
    """
    Encode categorical values by their frequency.
    """
    freq = {}

    for v in values:
        freq[v] = freq.get(v, 0) + 1

    n = len(values)
    return [freq[v] / n for v in values]