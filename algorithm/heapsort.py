__author__ = 'peter'


data = [0, 6, 20, 11, 1, 8, 7, 2, 4, 31, 61]


def build_max_heap(in_data, start, end):
    """Build a max heap"""
    if start >= end:
        return

    i = end / 2
    while i >= start:
        j = i
        if in_data[i] < in_data[2 * i]:
            j = 2 * i
        if (2 * i + 1 <= end) and in_data[j] < in_data[2 * i + 1]:
            j = 2 * i + 1
        if i != j:
            t = in_data[i]
            in_data[i] = in_data[j]
            in_data[j] = t
        i -= 1
    t = in_data[end]
    in_data[end] = in_data[start]
    in_data[start] = t
    print 'build_max_heap', in_data[start:end+1]


def heapsort(in_data):
    """Heap sort"""
    i = 0
    j = len(in_data) - 1
    while i < j:
        build_max_heap(in_data, 1, j - i)
        i += 1
    pass

heapsort(data)
print 'final:', data[1:]