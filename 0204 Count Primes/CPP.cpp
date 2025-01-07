class Solution {
public:
    
    int countPrimes(int n) {
        if (n < 3) return 0;
        return sieve_of_eratosthenes(n).size();
    }

    vector<int> sieve_of_eratosthenes(int n) {
        vector<int> primes(n - 2, 1);
        for (int i = 2; i < ceil(sqrt(n)); i++) {
            if (primes[i - 2] == 1) {
                for (int j = i * i; j < n; j += i) {
                    primes[j - 2] = 0;
                }
            }
        }
        vector<int> res;
        for (int i = 0; i < n - 2; i++) {
            if (primes[i] == 1) {
                res.push_back(i + 2);
            }
            
        }
        return res;
    } 
};