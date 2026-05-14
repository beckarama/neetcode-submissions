class TimeMap:
    def __init__(self):
        self.tm = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.tm.get(key):
            self.tm[key] = [(timestamp, value)]
        else:
            self.tm[key].append((timestamp, value))
        
    def __binary_search(self, arr: list, target: int):
        l, r = 0, len(arr) - 1
        res = ""
        
        while l <= r:
            mid = (l + r) // 2

            if arr[mid][0] <= target:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res

    def get(self, key: str, timestamp: int) -> str:
        if not self.tm.get(key):
            return ""
        return self.__binary_search(self.tm[key], timestamp)
