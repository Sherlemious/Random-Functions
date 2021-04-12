# This function takes paramteres of a list, start index and end index. It returns the list with only the elements between the start and end indices reversed
# leaving all other list elements untouched.

def reverse_list(list_name, st_index, end_index):
    if st_index == 0:
        lst = list_name[end_index::-1] + list_name[end_index+1:]

    else:
        lst = list_name[:st_index] + list_name[end_index:st_index-1:-1] + list_name[end_index+1:]

    return lst
