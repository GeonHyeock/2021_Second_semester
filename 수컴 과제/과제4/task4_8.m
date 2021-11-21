global tolerance maxits

tolerance = 1e-4;
maxits = 30;
x1 = input("x의 하한값을 입력하세요. : ");
x2 = input("x의 상한값을 입력하세요. : ");

[root, iflag] = bisect("f4_8",x1,x2);

switch iflag
    case -1
        disp("해를 찾지 못함")
    case -2
        disp("입력한 범위내 해가 존재하지 않음")
    otherwise
        disp(["초기범위",num2str(x1),num2str(x2),"에대하여" ,"해는", num2str(root)])
        disp(["탐색횟수 : ", num2str(iflag)])
end

x = linspace(x1,x2,1000);
y = f4_8(x);
plot(x,y);
grid on
