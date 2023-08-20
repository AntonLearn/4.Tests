def max_in_list(lst):
    max_number = lst[0]
    for num_l in lst:
        if num_l > max_number:
            max_number = num_l
    return max_number


def len_of_list(lst):
    return len(lst)


def find_ind_elem_in_list(lst, el):
    return lst.index(el)