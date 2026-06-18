class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        library = {}
        for i in strs:
            j = str(sorted(i))
            if j not in library:
                answer.append([i])
                library[str(j)] = len(answer)-1
            else:
                answer[library[str(j)]].append(i)
        return answer