#(6) day06 가장 많이 등장하는 알파벳 개수 구하기

def counter(word):
    counter_dic = {}
    for alphabet in word:
        if counter_dic.get(alphabet) == None:
            counter_dic[alphabet] = 1
        else:
            counter_dic[alphabet] += 1
    max = -1
    for key in counter_dic:
        if counter_dic[key] > max:
            max = counter_dic[key]
    return max
	

