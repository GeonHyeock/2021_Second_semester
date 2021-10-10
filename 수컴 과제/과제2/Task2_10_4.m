w = ones(1,9);
w(1) = 1;
for i = 1:4
    w(2*i) = 3;
    w(2*i+1) = 2*i+1;
end
w