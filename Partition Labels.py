Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8],   partition is "ababcbaca", "defegde", "hijhklij".
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}  # dictionary to store the last occurrence index of each character in the string
        # First pass: record the last occurrence of each character
        for i, c in enumerate(s):
            lastIndex[c] = i   # save the last index of character `c` in `lastIndex`

        res = []  # list to store the sizes of the partitions
        size, end = 0, 0  # initialize size and the current partition end

        # Second pass: determine partitions
        for i, c in enumerate(s):
            size += 1  # increase the size of the current partition
            end = max(end, lastIndex[c])  # extend the current partition's end to the furthest occurrence of the current character

            # When we reach the end of the current partition
            if i == end:
                res.append(size)  # add the size of the partition to the result
                size = 0  # reset the size for the next partition

        return res
