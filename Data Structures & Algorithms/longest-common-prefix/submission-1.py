class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        n_letters = [len(s) for s in strs]
        min_letters = min(n_letters)
        n_strs = len(n_letters)

        for i in range(0, min_letters):
            candidate = None
            
            for j, s in enumerate(strs):
                if j == 0:
                   candidate = s[i]
                elif candidate != s[i]:
                    return prefix
            prefix += candidate
        
        return prefix
    