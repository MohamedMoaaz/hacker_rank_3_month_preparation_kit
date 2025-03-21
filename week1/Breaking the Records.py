def breakingRecords(scores):
    _min = scores[0]
    _max = scores[0]
    cmin = 0
    cmax = 0
    for i in scores:
        if i < _min:
            _min = i
            cmin += 1
        elif i > _max:
            _max = i
            cmax +=1
    new_arr = [cmax, cmin]
    return new_arr
