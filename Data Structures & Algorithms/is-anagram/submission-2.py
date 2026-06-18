class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        library = {}
        for i in range(len(s)):
            if s[i] not in library:
                library[s[i]] = 1
            else:
                library[s[i]] += 1
        for j in t:
            if j not in library:
                return False
            else:
                library[j]-=1
                if library[j]==0:
                    library.pop(j)
        print(library)
        if library:
            return False
        return True
