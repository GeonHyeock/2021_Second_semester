x = input('x = ');
fzero('f4_14',x,optimset('disp','iter'))

%확인
x_plot=linspace(0,20,1000);
y=f4_14(x_plot);
plot(x_plot,y)
grid on
axis([0 20 -0.3 0.3])