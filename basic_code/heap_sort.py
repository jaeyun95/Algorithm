
def heapify(lst, index):
    parent = index
    child = 2 * index + 1
    if child < len(lst) and lst[child] > lst[parent]:
        parent = child
    if (child + 1) < len(lst) and lst[(child + 1)] > lst[parent]:
        parent = (child + 1)
    if parent != index:
        lst[parent], lst[index] = lst[index], lst[parent]
        heapify(lst, parent)

def heap_sort(lst):
    sorted_list = []
    for i in range(len(lst)//2-1,-1,-1):
        heapify(lst, i)

    for i in range(len(lst) - 1, 0, -1):
        sorted_list.insert(0,lst.pop(0))
        heapify(lst, 0)
    sorted_list.insert(0, lst.pop(0))
    return sorted_list