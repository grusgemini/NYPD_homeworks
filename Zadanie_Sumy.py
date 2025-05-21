def set_sum(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    difference = set1.symmetric_difference(set2)
    intersection = set1.intersection(set2)
    output = difference.union(intersection)

    return list(output)

print(set_sum([1, 3, -2], [-2, -3, 0, 1, 34]))


def sorted_set_sum(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    difference = set1.symmetric_difference(set2)
    intersection = set1.intersection(set2)
    output = list(difference.union(intersection))
    output.sort()

    return output

print(sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]))
