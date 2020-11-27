# -*- coding: utf-8 -*-
# @Time : 2020/9/29 14:24
# @Author : Jiangzhesheng
# @File : fasta_tools.py
# @Software: PyCharm

import sys
import myclass
import os
import traceback

class Fastafile(myclass.File_object):

    def __init__(self, path: str) -> None:
        super().__init__(path)

    def __iter__(self):
        fasta_message_list = super(Fastafile, self).__iter__(2)
        for fasta_message in fasta_message_list:
            fasta = Fasta_unit(info=fasta_message)
            yield fasta

    def isFastafile(self):
        try:
            flag=True
            for i in self:
                if i.id[0]!=myclass.SCAFFOLD_HEADER or i.base=='':
                    flag=False
                    print(i)
            return flag
        except Exception:
            traceback.print_exc()
            return False
    def delete_linebreak(self,overwriteflag:bool=False):
        filename = os.path.basename(self.path)
        tmp_filename=filename+'.delblank'
        tmp_filepath=os.path.join(os.path.dirname(self.path), tmp_filename)
        with open(self.path,mode='r') as sourcefasta,open(tmp_filepath,mode='w') as newfile:
            newfile.write(sourcefasta.readline())
            for line in sourcefasta:
                if myclass.SCAFFOLD_HEADER in line:
                    newfile.write('\n'+line)
                else:
                    newfile.write(line[:-1])
            if overwriteflag:
                os.remove(self.path)
                os.rename(tmp_filepath,filename)
        return tmp_filepath

    def delete_blank_scaffold(self,overwriteflag:bool=False):
        filename = os.path.basename(self.path)
        tmp_filename = filename + '.del_blank_scaffold'
        tmp_filepath = os.path.join(os.path.dirname(self.path), tmp_filename)
        with open(tmp_filepath, mode='w') as newfile:
            for i in self:
                if i.base!='':
                    newfile.write(str(i)+'\n')
        if overwriteflag:
            os.remove(self.path)
            os.rename(tmp_filepath, filename)
        return tmp_filepath

    def countscaffold(self):
        cnt=0
        with open(self.path,mode='r') as fastafile:
            for line in fastafile:
                if line[0]=='>':
                    cnt+=1
        return cnt

    def countcontig(self):
        # TODO:添加数contig功能
        pass

class Fasta_unit:
    def __init__(self,info='') -> None:
        tmp=info.split('\n')
        self.id=tmp[0][1:]
        self.base=tmp[1]

    def getslice(self,start:int,end:int,zero_based:bool=True)->str:
        """
        fasta切片功能，start是闭区间，end是开区间
        :param start:
        :param end:
        :param zero_based:
        :return: 切出的字符串
        """
        if zero_based:#0-based
            return self.base[start:end]
        else:#1-based
            return self.base[start-1:end-1]

    def setPE(self):
        if self.id[-1] in ['1','2']:
            self.PEinfo=self.id[-1]

    def __str__(self) -> str:
        return '\n'.join([self.id,self.base])

def main(argv):
    pass


if __name__ == '__main__':
    main(sys.argv)
