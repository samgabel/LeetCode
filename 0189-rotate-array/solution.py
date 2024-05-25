class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # we set k to be the modulo of k % n because after 1 full rotation of `len(arr)` we end up with the same array
        # k is now set to the optimal amount of "rotations" that we need to satisfy our condition
        k %= n

        # we want to create a helper function that will reverse the array between 2 specified indices
        def reverse(p1: int, p2: int) -> None:
            while p1 < p2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 -= 1

        # first reverse whole array
        reverse(0, n - 1)
        # next reverse up to our `k` -> "how many rotations we need"
        reverse(0, k - 1)
        # finally reverse from `k` to the end -> "resetting" the "unrotated" elements
        reverse(k, n - 1)

