from range_identifier import range_detection

if __name__ == '__main__':
    assert(range_detection([3,3,4,5,10,11,10,12], 3, 5) == 4)
    assert(range_detection([3,3,4,5,10,11,10,12], 10, 12) == 4)
    print("Range & Readings are perfect")