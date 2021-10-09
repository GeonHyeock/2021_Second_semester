x = 0:pi/10:2*pi
y = x;
[X,Y] = meshgrid(x,y);

f1 = func1(X,Y)
figure(1)
contour(X,Y,f1)
axis([0 2*pi 0 2*pi])
axis equal

f2 = func2(X,Y)
figure(2)
contour(X,Y,f2)
axis([0 2*pi 0 2*pi])

