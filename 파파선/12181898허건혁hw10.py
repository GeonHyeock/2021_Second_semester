def a_dot_b(a,b):
    return a[0]*b[0] + a[1]*b[1]

def add_tuples(a,b,alpha=1,beta=-1):
    return alpha * a[0] + beta * b[0] , alpha * a[1] + beta * b[1]

def Make_Straight(a,b): #직선의 방정식
    if b[0] - a[0] == 0:     #  y축과 평행할때
        return [a[0]]
    else :
        slope = (b[1] - a[1]) / (b[0] - a[0])
        return slope, b[1] - b[0] * slope     # return (기울기, y절편)

def Intersection_point(l1,l2): # 두 직선의 교점
    if len(l1) * len(l2) == 1: # 두 직선이 모두 y축과 평행할때
        return "NO Intersection"
    
    elif len(l1) * len(l2) == 2: # 두 직선중 한 직선이 y축과 평행할때
        if len(l1) == 1:
            return l1[0],l2[0] * l1[0] + l2[1]
        elif len(l2) == 1:
            return l2[0], l1[0] * l2[0] + l1[1]
    
    elif l1[0] == l2[0]: # 두 직선이 평행할때
        return "NO Intersection"
    
    else:
        x = (l1[1] - l2[1]) / (l2[0] - l1[0])
        return x , l2[0] * x + l2[1]

class Triangle:
    def __init__(self,vertex=[(0,0),(1,0),(0,1)], name = "T"):
        self.vertex = vertex
        self.name = name
        
    def area(self):
        a = add_tuples(self.vertex[0], self.vertex[1])
        b = add_tuples(self.vertex[0], self.vertex[2])
        return ((a_dot_b(a, a) * a_dot_b(b, b) - a_dot_b(a, b) ** 2) ** (1/2)) / 2

    def In_Triangle(self,pt):
        T_1 = Triangle([pt, self.vertex[0], self.vertex[1]])
        T_2 = Triangle([pt, self.vertex[0], self.vertex[2]])
        T_3 = Triangle([pt, self.vertex[1], self.vertex[2]])
        
        T_sum = T_1.area() + T_2.area() + T_3.area()

        if T_sum <= self.area():
            return True
        return False
    
    def centroid(self): # 무게중심
        return (self.vertex[0][0] + self.vertex[1][0] + self.vertex[2][0])/3,\
            (self.vertex[0][1] + self.vertex[1][1] + self.vertex[2][1])/3
    
    def Intersect(self,T):
        """
        step1) 삼각형의 꼭짓점으로 생성되는 직선의 교점이 두 삼각형 내부(라인)에 포함되는지 확인
        step2) 한 삼각형의 무게중심이 다른 삼각형 안에 포함되는지 확인
        
        step1 : 한 삼각형이 다른 삼각형과 일치하는 점이 적어도 한 점 있는 경우
        step2 : 한 삼각형이 다른 삼각형과 일치하는 점이 없는 경우 , 
                i.e) 한 삼각형이 다른 삼각형을 포함하는 경우
        """
        # step1
        
        L1 = Make_Straight(self.vertex[0], self.vertex[1])
        L2 = Make_Straight(self.vertex[0], self.vertex[2])
        L3 = Make_Straight(self.vertex[1], self.vertex[2])
        
        L4 = Make_Straight(T.vertex[0], T.vertex[1])
        L5 = Make_Straight(T.vertex[0], T.vertex[1])
        L6 = Make_Straight(T.vertex[0], T.vertex[1])
        
        for i in L1,L2,L3:
            for j in L4,L5,L6:
                if Intersection_point(i,j) != "NO Intersection":
                    if self.In_Triangle(Intersection_point(i,j)) and T.In_Triangle(Intersection_point(i,j)):
                        return True
        
        # step2
        
        if T.In_Triangle(self.centroid()) or self.In_Triangle(T.centroid()):
            return True
        
        return False
        
if __name__ == "__main__":
    
    T1 = Triangle(vertex=[(2,0),(2,4),(5,9)],
                  name="T1")

    
    T2 = Triangle(vertex=[(1,0),(2,2),(0,1)],
        name = "T2")
    
    print(T1.Intersect(T2))