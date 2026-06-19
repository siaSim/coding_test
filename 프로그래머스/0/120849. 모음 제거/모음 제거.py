def solution(my_string):
    answer = ''
    vowels = 'aeiou'
    
    for str in my_string:
        if str not in vowels:
            answer += str
    
    return answer