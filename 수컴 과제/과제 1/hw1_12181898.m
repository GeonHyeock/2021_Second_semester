% 1.2
x = [pi/3, pi/6]
y = abs(x) .* sin(x.^2)


% 1.4
x = [0.3, 1/3, 0.5, 1/2, 1.65, -1.34]
round = round(x)
ceil = ceil(x)
floor = floor(x)
fix = fix(x)

% 1.6
x = 1:0.1:2

y_1 = polyval([1,3,0,1],x)
y_2 = sin(x.^2)
y_3 = sin(x).^2
y_4 = sin(2 * x) + x .* cos(4 * x)
y_5 = x ./ (x.^2 + 1)
y_6 = cos(x) ./ (1+sin(x))
y_7 = 1./x + (x.^3)./(x.^4 + 5 * x.*sin(x))

% 1.8
x = -2:0.1:-1
y = (1./(x.^3))+(1./(x.^2))+(3./(x))

% 1.10
x = linspace(-2,2,20);
c = [1,0,0,0,-1];
y = polyval(c,x);
plot(x,y)