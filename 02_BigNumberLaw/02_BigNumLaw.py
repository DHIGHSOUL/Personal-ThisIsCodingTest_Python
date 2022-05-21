# N(num)개의 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M(sum)번 더하여 가장 큰 수를 만드는 법칙.
# 이 때, 배열의 특정한 인덱스에 해당하는 수가 연속하여 K(rep)번 이상으로 더해질 수 없다.
# 입력: 2<=N(num)<=1,000 | 1<=M(sum)<=10,000 | 1<=K(rep))<=10,000 \n 1<=N개의 자연수<=10,000 AND * K(rep)<=M(sum)
# 풀이 - 리스트에서 가장 큰 수와 두 번째로 큰 수를 찾아낸 후, 가장 큰 수를 K번, 두 번째로 큰 수를 한 번 더하는 연산을 M번 동안 반복한다.

num, sum, rep = map(int, input().split()) # N, M, K값을 입력받음
numbers = list(map(int, input().split())) # N개의 자연수를 리스트 형태로 입력받음

numbers.sort() # 리스트를 크기 순으로 정렬하고
largest = numbers[num-1] # 가장 큰 수(n개의 요소를 가지는 리스트의 n-1번째 인덱스->가장 뒤에 있는 요소)를 largest 변수에 저장
second = numbers[num-2] # 두 번째로 큰 수를 second 변수에 저장

result = 0

while True:
    for i in range(rep): # K번만큼 연속하여 가장 큰 수를 더하고
        if sum==0:
            break
        result+=largest
        sum-=1
    if sum==0: # 연산 중 M이 0이 되면 탈출하여 연산을 종료함
        break
    result+=second # K번이 지나면 두 번째로 큰 수를 한 번 더함
    sum-=1

# 혹은, 반복되는 수열을 계산하여 '가장 큰 수가 더해지는 횟수'를 구한 후 계산을 해도 된다.
# 가장 큰 수가 더해지는 횟수 -> M/(K+1) * K + M%(K+1)
# count = (sum/(rep+1) * rep + sum%(rep+1)
# result += largest * count
# result += second * sum-count

print(int(result))