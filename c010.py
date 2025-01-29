import heapq
import sys

class MedianFinder:
    def __init__(self):
        self.low = []  # 最大堆 (用負數模擬)
        self.high = []  # 最小堆

    def add_num(self, num: int):
        # 1. 新數字先加入最大堆 (low)
        heapq.heappush(self.low, -num)
        # 2. 將最大堆堆頂移入最小堆 (high)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        # 3. 平衡兩個堆的大小
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self) -> float:
        # 取中位數
        if len(self.low) > len(self.high):  # 奇數個數，最大堆堆頂即中位數
            return -self.low[0]
        else:  # 偶數個數，中位數為兩堆堆頂平均值
            return (-self.low[0] + self.high[0]) / 2

# 測試
median_finder = MedianFinder()
nums = [int(s) for s in sys.stdin]
for num in nums:
    median_finder.add_num(num)
    print(f"{int(median_finder.find_median())}")
