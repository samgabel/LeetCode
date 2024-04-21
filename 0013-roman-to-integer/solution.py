class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        number = 0
        for i in range(len(s) - 1):
            # if the numeral is smaller than the next numeral in the string,
            # the current numeral serves to subtract from the next numeral's value
            if roman[s[i]] < roman[s[(i + 1)]]:
                number -= roman[s[i]]
            else:
                number += roman[s[i]]
        # since we only loop until the second to last, we add the last back here
        return number + roman[s[-1]]

