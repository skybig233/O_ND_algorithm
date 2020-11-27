# -*- coding: utf-8 -*-
# @Time : 2020/11/25 16:23
# @Author : Jiangzhesheng
# @File : run.py
# @Software: PyCharm
import sys
import argparse
import os
import logging
import myclass
import algo
class Anchor_unit:
    def __init__(self,line) -> None:
        line=line.split()
        self.query_id=line[0]
        self.ref_id=line[3]
        self.ref_start=int(line[4])
        self.ref_end=int(line[5])
        self.orient=line[6]
        self.query_start = int(line[1])
        self.query_end = int(line[2])

    def __str__(self) -> str:
        info=[self.ref_id,
              str(self.ref_start),
              str(self.ref_end),
              self.query_id,
              str(self.query_start),
              str(self.query_end),
              self.orient]
        return '\t'.join(info)

def run(queryfastapath: str, reffastapath:str,anchorpath:str,outputdir: str, logger):
    with open(anchorpath,mode='r') as anchorfile,\
            open(queryfastapath,mode='r') as queryfasta,\
            open(reffastapath,mode='r') as reffasta,\
            open(os.path.join(outputdir,'ond_result'),mode='w') as out:
        query_d={}
        for i in myclass.Fastafile(queryfastapath):
            query_d[i.id]=i

        ref_fasta_unit=myclass.Fasta_unit(reffasta.read())
        for line in anchorfile:
            anchor_unit=Anchor_unit(line)
            query_fasta_unit=query_d[anchor_unit.query_id]
            if anchor_unit.orient=='+':
                query_string=query_fasta_unit.getslice(start=anchor_unit.query_start,end=anchor_unit.query_end)
            elif anchor_unit.orient=='-':
                query_string = query_fasta_unit.getslice(start=anchor_unit.query_end, end=anchor_unit.query_start)
                query_string=myclass.DNA_reverse(query_string)

            ref_string=ref_fasta_unit.getslice(start=anchor_unit.ref_start,end=anchor_unit.ref_end)

            query_string=query_string.upper()
            ref_string=ref_string.upper()

            edit_dist=algo.ond_algo(query_string,ref_string)
            idy=(len(ref_string)-edit_dist)/len(ref_string)
            line=str(anchor_unit)+'\t'+str(idy)+'\t'+str(edit_dist)+'\n'
            out.write(line)

def main(argv):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-ref', '--reffasta',required=True)
    parser.add_argument('-query', '--queryfasta',required=True)
    parser.add_argument('-anchor', '--anchorfilepath',required=True)
    parser.add_argument('-o', '--outputdir', default='ond_algo_result')
    args = parser.parse_args(argv[1:])

    reffasta=args.reffasta
    queryfasta=args.queryfasta
    anchor=args.anchorfilepath
    outputdir = args.outputdir

    try:
        os.mkdir(outputdir)
    except FileExistsError as e:
        logging.warning(outputdir + ' is exist, files in it may be overwritten')

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    totalfh = logging.FileHandler(filename=os.path.join(outputdir, 'totallog'))

    detailfmt = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    abstractfmt = logging.Formatter('%(asctime)s-%(message)s')

    sh.setFormatter(fmt=abstractfmt)
    totalfh.setFormatter(fmt=detailfmt)

    sh.setLevel(logging.INFO)
    totalfh.setLevel(logging.INFO)

    logger.addHandler(sh)
    logger.addHandler(totalfh)

    run(queryfastapath=os.path.abspath(queryfasta),
        reffastapath=os.path.abspath(reffasta),
        anchorpath=os.path.abspath(anchor),
        outputdir=os.path.abspath(outputdir),
        logger=logger)


if __name__ == '__main__':
    main(sys.argv)
