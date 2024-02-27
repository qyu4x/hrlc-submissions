class Solution:

    def __init__(self):
        pass

    def check_armstrong(self, number: int) -> bool:
        temp_number = number
        cd = 0
        if 1 < number < 999:
            while (number > 0):
                ld = number % 10
                cd += ld**3
                number = number // 10
        print(cd)
        return temp_number == cd

if __name__ == '__main__':
    so = Solution()
    print(so.check_armstrong(1))