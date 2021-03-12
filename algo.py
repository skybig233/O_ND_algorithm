# -*- coding: utf-8 -*-
# @Time : 2020/11/24 10:47
# @Author : Jiangzhesheng
# @File : algo.py
# @Software: PyCharm
import sys
import myclass
import time

def dp_algo(word1:str,word2:str)->int:
    """
    这是从leetcode官方题解上摘录下来的解法
    :param word1:
    :param word2:
    :return: 直接给出D值
    """
    n = len(word1)
    m = len(word2)
    # 有一个字符串为空串
    if n * m == 0:
        return n + m
    # DP 数组
    D = [[0] * (m + 1) for _ in range(n + 1)]
    # 边界状态初始化
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    # 计算所有 DP 值
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            left = D[i - 1][j] + 1
            down = D[i][j - 1] + 1
            left_down = D[i - 1][j - 1]
            if word1[i - 1] != word2[j - 1]:
                left_down += 1
            D[i][j] = min(left, down, left_down)
    return D[n][m]

def ond_algo(A:str,B:str)->int:
    """
    这是根据论文的伪代码描述写的，Insert Delete权值为1、Sub权值为2
    :param A:
    :param B:
    :return: 直接给出D值
    """
    n=len(A)
    m=len(B)
    max_value=m+n
    v=[-1]*(max_value+1)
    x,y=0,0
    while x < n and y < m and A[x] == B[y]:
        x, y = x + 1, y + 1
    v[m] = x
    for d in range(1,max_value):
        for k in range(-d,d+2,2):
            if k==-d or k!=d and v[k-1+m]<v[k+1+m]:
                x=v[k+1+m]#竖着走
            else:
                x=v[k-1+m]+1#横着走
            y=x-k
            while x<n and y<m and A[x]==B[y]:
                x,y=x+1,y+1
            v[k+m]=x
            if x>=n and y>=m:
                return d

class Point:
    def __init__(self,x,k) -> None:
        self.x=x
        self.k=k
        self.y=x-k

    def __str__(self) -> str:
        return '(%s,%s)' % (self.x,self.y)

def my_ond_algo_version0(A:str, B:str)->[[]]:
    n=len(A)
    m=len(B)
    max_value=m+n
    v=[]
    x,y=0,0
    while x < n and y < m and A[x] == B[y]:
        x, y = x + 1, y + 1
    v.append([x])
    for d in range(1,max_value):
        tmp_v=[-1]*(2*d+1)
        for k in range(-d,d+2,2):
            if k==-d:
                x=v[d-1][k+d]#竖着走
            elif k==d:
                x=v[d-1][k+d-2]+1#横着走
            else:
                p1 = Point(x=v[d - 1][k + d], k=k+1)#竖着走的点
                p2 = Point(x=v[d - 1][k + d - 2], k=k-1)#横着走的点
                if p1.x>p2.x:
                    x = v[d - 1][k + d]
                else:
                    x = v[d - 1][k + d - 2] + 1
            y=x-k
            while x<n and y<m and A[x]==B[y]:
                x,y=x+1,y+1
            tmp_v[k+d]=x
            if x>=n and y>=m:
                return v
        v.append(tmp_v)

def list_get(index:int, list:[], default=None):
    return list[index] if 0<= index < len(list) else default

def my_ond_algo_version1(A:str, B:str)->[[]]:
    """
    改进后的OND算法，IDS权值都为1，并且返回一个v数组，后续根据v数组计算D值和路径（编辑脚本）
    :param A:
    :param B:
    :return:v数组
    """
    n=len(A)
    m=len(B)
    max_value=m+n
    v=[]
    x,y=0,0
    while x < n and y < m and A[x] == B[y]:
        x, y = x + 1, y + 1
    v.append([x])
    # 边界值处理。。。。例如('aaaa','aaaa')、('','')
    if x>=n and y>=m:
        return v
    for d in range(1,max_value):
        tmp_v=[-1]*(2*d+1)
        for k in range(-d,d+1,1):
            x1=list_get(list=v[d-1],index=k+d-2,default=-1)
            x2=list_get(list=v[d-1],index=k+d-1,default=-1)
            x3=list_get(list=v[d-1],index=k+d,default=-1)
            p1 = Point(x=x1, k=k-1)#横着走的点
            p2= Point(x=x2,k=k)#substitution
            p3 = Point(x=x3, k=k+1)#竖着走的点
            x=max([p1.x+1,p2.x+1,p3.x])
            y=x-k
            while x<n and y<m and A[x]==B[y]:
                x,y=x+1,y+1
            tmp_v[k+d]=x
            if x>=n and y>=m:
                v.append(tmp_v)
                return v
        v.append(tmp_v)


def get_edit_distance(v:[[]]):
    return len(v)-1

def get_edit_script(v:[[]])->[]:
    script=[]
    d=len(v)-1
    k=v[-1].index(-1)-d-1 if -1 in v[-1] else d
    for d in range(len(v)-1,0,-1):
        x1 = list_get(list=v[d - 1], index=k + d - 2, default=-1)
        x2 = list_get(list=v[d - 1], index=k + d - 1, default=-1)
        x3 = list_get(list=v[d - 1], index=k + d, default=-1)
        p1 = Point(x=x1, k=k - 1)  # 横着走的点
        p2 = Point(x=x2, k=k)  # substitution
        p3 = Point(x=x3, k=k + 1)  # 竖着走的点
        p_list=[(p1.x+1,p1),(p2.x+1,p2),(p3.x,p3)]
        p_list.sort(key=lambda p:p[0])
        if p_list[-1][1]==p1:
            script.insert(0,(p_list[-1][1].x,'D'))
        elif p_list[-1][1]==p2:
            script.insert(0,(p_list[-1][1].x,'S'+str(p_list[-1][1].y)))
        elif p_list[-1][1]==p3:
            script.insert(0,(p_list[-1][1].x,'I'+str(p_list[-1][1].y)))
        k=p_list[-1][1].k
    return script

def main(argv):
    CASE_NUM=3
    queryfile = myclass.Fastafile('test_data/query')
    reffile = myclass.Fastafile('test_data/ref')
    case=list(zip(queryfile,reffile))
    i,j=case[CASE_NUM][0],case[CASE_NUM][1]
    start=time.time()
    ond_ans = get_edit_distance(my_ond_algo_version1(i.base, j.base))
    ond_end=time.time()
    print('ond excute',ond_end-start,'s with ans',str(ond_ans))
    dp_ans = dp_algo(i.base, j.base)
    dp_end=time.time()
    print('dp excute',dp_end - ond_end,'s with ans', str(dp_ans))
if __name__ == '__main__':
    main(sys.argv)