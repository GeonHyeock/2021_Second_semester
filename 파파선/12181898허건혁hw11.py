"""
두 선분을 대각선으로 하는 평행사변형은 유일하게 한 개 존재
평행사변형의 대각선의 교점의 성질 : 대각선의 교점
위 성질에 따라 두 선분의 중점이 일치하면 선분이 교점을 갖는다고 판단

두 선분이 만나지 않는다면 당연하게도 각 선분의 중점이 일치하지 않음
"""


def GH_line(a,b):
    a_middle = (a[0][0] + a[1][0])/2 , (a[0][1] + a[1][1])/2
    b_middle = (b[0][0] + b[1][0])/2 , (b[0][1] + b[1][1])/2
    
    if a_middle == b_middle:
        return True
    return False

a = ((1,2),(2,3))
b = ((1,3),(2,4))
c = ((1,-1), (-1,1))
d = ((1,1),(-1,-1))

print(GH_line(a, b))
print(GH_line(c, d))

# 선분 그래프 수정
import numpy as np
import matplotlib.pyplot as plt


def Point2D_Line( xs, ys, domain=[ (-5,5), (-5,5) ] ):
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111, aspect='equal')

    GH = xs + ys
    xs = [i[0] for i in GH]
    ys = [i[1] for i in GH]

    xsnp = np.array( xs )
    ysnp = np.array( ys )

    xy_pairs = np.c_[xsnp, ysnp]
    xy_args = xy_pairs.reshape(-1, 2, 2).swapaxes(1, 2).reshape(-1, 2)

    ax.set_xlim( domain[0] )
    ax.set_ylim( domain[1])
    # segments
    ax.plot(*xy_args, c='k')
    plt.show()

Point2D_Line(a, b)
Point2D_Line(c, d)