def solution(money):
    answer = []
    
    cup = money // 5500
    m = money % 5500
    
    answer.append(cup)
    answer.append(m)
    
    return answer