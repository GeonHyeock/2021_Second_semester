# 3
n <- 130 # 표본의 수
x <- 38 # 20시간 이상 공부하는 학생 수
p_sample <- x/n

# 귀무가설 : p = 0.25, 대립가설 : p > 0.25
p <- 0.25

p0 <- (p_sample - p) / sqrt(p*(1-p)/n) # 검정통걔량
p_value <- pnorm(p0, lower.tail = FALSE) # p_value가 약 0.133 이므로 유의수준 0.133 이상에서 귀무가설을 기각한다


