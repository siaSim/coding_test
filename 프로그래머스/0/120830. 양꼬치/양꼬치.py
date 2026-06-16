def solution(n, k):
    service = n//10
    
    total = 12000 * n + 2000 * k - 2000 * service
    return total