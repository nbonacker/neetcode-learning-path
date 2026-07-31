class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_letters = min(len(s) for s in strs)

        for i in range(0, min_letters):
            candidate = strs[0][i]
            
            for s in strs[1:]:
                if candidate != s[i]:
                    return prefix
            prefix += candidate
        
        return prefix

        # Alternative avoid immutable strings
        # prefix = []
        # ...
        # prefix.append(candidate)
        # ...
        # return "".join(prefix)

    