class Solution(object):
    
    def countPrimes(self, n):
        return len(self.sieve_of_eratosthenes(n))

    def sieve_of_eratosthenes(self, n):
        primes = [True] * (n - 2)
        for i in range(2, int(ceil(sqrt(n)))):
            if primes[i - 2] == True:
                for j in range(pow(i, 2), n, i):
                    primes[j - 2] = False
        return [i + 2 for i in range(len(primes)) if primes[i] == True]