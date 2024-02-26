import sys


class Solution:
    def reverse(self, x: int) -> int:
        max32bit = 2**31 - 1 if sys.maxsize > 2 ** 31 else 2**31 - 1
        if x <= max32bit:
            multiplier = 1
            if x < 1:
                multiplier = - 1
                x = x * multiplier

            rv = 0
            while x > 0:
                ld = x % 10
                x = x // 10
                rv = (rv * 10) + ld
            rv = rv * multiplier
            if rv > max32bit or rv < -max32bit:
                return 0
            else:
                return rv



if __name__ == '__main__':
    so = Solution()
    re = so.reverse(-321)
    print(re)