#!/usr/bin/env python
# coding: utf-8

# In[214]:


# 변경 순서
def det_even_odd(numbers):
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
    return num_count


# In[215]:


# det 계산 곱
def det_prod(mat, index):
    i = 0
    result = 1
    for j in index:
        result *= mat[i][j]
        i += 1
    return result


# In[216]:


# 계산 인덱스
def index(a):
    result = []
    index_local = []
    
    def per(b):
        if len(b) == 0:
            result.append(index_local[:])
        
        for i in b:
            b_copy = b.copy()
            b_copy.remove(i)
            
            index_local.append(i)
            per(b_copy)
            index_local.pop()
    per(a)
    return result

det_index = index([0,1,2,3])


# In[217]:


# det 계산 (big formula determinant)
def det_cal(path):
    file = list(open(path, "r"))
    matrix = []
    for i in file:
        matrix.append(list(map(int,i[:-1].split())))

    result = 0
    for i in det_index:
        if det_even_odd(" ".join(map(str,i))) % 2 == 0:
            result += det_prod(matrix,i)
        else:
            result -= det_prod(matrix,i)
    return result


# In[220]:


det_cal("/Users/heogeonhyeock/Desktop/파파선/4X4_matrix.txt")


# In[ ]:




