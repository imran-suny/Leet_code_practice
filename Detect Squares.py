["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output::: [null, null, null, null, 1, 0, null, 2]

class DetectSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)  # Dictionary to count occurrences of points  [3, 10] = 1 time
        self.pts = []                     # List to store added points

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)            # add/ append 

    def count(self, point: List[int]) -> int:   # count 
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py: # if not square continue, go to next pts,,, the diagonally opposite corners of a square 
                continue                                           # This checks if the current point (x, y) is on the same horizontal or vertical line
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]  # it multiplies the counts of the other two points required to form a square 
        return res
