'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    if cache == None:
        cache = [0] * (n + 1)

    if n <= 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif cache[n] == 0:
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

'''
    DP = [0 for i in range(0, n+1)]

    DP[0] = DP[1] = DP[2] = 1
    DP[3] = 2

    for i in range(4, n+1):
        DP[i] = DP[i - 1] + DP[i - 3] + DP[i - 4]

    return DP[n]

'''


