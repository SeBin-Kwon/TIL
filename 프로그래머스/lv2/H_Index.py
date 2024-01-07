a = [3, 0, 6, 1, 5]
  
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in citations:
        if i>answer:
            answer+=1
    return answer

def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

print(solution(a))