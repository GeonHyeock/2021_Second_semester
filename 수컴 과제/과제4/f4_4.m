function [y] = f4_4(x,b)
a = atan(b);
y = sin(x+a)/sqrt(b^2 + 1);