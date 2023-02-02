from sort_data import sort_input_range

def range_detection(input_list,start_index,end_index):
    sorted_list = sort_input_range(input_list)
    return len(list(x for x in sorted_list if start_index <= x <= end_index))