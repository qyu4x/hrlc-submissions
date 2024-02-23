from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0
        for num in nums:
            current_count = 0
            while(num > 0):
                current_count += 1
                # digit = num % 10
                num = num // 10
            if current_count % 2 == 0:
                even_count += 1
        return even_count


if __name__ == '__main__':
    nums = [22, 234]
    solution = Solution()
    re = solution.findNumbers(nums)
    print(re)
