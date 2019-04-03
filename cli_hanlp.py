# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:author: seanlee
:description: 结合LTP平台实现简单三元组抽取
:ctime: 2018.07.23 16:14
:mtime: 2018.07.23 16:14
"""

import argparse

from ie_single_hanlp import TripleIEHaNLP


def parse_args():
    parser = argparse.ArgumentParser('TripleIE')
    parser.add_argument('--data', type=str, default='data/normalize.txt',
                        help='the path to the data')
    parser.add_argument('--out', type=str, default='output/normalize_out_190403.txt',
                        help='the path to output')
    parser.add_argument('--ltp', type=str, default='ltp_data',
                        help='the path to LTP model')
    parser.add_argument('--clean', action='store_true',
                        help='output the clean relation(no tips)')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    with open(args.data, 'r', encoding='utf-8') as f:
        questions = f.readlines()

    with open(args.out, 'a+', encoding='utf-8') as f:
        for line in questions:
            line_sp = line.strip()
            triple_list = TripleIEHaNLP(line_sp).run()
            f.write(line_sp + '\n')
            for triple in triple_list:
                f.write('\t' + triple + '\n')
            f.flush()
