# 6-1
n <- 25
C.I. <- c(106.8,115.2)

t0.025 <- qt(0.025,df = n-1,lower.tail = FALSE)
sample_mean <- (C.I.[1] + C.I.[2])/2
sample_sd <- (C.I.[2] - C.I.[1])/2*sqrt(n)/t0.025
sampel_sd
# 6-2 H0 : ∂ = 8.0 , ∂ > 8.0
sigma0 <- (n-1)*sample_sd^2/8^2
p_value <- pchisq(sigma0,df = n-1,lower.tail = FALSE)
p_value < 0.05 # 이므로 귀무가설을 기각


