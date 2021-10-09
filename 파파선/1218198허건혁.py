
#hw 1번

Given_str = input("Given_str을 입력하세요. : ")
Remove_str = input("Remove_str을 입력하세요. : ")

Given_str_list = list(Given_str)
for x in Remove_str:
    Given_str_list.pop(Given_str.find(x))
    Given_str = "".join(Given_str_list)

print("Given str에서 Remove str을 제거한 결과는 :",Given_str,"입니다")





# hw 2번
row = int(input("행렬의 행의 갯수를 입력하세요. : "))
col = int(input("행렬의 열의 갯수를 입력하세요. : "))


Mat = [None] * row
for i in range(row):
    Mat[i] = [int(input("Mat의 {0}행 {1}열의 값을 입력하세요. : ".format(i,j))) for j in range(col)]
print("입력된 행렬은 다음과 같습니다 : ", Mat)


col_sum_index = int(input("합계를 원하는 열의 index를 입력하세요. : "))    
col_sum = 0
for x in range(row):
    col_sum += Mat[x][col_sum_index]

print("{0}열의 합계는 {1}입니다".format(col_sum_index,col_sum))

