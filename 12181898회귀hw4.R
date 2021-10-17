setwd("/Users/heogeonhyeock/Downloads")

data <- read.csv("AT2.txt", header = T, sep = "")
x <- data$X
y <- data$Y
fit <- lm(y~x)
summary(fit)

#b 
fit$coefficients

#c
anova(fit)
sd <- 1684.08/21

#d,e 절편추정값과 기울기추정값 모두 0.05 유의수준에서 기각하지 못한다. 
summary(fit)

#f
anova(fit)

#g : ,0.05 하에서 귀무가설을 기각하지 못한다.

anova(fit)

#h,i
confint(fit, level = 0.95)

#j
new.data=data.frame(x=c(75))
predict(fit,new.data,interval = "confidence", level = 0.95)

#k
predict(fit,new.data,interval = "prediction", level = 0.95)

#l, 0.1318
summary(fit)
