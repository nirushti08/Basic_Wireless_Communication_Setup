#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Padded_File_Source.py

import os.path
import sys

Pkt_len = 8
_debug = 1          # set to zero to turn off diagnostics
padding = '        ' #8bytes padding

if (len(sys.argv) < 2):
    print ('Usage: python3 Padded_File_Source.py <input file>')
    print ('Number of arguments=', len(sys.argv))
    print ('Argument List:', str(sys.argv))
    exit (1)
# test if file exists
fn = sys.argv[1]
if (_debug):
    print (fn)
if not(os.path.exists(fn)):
    print('The input file does not exist')
    exit (1)

# open input file
f_in = open (fn, 'r')

# open output file
f_out = open ("padded.txt", 'w')

while True:
    buff = f_in.read (Pkt_len)
    b_len = len(buff)
    if (_debug):
        print (b_len)
    if b_len == 0:
        print ('End of file')
        f_out.write(padding.rstrip('\n'))
        break
    while (b_len < Pkt_len):
        buff += ' '
        buff1 = buff
        b_len += 1
    # write output
    f_out.write(buff)

f_in.close()
f_out.close()
