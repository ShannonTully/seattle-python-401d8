from itertools import islice


def adam_selection(array):
    """
    Sort an array using a selection sort.
    """
    array = list(array)
    for i in range(len(array)):
        swap = min(
            enumerate(islice(array, i, len(array))), key=lambda t: t[1])
        j = swap[0] + i
        array[i], array[j] = array[j], array[i]
    return array


def tyler_selection(input_list):
    """
    Sort a given list using selection sort algorithm
    and return a that list with the values ascending.
    """
    input_list_length = len(input_list)

    for i in range(input_list_length):
        current_smallest_index = i
        try:
            for j in range(i, input_list_length):
                if input_list[j] < input_list[current_smallest_index]:
                    current_smallest_index = j
            if current_smallest_index != i:
                input_list[current_smallest_index], input_list[i] = \
                    input_list[i], input_list[current_smallest_index]
        except TypeError:
            print('All data must be same type i.e. int, str, etc...')
            return None
