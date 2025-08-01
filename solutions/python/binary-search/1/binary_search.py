def find(search_list, value) -> int:

    start = 0
    end = len(search_list) - 1

    while start <= end:
        print(f"Current range: {search_list[start:end + 1]}")
        middle = (start + end) // 2
        print(f"Middle position is {middle} with value: {search_list[middle]}")

        if search_list[middle] == value:
            print("Value was found!")
            return middle

        elif search_list[middle] > value:
            print('Value is in the left side of the list')
            end = middle - 1


        else:
            print('Value is in the right side of the list')
            start = middle + 1
    raise ValueError('value not in array')