__author__ = 'angelo'


class Sieve:

    def __init__(self, max_num):
        self.max_num = max_num


    def findPrimes(self):
        number_list = [True] * self.max_num
        number_list[0] = False
        number_list[1] = False
        for x in range(2, self.max_num):
            if number_list[x] and not self.isPrime(x):
                for y in range(x, self.max_num, x):
                    number_list[y] = False

        return [num for num in range(0, self.max_num) if number_list[num]]

    def isPrime(self, x):
        for i in range(2,int(x ** 0.5) + 1):
            if x % i==0:
                return False

        return True