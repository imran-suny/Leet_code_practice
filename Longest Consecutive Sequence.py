#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

my_set = set([1, 2, 3, 4, 4, 5, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}

1. set() for all > starting point /(n-1) in set()> again  n+count in set() hole max ber   korbo...
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)     # set() creates an unordered collection of unique elements// O(n) worst case 
        longest = 0            # Sets are defined by enclosing a comma-separated list of elements within curly braces {}
                               # unique digit dorkar holei set() use korbo//// 
        for n in numSet:
                               # Inside the loop, the code checks if (n - 1) is not in numSet.
                               #If true, it means that n is the start of a new consecutive sequence.
            if (n - 1) not in numSet: # strating point of a sequence?// 1.. 2-1=1 in subset, so 1 starting point 
                length = 1
                while (n + length) in numSet: # jotokhon sequence continue hobe 
                    length += 1
                longest = max(length, longest) # longest is updated to the maximum of the current length
        return longest         # the existing longest value, ensuring it holds the length of the longest sequence found

let, n= 100, n-1= 99 ki set a ache? na? thle 100 starting point> sequence lenght count? while (n+lenght) in numset: count++