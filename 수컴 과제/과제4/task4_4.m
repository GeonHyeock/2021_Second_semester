b = input("b의 값을 입력하세요. : ");

x1 = -1.5;
x2 = 1.53;
x = x1;



tolerance = 1e-4;
iters = 0;

while ((iters<10000) & (abs(f4_4(x,b)) > tolerance) | (iters == 0))
    iters = iters+1;
    y1 = f4_4(x1,b);
    y2 = f4_4(x2,b);
    x = x1 - y1 * (x2-x1) / (y2-y1);
    y = f4_4(x,b);
    
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
    disp(["해는", num2str(x), "+n*pi, n은정수"])
    disp(["탐색횟수 : ", num2str(iters)])
end