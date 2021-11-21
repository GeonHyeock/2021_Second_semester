x = -5:0.01:5;
y = exp(x);

coshx = (y+1./y)./2;
sinhx = (y-1./y)./2;

coshx_0 = find(coshx==0);
if isempty(coshx_0)
    disp("cosh가 0이 되는 x값이 존재하지 않는다.")
else
    disp("cosh가 0이 되는 x값이 존재한다.")
end

sinhx_0 = find(sinhx==0);
if isempty(sinhx_0)
    disp("sinh가 0이 되는 x값이 존재하지 않는다.")
else
    disp("sinh가 0이 되는 x값이 존재한다.")
end

m = input("m의 값을 입력하세요.");
n = input("n의 값을 입력하세요.");
z = (cosh(x)).^m.*(sinh(x)).^n;

z_0 = find(z==0);
if isempty(z_0)
    disp("z가 0이 되는 x값이 존재하지 않는다.")
else
    disp("z가 0이 되는 x값이 존재한다")
end
