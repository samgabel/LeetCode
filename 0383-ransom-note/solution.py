from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # this creates a dictionary of "magazine letter" -> "# of occurances" pair
        # this allows us to have a space complexity of O(1)
        mag_num = dict(Counter(magazine))
        for letter in ransomNote:
            if letter not in mag_num:
                return False
            else:
                mag_num[letter] -= 1
                if mag_num[letter] == 0:
                    del mag_num[letter]
        return True

