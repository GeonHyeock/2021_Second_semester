sum = 0;
for i = 1:2:100
    sum = sum + (1/i)^2;
end
disp(['Required value is ' num2str(sum)])