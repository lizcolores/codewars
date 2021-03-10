def find_uniq(arr):
    counts = {}
    for i in arr:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    for i in arr:
        if counts[i] == 1:
            return i
