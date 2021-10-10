function [outx,outy] = multi(inx,iny)
outx = mod(inx+iny,1);
outy = mod(inx+2*iny,1);