class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        for customer in accounts:
            total = 0
            for account in customer:
                total += account
            if total > richest:
                richest = total
        return richest
