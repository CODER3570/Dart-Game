def score(x, y):
    distance = (x **2 + y **2) ** 0.5
    if distance > 10:
        return 0  # Dart lands outside the target (0 points)
    elif distance > 5:
        return 1  # Dart lands in the outer circle (1 point)
    elif distance > 1:
        return 5  # Dart lands in the middle circle (5 points)
    else:
        return 10
