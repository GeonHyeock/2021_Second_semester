str = 'abcdefghij';
msg = 'Enter an integer from 1 to 10: ';
n = input(msg);
while (round(n) ~= n) | (n<1 | n>10)
    n = input(msg);
end
str(1:n)