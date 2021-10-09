#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
string : [str1, str2 ,str3]
location : [(start_row start_col cr),(start_row start_col cr),(start_row start_col cr)]
start_row : 문자입력 시작행
start_col : 문자입력 시작열
cr : 행렬 구분
"""


# In[ ]:


def SuCum(string,location,row,col):
    M = dict()
    
    for i in range(len(location)):
        
        start_row = location[i][0]
        while start_row > row:
            print("시작지점이 행렬을 범위를 벗어납니다. 다시입력해 주세요.")
            start_row = int(input("문자열을 입력할 행의 기준을 입력하세요. : "))
            
        start_col = location[i][1]
        while start_col > col:
            print("시작지점이 행렬을 범위를 벗어납니다. 다시입력해 주세요.")
            start_col = int(input("문자열을 입력할 열의 기준을 입력하세요. : "))
            
        cr = location[i][2]
        
        if cr == 0: #열을 고정하여 입력
            while row < len(string[i]):
                print("행렬의 행의 크기가 문자열의 길이보다 크게 설정하세요.")
                row = int(input("행렬의 행의 크기를 입력하세요. : "))
            while start_row + len(string) > row:
                print("문자열이 행렬의 범위를 넘어가므로 다시입력해주세요.")
                start_row = int(input("문자열을 입력할 행의 기준을 입력하세요. : ")) 
                
            for j in range(len(string[i])):
                while M.get((start_row+j,start_col),string[i][j]) != string[i][j]:
                    print("{0}의 {1}가 이전에 입력된 {2}행 {3}열의 {4}와 불일치 합니다. {0}을 입력할 행렬의 기준점을 다시 입력하시오."                          .format(string[i],string[i][j],start_row+j,start_col,M[start_row+j,start_col]))
                    
                    start_row = int(input("{}을 입력할 행의 기준을 입력하세요. : ".format(string[i])))
                    while start_row > row:
                        print("시작지점이 행렬을 범위를 벗어납니다. 다시입력해 주세요.")
                        start_row = int(input("문자열을 입력할 행의 기준을 입력하세요. : "))
                        
                    start_col = int(input("{}을 입력할 열의 기준을 입력하세요. : ".format(string[i])))
                    while start_col > col:
                        print("시작지점이 행렬을 범위를 벗어납니다. 다시입력해 주세요.")
                        start_col = int(input("문자열을 입력할 열의 기준을 입력하세요. : "))
                        
                M[start_row+j,start_col] = string[i][j]
                
        else: # 행을 고정하여 입력
            while col < len(string):
                print("행렬의 열의 크기가 문자열의 길이보다 크게 설정하세요.")
                col = int(input("행렬의 열의 크기를 입력하세요. : "))
            while start_col + len(string) > col:
                print("문자열이 행렬의 범위를 넘어가므로 다시입력해주세요.")
                start_col = int(input("문자열을 입력할 열의 기준을 입력하세요. : "))
                
            for j in range(len(string[i])):
                while M.get((start_row,start_col+j),string[i][j]) != string[i][j]:
                    print("{0}의 {1}가 이전에 입력된 {2}행 {3}열의 {4}와 불일치 합니다. {0}을 입력할 행렬의 기준점을 다시 입력하시오."                          .format(string[i],string[i][j],start_row,start_col+j,M[start_row,start_col+j]))
                    
                    start_row = int(input("{}을 입력할 행의 기준을 입력하세요. : ".format(string[i])))
                    while start_row > row:
                        print("시작지점이 행렬을 범위를 벗어납니다. 다시입력해 주세요.")
                        start_row = int(input("문자열을 입력할 행의 기준을 입력하세요. : "))
                        
                    start_col = int(input("{}을 입력할 열의 기준을 입력하세요. : ".format(string[i])))
                    while start_col > col:
                        print("시작지점이 행렬을 범위를 벗어납니다. 다시입력해 주세요.")
                        start_col = int(input("문자열을 입력할 열의 기준을 입력하세요. : "))
                    
                M[start_row,start_col+j] = string[i][j]          
        
    for j in range(row):
        print("+-"*col+"+")
        for k in range(col):
            print("|"+M.get((j,k)," "), end="")
        print("|")
    print("+-"*col+"+")


# In[15]:


input_num = int(input("입력할 데이터의 숫자를 입력하세요. : "))
Mat = input("0을 시작으로하는 행렬의 (행의크기 열의크기)를 띄어쓰기를 구분자로 입력하세요. : ")

string = []
location = []
row = int(Mat.split()[0])
col = int(Mat.split()[1])

for i in range(input_num):
    input_string = input("입력할 {0}번째 문자를 입력하세요. : ".format(i+1))
    input_location = input("입력할 {}번째 문자를 출력할 0부터 시작하는 행렬의 (시작행 시작열 행열구분)을 띄어쓰기를 구분자로 입력하세요                           \n<행렬구분 : 행을 고정하면 0이외의 숫자를 열을 고정하면 숫자 0을 입력하세요> : ".format(i+1))
    input_location2 = int(input_location.split()[0]),int(input_location.split()[1]),int(input_location.split()[2])
    
    location.append(input_location2)
    string.append(input_string)

SuCum(string,location,row,col)


# In[16]:


""" 
예시)

입력할 데이터의 숫자를 입력하세요. : 2
0을 시작으로하는 행렬의 (행의크기 열의크기)를 띄어쓰기를 구분자로 입력하세요. : 10 10
입력할 1번째 문자를 입력하세요. : tiger
입력할 1번째 문자를 출력할 0부터 시작하는 행렬의 (시작행 시작열 행열구분)을 띄어쓰기를 구분자로 입력하세요                           
<행렬구분 : 행을 고정하면 0이외의 숫자를 열을 고정하면 숫자 0을 입력하세요> : 2 3 0
입력할 2번째 문자를 입력하세요. : lion
입력할 2번째 문자를 출력할 0부터 시작하는 행렬의 (시작행 시작열 행열구분)을 띄어쓰기를 구분자로 입력하세요                           
<행렬구분 : 행을 고정하면 0이외의 숫자를 열을 고정하면 숫자 0을 입력하세요> : 3 3 1
lion의 l가 이전에 입력된 3행 3열의 i와 불일치 합니다. lion을 입력할 행렬의 기준점을 다시 입력하시오.
lion을 입력할 행의 기준을 입력하세요. : 3
lion을 입력할 열의 기준을 입력하세요. : 2

+-+-+-+-+-+-+-+-+-+-+
| | | | | | | | | | |
+-+-+-+-+-+-+-+-+-+-+
| | | | | | | | | | |
+-+-+-+-+-+-+-+-+-+-+
| | | |t| | | | | | |
+-+-+-+-+-+-+-+-+-+-+
| | |l|i|o|n| | | | |
+-+-+-+-+-+-+-+-+-+-+
| | | |g| | | | | | |
+-+-+-+-+-+-+-+-+-+-+
| | | |e| | | | | | |
+-+-+-+-+-+-+-+-+-+-+
| | | |r| | | | | | |
+-+-+-+-+-+-+-+-+-+-+
| | | | | | | | | | |
+-+-+-+-+-+-+-+-+-+-+
| | | | | | | | | | |
+-+-+-+-+-+-+-+-+-+-+
| | | | | | | | | | |
+-+-+-+-+-+-+-+-+-+-+
"""


# In[ ]:




