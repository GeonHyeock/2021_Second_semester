#!/usr/bin/env python
# coding: utf-8

# In[158]:


"""
파일 설명:
SuCum_cross(주소)
input파일은 = 1개와 띄어쓰기를 구분자로함
첫줄 : 
Matrix_size = 매트릭스 행, 매트릭스 열
그 이후:
문자 = 행 열 행열구분
행열구분 : 0이면 0을 고정 0이외면 행을 고정
ex)
tiger = 2 3 0
lion = 3 2 1

변수 설명:
string : [str1, str2 ,str3]
location : [(start_row start_col cr),(start_row start_col cr),(start_row start_col cr)]
start_row : 문자입력 시작행
start_col : 문자입력 시작열
cr : 행열 구분
"""


# In[159]:


def SuCum(string,location,row,col):
    M = dict()
    output = []
    
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
        output.append("+-"*col+"+\n")
        A = ""
        for k in range(col):
            A = A + "|"+M.get((j,k)," ")
        output.append(A+"|\n")
    output.append("+-"*col+"+")
    return output


# In[163]:


def SuCum_cross(address):
    input_file = list(open(address,"r"))
    input_num = len(input_file) - 1
    Mat = input_file[0][input_file[0].rfind("=")+1:input_file[0].rfind("\n")]
    
    string = [input_string[:input_string.rfind("=")].split()[0] for input_string in input_file][1:]
    location = [tuple(map(int,input_location[input_location.rfind("=")+1:].split()))
                for input_location in input_file][1:]
    row = int(Mat.split()[0])
    col = int(Mat.split()[1])
    
    path = "/".join(address.split("/")[:-1])+"/output.txt"
    open(path,"w").writelines(SuCum(string,location,row,col))


# In[164]:


SuCum_cross("/Users/heogeonhyeock/Desktop/파파선/input.txt")


# In[156]:





# In[157]:




