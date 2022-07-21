# n의 배수 / n, 2n, 3n ... kn
# 각 자리수에서 0~9까지 모든 숫자 보면 멈추기
# n = 5 5*1 5*2 ...
# n과 곱할 k 변수
# while에서 for로 
#todo 숫자로 접근하니 코드가 너무 복잡해졌다.
#todo 0~9까지의 숫자 수집 -> 문자열 접근
#todo 리스트에 담아서 숫자 확인 or 세트
#! 리스트를 인덱싱으로 접근해서 0~9까지의 문자를 숫자, 그리고 인덱스로 바꿈. 그 후 대충 1로 체크하고 0이 없다면 다채운것. break로 반복문 빠져나오기. 프린트



t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    l = [0]*10 
    k = 0
    while True:
        if 0 not in l:
            break
        else:
            k += 1
            num = str(n*k)
            for i in range(len(num)):
                l[int(num[i])] = 1
    print(f'#{test_case} {num}')

    
    #     for j in range(len(n)):
    #         l[int(n[j])] += 1
    #     if not l.conut(0):
    #         print(f'#{i} {int(n)}')
    #         break
    #     n = str(v+int(n))


        # result = n*k
        # k += 1
        # while result:
        #     a = result % 10
        #     result //= 10
        #     l.append(a)
        #     # print(set(l))

        # for i in range(0,10):
        #     for j in set(l):
        #         if i == j:
        #             k -= 1
        # result = n*k
        # print(result)
        # break