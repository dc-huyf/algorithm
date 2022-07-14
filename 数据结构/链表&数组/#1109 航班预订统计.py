class Solution:
    def corpFlightBookings(self, bookings: [[int]], n: int) -> [int]:
        diff = [0] * n
        for s, e, num in bookings:
            diff[s-1] += num
            if e < len(diff):
                diff[e] -= num

        # 恢复
        for i in range(1, len(diff)):
            diff[i] += diff[i-1]
        return diff


if __name__ == "__main__":
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    s = Solution()
    print(s.corpFlightBookings(bookings, n))