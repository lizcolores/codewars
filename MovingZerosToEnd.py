def move_zeros(array):
    zeros = []
    new = []
    for i,v in enumerate(array):
        if v==0:
            zeros.append(v)
        else:
            new.append(v)
    array = new + zeros
    return array
