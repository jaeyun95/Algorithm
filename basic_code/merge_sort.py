
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])
    return merge(left_list,right_list)

def merge(left_list, right_list):
    sorted_list = []
    li = 0
    ri = 0
    while (li < len(left_list) and ri < len(right_list)):
        if left_list[li] < right_list[ri]:
            sorted_list.append(left_list[li])
            li += 1
        else:
            sorted_list.append(right_list[ri])
            ri += 1

    while(li < len(left_list)):
        sorted_list.append(left_list[li])
        li += 1
    while (ri < len(right_list)):
        sorted_list.append(right_list[ri])
        ri += 1
    return sorted_list
