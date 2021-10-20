#4
n <- 18 # 표본수
sample_mean <- 4.1 # 표본평균
sampel_sd <- 1.6 # 표본 표준편차

# 가정 : 표본의 모집단이 정규분포를 따른다.
# H0 : u = 3.5, H1 : u > 3.5

t0 <- (sample_mean - 3.5) / (1.6/sqrt(18))
p_value <- pt(t0,n-1,lower.tail = FALSE)
p_value > 0.05 # 가 참이므로 H0를 기각한다.즉 u = 3.5라 이야기 하기 어렵다
