class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lib = {}
        for word in strs:
            letters = str(sorted(word))
            print(letters)
            
            if letters in lib:
                lib[letters].append(word)
            else:
                lib[letters]=[word]
        return lib.values()