# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences_naive(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]


def PolyHash(S,p,x):
    ans = 0
    for c in reversed(S):
        ans = (ans*x+ord(c)) % p
    return ans


def pre_compute_hashes(T, P_len, p, x):
    T_len = len(T)
    Hashes = [0]*(T_len-P_len+1)
    start = T[T_len-P_len:]
    Hashes[-1] = PolyHash(start, p, x)
    y = 1
    for i in range(1, P_len+1):
        y = (y*x) % p
    for i in range(T_len-P_len-1, -1, -1):
        Hashes[i] = (x*Hashes[i+1] + ord(T[i]) - y*ord(T[i+P_len])) % p
    return Hashes


def RabinKarp(P, T):
    p, x = 1000000007, 263
    P_len = len(P)
    T_len = len(T)
    result = []
    pHash = PolyHash(P, p, x)
    H = pre_compute_hashes(T, P_len, p, x)
    for i in range(T_len-P_len+1):
        if pHash != H[i]:
            continue
        if T[i:i+P_len] == P:
            result.append(i)
    return result



if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))

