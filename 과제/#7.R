#7
n <- 27
n1 <- 12 # 새로운 살충제
n2 <- 15 # 기존의 살충제

mean1 <- 73.9
mean2 <- 62.4
sd1 <- 3.7
sd2 <- 5.5

# 가정 : 두 확률변수가 서로 독립이고 정규분포를 따른다.
mean_diff <- mean1 - mean2
n_diff <- min(n1-1,n2-1)

# 귀무가설 주어진 두 표본의 모집단의 평균을 각각 u1,u2라 가정하자
# H0 : u1-u2 = 0, H1 : u1 - u2 > 0
t0 <- mean_diff/sqrt(sd1^2/n1 + sd2^2/n2)
p_value <- pt(t0, df = n_diff,lower.tail = FALSE)
p_value < 0.05 #가 참이므로 귀무가설을 기각한다. 즉 유의수준 0.05 하에서  u1 > u2 가 옳다고 주장할 수 있다.

 