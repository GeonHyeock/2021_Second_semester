N = 1000000;

sum1 = 0;
for n = 1:N
    sum1 = sum1 + (-1)^(n)/(n);
end
sum1


sum2 = 0;
for n = 1:N;
    sum2 = sum2 + 1/((n+1)*(n));
end
sum2
