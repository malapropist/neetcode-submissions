class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        print(d)
        l = []
        for word in strs:
            a = str(sorted(word))
            if a not in d:
                d[a]=[word]
            else:
                d[a].append(word)
                
        return list(d.values())