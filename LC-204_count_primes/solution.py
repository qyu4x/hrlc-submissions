from math import sqrt
class Solution:

    def __init__(self):
        pass
    def countPrimes(n: int) -> int:
        if 0 <= n <= 5 * 10**6:
            total = 0
            for i in range(n):
                count = 0
                for j in range(1, int(sqrt(i) + 1)):
                    if i % j == 0:
                        count += 1
                        if i//j != j:
                            count += 1
                if count == 2:
                    total += 1

            return total

if __name__ == '__main__':
    so = Solution
    re = so.countPrimes(13)
    print(re)