def merge_sort(strings):
    if len(strings) <= 1:
        return strings
    mid = len(strings) // 2
    left = merge_sort(strings[:mid])
    right = merge_sort(strings[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if len(left[i]) > len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


list1 = ['cat', 'apple', 'chair', 'zebra', 'car', 'dog', 'bed', 'banana', 'table', 'elephant']
list2 = ['moon', 'sun', 'stars', 'galaxy', 'planets', 'comet', 'earth', 'orbit', 'telescope', 'nebula']
list3 = ['programming', 'algorithm', 'computer', 'language', 'development', 'technology', 'python', 'database', 'code', 'debugging']

sorted_list1 = merge_sort(list1)
sorted_list2 = merge_sort(list2)
sorted_list3 = merge_sort(list3)

print(sorted_list1)
print(sorted_list2)
print(sorted_list3)


# reference - https://stackoverflow.com/questions/75286376/using-the-merge-sort-algorithm-to-order-a-list-of-strings-by-string-length-from