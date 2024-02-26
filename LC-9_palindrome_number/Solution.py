class Solution:
    def isPalindrome(self, x: int) -> bool:
        tx = x
        desc_order = 0
        while x > 0:
            ld = x % 10
            x = x // 10
            desc_order = (desc_order * 10) + ld
        return tx == desc_order


if __name__ == '__main__':
    so = Solution()
    re = so.isPalindrome(1221)
    print(re)