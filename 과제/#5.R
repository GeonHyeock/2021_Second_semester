#5
n <- 18 # 표본수
sample_mean <- 4.1 # 표본평균
sampel_sd <- 1.6 # 표본 표준편차

# 가정 : 표본의 모집단이 정규분포를 따른다.
# H0 : u = 3.5, H1 : u > 3.5
t_0.025 <- qt(0.025,df = n-1,lower.tail = FALSE)
C.I. <- c(sample_mean-t_0.025*(1.6/sqrt(n)),sample_mean+t_0.025*(1.6/sqrt(n)));C.I.
# t0가 신뢰구간 안에 있으므로 H0를 기각하지 못한다.
