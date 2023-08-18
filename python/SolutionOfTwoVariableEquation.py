#let ax+by=c
#    px+qy=r
#here e1 is [a,b,c] and e2 is[p,q,r]


def det(m):
    return (m[0] * m[3] - m[1] * m[2])

def solution(e1,e2):
    d = det([e1[0],e1[1],e2[0],e2[1]])
    if d ==0:
        return "There is no unique solution..."
    x = det([e1[2],e1[1],e2[2],e2[1]])/d
    y = det([e1[0],e1[2],e2[0],e2[2]])/d
    return x,y

print(solution([1,2,3],[2,4,4]))