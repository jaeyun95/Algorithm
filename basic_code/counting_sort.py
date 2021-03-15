
def counting_sort(lst, K):
    count_lst = [0] * K
    sorted_lst = [0] * len(lst)

    for item in lst:
        count_lst[item] += 1

    for count in range(1,K):
        count_lst[count] += count_lst[count-1]

    for index in range(len(lst)):
        sorted_lst[count_lst[lst[index]]] = lst[index]
        count_lst[lst[index]] -= 1
    return sorted_lst