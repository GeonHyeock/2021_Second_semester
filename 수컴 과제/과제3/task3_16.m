x = linspace(-3,5,1000);
for i = 1:length(x)
    if x(i) >= -1 & x(i) <= 1
        f(i) = x(i)^2;
    elseif x(i) > 1 & x(i) <4
        f(i) = 1;
    else 
        f(i) = 0;
    end
end
figure(1)
plot(x,f)