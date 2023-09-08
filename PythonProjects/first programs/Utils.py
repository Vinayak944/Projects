def find_max(numberss):
    max = numberss[0]
    for number in numberss:
        if number > max:
            max = number
    return max
    
