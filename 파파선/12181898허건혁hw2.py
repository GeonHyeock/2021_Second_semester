#!/usr/bin/env python
# coding: utf-8

# In[219]:


#1
Input_str = input("문자열을 입력해 주세요. : ")
Input_str2 = "|" + "|".join(list(Input_str)) + "|"

print("+-"*len(Input_str)+"+")
print(Input_str2)
print("+-"*len(Input_str)+"+")


# In[ ]:


#2

# Input 입력
string = input("문자열을 입력해 주세요. : ")

row = int(input("0을 시작으로하는 행렬의 행의 크기를 입력하세요. : "))
while row < len(string):
    print("행렬의 행의 크기가 문자열의 길이보다 크게 설정하세요.")
    row = int(input("행렬의 행의 크기를 입력하세요. : "))
    
col = int(input("0을 시작으로하는 행렬의 열의 크기를 입력하세요. : "))
while col < len(string):
    print("행렬의 열의 크기가 문자열의 길이보다 크게 설정하세요.")
    col = int(input("행렬의 열의 크기를 입력하세요. : "))

start_row = int(input("문자열을 입력할 행의 기준을 입력하세요. : "))
while start_row > row:
    print("시작지점이 행렬을 범위를 벗어납니다. 다시입력해 주세요.")
    start_row = int(input("문자열을 입력할 행의 기준을 입력하세요. : "))

start_col = int(input("문자열을 입력할 열의 기준을 입력하세요. : ")) 
while start_col > col:
    print("시작지점이 행렬을 범위를 벗어납니다. 다시입력해 주세요.")
    start_col = int(input("문자열을 입력할 열의 기준을 입력하세요. : ")) 

cr = int(input("행을 고정하여 문자열을 작성하면 0이외의 숫자를\n열을 고정하여 문자열을 작성하면 0을 입력하세요 : "))
if cr == 0:
    while start_row + len(string) > row:
        print("문자열이 행렬의 범위를 넘어가므로 다시입력해주세요.")
        start_row = int(input("문자열을 입력할 행의 기준을 입력하세요. : ")) 
else:
    while start_col + len(string) > col:
        print("문자열이 행렬의 범위를 넘어가므로 다시입력해주세요.")
        start_col = int(input("문자열을 입력할 열의 기준을 입력하세요. : ")) 
    
# 행렬 생성
M = dict()
if cr == 0:
    for i in range(len(string)):
        M[start_row+i,start_col] = string[i]
else:
    for i in range(len(string)):
        M[start_row,start_col+i] = string[i]
        
# 행렬 출력
for i in range(row):
    print("+-"*col+"+")
    for j in range(col):
        print("|"+M.get((i,j)," "), end="")
    print("|")
print("+-"*col+"+")

