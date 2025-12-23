def RemoveRows(A, K1, K2):
    M = len(A)
    if M == 0:
        return A
    
    if K2 > M:
        K2 = M
    
    if K1 > M or K1 > K2:
        return A
    start = K1 - 1
    end = K2
    
    result = A[:start] + A[end:]
    
    return result
