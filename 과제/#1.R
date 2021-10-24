# 1 - 1
n <- 42 # 표본의 수
sample_mean <- 8.79 # 표본평균
sd <- 1.27 # 표본 표준편차

# H0 : u = 8.5, u != 8.5
mean <- 8.5 # 귀무가설이 참이라는 가정하에 모평균
x0 <- (8.79 - 8.5)/(sd/sqrt(n)) # 검정통계량
a_upper <- qnorm(0.05, lower.tail = FALSE) # 유의수준 0.1에 대한 상한 값
a_lower <- qnorm(0.05, lower.tail = TRUE) # 유의수준 0.1에 대한 하한 값
a_lower > x0 | x0 > a_upper # 가 거짓이므로 귀무가설을 기각하지 못한다.

# 1 - 2
p_value <- pnorm(x0, lower.tail = FALSE) + pnorm(-x0, lower.tail = TRUE)
p_value # p_value가 약 0.139이므로 유의수준이 0.139이상일 경우에 귀무가설을 기각 할 수 있다.


