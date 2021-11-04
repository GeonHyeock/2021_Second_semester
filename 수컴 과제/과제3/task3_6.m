sum = 0;
N = 1000000;
for n = 1:N
    sum = sum + (1/n)^2;
end
c = pi^2 / sum