global tolerance maxits
tolerance = 1e-4;
maxits = 30;
init_value = input("초기값을 입력하세요. : ");


% 1
disp("문제 1, b=3인경우")
[root, iflag] = fixed('f4_6_1',init_value);
switch iflag
    case -1
        disp("해를 찾지 못하였습니다.")
    otherwise
        disp(["초기값",num2str(init_value),"에대하여" ,"해는", num2str(root)])
        disp(["탐색횟수 : ", num2str(iflag)])
end

% 2
disp("문제 2, b=3인경우")
[root, iflag] = fixed('f4_6_2',init_value);
switch iflag
    case -1
        disp("해를 찾지 못하였습니다.")
    otherwise
        disp(["초기값",num2str(init_value),"에대하여" ,"해는", num2str(root)])
        disp(["탐색횟수 : ", num2str(iflag)])
end
