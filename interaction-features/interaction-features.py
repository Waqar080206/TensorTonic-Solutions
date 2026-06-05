def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    result = []

    for row in X:
        new_row = row[:]
        n = len(row)

        for i in range(n):
            for j in range(i + 1, n):
                new_row.append(row[i] * row[j])

        result.append(new_row)

    return result