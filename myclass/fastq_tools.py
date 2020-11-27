# -*- coding: utf-8 -*-
# @Time : 2020/9/27 9:40
# @Author : Jiangzhesheng
# @File : fastq.py
# @Software: PyCharm

import sys
import myclass

def Fastqlist2file(Fastqlist,outfilepath:str):
    with open(outfilepath,mode='w') as outfile:
        for fastq in Fastqlist:
            outfile.write(str(fastq))
    return outfilepath

class Fastqfile(myclass.File_object):
    """
    Fastq文件类，继承File_object，只含path属性
    """
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def __iter__(self):
        """
        实现了给定Fastqfile文件路径，对其中的Fastq_Unit进行遍历
        fastq文件中，一个Fastq_unit是由4行信息构成

        Usage:

        a=Fastqfile(path)
        for i in a:
            process(i)

        :return: a Fastq_unit
        """
        fastq_message_list=super(Fastqfile, self).__iter__(4)
        for fastq_message in fastq_message_list:
            fastq=Fastq_unit(info=fastq_message)
            yield fastq

    def preprocess(self):
        # 因为不是所有的fastq的base序列都是用一行表达的，也有可能是多行表达
        # TODO:添加fastq预处理模块
        with open(self.path,mode='w') as fq_file:
            for line in fq_file:
                pass


    def writefastq(self,Fastq_unit_list):
        with open(self.path,mode='w') as fq_file:
            for fq in Fastq_unit_list:
                fq_file.write(fq)

class Fastq_unit(myclass.Fasta_unit):
    def __init__(self, info='') -> None:
        super().__init__(info)
        tmp=info.split('\n')
        self.orient=tmp[2]
        self.quality=tmp[3]
    def __str__(self) -> str:
        return '\n'.join([self.id,self.base,self.orient,self.quality])+'\n'

    def __eq__(self, o: object) -> bool:
        if isinstance(o,self.__class__):
            return self.__dict__==o.__dict__
        else:return False


def main(argv):
    pass

if __name__ == '__main__':
    main(sys.argv)