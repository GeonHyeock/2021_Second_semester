N = input('Enter N')

sum =0;
for i = 1:N
    sum = sum + 1/i +1/((i+2)*(i+3))
end

disp(["The answer is " num2str(sum)])
