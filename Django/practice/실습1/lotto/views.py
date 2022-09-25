from django.shortcuts import render
import random
# Create your views here.

def lotto(requset):
    number_result = random.sample(range(1,46),7)    
    random_nums = []
    for i in range(5):
        cnt = 0
        random_num = random.sample(range(1,46),6)
        for j in range(6):
            if random_num[j] in number_result:
                cnt += 1
        if cnt == 3:
            win = '5등'
        elif cnt < 3:
            win = '꽝'
        elif cnt == 4:
            win = '4등'
        elif cnt == 5:
            win = '3등'
        elif (cnt == 5) and (random_nums in number_result[-1]):
            win = '2등'
        elif cnt == 6:
            win = '1등'
        dic = { 'lotto' : random_num, 'win' : win }
        random_nums.append(dic)
    
    context = {
        'numbers' : random_nums,
    }
    return render(requset, 'lotto.html', context)
