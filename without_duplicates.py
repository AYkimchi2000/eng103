def without_duplicates(lst):
    seen = []
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.append(item)
    return result