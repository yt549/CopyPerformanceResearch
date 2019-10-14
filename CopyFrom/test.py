num1 = '555'
num2 =  '321'

len1 = len(num1)
len2 = len(num2)
len3 = len1 + len2

# num2 的每一个digits去乘
num3 = [0 for _ in range(len3)]
for i in range(len1 - 1, -1, -1):
    carry = 0
    
    for j in range(len2 - 1, -1, -1):
        product = carry + num3[i + j + 1] + int(num1[i]) * int(num2[j])
        num3[i + j + 1] = product % 10
        carry = product // 10
        
    num3[i] = carry

result = ""
i = 0

# num3.strip()
while i < len3 - 1 and num3[i] == 0:
    i += 1
# convert to string
while i < len3:
    result += str(num3[i])
    i += 1



l1 = len(num1)
l2 = len(num2)
ans = [0]*(len1 + len2 + 1)
# 先不管进位
for i in range(l1):
    for j in range(l2):
        ans[i+j] += int(num1[l1-i-1]) * int(num2[l2-j-1])

for i in range(l1+l2):
    ans[i+1] += ans[i]//10
    ans[i] %= 10

result2 = ""
i = 0

# ans.rstrip()
while i < len(ans) - 1 and ans[i] == 0:
    i += 1
# convert to string
while i < len(ans) - 1:
    result2 += str(ans[i])
    i += 1

result2 = result2[]


print(result)
print('next')
print(ans)
print(result2)