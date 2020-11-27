# -*- coding: utf-8 -*-
# @Time : 2020/11/24 10:51
# @Author : Jiangzhesheng
# @File : test_algo.py
# @Software: PyCharm
import sys
import algo
import myclass
from unittest import TestCase
import logging
class Test(TestCase):
    def test_ond_algo(self):
        A='ABCABBA'
        B='CBABAC'
        ans=5
        ond_ans=algo.ond_algo(A,B)
        self.assertEqual(ond_ans,ans,'ond_ans is %d but ans is '%ond_ans+str(ans))
    def test_my_ond_algo(self):
        A = 'ABCABBA'
        B = 'CBABAC'
        ans = 5
        ond_ans = algo.my_ond_algo(A, B)
        self.assertEqual(ond_ans, ans, 'ond_ans is %d but ans is ' % ond_ans + str(ans))
    def test_ond_and_dp_algo(self):
        testcase=[('horse','rose'),('intension','execution')]
        for i in testcase:
            ond_ans=algo.ond_algo(i[0],i[1])
            dp_ans=algo.dp_algo(i[0],i[1])
            self.assertEqual(ond_ans,dp_ans,'wops')
    def test(self):
        queryfile=myclass.Fastafile('/test_data/query')
        reffile=myclass.Fastafile('/test_data/ref')
        for i,j in zip(queryfile,reffile):
            ond_ans=algo.ond_algo(i.base,j.base)
            dp_ans=algo.dp_algo(i.base,j.base)
