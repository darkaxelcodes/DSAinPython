def find_minimum(arr):
    minimum = arr[0]
    for number in arr[1:]:
        if number < minimum:
            minimum = number
    return minimum