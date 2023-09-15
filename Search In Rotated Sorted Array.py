Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

1. Place the 2 pointers i.e. low and high:
2. Calculate mid = (low+high) // 2 ( ‘//’ refers to integer division)
3. if arr[mid] == target: return the index mid.

4. Identify the sorted half, check where the target is located, and then eliminate one half accordingly:

If arr[low] <= arr[mid]: This condition ensures that the left part is sorted.
If arr[low] <= target && target <= arr[mid]: It signifies that the target is in this sorted half. So, we will eliminate the right half (high = mid-1).
Otherwise, the target does not exist in the sorted half. So, we will eliminate this left half by doing  low = mid+1.

Otherwise, if the right half is sorted:
If arr[mid] <= target && target <= arr[high]: It signifies that the target is in this sorted right half. So, we will eliminate the left half (low = mid+1).
Otherwise, the target does not exist in this sorted half. So, we will eliminate this right half by doing high = mid-1.

5. Once, the ‘mid’ points to the target, the index will be returned and the loop will continue until low crosses high. If no index is found, we will return -1.

def search(arr, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2

        # if mid points the target
        if arr[mid] == k:
            return mid

        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if arr[mid] <= k and k <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)
      

