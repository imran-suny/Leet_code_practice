["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output:
[null, null, "bar", "bar", null, "bar2", "bar2"]

class TimeMap:
    def __init__(self):
        self.keyStore = {}  ## Initialize a defaultdict with lists to store key-value pairs.

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values =  self.keyStore.get(key, []) # key thakle value  ["foo", 1], ["foo", 3] ,  na hole empty list 
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:  #  any valid timestamp must be to the left of m. this timestamp is a candidate for the most recent timestamp
                res = values[m][0]  # return value 
                l = m + 1
            else:
                r = m - 1
        return res
