#!/usr/bin/env python
# coding: utf-8

# In[36]:


numbers = input("숫자를 띄어쓰기를 구분자로 입력하시오. : ")
num_list = []
rank_list = []
num_count = 0

for i in range(len(numbers.split())):
    num_list.append(int(numbers.split()[i]))

for j in range(len(num_list)):
    ranking = 0
    for k in range(len(num_list)):
        if num_list[j] > num_list[k]:
            ranking += 1
    while ranking in rank_list:
        ranking += 1
    rank_list.append(ranking)

while rank_list != [i for i in range(len(num_list))]:
    for j in range(len(num_list)):
        if rank_list[j] != j:
            num_count += 1
            num_list[rank_list.index(j)], num_list[j] = num_list[j], num_list[rank_list.index(j)]
            rank_list[rank_list.index(j)], rank_list[j] = rank_list[j], rank_list[rank_list.index(j)]
            print("{}번째 변경입니다. : ".format(num_count),num_list)


# In[ ]:


"""
숫자를 띄어쓰기를 구분자로 입력하시오. : 5 3 4 2 1
1번째 변경입니다. :  [1, 3, 4, 2, 5]
2번째 변경입니다. :  [1, 2, 4, 3, 5]
3번째 변경입니다. :  [1, 2, 3, 4, 5]
"""

