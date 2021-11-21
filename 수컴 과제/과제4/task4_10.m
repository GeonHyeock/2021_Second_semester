x1 = input("좌측 초기값을 입력하세요. : ");
x2 = input("우측 초기값을 입력하세요. : ");
x = x1;



tolerance = 1e-4;
iters = 0;

while ((iters<10000) & (abs(sin(x - x.^3)) > tolerance) | (iters == 0))
    iters = iters+1;
    y1 = sin(x1 - x1.^3);
    y2 = sin(x2 - x2.^3);
    x = x1 - y1 * (x2-x1) / (y2-y1);
    y = sin(x - x^3);
    
    if y * y1 < 0
        x2 = x;
    else
        x1 = x;
    end
end

if iters == 10000
    disp("해를 찾지 못함")
elseif isnan(x)
    disp("직선이 축과 평행하여 오류")
else
    disp(["해는", num2str(x)])
    disp(["탐색횟수 : ", num2str(iters)])
end

        

%확인
a=linspace(0,6,300);
b=sin(a-a.^3);
plot(a,b)
grid on