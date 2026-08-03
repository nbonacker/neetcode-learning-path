class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Improvement create a key to look up the answer directly instead of comparing
        def _isAnagram(s: str, t: str) -> bool:
            letters_s = dict()
            letters_t = dict()
            
            for letter in s:
                if letter in letters_s.keys():
                    letters_s[letter] += 1
                else:
                    letters_s[letter] = 1

            for letter in t:
                if letter in letters_t.keys():
                    letters_t[letter] += 1
                else:
                    letters_t[letter] = 1

            for letter in set(list(letters_s.keys()) + list(letters_t.keys())):
                if letters_s.get(letter) != letters_t.get(letter):
                    return False
            return True

        strs_grouped = [[strs[0]]]

        for s in strs[1:]:
            found_group = False
            for group in strs_grouped:
                if _isAnagram(s, group[0]):
                    found_group = True
                    group.append(s)
            
            if not found_group:
                strs_grouped.append([s])

        return strs_grouped


