
def quick_sort(lst):
    if len(lst) <= 1: return lst
    pivot, lst2 = lst[0], lst[1:]
    left, right = [], []
    for item in lst2:
        right.append(item) if pivot < item else left.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)
