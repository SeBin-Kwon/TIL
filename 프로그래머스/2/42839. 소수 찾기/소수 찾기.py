from itertools import permutations
import math

def solution(numbers):
    answer = 0
    num_array = list(numbers)
    check = []
    for i in range(1, len(num_array)+1):
        case = set(permutations(num_array,i))
        for j in case:
            num = int("".join(j))
            if num > 1 and num not in check:
                if is_prime(num):
                    answer += 1
                    check.append(num)
    return answer

def is_prime(num):
    if num != 2 and num % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
    