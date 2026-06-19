class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [  1,-1,0,0,0,0]
        # [0,0, 6,6,3,1]

        # [    1, 1, 2, 8,24]
        # [48,48,24, 6, 1]
        lr,rl = [1],[1]
        for i in nums:
            lr.append(lr[-1]*i)
        for j in nums[::-1]:
            rl.append(rl[-1]*j)
        lr = lr[0:-1]
        rl = rl[::-1][1:]
        for spot,x in enumerate(lr):
            lr[spot]=x*rl[spot]
        return lr