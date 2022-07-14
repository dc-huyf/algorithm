class Solution:
    def carPooling(self, trips: [[int]], capacity: int) -> bool:

        # [numPassengersi, fromi, toi]
        # 申请一个长数组,先操作上下车，最后检验每个站点人数是否超标
        stations = [0] * 1001
        for num, s, e in trips:
            stations[s-1] += num
            stations[e-1] -= num

        for i in range(len(stations)):
            if i == 0:
                if stations[i] > capacity:
                    return False
                continue
            stations[i] += stations[i-1]
            if stations[i] > capacity:
                return False

        return True

if __name__ == "__main__":
    trips = [[2,1,5],[3,5,7]]
    capacity = 3
    s = Solution()
    print(s.carPooling(trips, capacity))