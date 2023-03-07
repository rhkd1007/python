nums=[1,1,1,2,2,3,2,3,2,3,3,3,1]


def max_count(nums):
    counts = {} 
    for i in nums:
        if i in counts: #dict에 이미 있는 값
            counts[i] += 1
        else: #dict에 없는 값
            counts[i] =1
    return counts


counts = max_count(nums)
print(counts) #{1: 4, 2: 4, 3: 5}

#counts dict에서 최대값 출력
max_num = max(counts.values())
print("최대값", max_num)

# key : value
# 1 : 4 번
# 2 : 4 번
# 3 : 5 번
# maxKey : [3]

f = [] # list 형
for key, count in counts.items():
    print(key, ":", count , "번")
    if count == max_num:
        f.append(key)

print('mayKey : ', f)
#############


def sum(num):
    hap = 0
    for i in range(1, num+1):
        hap += i        
    return hap


print(sum(10)) # 1부터 10까지 합 출력
