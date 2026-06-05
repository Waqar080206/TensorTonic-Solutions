def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    n = len(values)
    pairs = sorted((v, i) for i, v in enumerate(values))

    ranks = [0.0] * n
    i = 0

    while i < n:
        j = i

        while j + 1 < n and pairs[j + 1][0] == pairs[i][0]:
            j += 1

        avg_rank = (i + 1 + j + 1) / 2.0  # 1-based average rank

        for k in range(i, j + 1):
            ranks[pairs[k][1]] = avg_rank

        i = j + 1

    return ranks