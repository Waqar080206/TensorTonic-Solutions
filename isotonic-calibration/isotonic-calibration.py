def calibrate_isotonic(cal_labels, cal_probs, new_probs):
    pairs = sorted(zip(cal_probs, cal_labels))
    probs = [p for p, _ in pairs]
    labels = [y for _, y in pairs]

    # PAV algorithm
    blocks = []
    for y in labels:
        blocks.append([float(y), 1])

        while len(blocks) >= 2 and blocks[-2][0] > blocks[-1][0]:
            m1, c1 = blocks[-2]
            m2, c2 = blocks[-1]

            merged_mean = (m1 * c1 + m2 * c2) / (c1 + c2)
            blocks[-2] = [merged_mean, c1 + c2]
            blocks.pop()

    calibrated = []
    for mean, count in blocks:
        calibrated.extend([mean] * count)

    result = []

    for q in new_probs:
        if q <= probs[0]:
            result.append(calibrated[0])
            continue

        if q >= probs[-1]:
            result.append(calibrated[-1])
            continue

        lo, hi = 0, len(probs) - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if probs[mid] <= q:
                lo = mid
            else:
                hi = mid

        p1, p2 = probs[lo], probs[lo + 1]
        c1, c2 = calibrated[lo], calibrated[lo + 1]

        value = c1 + (q - p1) * (c2 - c1) / (p2 - p1)
        result.append(value)

    return result