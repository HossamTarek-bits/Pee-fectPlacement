def calculate_score(urinals: list, index: int) -> float:
    """
    Calculates a score for a given urinal based on the greedy scoring algorithm.
    :param urinals: List of integers (1 for occupied, 0 for empty).
    :param index: Index of the urinal to calculate the score for.
    :return: Score for the given urinal.
    """
    score = 0
    n = len(urinals)

    # Count empty and filled urinals to the left
    left = index - 1
    if left >= 0:
        urinalType = urinals[left]
        while left >= 0 and urinals[left] == urinalType:
            score += 1 if urinalType == 0 else -1
            left -= 1

    # Count empty and filled urinals to the right
    right = index + 1
    if right < n:
        urinalType = urinals[right]
        while right < n and urinals[right] == urinalType:
            score += 1 if urinalType == 0 else -1
            right += 1

    # Check if next to a wall
    if index == 0 or index == n - 1:
        score += 0.5

    return score


def find_best_urinal(urinals: list) -> int:
    """
    Determines the best urinal to choose based on the greedy scoring algorithm.
    :param urinals: List of integers (1 for occupied, 0 for empty).
    :return: Index of the best urinal or -1 if no valid urinal exists.
    """
    best_score = float("-inf")
    best_index = -1

    for i, urinal in enumerate(urinals):
        if urinal == 0:  # Only consider empty urinals
            score = calculate_score(urinals, i)
            if score > best_score:
                best_score = score
                best_index = i

    return best_index
