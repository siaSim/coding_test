def solution(age):
    answer = ''
    
    planet = "abcdefghij"
    for i in str(age):
        answer += planet[int(i)]
    
    
    return answer