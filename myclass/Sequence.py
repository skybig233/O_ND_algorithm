# -*- coding: utf-8 -*-
# @Time : 2020/9/10 15:32
# @Author : Jiangzhesheng
# @File : Sequence.py
# @Software: PyCharm
import argparse
import sys
import logging
BASE_LIST=['A','G','C','T','a','g','c','t','N','n']
PRINCIPLE_DICT={'A':'T','a':'T','T':'A','t':'A',
                'C':'G','c':'G','G':'C','g':'C',
                'N':'N','n':'n'}

def DNA_reverse(s:str)->str:
    ans = ''
    for i in s:
        ans = PRINCIPLE_DICT.get(i,'?') + ans
    return ans

class Sequence:
    def __init__(self, base_string='', orient='') -> None:
        self.base_string=base_string
        self.orient=orient
class Dna_Sequence(Sequence):
    def __init__(self, base_string='', orient='') -> None:
        for i in base_string:
            if not i in BASE_LIST:
                logging.warning(base_string+' is not a DNA seq')
                return
        super().__init__(base_string, orient)
    def reverse(self)->str:
        DNA_reverse(self.base_string)

if __name__ == '__main__':
    s=Sequence('AGCTatcc')
    print(s.reverse())