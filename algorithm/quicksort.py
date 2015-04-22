__author__ = 'peter'


data = [3, 7, 8, 5, 2, 1, 9, 5, 4, 8, 18, 41, 1, 13]


def partition(in_data, start, end):
    store_index = start
    pivot = in_data[end]
    i = start
    while i < end:
        if in_data[i] < pivot:
            t = in_data[i]
            in_data[i] = in_data[store_index]
            in_data[store_index] = t
            store_index += 1
        i += 1
        print in_data
    t = in_data[store_index]
    in_data[store_index] = in_data[end]
    in_data[end] = t
    print "index is: ", store_index
    print 'partition: ', in_data
    return store_index


def partition2(in_data, start, end):
    store_index = end
    pivot = in_data[start]
    i = end
    while i > start:
        if in_data[i] < pivot:
            t = in_data[i]
            in_data[i] = in_data[store_index]
            in_data[store_index] = t
            store_index -= 1
        i -= 1
    t = in_data[store_index]
    in_data[store_index] = in_data[start]
    in_data[start] = t
    return store_index


def quicksort(in_data, i, j):
    if i < j:
        p = partition(in_data, i, j)
        quicksort(in_data, i, p-1)
        quicksort(in_data, p+1, j)
        print in_data

quicksort(data, 0, len(data)-1)

print "data:" ,data