class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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