from range_identifier import range_detection

def print_output(range_list,start_index,end_index):
    if len(range_list) == 0:
        return False
    count = range_detection(range_list,start_index,end_index)
    print(f"Range of {start_index} to {end_index} in {range_list} is {count}")