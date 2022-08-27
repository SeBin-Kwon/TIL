def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    a_n = (10000 // len(a))
    b_n = (10000 // len(b))
    c_n = (10000 // len(c))
    
    a_l = a * a_n
    b_l = b * b_n
    c_l = c * c_n
    
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    
    for i in range(len(answers)):
        if answers[i] == a_l[i]:
            a_cnt += 1
        if answers[i] == b_l[i]:
            b_cnt += 1
        if answers[i] == c_l[i]:
            c_cnt += 1
            
    if max(a_cnt,b_cnt,c_cnt) == a_cnt:
        answer.append(1)
    if max(a_cnt,b_cnt,c_cnt) == b_cnt:
        answer.append(2)
    if max(a_cnt,b_cnt,c_cnt) == c_cnt:
        answer.append(3)
        
    return answer