class Solution {
    
    public static int countPrimes(int n) {
        if (n < 3) return 0;
        return sieve_of_eratosthenes(n).length;
    }

    public static int[] sieve_of_eratosthenes(int n) {
        int[] primes = IntStream.generate(() -> 1).limit(n - 2).toArray();
        for (int i = 2; i < Math.ceil(Math.sqrt(n)); i++) {
            if (primes[i - 2] == 1) {
                for (int j = i * i; j < n; j += i) {
                    primes[j - 2] = 0;
                }
            }
        }
        return IntStream.range(0, n - 2)
                .filter(i -> primes[i] == 1)
                .map(i -> i + 2)
                .toArray();
    }
    
}