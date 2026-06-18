class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for i in strs:
            count = [0]*26
            for letter in i:
                count[ord(letter) - ord("a")] += 1
            if tuple(count) in ans:
                ans[tuple(count)].append(i)
            else:
                ans[tuple(count)] = [i]
        return ans.values()