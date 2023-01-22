survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

answer = ''
dic = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0 }
for i in range(len(survey)):
    score =  abs(choices[i] - 4)
    if choices[i] < 4:
        dic[survey[i][0]] += score
    elif choices[i] > 4:
        dic[survey[i][1]] += score
    
if dic['R'] >= dic['T']:
    answer += 'R'
else:
    answer += 'T'
if dic['C'] >= dic['F']:
    answer += 'C'
else:
    answer += 'F'
if dic['J'] >= dic['M']:
    answer += 'J'
else:
    answer += 'M'
if dic['A'] >= dic['N']:
    answer += 'A'
else:
    answer += 'N'

print(answer)