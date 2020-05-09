def max_rotated_sortd_array(arr):
    low = 0
    high = len(arr) - 1
    while(arr[low] > arr[high]):
        mid = (low + high) // 2
        if( arr[mid] < arr[high]):
            high = mid
        else:
            low = mid
            high -= 1

    return arr[high]

if __name__ == "__main__":
    print(max_rotated_sortd_array([1,2,3,4,5,6,7,8,9]) == 9)
    print(max_rotated_sortd_array([9,1,2,3,4,5,6,7,8]) == 9)
    print(max_rotated_sortd_array([8,9,1,2,3,4,5,6,7]) == 9)
    print(max_rotated_sortd_array([7,8,9,1,2,3,4,5,6]) == 9)
    print(max_rotated_sortd_array([6,7,8,9,1,2,3,4,5]) == 9)
    print(max_rotated_sortd_array([5,6,7,8,9,1,2,3,4]) == 9)
    print(max_rotated_sortd_array([4,5,6,7,8,9,1,2,3]) == 9)
    print(max_rotated_sortd_array([3,4,5,6,7,8,9,1,2]) == 9)
    print(max_rotated_sortd_array([2,3,4,5,6,7,8,9,1]) == 9)

    print("Done! Success")
