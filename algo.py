# -*- coding: utf-8 -*-
# @Time : 2020/11/24 10:47
# @Author : Jiangzhesheng
# @File : algo.py
# @Software: PyCharm
import sys
import myclass
import time
def dp_algo(word1:str,word2:str)->int:
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
                left_down += 2
            D[i][j] = min(left, down, left_down)
    return D[n][m]

def ond_algo(A:str,B:str)->int:
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

def main(argv):
    queryfile = myclass.Fastafile('test_data/query')
    reffile = myclass.Fastafile('test_data/ref')
    cnt=0
    for i, j in zip(queryfile, reffile):
        if cnt>1:
            break
        cnt+=1
        start=time.time()
        ond_ans = ond_algo(i.base, j.base)
        ond_end=time.time()
        dp_ans = dp_algo(i.base, j.base)
        dp_end=time.time()
        print('ond excute',ond_end-start,'s with ans',str(ond_ans))
        print('dp excute',dp_end - ond_end,'s with ans', str(dp_ans))
if __name__ == '__main__':
    main(sys.argv)