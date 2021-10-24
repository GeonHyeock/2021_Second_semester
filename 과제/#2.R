# 2 - 1
n <- 2000 #표본수
x <- 165 # 직업을 갖지 않은 사람의 수
p_sample <- x/n # 추정된 실업률
p_sample

# 2 - 2
z_0.025 <- qnorm(0.025, lower.tail = FALSE)
C.I. <- c(p_sample - z_0.025*sqrt(p_sample*(1-p_sample)/n),p_sample + z_0.025*sqrt(p_sample*(1-p_sample)/n))
C.I. # 95% 신뢰구간