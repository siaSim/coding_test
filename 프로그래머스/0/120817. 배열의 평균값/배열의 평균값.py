def solution(numbers):
    total = 0
    
    for num in numbers: # 다 더하기
        total += num
        
    answer = total / len(numbers) # 총합을 갯수로 나누기
    return answer