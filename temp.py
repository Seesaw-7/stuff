# import sys

# num = int(sys.stdin.readline())

# nums = sys.stdin.readline().split()
# nums = [int(n) for n in nums]

# # print(nums)

# mul = 1
# for i in range(num):
#     mul = mul * nums[i]

# temp = str(mul)

# cnt = 0
# for c in reversed(temp):
#     if c == '0':
#         cnt += 1

# ans = cnt
# # print(cnt)

# # for i in range(num):
# #     temp = 1
# #     for j in range(num):
# #         if j == i:
# #             temp = temp * (nums[j] + 1)
# #         else:
# #             temp = temp * nums[j]
# #     # temp = mul / nums[i] * (nums[i] + 1)
# #     temp = str(temp)
# #     counter = 0
# #     for c in reversed(temp):
# #         if c == '0':
# #             counter += 1
# #         else:
# #             break
# #     ans = max(counter, ans)

# # print(ans)
# # mul = 1
# # for i in range(num):
# #     mul = mul * nums[i]

# # all_mul = mul

# # cnt = 0
# # while mul % 10 == 0:
# #     mul = mul // 10
# #     cnt += 1
# # ans = cnt

# # for i in range(num):
# #     temp = all_mul
# #     # for j in range(num):
# #     #     if j == i:
# #     #         mul = mul * (nums[j] + 1)
# #     #     else:
# #     #         mul = mul * nums[j]
# #     cnt = 0
# #     temp = temp * (nums[i] + 1)
# #     temp = temp / nums[i]
# #     while temp % 10 == 0:
# #         temp = temp // 10
# #         cnt += 1
# #     ans = max(ans, cnt)

# # print(ans)

import sys

num = int(sys.stdin.readline())

nums = sys.stdin.readline().split()
nums = [int(n) for n in nums]

mul = 1
for i in range(num):
    mul = mul * nums[i]

all_mul = mul

cnt = 0
while mul % 10 == 0:
    mul = mul // 10
    cnt += 1
ans = cnt

for i in range(num):
    temp = int(all_mul / nums[i])
    temp = temp * (nums[i]+1)
    # temp = 1
    # for j in range(num):
    #     if j == i:
    #         temp = temp * (nums[j] + 1)
    #     else:
    #         temp = temp * nums[j]
    cnt = 0
    while temp % 10 == 0:
        temp = temp // 10
        cnt += 1
    ans = max(ans, cnt)

print(ans)