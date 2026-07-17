class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            count_letters = {l:0 for l in 'abcdefghijklmnopqrstuvwxyz'}
            for letter in word:
                count_letters[letter]+=1
            if tuple(count_letters.values()) not in ans:
                ans[tuple(count_letters.values())]=[word]
            else:
                ans[tuple(count_letters.values())].append(word)
        return list(ans.values())