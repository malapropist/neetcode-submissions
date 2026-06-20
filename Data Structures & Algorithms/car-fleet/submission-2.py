class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position,speed)))[::-1]
        fleets = 0
        res = []
        for p,s in cars:
            time=(target-p)/s
            print(time, p,s)
            if not res or res[-1]<time:
                res.append(time)
        return len(res)