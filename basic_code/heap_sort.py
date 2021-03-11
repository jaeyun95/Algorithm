
def heapify(lst, index, size):
    parent = index
    child = 2 * index + 1
    if child < size and lst[child] > lst[parent]:
        parent = child
    if (child + 1) < size and lst[(child + 1)] > lst[parent]:
        parent = (child + 1)
    if parent != index:
        lst[parent], lst[index] = lst[index], lst[parent]
        heapify(lst, parent, size)

def heap_sort(lst):
    for i in range(len(lst)//2-1,-1,-1):
        heapify(lst, i, len(lst))
    for i in range(len(lst) - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, 0, i)
    return lst