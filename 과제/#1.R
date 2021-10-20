# 1 - 1
n <- 42 # 표본의 수
mean <- 8.5 # 귀무가설이 참일때 모평균
sample_mean <- 8.79 # 표본평균
sd <- 1.27 # 표본 표준편차
x0 <- (8.79 - 8.5)/(sd/sqrt(n)) # 검정통계량
a_upper <- qnorm(0.05, lower.tail = FALSE) # 유의수준 0.1에 대한 상한 값
a_lower <- qnorm(0.05, lower.tail = TRUE) # 유의수준 0.1에 대한 상한 값
a_lower > x0 | x0 > a_upper # 기각역에 포함되지 않으므로 귀무가설을 기각한다.

# 1 - 2
p_value <- pnorm(x0, lower.tail = FALSE) + pnorm(-x0, lower.tail = TRUE)
# p_value 값이 약 0.139이므로 유의수준이 0.139 이상인 경우 귀무가설을 기각 할 수 있다.

